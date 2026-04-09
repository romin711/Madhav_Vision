import cv2
import math
import random


class ChakraRenderer:
    def __init__(self):
        self.angle = 0
        self.prev_x = None
        self.prev_y = None
        self.particles = []

    def smooth(self, x, y, alpha=0.75):
        if self.prev_x is None:
            self.prev_x, self.prev_y = x, y
            return x, y

        x = int(self.prev_x * alpha + x * (1 - alpha))
        y = int(self.prev_y * alpha + y * (1 - alpha))

        self.prev_x, self.prev_y = x, y
        return x, y

    def spawn_particles(self, x, y):
        for _ in range(3):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(1, 2.5)

            self.particles.append({
                "x": x,
                "y": y,
                "vx": math.cos(angle) * speed,
                "vy": math.sin(angle) * speed,
                "life": random.randint(10, 25)
            })

    def update_particles(self, frame):
        new_particles = []

        for p in self.particles:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["life"] -= 1

            if p["life"] > 0:
                alpha = p["life"] / 25.0
                color = (0, int(200 * alpha), 255)

                cv2.circle(frame, (int(p["x"]), int(p["y"])), 2, color, -1)
                new_particles.append(p)

        self.particles = new_particles

    def render(self, frame, x, y, z):
        x, y = self.smooth(x, y)

        # --- DEPTH NORMALIZATION ---
        z = max(min(z, 0.15), -0.15)

        # --- SIZE + PERSPECTIVE ---
        base_radius = 120
        radius = int(base_radius - z * 60)

        # dynamic tilt (more z = more tilt)
        tilt = 0.55 + (z * 1.5)
        tilt = max(0.4, min(tilt, 0.9))

        axes = (radius, int(radius * tilt))

        overlay = frame.copy()
        self.angle = (self.angle + 25) % 360

        # =========================
        # 1. BACK RING (darker)
        # =========================
        for i in range(12):
            depth_fade = 1 - (i / 12)
            color = (0, int(80 * depth_fade), int(160 * depth_fade))
            cv2.ellipse(
                overlay,
                (x, y),
                (axes[0] - i, axes[1] - i),
                0,
                0,
                360,
                color,
                2
            )

        # =========================
        # 2. BLADES (3D SPLIT)
        # =========================
        blade_count = 28
        front_blades = []
        back_blades = []

        for i in range(blade_count):
            theta = (2 * math.pi / blade_count) * i + math.radians(self.angle)

            bx = int(x + axes[0] * math.cos(theta))
            by = int(y + axes[1] * math.sin(theta))

            bx2 = int(x + (axes[0] + 25) * math.cos(theta))
            by2 = int(y + (axes[1] + 25 * tilt) * math.sin(theta))

            depth = math.sin(theta)

            blade = (bx, by, bx2, by2, depth)

            if depth < 0:
                back_blades.append(blade)
            else:
                front_blades.append(blade)

        # --- draw back blades (darker) ---
        for bx, by, bx2, by2, depth in back_blades:
            shade = 0.5 + (depth + 1) * 0.25
            color = (0, int(100 * shade), int(180 * shade))
            cv2.line(overlay, (bx, by), (bx2, by2), color, 2)

        # =========================
        # 3. INNER SHADOW (depth)
        # =========================
        cv2.ellipse(
            overlay,
            (x, y),
            (int(axes[0] * 0.75), int(axes[1] * 0.75)),
            0,
            0,
            360,
            (0, 60, 120),
            -1
        )

        # =========================
        # 4. FRONT BLADES (bright)
        # =========================
        for bx, by, bx2, by2, depth in front_blades:
            highlight = 0.6 + depth * 0.4
            color = (0, int(180 * highlight), int(255 * highlight))
            thickness = 3 if depth > 0.5 else 2
            cv2.line(overlay, (bx, by), (bx2, by2), color, thickness)

        # =========================
        # 5. FRONT RING (highlight)
        # =========================
        for i in range(6):
            glow_intensity = 200 + i * 10
            cv2.ellipse(
                overlay,
                (x, y),
                (axes[0] - i, axes[1] - i),
                0,
                0,
                360,
                (0, glow_intensity, 255),
                2
            )

        # =========================
        # 6. SPECULAR LIGHT (fake sun)
        # =========================
        light_x = int(x - axes[0] * 0.3)
        light_y = int(y - axes[1] * 0.3)

        cv2.circle(overlay, (light_x, light_y), int(radius * 0.15), (255, 255, 255), -1)

        # =========================
        # 7. CORE
        # =========================
        cv2.ellipse(
            overlay,
            (x, y),
            (int(axes[0] * 0.25), int(axes[1] * 0.25)),
            0,
            0,
            360,
            (0, 140, 255),
            -1
        )

        # =========================
        # POST PROCESS (GLOW)
        # =========================
        blur = cv2.GaussianBlur(overlay, (9, 9), 2)
        glow = cv2.GaussianBlur(blur, (35, 35), 0)

        self.spawn_particles(x, y)
        self.update_particles(glow)

        return cv2.addWeighted(glow, 0.75, frame, 0.25, 0)
import cv2


class MukutRenderer:
    def __init__(self):
        self.prev_x = None
        self.prev_y = None

    def smooth(self, x, y, alpha=0.7):
        if self.prev_x is None:
            self.prev_x, self.prev_y = x, y
            return x, y

        x = int(self.prev_x * alpha + x * (1 - alpha))
        y = int(self.prev_y * alpha + y * (1 - alpha))

        self.prev_x, self.prev_y = x, y
        return x, y

    def render(self, frame, x, y, face_width):
        x, y = self.smooth(x, y)

        overlay = frame.copy()

        # 👉 dynamic scaling
        w = int(face_width * 1.0)

        # 👉 vertical control
        y = y - int(w * 0.05)

        # BASE BAND
        for i in range(25):
            cv2.ellipse(
                overlay,
                (x, y),
                (w - i, int(w * 0.4) - i),
                0,
                180,
                360,
                (0, 170 + i * 3, 255),
                2
            )

        # ARCHES
        peaks = 7
        for i in range(peaks):
            ratio = (i - peaks // 2) / (peaks // 2)
            px = int(x + ratio * w * 0.8)
            py = y - int(w * (0.35 + 0.25 * (1 - abs(ratio))))

            cv2.line(overlay, (px, y), (px, py), (0, 200, 255), 2)
            cv2.circle(overlay, (px, py), 6, (0, 0, 255), -1)

        # CENTER
        top = y - int(w * 0.7)
        cv2.line(overlay, (x, y), (x, top), (0, 220, 255), 3)
        cv2.circle(overlay, (x, top), 10, (0, 0, 255), -1)

        # FEATHER
        fx = x - int(w * 0.6)
        fy = y - int(w * 0.9)

        cv2.line(overlay, (x, y - 50), (fx, fy), (0, 160, 0), 3)
        cv2.ellipse(overlay, (fx, fy), (30, 55), -20, 0, 360, (255, 0, 0), -1)
        cv2.ellipse(overlay, (fx, fy), (20, 35), -20, 0, 360, (0, 255, 255), -1)

        glow = cv2.GaussianBlur(overlay, (31, 31), 0)

        return cv2.addWeighted(glow, 0.75, frame, 0.25, 0)
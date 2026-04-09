import mediapipe as mp


class FaceTracker:
    def __init__(self):
        self.face = mp.solutions.face_mesh.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True
        )

    def process(self, frame_rgb):
        return self.face.process(frame_rgb)

    def get_forehead_anchor(self, landmarks, w, h):
        left = landmarks.landmark[103]
        right = landmarks.landmark[332]
        top = landmarks.landmark[10]

        x = int((left.x + right.x) / 2 * w)
        y = int(top.y * h) + int(0.04 * h)

        face_width = int(abs(right.x - left.x) * w)

        return x, y, face_width
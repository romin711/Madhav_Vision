from mediapipe.python.solutions import hands as mp_hands
from mediapipe.python.solutions import drawing_utils as mp_draw


class HandTracker:
    def __init__(self):
        self.hands = mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp_draw

    def process(self, frame_rgb):
        return self.hands.process(frame_rgb)

    def get_index_tip(self, landmarks, width, height):
        tip = landmarks.landmark[8]
        return int(tip.x * width), int(tip.y * height), tip.z

    def is_index_open(self, landmarks):
        tip = landmarks.landmark[8]
        pip = landmarks.landmark[6]
        return tip.y < pip.y

    def draw(self, frame, landmarks):
        self.mp_draw.draw_landmarks(
            frame,
            landmarks,
            mp_hands.HAND_CONNECTIONS
        )
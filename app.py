import cv2

from hand.tracker import HandTracker
from chakra.renderer import ChakraRenderer

from face.face_tracker import FaceTracker
from crown.mukut_renderer import MukutRenderer


def main():
    cap = cv2.VideoCapture(0)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 960)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    hand_tracker = HandTracker()
    chakra = ChakraRenderer()

    face_tracker = FaceTracker()
    mukut = MukutRenderer()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # ---------------- HAND ----------------
        hand_results = hand_tracker.process(rgb)

        if hand_results.multi_hand_landmarks:
            for landmarks in hand_results.multi_hand_landmarks:
                h, w, _ = frame.shape

                x, y, z = hand_tracker.get_index_tip(landmarks, w, h)

                if hand_tracker.is_index_open(landmarks):
                    frame = chakra.render(frame, x, y, z)

                hand_tracker.draw(frame, landmarks)

        # ---------------- FACE ----------------
        face_results = face_tracker.process(rgb)

        if face_results.multi_face_landmarks:
            for face_landmarks in face_results.multi_face_landmarks:
                h, w, _ = frame.shape

                x, y, face_width = face_tracker.get_forehead_anchor(
                    face_landmarks, w, h
                )

                frame = mukut.render(frame, x, y, face_width)

        cv2.imshow("Krishna AR (Chakra + Mukut)", frame)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
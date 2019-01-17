import cv2
import face_recognition


def start_game(camera_id=0):
    # Run face location every 30 frames. If good hardware(like GPU) is available, set interval to lower values.
    i = 0
    interval = 30
    cap = cv2.VideoCapture(camera_id)
    boxes = []
    while True:
        ret, bgr = cap.read()
        if not ret:
            break

        if i % interval == 0:
            rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
            boxes = face_recognition.face_locations(rgb, model='hog')   # 'hog' or 'cnn'

        for box in boxes:
            # box is (top, right, bottom, left)
            cv2.rectangle(bgr,
                          pt1=(box[3], box[0]),
                          pt2=(box[1], box[2]),
                          color=(0, 255, 0),
                          thickness=3)

        i = (i + 1) % interval
        cv2.imshow("face_recognition", bgr)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break


if __name__ == '__main__':
    start_game()


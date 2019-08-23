import cv2
import face_recognition
import time
from multiprocessing import Process, Manager, Lock


def face_detector_process(s, l, d_args):
    """
    Subprocess to do face detection operation. When detection is done, result is sent back to main process by d_args.
    :param s: seconds to sleep. Can be a floating number for subsecond precision.
    :param l: Lock to ensure synchronization.
    :param d_args: One dict container to share variables.
    """
    while True:
        l.acquire()
        over = d_args['over']
        has_data = d_args['has_data']
        d_args['has_data'] = False
        if has_data:
            rgb = d_args['rgb'].copy()
        l.release()

        if over:
            return

        if has_data:
            boxes = face_recognition.face_locations(rgb, model='hog')  # 'hog' or 'cnn'
            print("in subprocess: ", boxes)
            l.acquire()
            d_args['boxes'] = boxes
            l.release()

        if s:
            time.sleep(s)


def app(camera_id=0):
    lock = Lock()

    manager = Manager()
    d_args = manager.dict()
    d_args['over'] = False
    d_args['has_data'] = False
    d_args['boxes'] = []
    sleep_seconds = 0.1
    p = Process(target=face_detector_process, args=(sleep_seconds, lock, d_args, ))

    cap = cv2.VideoCapture(camera_id)

    p.start()

    while True:
        ret, bgr = cap.read()
        if not ret:
            d_args['over'] = True
            break

        rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

        lock.acquire()
        d_args['rgb'] = rgb
        d_args['has_data'] = True
        boxes = d_args['boxes'].copy()
        lock.release()

        for box in boxes:
            # box is (top, right, bottom, left)
            cv2.rectangle(bgr,
                          pt1=(box[3], box[0]),
                          pt2=(box[1], box[2]),
                          color=(0, 255, 0),
                          thickness=3)

        cv2.imshow("face_recognition", bgr)

        if cv2.waitKey(1) & 0xff == ord('q'):
            d_args['over'] = True
            break

    p.join()


if __name__ == '__main__':
    app()

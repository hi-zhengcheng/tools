import cv2
import tensorflow as tf
from model import Model
import numpy as np
import os


class Infer(object):
    def __init__(self):
        self._top_k = 4
        self._top_colors = [
            (0, 0, 255),
            (0, 255, 0),
            (255, 0, 255),
            (182, 89, 155)
        ]

        self.model = Model()

    def __call__(self, image_path):
        assert os.path.isfile(image_path), "{} is not a file.".format(image_path)

        with tf.Session() as sess:
            sess.run([tf.global_variables_initializer(), tf.tables_initializer()])

            image_bgr = cv2.imread(image_path)
            image = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
            images = np.expand_dims(image, 0)
            names, frames = self.model(sess, images, self._top_k)

            print(names)
            print(frames)

            w, h, c = image_bgr.shape
            for idx, rect in enumerate(frames):
                cv2.rectangle(image_bgr,
                              pt1=(int(rect[1] * h), int(rect[0] * w)),
                              pt2=(int(rect[3] * h), int(rect[2] * w)),
                              color=self._top_colors[idx],
                              thickness=1)

                cv2.putText(image_bgr,
                            "[{}] {}".format(idx, names[idx].decode('utf-8')),
                            (int(rect[1] * h), int(rect[0] * w)),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            self._top_colors[idx],
                            2)

            cv2.imshow('test', image_bgr)

            cv2.waitKey()
            cv2.destroyAllWindows()


if __name__ == '__main__':
    os.environ['TFHUB_CACHE_DIR'] = 'module_cache'
    infer = Infer()
    infer('../test.jpg')

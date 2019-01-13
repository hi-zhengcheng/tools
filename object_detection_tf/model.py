import tensorflow_hub as hub
import tensorflow as tf


class Model(object):
    """"""
    def __init__(self):
        self.input_image = tf.placeholder(tf.float32)
        module = hub.Module('https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1')
        detector = module(self.input_image, as_dict=True)
        self.class_names = detector['detection_class_entities']
        self.boxes = detector['detection_boxes']

    def __call__(self, sess, batch_images, top_k):
        names, boxes = sess.run([self.class_names, self.boxes], feed_dict={self.input_image: batch_images})
        names = names[:top_k]
        boxes = boxes[:top_k]
        return names, boxes

import tensorflow_hub as hub
import tensorflow as tf


class Model(object):
    def __init__(self):
        """Init model, do things like:
            1. Create input placeholder
            2. load pre-trained model
            3. extract interested tensor out from the model
        """
        self.input_image = tf.placeholder(tf.float32)
        module = hub.Module('https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1')
        detector = module(self.input_image, as_dict=True)
        self.class_names = detector['detection_class_entities']
        self.boxes = detector['detection_boxes']

    def __call__(self, sess, batch_images, top_k):
        """
        Args:
            sess: tf.Session obj
            batch_images: numpy array with shape (1, height, width, channel)
            top_k: integer, only return top_k result

        Returns:
            names: top_k class names sorted by score, with shape (top_k)
            boxes: top_k bounding boxes sorted by score, with shape (top_k, 4).
                Last dim data means (h1, w1, h2, w2)

        Note: This pre-trained model only support batch_size 1. It will do squeeze dim[0] when model returns output.
        """
        names, boxes = sess.run([self.class_names, self.boxes], feed_dict={self.input_image: batch_images})
        names = names[:top_k]
        boxes = boxes[:top_k]
        return names, boxes

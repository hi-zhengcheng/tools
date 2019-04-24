import tensorflow as tf
from PIL import Image

try:
    # python 2.7
    from StringIO import StringIO
except ImportError:
    # python 3.x
    from io import BytesIO


class Logger(object):
    def __init__(self, log_dir):
        self.writer = tf.summary.FileWriter(log_dir)

    def scalar_summary(self, tag, value, step):
        """
        tag: str
        value: scalar value
        step: int
        """
        summary = tf.Summary(value=[
            tf.Summary.Value(tag=tag, simple_value=value)
        ])
        self.writer.add_summary(summary, step)

    def image_summary(self, tag, images, step):
        """
        tag: str
        images: ndarray with shape: [batch, h, w, c]
        step: int
        """
        img_summaries = []
        for i in range(images.shape[0]):
            try:
                s = StringIO()
            except:
                s = BytesIO()
            Image.fromarray(images[i]).save(s, format="png")
            img_sum = tf.Summary.Image(
                encoded_image_string=s.getvalue(),
                height=images.shape[1],
                width=images.shape[2]
            )

            img_summaries.append(tf.Summary.Value(tag='{}/{}'.format(tag, i), image=img_sum))

        summary = tf.Summary(value=img_summaries)
        self.writer.add_summary(summary, step)

    def flush(self):
        self.writer.flush()


if __name__ == '__main__':

    def test_scalar():
        logger = Logger('test_summary')
        tag = 'test_scalar/a'
        for i in range(10):
            logger.scalar_summary(tag, i ** 2, i)

        logger.flush()


    def test_image():
        import imageio
        import numpy as np
        img = imageio.imread('zzz.jpg')
        imgs = np.tile(img, [2, 1, 1, 1])
        logger = Logger('test_summary2')
        logger.image_summary('tag1', imgs, 0)
        logger.image_summary('tag1', imgs, 1)
        logger.image_summary('tag1', imgs, 2)
        logger.image_summary('tag1', imgs, 3)
        logger.flush()


    def test_tensor():

        summary_writer = tf.summary.FileWriter('test_summary4')

        input_a = tf.placeholder(dtype=tf.float32, shape=[])
        a = input_a
        b = input_a ** 2
        c = input_a ** 3

        tf.summary.scalar('a', a)
        tf.summary.scalar('b', b)
        tf.summary.scalar('c', c)

        summary_op = tf.summary.merge_all()

        sess = tf.Session()

        for i in range(10):
            sa, sb, sc, ss = sess.run([a, b, c, summary_op], feed_dict={input_a: i})
            print(i, [sa, sb, sc])
            summary_writer.add_summary(ss, i)

        summary_writer.flush()

    test_scalar()

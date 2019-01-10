import tensorflow as tf
import collections


"""
The old version tf data load API is work on the Queue concept. 
The new version API uses the concept of DataSet.

This demo illustrates some common usage of DataSet API.
"""


"""
Condition 1: one txt file, each line is one training example, like image_path and label.
"""


class OneTrainingExampleObject(collections.namedtuple('OneTrainingExampleObject', ['path', 'label'])):
    pass


def parse_file_line1(line):
    record_defaults = [[''], ['']]
    data = tf.decode_csv(line, record_defaults, field_delim=' ')
    return OneTrainingExampleObject(data[0], data[1])


def tf_read_txt_file_pipeline1(file_path_tensor):
    """Read txt file

    Suppose one txt file contains all training example.
    """
    _dataset = (
        tf.data.TextLineDataset(file_path_tensor)
        .filter(lambda line: tf.not_equal(line, ''))
        .filter(lambda line: tf.not_equal(tf.substr(line, 0, 1), '#'))
        .map(parse_file_line1)
        .shuffle(10)
        .repeat(5))

    _iterator = _dataset.make_one_shot_iterator()
    return _iterator.get_next()


def test1():
    file_path_tensor = tf.constant('train/1.txt')
    one_example = tf_read_txt_file_pipeline1(file_path_tensor)

    sess = tf.Session()
    c = 1
    while True:
        try:
            print(c, sess.run(one_example))
            c += 1
        except:
            break


"""
Condition 2: many txt files, one txt file represents one training example.
"""


def read_file_lines2(file_path, max_lines=10000):
    """Reads a txt file, skips comments

    Args:
        file_path: the file path to read
        max_lines: how many lines to combine to a single element.
            Any further lines will be skipped.

    Returns:
        The lines of the file, as a 1 dimensional tensor.
    """
    lines = (tf.data.TextLineDataset(file_path)
             .filter(lambda line: tf.not_equal(tf.substr(line, 0, 1), '#'))

             .batch(max_lines)
             .take(1))
    return tf.data.experimental.get_single_element(lines)


def parse_file_lines2(lines):
    """parse lines as image, label.

    Args:
        lines: lines contents in one file. Each line has form:
            image_path label

    Returns:
        One training example object.
    """
    record_defaults = [[''], ['']]
    data = tf.decode_csv(lines, record_defaults, field_delim=' ')
    return OneTrainingExampleObject(data[0], data[1])


def tf_read_txt_file_pipeline2():
    """Read txt file demo.

    Suppose one txt file contains one training example.
    """
    txt_glob = 'train/*.txt'
    assert tf.gfile.Glob(txt_glob)

    files = (
        tf.data.Dataset.list_files(txt_glob, shuffle=False)
        .map(read_file_lines2, num_parallel_calls=10)
        .map(parse_file_lines2)
        .shuffle(10)
        .repeat(5))

    _iterator = files.make_one_shot_iterator()
    return _iterator.get_next()


def test2():
    one_example = tf_read_txt_file_pipeline2()

    sess = tf.Session()
    c = 1
    while True:
        try:
            print(c, sess.run(one_example))
            c += 1
        except:
            break


if __name__ == '__main__':
    print('one file, all training examples'.center(100, '-'))
    test1()
    print('many files, one file one training example'.center(100, '-'))
    test2()

import tensorflow as tf
import numpy as np


"""
The old version tf data load API is work on the Queue concept. 
The new version API uses the concept of DataSet.

This demo illustrates some common usage of DataSet API.

Core logic:
1. Create Dataset from data source. Data source can be:
    1. numpy or tensor
    2. TFRecords
    3. txt files
    4. csv files
    
2. Transformation dataset. Do operations like:
    1. Batch
    2. Repeat
    3. Shuffle
    4. Map
    5. Filter
    
    Note: the order of transformation is import, different order leads to different result.
    
3. Use Iterator to get data from Dataset. Several different types of iterator:
    1. One shot iterator
    2. Initializable iterator
    3. Reinitializable iterator
    4. Feedable iterator
    
4. Use data in train or inference process.
    
"""


"""
1. Create Dataset from different data source
"""


# create dataset from numpy array
def create_dataset1():
    dataset1 = tf.data.Dataset.from_tensor_slices(np.arange(0, 10, 1))
    return dataset1


# create dataset from 1-D tensor
def create_dataset2():
    dataset2 = tf.data.Dataset.from_tensor_slices(tf.range(10))
    return dataset2


# create dataset from multiple objects. Each object must have same size in 0-dim.
def create_dataset3():
    dataset3 = tf.data.Dataset.from_tensor_slices((tf.range(0, 10, 1), tf.range(10, 20, 1)))
    return dataset3


"""
2. Transform dataset
"""


def transform_dataset(dataset):
    dataset = dataset.shuffle(5)\
        .repeat(2)\
        .batch(2)
    return dataset


"""
3. Get data by Iterator.
"""


def get_data_from(dataset):
    iterator = dataset.make_one_shot_iterator()
    data = iterator.get_next()
    return data


"""
4. Train
"""


def train(data):
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        try:
            while True:
                # run model optimizer, do checkpoint and some logs
                print(sess.run(data))
        except tf.errors.OutOfRangeError:
            pass


"""
Put them together
"""


def map_fn(x):
    return x * 3


def filter_fn(x):
    return tf.not_equal(x % 5, 1)


def tf_dataset_workflow_demo():
    dataset = (
        tf.data.Dataset.from_tensor_slices(np.arange(0, 10, 1))
        .shuffle(10)
        .repeat(2)
        .map(map_fn)
        .filter(filter_fn)
        .batch(2))

    iterator = dataset.make_one_shot_iterator()
    data = iterator.get_next()

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        try:
            while True:
                # run model optimizer, do checkpoint and some logs
                print(sess.run(data))
        except tf.errors.OutOfRangeError:
            pass


if __name__ == '__main__':
    tf_dataset_workflow_demo()


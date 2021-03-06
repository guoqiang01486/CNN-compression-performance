import tensorflow as tf


def weight_variable(shape, name=None):
    # use get variable for variable reuse, it gets an another variable if it exists
    if name is not None:
    	initial = tf.truncated_normal_initializer(stddev=0.1)
    	return tf.get_variable(name, shape=shape, initializer=initial)
    else:
    	initial = tf.truncated_normal(shape, stddev=0.1)
    	return tf.Variable(initial,name=name)


def bias_variable(shape, name=None):
	if name is not None:
	    initial = tf.constant_initializer(0.1)
	    return tf.get_variable(name, shape=shape, initializer=initial)
	else:
		initial = tf.constant(0.1, shape=shape)
    	return tf.Variable(initial, name=name)


def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],
                          strides=[1, 2, 2, 1], padding='SAME')

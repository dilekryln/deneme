import tensorflow as tf

x1 = tf.constant(10)
x2 = tf.constant(2)

add = tf.math.divide(x1, x2)

session = tf.Session()

output = session.run(add)

print(output)

session.close()
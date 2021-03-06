#coding=utf-8
import tensorflow as tf

c = tf.constant("hello from server2!")

cluster = tf.train.ClusterSpec(
    {"local": ["192.168.1.165:2222", "192.168.1.165:2223"]})

server = tf.train.Server(cluster, job_name="local", task_index=1)

sess = tf.Session(server.target, config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))
server.join()
sess.close()
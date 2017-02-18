import logging
import os
import tensorflow as tf
from logging.config import fileConfig
from flask import Flask
from flask import jsonify

fileConfig('logging_config.ini')
logger = logging.getLogger('app')
DEFAULT_PORT = '8080'

app = Flask(__name__)


@app.route('/')
def home():
    logger.info('processing home request.')
    return 'Hello World! I am running'


@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(e)
    return 'Error: ' + str(e)


@app.route('/tensorflow')
def tensorflow():
    logger.info('processing tensorflow request.')
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    message = sess.run(hello).decode('utf-8')
    logger.info(message)

    a = tf.constant(10)
    b = tf.constant(32)
    number = sess.run(a + b).item()
    logger.info(number)
    return jsonify(message=message, number=number)


if __name__ == '__main__':
    port = os.getenv('PORT', DEFAULT_PORT)
    logger.info("starting app at port {}".format(port))
    app.run(host='0.0.0.0', port=int(port))
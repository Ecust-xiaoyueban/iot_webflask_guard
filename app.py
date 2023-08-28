# -*- coding:utf-8 -*-
from flask import Flask
from threading import Thread

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

# 设置flask服务启动函数，便于在其他文件中调用
def start_app():
    # 值得注意的是，如果直接在别的地方调用这个方法，flask的启动会直接导致程序的阻塞，所以要用多线程技术来解决这一问题
    # 这里的实现方式就是用下面的start_webflask启动一个新的线程来启动flask服务
    app.run(host='0.0.0.0')
def start_webflask():
    flask_thread = Thread(target=start_app)
    flask_thread.start()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

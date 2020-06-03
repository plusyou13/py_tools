# import tensorflow as tf
# from tensorflow import keras
# (x,y),(x_test,y_test)=keras.datasets.cifar10.load_data()
# from selenium import webdriver
# browser=webdriver.phantomJS()
# browser.get('http://www.baidu.com')
# print(browser.current_url)

# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# def hello():
#     return "hello lic"
# if __name__ == '__main__':
#     app.run()

# import tornado.ioloop
# import tornado.web
# class MainHandler(tornado.web.RequestHandler):
#     def get(self):
#         self.write("hello")
#
# def make_app():
#     return tornado.web.Application([
#         (r"/",MainHandler),
#     ])
#
# if __name__ == '__main__':
#     app=make_app()
#     app.listen(8888)
#     tornado.ioloop.IOLoop.current().start()
#
#
# import urllib.request
# response= urllib.request.urlopen("http://www.baidu.com")
# #print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())


# import urllib.parse
# import urllib.request
#data必须是bytes（字节流）
# data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())
#
# import urllib.parse
# import urllib.request
# import socket
# import urllib.error
#
# #data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
#
# try:
#     response=urllib.request.urlopen('http://www.baidu.com',timeout=5)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')
#
#
# print(response.read().decode('utf-8'))

#encoding:utf-8


# import pymysql
# import time
# import random
# #连接mysql
# db = pymysql.connect('101.132.253.52','root','1123','test_db')
# #获取mysql操作光标
# cursor = db.cursor()
# #初始化变量
# count = 0
# #设置sql语句循环次数
# while count <= 1000000:
#     count += 1
#     #定义mysql字段的范围随机数变量
#     num = random.randint(0,200)
#     memo_num = random.randint(500,811)
#     city_list = ['a','b','c','d']
#     a = random.choice(city_list)
#     #生成mysql语句插入语句
#     sql = "insert  into city(id,city_code,city_name,memo)values(%d,%s,'%s',%s)" %(count,num,a,memo_num)
#     #执行sql语句

#     try:
#         cursor.execute(sql)
#         db.commit()
#         print("1")
#     #错误回滚    
#     except:
#         db.rollback()
# #关闭mysql
#         print("0")

# db.close()

import sense2vec
sense2vec.download()









#!usr/bin/env/python3
# -*-coding:utf-8 -*-
"""
Author: Blinkliu
Created on 2018-07-20 17:07
"""
"""进程间通信：python的multiprocessing模块提供了Queue、Pipes等多种方式交换数据"""
"""下面以Queue为例"""
from multiprocessing import Queue,Process
import os,time,random
def write(name):
    print("process to write:%s"%os.getpid())
    for i in ['A','B','C']:
        print("put %s in Queue"%i)
        name.put(i)
        time.sleep(random.random())

#读数据进程执行的代码
def read(name):
    print("Process to read:%s"%os.getpid())
    plist =[]
    size =len(plist)
    while True:
        i =name.get(True)
        print("Get %s from queue."%i)
if __name__=="__main__":
    name = Queue()
    pw = Process(target=write,args=(name,)) #把Queue()当做参数传给前面的target函数，用Queue控制进程（指write和read两个进程）的数据通信
    pr = Process(target=read,args=(name,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
from multiprocessing import Pipe
import multiprocessing
a = Pipe(duplex=True) #通过duplex参数控制管道是单向还是双向的；false为单向
def proc1(pipe):
    pipe.send('hello')
    print('proc1 rec:',pipe.recv())

def proc2(pipe):

    print('proc2 rec:',pipe.recv())
    pipe.send('hello, too')
p1 = multiprocessing.Process(target=proc1, args=(a[0],))
p2 = multiprocessing.Process(target=proc2, args=(a[1],))

p1.start()
p2.start()
p1.join()
p2.join()
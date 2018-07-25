# -*- coding: utf-8 -*-
"""
@author: liubinghong
"""
import threading,time,multiprocessing
#线程需要加锁
lock = threading.Lock()
def foo():
    lock.acquire() #通过acquire获取锁

#新线程执行的代码
# def loop():
#     print("thread %s is running"%threading.current_thread().name)
#     n = 0
#     while n<5:
#         n +=1
#         print('thread %s >>> %s' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('thread %s ended.' % threading.current_thread().name)
# print('thread %s is running...' % threading.current_thread().name)

# t=threading.Thread(target=loop,name='Loopthread_test')
# a = threading.Thread()
# t.start()
# t.join()
# print("thread %s is ended"%threading.current_thread().name)
print(multiprocessing.cpu_count())
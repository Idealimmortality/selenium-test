# coding=utf-8
from multiprocessing import Process

from multiprocessing import Pool    #使用Pool进程池创建大量进程
import subprocess                   #子进程
import os,time,random

print('$ nslookup www.python.org')
r = subprocess.call(['sc','query'])
print("exitcode:",r)
# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',)) #注意这里贼坑，必须加，号；因为args这个参数代表的是前面调用对象的位置参数元组；
#     print('Child pro cess will start.')
#     p.start()
#     p.join()
#
#     print('Child process end.')
#
# def long_time_tase(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))
# if __name__ =="__main__":
#     print("Parent process is (%s)"%os.getpid())
#     p = Pool(2)
#     for i in range(10):
#         p.apply_async(long_time_tase,args=(i,))
#     print("waiting all subprocesses done...")
#     p.close()
#     p.join()
#     print("All processing done.")


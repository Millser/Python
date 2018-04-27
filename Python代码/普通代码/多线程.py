import time
import threading

def loop1():
    #ctime得到当前时间
    print("loop1开始时间为：", time.ctime())

    time.sleep(4)
    print("loop1结束时间为：", time.ctime())

def loop2():
    print("loop1开始时间为：", time.ctime())

    time.sleep(2)

    print("loop2结束时间为：", time.ctime())

def main():

    print("开始时间为：", time.ctime())

    threading._start_new_thread(loop1, ())

    threading._start_new_thread(loop2, ())

    print("结束时间为：", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)

#! /usr/local/bin python3.6
"""
@Time    : 2018/3/14 21:10
@Author  : ysj
@Site    : 
@File    : spiner_thread.py
@Software: PyCharm
"""
import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            break
    write(' ' * len(status) + '\x08')


def slow_function():
    time.sleep(10)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin, args=('thinjing!', signal))
    print('spinner object:', spinner)
    spinner.start()
    result = slow_function()
    signal.go = False
    spinner.join()
    return result

def main():
    answer = supervisor()
    print('Answer:', answer)

if __name__ == '__main__':
    main()
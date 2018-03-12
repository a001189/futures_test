#! /usr/local/bin python3.6
"""
@Time    : 2018/3/12 22:41
@Author  : ysj
@Site    : 
@File    : flags_threadpool.py
@Software: PyCharm
"""
from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20


def download_one(cc):
    img = get_flag(cc)
    save_flag(img, cc.lower() + '.gif')
    show(cc)
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list), timeout=10)
    return len(list(res))


if __name__ == '__main__':
    main(download_many)

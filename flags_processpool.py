#! /usr/local/bin python3.6
"""
@Time    : 2018/3/13 21:05
@Author  : ysj
@Site    : 
@File    : flags_processpool.py.py
@Software: PyCharm
"""

from concurrent import futures

from flags import save_flag, get_flag, show, main
import time
MAX_WORKERS = 20


def download_one(cc):
    img = get_flag(cc)
    save_flag(img, cc.lower() + '.gif')
    time.sleep(10)
    show(cc)
    return cc


def download_many(cc_list):
    # workers = min(MAX_WORKERS, len(cc_list))
    with futures.ProcessPoolExecutor() as executor:
        res = executor.map(download_one, sorted(cc_list), timeout=10)
    return len(list(res))


if __name__ == '__main__':
    main(download_many)

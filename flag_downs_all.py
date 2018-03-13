#! /usr/local/bin python3.6
"""
@Time    : 2018/3/13 22:20
@Author  : ysj
@Site    : 
@File    : flag_downs_all.py
@Software: PyCharm
"""
import time
import string
from concurrent import futures
from flags_threadpool import download_one
import tqdm

lt = []
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        lt.append(i + j)


def down_many(cc_list):

    with futures.ThreadPoolExecutor(max_workers=1000) as executor:
        to_do_map = {}
        for cc in lt:
            future = executor.submit(download_one, cc)
            to_do_map[future] = cc
        done_iter = tqdm.tqdm(futures.as_completed(to_do_map),total=len(cc_list))

        for future in done_iter:
            try:
                res = future.result()
            except Exception:
                pass
            # print(res)


if __name__ == '__main__':

    start = time.time()
    down_many(lt)
    use_time = time.time() - start
    print('time use %.2f' % use_time)
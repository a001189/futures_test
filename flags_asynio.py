#! /usr/local/bin python3.6
"""
@Time    : 2018/3/14 23:51
@Author  : ysj
@Site    : 
@File    : flags_asynio.py
@Software: PyCharm
"""
import asyncio
import aiohttp
import string
import time
from flags import BASE_URL, save_flag, show

lt = []
for i in string.ascii_lowercase:
    for j in string.ascii_lowercase:
        lt.append(i + j)
POP20_CC = lt


@asyncio.coroutine
def get_flag(cc):
    url = '{}/{cc}/{cc}.git'.format(BASE_URL, cc=cc.lower())
    resp = yield from aiohttp.request('GET', url)
    image = yield from resp.read()
    return image


@asyncio.coroutine
def download_one(cc):
    image = yield from get_flag(cc)
    show(cc)
    save_flag(image, 'gif2/' + cc.lower() + '.git')
    return cc

def download_many(cc_list):
    loop = asyncio.get_event_loop()
    to_do = [download_one(cc) for cc in cc_list]
    wait_coro = asyncio.wait(to_do)
    res, _ = loop.run_until_complete(wait_coro)
    loop.close()
    return len(res)


def main(down_many):
    start = time.time()
    count = down_many(POP20_CC)
    time_use = time.time() - start
    print('\n{} flags downloaded in {:.2f}s'.format(count, time_use))

if __name__ == '__main__':
    main(download_many)
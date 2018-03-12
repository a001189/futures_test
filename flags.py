import os
import sys
import time

import requests

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

DEST_DIR = 'gif'



BASE_URL = 'http://flupy.org/data/flags'


def save_flag(img, filename):
    os.mkdir(DEST_DIR) if not os.path.exists(DEST_DIR) else None
    path = os.path.join(DEST_DIR, filename)
    with open(path, 'wb') as f:
        f.write(img)


def get_flag(cc):
    url = '{}/{cc}/{cc}.gif'.format(BASE_URL, cc=cc.lower())
    resp = requests.get(url)
    return resp.content


def show(text):
    print(text, end=' ')
    sys.stdout.flush()


def down_many(cc_list):
    for cc in sorted(cc_list):
        show(cc)
        img = get_flag(cc)
        save_flag(img, cc.lower() + '.gif')
    return len(cc_list)


def main(down_many):
    start = time.time()
    count = down_many(POP20_CC)
    time_use = time.time() - start
    print('\n{} flags downloaded in {:.2f}s'.format(count, time_use))


if __name__ == '__main__':
    main(down_many)

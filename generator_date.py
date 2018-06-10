import time
import random

start = (1900, 1, 1, 0, 0, 0, 0, 0, 0)
time_start = time.mktime(start)
end = (2018, 1, 1, 0, 0, 0, 0, 0, 0)
time_end = time.mktime(end)


class Date():
    def __init__(self):
        self.y = 1900
        self.m = 1
        self.d = 1

    def get_date(self, date):
        self.y = date.Y
        self.m = date.m
        self.d = date.d

    def __del__(self):
        pass


def get_date():
    time_ = random.randint(time_start, time_end)
    date_touple = time.localtime(time_)
    date = Date()
    date.y = time.strftime("%Y", date_touple)
    date.m = time.strftime("%m", date_touple)
    date.d = time.strftime("%d", date_touple)
    return date


if __name__ == '__main__':
    for i in range(10):
        time_ = random.randint(time_start, time_end)
        date_touple = time.localtime(time_)
        date = Date()
        date.y = time.strftime("%Y", date_touple)
        date.m = time.strftime("%m", date_touple)
        date.d = time.strftime("%d", date_touple)
        print(date.y, date.m, date.d)

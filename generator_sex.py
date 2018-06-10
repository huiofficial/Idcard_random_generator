import random
import string

sex = ['男', '女']


def random_sex():
    return ''.join(random.choice(sex) for _ in range(1))


def get_sex():
    sex = random_sex()
    return sex


if __name__ == '__main__':
    for i in range(10):
        print(get_sex())

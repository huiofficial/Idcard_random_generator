import random
import string

country = ['中国', '美国', '俄罗斯', '日本', '韩国', '新加坡', '尼泊尔', '英国',
          '德国', '意大利', '埃及', '南非', '保加利亚', '利比亚', '塞尔维亚', '挪威',
          '加拿大', '白俄罗斯', '缅甸', '印度', '菲律宾', '墨西哥', '朝鲜', '蒙古',
          '毛里求斯', '法国', '秘鲁', '阿根廷', '葡萄牙', '西班牙', '荷兰', '冰岛']


def random_country():
    return ''.join(random.choice(country) for _ in range(1))


def get_country():
    country = random_country()
    return country


if __name__ == '__main__':
    for i in range(50):
        print(random_country())

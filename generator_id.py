# -*- coding: utf-8 -*-
import random
import datetime


def getValidateCheckout(id17):
    '''获得校验码算法'''
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3,
              7, 9, 10, 5, 8, 4, 2]  # 十七位数字本体码权重
    validate = ['1', '0', 'X', '9', '8', '7',
                '6', '5', '4', '3', '2']  # mod11,对应校验码字符值

    sum = 0
    mode = 0
    for i in range(0, len(id17)):
        sum = sum + int(id17[i]) * weight[i]
    mode = sum % 11
    return validate[mode]


def get_id(sex=1):
    '''产生随机可用身份证号，sex = 1表示男性，sex = 0表示女性'''
    # 地址码产生
    from addr import addr  # 地址码
    addrInfo = random.randint(0, len(addr) - 1)
    addrId = addr[addrInfo][0]
    addrName = addr[addrInfo][1]
    idNumber = str(addrId)
    # 出生日期码
    start, end = "1960-01-01", "2018-01-01"  # 生日起止日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") -
            datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthDays = datetime.datetime.strftime(datetime.datetime.strptime(
        start, "%Y-%m-%d") + datetime.timedelta(random.randint(0, days)), "%Y%m%d")
    idNumber = idNumber + str(birthDays)
    # 顺序码
    for i in range(2):  # 产生前面的随机值
        n = random.randint(0, 9)  # 最后一个值可以包括
        idNumber = idNumber + str(n)
    # 性别数字码
    sexId = random.randrange(sex, 10, step=2)  # 性别码
    idNumber = idNumber + str(sexId)
    # 校验码
    checkOut = getValidateCheckout(idNumber)
    idNumber = idNumber + str(checkOut)
    # return idNumber,addrName,addrId,birthDays,sex,checkOut
    return idNumber


def getInfoFromId(id18):
    '''从身份证号码中得出个人信息：地址、生日、性别'''
    addrId = id18[0:6]
    from addr import addr  # 地址码
    for it in addr:
        if addrId == str(it[0]):  # 校验码
            addrName = it[1]
            break
    else:  # 未被break终止
        addrName = 'unknown'

    birthDays = datetime.datetime.strftime(
        datetime.datetime.strptime(id18[6:14], "%Y%m%d"), "%Y-%m-%d")
    sex = 'man' if int(id18[-2]) % 2 else 'woman'  # 0为女性，1为男性

    return addrName, birthDays, sex


if __name__ == '__main__':
    for i in range(10):
        print(get_id(0))

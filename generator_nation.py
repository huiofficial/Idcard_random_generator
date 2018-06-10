import random
import string

nation = ['汉族', '回族', '畲族', '塔塔尔族', '阿昌族', '哈萨克族', '土家族', '景颇族',
          '哈尼族', '土族', '白族', '维吾尔族', '保安族', '赫哲族', '乌孜别克族', '基诺族',
          '布依族', '拉祜族', '锡伯族', '黎族', '东乡族', '蒙古族', '仫佬族', '达斡尔族',
          '藏族', '毛南族', '裕固族', '俄罗斯族', '德昂族', '僳僳族', '瑶族', '朝鲜族',
          '布朗族', '满族', '彝族', '门巴族', '侗族', '苗族', '佤族', '羌族', '独龙族',
          '怒族', '珞巴族', '普米族', '傣族', '纳西族', '高山族', '壮族', '额伦春族',
          '塔吉克族', '京族', '仡佬族', '鄂温克族', '撒拉族', '柯尔克孜族', '水族']


def random_nation():
    return ''.join(random.choice(nation) for _ in range(1))


def get_nation():
    nation = random_nation()
    return nation


if __name__ == '__main__':
    for i in range(50):
        print(random_nation())

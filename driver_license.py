# -*- coding: utf-8 -*-
from generator_name import get_name
from generator_sex import get_sex
from generator_country import get_country
from generator_addr import get_addr
from generator_date import get_date
from generator_class import get_class

def generate():
    driver_license = []

    name = get_name()
    driver_license.append(name)

    sex = get_sex()
    driver_license.append(sex)

    country = get_country()
    driver_license.append(country)

    addr = get_addr(15)
    driver_license.append(addr)

    birthday_ = get_date()
    birthday = str(birthday_.y) + '-' + \
        str(birthday_.m) + '-' + str(birthday_.d)
    driver_license.append(birthday)

    license_validation_ = get_date()
    license_validation = str(license_validation_.y) + '-' + \
        str(license_validation_.m) + '-' + str(license_validation_.d)
    driver_license.append(license_validation)

    license_class = get_class()
    driver_license.append(license_class)

    return driver_license

if __name__ == '__main__':
    for i in range(10):
        driver_license = generate()
        '''
        for name, sex, country, addr, birthday, license_validation, license_class in driver_license:
            print('\n')
            print("***********************************************************")
            print("Name: ", name)
            print("Sex: ", sex)
            print("Nationality: ", country)
            print("Address: ", addr)
            print("Birthday: ", birthday)
            print("Date of first issue: ", license_validation)
            print("Class: ", license_class)
        '''
        print("***********************************************************")
        print("Name: ", driver_license[0])
        print("Sex: ", driver_license[1])
        print("Nationality: ", driver_license[2])
        print("Address: ", driver_license[3])
        print("Birthday: ", driver_license[4])
        print("Date of first issue: ", driver_license[5])
        print("Class: ", driver_license[6])

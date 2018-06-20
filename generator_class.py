import random
import string

license_classes = ['A1', 'A2', 'A3', 'B1', 'B2', 'C1', 'C2', 'C3',
          'C4', 'C5', 'D', 'E', 'F', 'M', 'N', 'P']


def random_class():
    return ''.join(random.choice(license_classes) for _ in range(1))


def get_class():
    license_class = random_class()
    return license_class


if __name__ == '__main__':
    for i in range(50):
        print(random_class())

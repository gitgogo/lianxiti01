#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 19:40
# @Author  : ralphliu
# @Site    : 
# @File    : study1201-class.py
# @Software: PyCharm

from time import sleep, localtime, time

# 当一个类中的属性、方法以双下划线开头，对象无法直接访问（会报错对象没有这个属性），但可以通过 obj._Clock__run() 访问到
# 单下划线开头的属性、方法，只是一种约定-表示类的私有属性，谨慎访问实际可以正常访问。
class Clock(object):
    """数字时钟"""

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    # clock = Clock(23, 59, 58)
    clock = Clock.now()  # 通过调用类方法创建对象
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

# property 装饰器的应用，实现getter setter方法
# __slots__变量限定属性
class Person:

    __slots__ = ['_name', '_age', '_gender']

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age < 16:
            print(f'{self._name}正在玩游戏')
        else:
            print(f'{self._name}正在学习')


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)  # 继承父类初始化方法
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self):
        pass

    def play(self):
        print(f'{self._name}重写父类方法')


# 静态方法的应用，在创建对象之前就可以调用的方法 属于类本身
class Triangle:

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c


def do_triangle():
    a, b, c = 3, 4, 5
    if Triangle.is_valid(a, b, c):
        t = Triangle(a, b, c)
        print(t.perimeter())


if __name__ == '__main__':
    # main()
    person = Person('小丽', 23)
    person.age = 25
    person._gender = 'female'
    print(person.name, person.age)
    person.play()

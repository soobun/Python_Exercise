# 9-3 用户：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。
# 在类User 中定义一个名为describe_user() 的方法，它打印用户信息摘要；
# 再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。


class User:
    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + ', ' + str(self.age) + ' years old.')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')


person1 = User('Eric', 'Brown', 22)
person1.describe_user()
person1.greet_user()

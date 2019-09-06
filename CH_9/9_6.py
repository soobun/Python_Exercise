# 9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为IceCreamStand 的类，
# 让它继承你为完成练习9-1或练习9-4而编写的Restaurant 类。
# 添加一个名为flavors 的属性，用于存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。
# 创建一个IceCreamStand 实例，并调用这个方法。


class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        self.cuisine_type = 'open'
        print('We are opening!')

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num


class IceCreamStand(Restaurant):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.flavors = ['Salt', 'Pine', 'Apple']


ics = IceCreamStand('DQ', 'ice-cream')
print(ics.flavors)

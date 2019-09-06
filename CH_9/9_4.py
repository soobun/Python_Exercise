# 9-4 就餐人数：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant 的实例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。
# 添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值，然后再次打印这个值。
# 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。


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


restaurant = Restaurant('KFC', 'Fast food')
print(restaurant.number_served)
restaurant.number_served = 100
print(restaurant.number_served)
restaurant.set_number_served(200)
print(restaurant.number_served)
restaurant.increment_number_served(70)
print(restaurant.number_served)

# 9-1 餐馆：创建一个名为Restaurant 的类，
# 其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。
# 创建一个名为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，
# 其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant 的实例，分别打印其两个属性，再调用前述两个方法。


class Restaurant:
    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self):
        print(self.restaurant_name + " " + self.cuisine_type)

    def open_restaurant(self):
        self.cuisine_type = 'open'
        print('We are opening!')


restaurant = Restaurant('Chinese restaurant', 'Chinese food')
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 8-6 城市名 ：编写一个名为city_country() 的函数，它接受城市的名称及其所属的国家。这个函数应返回一个格式类似于下面这样的字符串：
# "Santiago, Chile"
# 至少使用三个城市-国家对调用这个函数，并打印它返回的值。


def city_country(city, country):
    return city.title() + ', ' + country.title()


print(city_country('beijing', 'china'))
print(city_country('tokyo', 'Japan'))
print(city_country('london', 'United Kingdom'))

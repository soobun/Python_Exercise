# 6-11 城市 ：创建一个名为cities 的字典，其中将三个城市名用作键；
# 对于每座城市，都创建一个字典，并在其中包含该城市所属的国家、人口约数以及一个有关该城市的事实。
# 在表示每座城市的字典中，应包含country 、population 和fact 等键。将每座城市的名字以及有关它们的信息都打印出来。

cities = {'Beijing': {'country': 'China', 'population': 17000000, 'fact': 'the captial'},
          'Tokyo': {'country': 'Japan', 'population': 10000000, 'fact': 'the captial'},
          'Qingdao': {'country': 'China', 'population': 8000000, 'fact': 'the tour city'}
          }

for key, value in cities.items():
    print(key + ', a city of ' + value['country'] + ', has about ' + str(value['population']) + ' persons, '
          + value['fact'] + '.')

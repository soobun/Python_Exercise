# 6-9 喜欢的地方 ：创建一个名为favorite_places 的字典。在这个字典中，将三个人的名字用作键；对于其中的每个人，都存储他喜欢的1~3个地方。
# 遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {'Alice': ['Beijing', 'Shanghai', 'Guangzhou'],
                   'Bean': ['London', 'Paris', 'Lion'],
                   'Eric': ['Hong Kong', 'Macau', 'Singapore']}
for key, value in favorite_places.items():
    print(key + ' wants to go to ' + value[0] + ', ' + value[1] + ' and ' + value[2] + '.')

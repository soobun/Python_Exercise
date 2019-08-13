# 6-7 人 ：在为完成练习6-1而编写的程序中，再创建两个表示人的字典，然后将这三个字典都存储在一个名为people 的列表中。
# 遍历这个列表，将其中每个人的所有信息都打印出来。

user_info_1 = {'first_name': 'Eric',
               'last_name': 'Brown',
               'age': 22,
               'city': 'Qingdao'}
user_info_2 = {'first_name': 'Alice',
               'last_name': 'C',
               'age': 27,
               'city': 'Beijing'}
user_info_3 = {'first_name': 'Tommy',
               'last_name': 'Trump',
               'age': 72,
               'city': 'New York'}
people = [user_info_1, user_info_2, user_info_3]
for user_info in people:
    print(user_info['first_name'] + ' ' + user_info['last_name'] + ', ' + str(user_info['age']) +
          ' years old, lives in ' + user_info['city'] + '.')

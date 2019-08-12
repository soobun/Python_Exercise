# 5-9 处理没有用户的情形 ：在为完成练习5-8编写的程序中，添加一条if 语句，检查用户名列表是否为空。
# 如果为空，就打印消息“We need to find some users!”。
# 删除列表中的所有用户名，确定将打印正确的消息。

user_list = ['admin', 'Eric', 'Sam', 'Tom', 'Jerry']
user_list.clear()
if user_list:
    for user in user_list:
        if user == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello ' + user + ', thank you for logging in again')
else:
    print("We need to find some users!")

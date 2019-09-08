# 10-12 记住喜欢的数字：如果存储了用户喜欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。
# 运行这个程序两次，看看它是否像预期的那样工作。

import json

try:
    with open('like_number.json') as file_object:
        num = json.load(file_object)
        print('The number you like is ' + str(num))
except FileNotFoundError:
    print('File Not Found...')
    num = int(input('Please input your favorite number here: '))
    with open('like_number.json', 'w') as file_object:
        json.dump(num, file_object)

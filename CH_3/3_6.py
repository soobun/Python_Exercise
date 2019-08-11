# 3-6 添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
# 以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
# 使用insert() 将一位新嘉宾添加到名单开头。
# 使用insert() 将另一位新嘉宾添加到名单中间。
# 使用append() 将最后一位新嘉宾添加到名单末尾。
# 打印一系列消息，向名单中的每位嘉宾发出邀请。

names = ['Sam', 'Amy', 'Tom', 'Jerry']
print(names[0] + ', eat dinner with me.')
print(names[1] + ', eat dinner with me.')
print(names[2] + ', eat dinner with me.')
print(names[3] + ', eat dinner with me.')

print(names[3] + " can't eat dinner with me.")
names[3] = 'Nephew'
print(names[3] + ', eat dinner with me.')

print('I found a bigger table!')
names.insert(0, 'Sara')
names.insert(3, 'Daming')
names.append('Zac')
print(names[0] + ', eat dinner with me.')
print(names[1] + ', eat dinner with me.')
print(names[2] + ', eat dinner with me.')
print(names[3] + ', eat dinner with me.')
print(names[4] + ', eat dinner with me.')
print(names[5] + ', eat dinner with me.')

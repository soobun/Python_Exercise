# 3-7 缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
# 使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进晚餐。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
# 使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。


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

print('Today, only two person can eat with me.')
print(names.pop() + ', sorry.')
print(names.pop() + ', sorry.')
print(names.pop() + ', sorry.')
print(names.pop() + ', sorry.')
print('Welcome, ' + names[0])
print('Welcome, ' + names[1])
del names[0]
del names[1]
print(names)

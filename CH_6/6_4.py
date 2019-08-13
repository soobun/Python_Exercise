# 6-4 词汇表2 ：既然你知道了如何遍历字典，现在请整理你为完成练习6-3而编写的代码，将其中的一系列print 语句替换为一个遍历字典中的键和值的循环。
# 确定该循环正确无误后，再在词汇表中添加5个Python术语。当你再次运行这个程序时，这些新术语及其含义将自动包含在输出中。

dictionary = {'int': '整型',
              'char': '字符型',
              'float': '浮点型',
              'long': '长整型',
              'byte': '字节型'}
for key,value in dictionary.items():
    print(key+':\n\t'+value)

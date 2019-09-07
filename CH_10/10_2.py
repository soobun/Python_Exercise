# 10-2 C语言学习笔记：可使用方法replace() 将字符串中的特定单词都替换为另一个单词。
# 读取你刚创建的文件learning_python.txt中的每一行，
# 将其中的Python都替换为另一门语言的名称，如C。将修改后的各行都打印到屏幕上。

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line.replace('python', 'Java').rstrip())

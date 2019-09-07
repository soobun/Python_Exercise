# 编写一个程序，它读取你在项目Gutenberg中获取的文件，并计算单词'the' 在每个文件中分别出现了多少次。

num = 0
with open('George Washington.txt', encoding='utf-8') as file_object:
    for line in file_object:
        num += line.lower().count('the')
print(num)

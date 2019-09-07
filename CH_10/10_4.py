# 10-4 访客名单：编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，
# 并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。

with open('guest_book.txt', 'w') as file_object:
    name = input("What's your name? Input 'q' to quit. ")
    while name != 'q':
        print('Hello, ' + name + '!')
        file_object.write(name + '\n')
        name = input("What's your name? Input 'q' to quit. ")

# 8-8 用户的专辑 ：在为完成练习8-7编写的程序中，编写一个while 循环，让用户输入一个专辑的歌手和名称。
# 获取这些信息后，使用它们来调用函数make_album() ，并将创建的字典打印出来。在这个while 循环中，务必要提供退出途径。


def make_album(singer, album, num=0):
    if num == 0:
        return {'singer': singer, 'album': album}
    else:
        return {'singer': singer, 'album': album, 'num': num}


name = input('Input a name here, enter q to quit: ')
while name != 'q':
    album = input('Input album name here: ')
    print(make_album(name, album))
    name = input('Input a name here, enter q to quit: ')

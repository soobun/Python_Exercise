# 8-11 不变的魔术师 ：修改你为完成练习8-10而编写的程序，在调用函数make_great() 时，向它传递魔术师列表的副本。
# 由于不想修改原始列表，请返回修改后的列表，并将其存储到另一个列表中。
# 分别使用这两个列表来调用show_magicians() ，确认一个列表包含的是原来的魔术师名字，
# 而另一个列表包含的是添加了字样“the Great”的魔术师名字。


def show_magicians(list):
    for name in list:
        print(name)


def make_great(list):
    for i in range(len(list)):
        list[i] = 'the Great ' + list[i]
    return list


list = ['Bean', 'Eric', 'Amy', 'Sara', 'Trump']
list_copy = make_great(list[:])
show_magicians(list)
show_magicians(list_copy)

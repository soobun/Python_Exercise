# 8-9 魔术师 ：创建一个包含魔术师名字的列表，
# 并将其传递给一个名为show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。


def show_magicians(list):
    for name in list:
        print(name)


list = ['Bean', 'Eric', 'Amy', 'Sara', 'Trump']
show_magicians(list)

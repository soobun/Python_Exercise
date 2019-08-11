# 4-7 3的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。

list = [num for num in range(3, 31, 3)]
for num in list:
    print(num)

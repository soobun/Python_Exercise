# 4-8 立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。
# 请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循环将这些立方数都打印出来。

list = []
for num in range(1, 11):
    list.append(num ** 3)
for num in list:
    print(num)

# 4-6 奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；
# 再使用一个for 循环将这些数字都打印出来。

numbers = [num for num in range(1, 21, 2)]
for num in numbers:
    print(num)

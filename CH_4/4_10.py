# 4-10 切片 ：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
# 打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
# 打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
# 打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。

list = [num for num in range(1, 8)]
print("The first three items in the list are:" + str(list[:3]))
print("Three items from the middle of the list are:" + str(list[2:5]))
print("The last three items in the list are:" + str(list[-3:]))

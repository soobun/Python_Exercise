# 5-2 更多的条件测试 ：你并非只能创建10个测试。如果你想尝试做更多的比较，可再编写一些测试，并将它们加入到conditional_tests.py中。
# 对于下面列出的各种测试，至少编写一个结果为True 和False 的测试。
# 检查两个字符串相等和不等。
# 使用函数lower() 的测试。
# 检查两个数字相等、不等、大于、小于、大于等于和小于等于。
# 使用关键字and 和or 的测试。
# 测试特定的值是否包含在列表中。
# 测试特定的值是否未包含在列表中。

print('apple' == 'apple')
print('apple' == 'Apple')

print('Apple'.lower() == 'apple')

print(1 == 1)
print(1 != 0)
print(1 > 0)
print(1 < 0)
print(1 >= 0)
print(1 <= 0)

print(1 >= 0 and 5 < 7)
print(1 >= 0 or 8 < 7)

list = [1, 3, 5, 7, 9]
print(1 in list)
print(2 not in list)

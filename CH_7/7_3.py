# 7-3 10的整数倍 ：让用户输入一个数字，并指出这个数字是否是10的整数倍。

num = input('Input a number here:')
if int(num) % 10 == 0:
    print('Yes')
else:
    print('No')

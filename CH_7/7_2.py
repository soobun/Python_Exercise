# 7-2 餐馆订位 ：编写一个程序，询问用户有多少人用餐。如果超过8人，就打印一条消息，指出没有空桌；否则指出有空桌。

num = input('How many people? ')
if int(num) > 8:
    print("Sorry, we don't have big table.")
else:
    print("Welcome!")

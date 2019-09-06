# 9-5 尝试登录次数：在为完成练习9-3而编写的User 类中，添加一个名为login_attempts 的属性。
# 编写一个名为increment_login_attempts() 的方法，
# 它将属性login_attempts 的值加1。再编写一个名为reset_login_attempts() 的方法，它将属性login_attempts 的值重置为0。
# 根据User 类创建一个实例，再调用方法increment_login_attempts() 多次。
# 打印属性login_attempts 的值，确认它被正确地递增；
# 然后，调用方法reset_login_attempts() ，并再次打印属性login_attempts 的值，确认它被重置为0。


class User:
    def __init__(self, fn, ln, age):
        self.first_name = fn
        self.last_name = ln
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + ', ' + str(self.age) + ' years old.')

    def greet_user(self):
        print('Hello, ' + self.first_name.title() + ' ' + self.last_name.title() + '!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Eric', 'Brown', 22)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)

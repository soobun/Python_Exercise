# 9-7 管理员：管理员是一种特殊的用户。编写一个名为Admin 的类，让它继承你为完成练习9-3或练习9-5而编写的User 类。
# 添加一个名为privileges 的属性，用于存储一个由字符串（如"can add post" 、"can delete post" 、"can ban user" 等）组成的列表。
# 编写一个名为show_privileges() 的方法，它显示管理员的权限。创建一个Admin 实例，并调用这个方法。


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


class Admin(User):
    def __init__(self, fn, ln, age):
        super().__init__(fn, ln, age)
        self.privileges = 'can add post'

    def show_privileges(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + ' ' + self.privileges + '.')


user = Admin('Eric', 'Brown', 22)
user.show_privileges()

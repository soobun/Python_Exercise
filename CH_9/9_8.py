# 9-8 权限：编写一个名为Privileges 的类，它只有一个属性——privileges ，其中存储了练习9-7 所说的字符串列表。
# 将方法show_privileges() 移到这个类中。
# 在Admin 类中，将一个Privileges 实例用作其属性。创建一个Admin 实例，并使用方法show_privileges() 来显示其权限。


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


class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print(self.privileges, end='')


class Admin(User):
    def __init__(self, fn, ln, age, privileges):
        super().__init__(fn, ln, age)
        self.privileges = Privileges(privileges)

    def show_privileges(self):
        print(self.first_name.title() + ' ' + self.last_name.title() + ' ', end='')
        self.privileges.show_privileges()
        print('.')


user = Admin('Eric', 'Brown', 22, 'can ban user')
user.show_privileges()

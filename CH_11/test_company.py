import unittest
from CH_11.company import Employee


class TestCompany(unittest.TestCase):
    def setUp(self):
        self.my_employee = Employee('Eric', 'Brown', 17000)
        self.add_salary = [3000, 5000, 7000]
        self.result_salary = [20000, 22000, 24000]

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        test_result = self.my_employee.show_salary()
        self.assertEqual(test_result, 22000)
        self.my_employee.salary=17000

    def test_give_custom_raise(self):
        for num in self.add_salary:
            self.my_employee.give_raise(num)
            test_result = self.my_employee.show_salary()
            self.assertIn(test_result, self.result_salary)
            self.my_employee.salary = 17000


unittest.main()

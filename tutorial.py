# from car import Car
#
# my_car = Car("Honda", "Civic", 2008)
# print(my_car.make)
# my_car.stop()

class A:
    def __init__(self):
        print("Im class A")
        self.a_var = "Hi"

class B(A):
    pass

a = A()
b = B()

# class Person:
#     def __init__(self, f_name, l_name):
#         self._first_name = f_name
#         self._last_name = l_name
# 
#     def print_name(self):
#         print(self._first_name, self._last_name)
#
# class Student(Person):
#     def __init__(self, s_id, f_name, l_name):
#         super().__init__(f_name, l_name)
#         self._student_ID = s_id
#
#     def print_name(self):
#         print(self._student_ID)
#         super().print_name()





# x = Student(12345, "Deidre", "Murphy")
# x.print_name()
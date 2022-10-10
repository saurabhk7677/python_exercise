# class Animal(object):
#     pass

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name

# class Person(object):
#     def __init__(self, name):
#         self.name = name
#         self.pet = None 

# class Employee(Person):
#     def __init__(self, name, salary):
#         super(Employee, self).__init__(name)
#         self.salary = salary

# class Fish(object):
#     pass 

# class Salmon(Fish):
#     pass

# class Halibut(Fish):
#     pass

#########################################################################################################

class Father:
    def __init__(self):
        print("Father class constructor")
        self._name = "prakash"
        self._age = 26

    def _get_varible(self):
        print("Father class instance method")
        print("name: ",self._name)
        print("Age:",self._age)

class Son(Father):
    def __init__(self):
        #super().__init__(self)
        print("son class constructor")
        self._name = "abhi"
        self._age = 25

    def _get_values(self):
        print("son class instance method")
        print("Name:", self._name)
        print("Age:",self._age)

s = Son()
s._get_values()
s._get_varible()
# #x = 10
# try:
#   print(x)
# except Exception as e:
#     print(e)   
#     print("Software not working")


# import random
# x = random.randint(999,9999)
# print(x)

#########################################


class A:
  def __init__(self):
    self.__dog = "German tell"

  def __num(self):
    print("This is a integer data type")

  def __sen(self):
    print("This is a string data type")

class B:
  def __init__(self):
    super().__init__()
    self.__number = 7677
    self.__string = "hii saurabh"

a = A()
print(a._A__dog)
a._A__num()
a._A__sen()

b = B()
print(b._B__number)
print(b._B__string)

# public
# protected
# private


# public access specifire.............................................................................................
# class A:
#     def __init__(self):
#         self.sk = 20
#     def cont(self):
#         print("This is a contact page")

# class B:
#     def abt(self):
#         print("This is aboutus page")

# a = A()
# a.cont()
# print(a.sk)

# b = B()
# b.abt()
# print()

# protected access specifire.........................................................................................

# class ABC:
#     def __init__(self):
#         self._pk = 30
#         # df = XYZ()
#         # df._caltr()

#     def _cal(self):
#         print("This is a calender page")

# class XYZ:
#     def __init__(self):
#         self._kb = 100
#         ad = ABC()
#         ad._cal()
#         print(ad._pk)
        
#     def _caltr(self):
#         print("This is a calculator page")

# ab = ABC()
# ab._cal()
# print(ab._pk)
# print()

# xy = XYZ()
# xy._caltr()
# print(xy._kb)
# print()


# private access specifire..........................................................................................

class Pen:
    def __init__(self):
        self.__pen = 10

    def __color(self):
        print("This is a red pen")

# p = Pen()
# p._Pen__color()

class Book:
    def __init__(self,book):
        self.__book = book

    def __rougf(self):
        print("This is a rougf book")

p = Pen()
print(p._Pen__pen)
p._Pen__color()

b = Book("The Gang of foure")
print(b._Book__book)
b._Book__rougf()
print()

###########################################################################################################################


# class Primary():
# 	def __init__(self, param1, param2):
# 		self.param1 = param1
# 		self.__param2 = param2

# 	def getP1(self):
# 		return self.param1

# 	def getP2(self):
# 		return self.__param2
    
#     def help(self):
#         self.getP1()
#         self.__getP2()
    
# a = Primary('x', 'y')
# a.help()


# class Secondary(Primary):
# 	def __init__(self, param1, param2, param3):
# 		Primary.__init__(self, param1, param2)
# 		self.__param3 = param3

# 	def getP3(self):
# 		return self.__param3

# 	def test(self):
# 		print (self.__param2)

# Main

# p = Primary('a', 'b')
# s = Secondary('a', 'b', 'c')
# print(s.param1)
# #print(s.__param2)

# print(s.getP1())
# #print(s.__param2())
# print(s.getP3())
# print("********************************************")
# print()

# ###################################################################################################

# Creating a class
# class A:

# 	# Declaring public method
# 	def fun(self):
# 		print("Public method")

# 	# Declaring private method
# 	def __fun(self):
# 		print("Private method")

# 	# Calling private method via
# 	# another method
# 	def Help(self):
# 		self.fun()
# 		self.__fun()


# # Driver's code
# obj = A()
# obj.Help()
# print()
#################################################################

# Creating a class
class A:

	# Declaring public method
	def fun(self):
		print("Public method")

	# Declaring private method
	def __fun(self):
		print("Private method")


# Driver's code
obj = A()
obj.fun()

# Calling the private member
# through name mangling
obj._A__fun()

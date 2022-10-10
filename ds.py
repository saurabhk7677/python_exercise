class Parent(object):
    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        a = super(Child, self).altered()
        print(a)
        print("CHILD, AFTER PARENT altered()")


dad = Parent()
son = Child()
a = son.altered()

print(a)
print(type(a))
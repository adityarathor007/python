class A:
    label="A: Base class"

class B(A):
    label="B: Child1 class"


class C(A):
    label="C: Child2 class"

# MRO: order of inheritance decides whose attributes and method will be called if collision happens
class D(C,B):
    pass


obj=D()
print(obj.label)



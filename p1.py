# function without parameter
def fun():
    print("hello")
    
fun()
# function with parameter
def fun1(a,b):
    print(a+b)
fun1(1,2)
# class without parameter
class fun2:
    def f1():
        print("hello : 11111")
a=fun2
a.f1()

# class with parameter
class fun3():
    def f2(a,b):
        print("mul is ",a+b)
a=fun3
a.f2(2,5)


# this code will not work because it not support method overloading
#class fun4:
#    def sum():
#        print("sum")
#    def sum(a):
#        print("mul",a)
#aa=fun4
#aa.sum()
#aa.sum(5)

# class with parameter overridding
class fun4:
    def sum():
        print("sum")
    def sum():
        print("mul")
aa=fun4
aa.super().sum()



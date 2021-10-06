class A:

    def method(self):
        print('method of A class')

class B(A):

    def method(self):
        print('method of B class')

class C(A):

    def method(self):
        print('method of C class')

    def method_of_c(self):
        print('secondary method')

class D(C, B):

    def method(self):
        print('method of D class')
        B.method(self)
        C.method(self)

obj = D()
obj.method()
print(D.mro())












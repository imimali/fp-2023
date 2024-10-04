class A:
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b

    def f(self):
        print("F")

    def g(self):
        print("G")

if __name__ == '__main__':
    a=A()
    print(getattr(a,'f'))
    print(getattr(A,'f'))
    print(a.__dict__)
    print(A.__dict__)
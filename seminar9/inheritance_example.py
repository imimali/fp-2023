class A:
    def __init__(self, a):
        self.a = a

    def f(self):
        print(f"I am {self} and with a={self.a}")


class B(A):
    def __init__(self, a):
        super().__init__(a)

    def f(self):
        super().f()
        print(f"I am B={self} and overrode A.f ")


if __name__ == "__main__":
    a = A(123)
    a.f()
    a2 = A(123)
    a2.f()
    print(a, a2)
    B(234).f()

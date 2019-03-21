# python反射机制
class A:
    x = 1
    y = 2.3
    z = 'hello'


if __name__ == "__main__":
    A1 = A()
    t = 'z'
    print(getattr(A1, t))
    setattr(A1, t, 'bye')
    print(getattr(A1, t))
    print(A1.z)
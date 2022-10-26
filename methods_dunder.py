# Magic Methods and Dunder

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):  # Object String
        return 'X:{}, Y:{}'.format(self.x, self.y)

    def __repr__(self):  # Representation
        return 'X:{}, Y:{}'.format(self.x, self.y)

    def __len__(self):
        return self.x * self.y

    def __call__(self, *args, **kwargs):
        print("Call me Vector!")


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")

    def __str__(self):
        return '{} {}'.format(self.name, self.age)

    def __repr__(self):
        return '{} {}'.format(self.name, self.age)


if __name__ == '__main__':

    p = Person("Henrique", 25)
    print(p)
    v1 = Vector(15, 25)
    v2 = Vector(60, 30)
    v3 = v1 + v2
    print(v3)

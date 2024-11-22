# throw an operator overloading error
"""
class sum:
    def __init__(self, a, b) -> None:
        self.num = a * b


s1 = sum(1, 2)
s2 = sum(2, 3)
print(s1 + s2)
"""

# solving an operator overloading error


class sum:
    def __init__(self, x) -> None:
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __gt__(self, other):
        return self.x > other.x

    def __lt__(self, other):
        return self.x < other.x

    def __eq__(self, other) -> bool:
        return self.x == other.x


num1 = sum(10)
num2 = sum(20)
str1 = sum("cse")
str2 = sum("111")
print(num1 + num2)
print(num1.__add__(num2))

print(str1 + str2)  # str1.__add__(str2)

print(num1 > num2)
print(num1.__gt__(num2))

print(num1 < num2)
print(num1.__lt__(num2))

print(num1 == num2)
print(num1.__eq__(num2))

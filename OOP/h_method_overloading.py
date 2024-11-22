from multipledispatch import dispatch


class Calculator:  # default constructor runing and method overloading
    # def product(self, num1=None, num2=None, num3=None):
    #     if num1 != None and num2 != None and num3 != None:
    #         print(num1 * num2 * num3)
    #     elif num1 != None and num2 != None:
    #         print(num1 * num2)
    #     else:
    #         print(num1)

    # def product(self, *nums):  # unknown number of arguments, tuple
    #     print(nums)
    #     pro = 1
    #     for x in nums:
    #         pro *= x
    #     print(pro)

    @dispatch(int, int)
    def product(self, a, b):
        print(a * b)

    @dispatch(int, int, int)
    def product(self, a, b, c):
        print(a * b * c)


c1 = Calculator()
# c1.product()
# c1.product(1)
c1.product(1, 2)
c1.product(1, 2, 3)
# c1.product(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

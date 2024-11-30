from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def method1(self):
        pass


class B(A):
    def method1(self):
        print("method1")

    def method2(self):
        print("method2")


a = B()

import re

class I1(int):
    def __init__(self, a):
        self.a = a
    def __add__(self, b):
        return I1(self.a + b.a)
    def __sub__(self, b):
        return I1(self.a * b.a)

class I2(I1):
    def __add__(self, b):
        return I2(self.a * b.a)
    def __mul__(self, b):
        return I2(self.a + b.a)

f1 = [ l.replace('*','-') for l in open('input').readlines()]
print(sum([eval(re.sub(r"(\d+)", r"I1(\1)", l)) for l in f1]))

f2 = [ l.replace('+','*').replace('-','+') for l in f1]
print(sum([eval(re.sub(r"(\d+)", r"I2(\1)", l)) for l in f2]))

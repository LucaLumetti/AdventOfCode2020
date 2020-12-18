import re

class I1(int):
    def __add__(self, b):
        return I1(self.real + b.real)
    def __sub__(self, b):
        return I1(self.real * b.real)

class I2(int):
    def __add__(self, b):
        return I2(self.real * b.real)
    def __mul__(self, b):
        return I2(self.real + b.real)

f1 = [ l.replace('*','-') for l in open('input').readlines()]
print(sum([eval(re.sub(r"(\d+)", r"I1(\1)", l)) for l in f1]))

f2 = [ l.replace('+','*').replace('-','+') for l in f1]
print(sum([eval(re.sub(r"(\d+)", r"I2(\1)", l)) for l in f2]))

import re

class NewInteger(int):
    def __init__(self, a):
        self.a = a
    def __add__(self, b):
        return NewInteger(self.a * b.a)
    def __mul__(self, b):
        return NewInteger(self.a + b.a)

f = open('input').readlines()
print(sum([eval(re.sub(r"(\d+)", r"NewInteger(\1)", l, 0, re.MULTILINE).replace('+','p').replace('*','m').replace('p','*').replace('m','+')) for l in f]))

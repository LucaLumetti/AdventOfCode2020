import numpy as np
class Interpreter:
    def __init__(self, code, acc=0, ip=0):
        self.code = code
        self.accumulator = acc
        self.instr_pointer = ip
        self.history = []
        self.executing = True
        self.loop = False

    def exec(self):
        if(not self.executing): return
        if(self.instr_pointer >= len(self.code)):
            self.executing = False
            return

        instr, value = self.code[self.instr_pointer]
        if(type(value) != "int"):
            value = int(value)
        self._exec(instr, value)

    def _exec(self, instr, value):
        if(self.instr_pointer in self.history):
            self.executing = False
            self.loop = True

        self.history.append(self.instr_pointer)
        if(instr == "acc"):
            self._acc(value)
        elif(instr == "jmp"):
            self._jmp(value)
            return
        elif(instr == "nop"):
            pass
        self.instr_pointer += 1

    def _acc(self, value):
        self.accumulator += value
        pass

    def _jmp(self, value):
        self.instr_pointer += value
        pass

    def _nop(self):
        pass

f = np.array([ np.array(l.rstrip().split(' ')) for l in open('input', 'r').readlines() ])

interpreter = Interpreter(code=f)
while(interpreter.executing):
    interpreter.exec()

print(interpreter.accumulator)

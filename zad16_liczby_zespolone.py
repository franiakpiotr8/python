# !python


import math

print("==========zadanie16==========")

class Complex:
    def __init__(self, realpart, imagpart):
        self.real = realpart
        self.imag = imagpart

    def __add__(self, obj_b):
        temp = Complex(0, 0)
        temp.real = self.real + obj_b.real
        temp.imag = self.imag + obj_b.imag
        return temp

    def __sub__(self, obj_b):
        temp = Complex(0, 0)
        temp.real = self.real - obj_b.real
        temp.imag = self.imag - obj_b.imag
        return temp

    def __mul__(self, obj_b):
        temp = Complex(0, 0)
        temp.real = self.real * obj_b.real - self.imag * obj_b.imag
        temp.imag = self.imag * obj_b.real + self.real * obj_b.imag
        return temp

    def conj(self):
        self.imag = -self.imag

    def modulus(self):
        return math.sqrt(pow(self.real, 2) + pow(self.imag, 2))


a = Complex(10, 3)
b = Complex(7, 12)
print("a =" + str(a.real) + "+i(" + str(a.imag) + ")")
print("b =" + str(b.real) + "+i(" + str(b.imag) + ")")
print("a + b=" + str((a+b).real) + "+i(" + str((a+b).imag) + ")")
print("a - b=" + str((a-b).real) + "+i(" + str((a-b).imag) + ")")
print("a * b=" + str((a*b).real) + "+i(" + str((a*b).imag) + ")")
a.conj()
print("Conjunction a =" + str(a.real) + "+i(" + str(a.imag) + ")")
b.modulus()
print("Modulus b =" + str(b.modulus()))

import random
import math
import sys
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = (b**2)- (4*a*c)

if D > 0:
    D = math.sqrt(D)
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    print({x1},{x2})
elif D == 0:
    x = -b / 2 * a
    print({x})
elif D < 0:
    print("Нет корней")
import math

def bisection(f, a, b):
    while (b - a) / 2 > 0.0000005:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# 1(a) x^3 = 9
f1a = lambda x: x**3 - 9
root1a = bisection(f1a, 2, 3)


# 1(b) 3x^3 + x^2 = x + 5
f1b = lambda x: 3*x**3 + x**2 - x - 5
root1b = bisection(f1b, 1, 2)


# 1(c) cos^2(x) + 6 = x
f1c = lambda x: math.cos(x)**2 + 6 - x
root1c = bisection(f1c, 6, 7)


print("1(a) =", f"{root1a:.6f}")
print("1(b) =", f"{root1b:.6f}")
print("1(c) =", f"{root1c:.6f}")

import math

def bisection(f, a, b):
    while (b - a) / 2 > 0.000000005:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# 2(a) x^5 + x = 1
f2a = lambda x: x**5 + x - 1
root2a = bisection(f2a, 0, 1)


# 2(b) sin(x) = 6x + 5
f2b = lambda x: math.sin(x) - 6*x - 5
root2b = bisection(f2b, -1, 0)


# 2(c) ln(x) + x^2 = 3
f2c = lambda x: math.log(x) + x**2 - 3
root2c = bisection(f2c, 1, 2)


print("2(a) =", f"{root2a:.8f}")
print("2(b) =", f"{root2b:.8f}")
print("2(c) =", f"{root2c:.8f}")

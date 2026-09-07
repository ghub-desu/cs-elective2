import math
import matplotlib.pyplot as plt


# Bisection Method
def bisection(f, a, b):
    while (b - a) / 2 > 0.0000005:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# ==================================================
# 3(a) 2x^3 - 6x - 1 = 0
# ==================================================

f3a = lambda x: 2*x**3 - 6*x - 1

intervals3a = [(-2, -1), (-1, 0), (1, 2)]

print("3(a)")
for a, b in intervals3a:
    root = bisection(f3a, a, b)
    print(f"Interval [{a}, {b}] -> Root = {root:.6f}")


# Plot 3(a)
x = [i / 100 for i in range(-300, 301)]
y = [f3a(i) for i in x]

plt.figure()
plt.plot(x, y)
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.title(r"$2x^3 - 6x - 1 = 0$")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")
plt.show()


# ==================================================
# 3(b) e^(x-2) + x^3 - x = 0
# ==================================================

f3b = lambda x: math.exp(x - 2) + x**3 - x

intervals3b = [(-2, -1), (-0.5, 0.5), (0.5, 1.5)]

print("\n3(b)")
for a, b in intervals3b:
    root = bisection(f3b, a, b)
    print(f"Interval [{a}, {b}] -> Root = {root:.6f}")


# Plot 3(b)
x = [i / 100 for i in range(-200, 151)]
y = [f3b(i) for i in x]

plt.figure()
plt.plot(x, y)
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.title(r"$e^{x-2} + x^3 - x = 0$")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")
plt.show()


# ==================================================
# 3(c) 1 + 5x - 6x^3 - e^(2x) = 0
# ==================================================

f3c = lambda x: 1 + 5*x - 6*x**3 - math.exp(2*x)

intervals3c = [(-1.7, -0.7), (-0.7, 0.3), (0.3, 1.3)]

print("\n3(c)")
for a, b in intervals3c:
    root = bisection(f3c, a, b)
    print(f"Interval [{a}, {b}] -> Root = {root:.6f}")


# Plot 3(c)
x = [i / 100 for i in range(-170, 131)]
y = [f3c(i) for i in x]

plt.figure()
plt.plot(x, y)
plt.axhline(0)
plt.axvline(0)
plt.grid()
plt.title(r"$1 + 5x - 6x^3 - e^{2x} = 0$")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")
plt.show()

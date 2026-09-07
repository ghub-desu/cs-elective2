import math
import matplotlib.pyplot as plt


# --------------------------------------------------
# Bisection Method
# --------------------------------------------------

def bisection(f, a, b):
    if f(a) == 0:
        return a

    if f(b) == 0:
        return b

    while (b - a) / 2 > 0.0000005:
        c = (a + b) / 2

        if f(c) == 0:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2


# --------------------------------------------------
# Find intervals of length 1
# --------------------------------------------------

def find_intervals(f, start=-5, end=5, step=0.01):
    intervals = []
    x = start

    while x + 1 <= end:
        a = round(x, 2)
        b = round(x + 1, 2)

        if f(a) == 0 or f(a) * f(b) < 0:
            intervals.append((a, b))

        x += step

    return intervals


# --------------------------------------------------
# Remove overlapping intervals
# --------------------------------------------------

def choose_intervals(f, intervals):
    selected = []
    roots = []

    for a, b in intervals:
        root = bisection(f, a, b)

        # Check if this root is already found
        already_found = False

        for r in roots:
            if abs(root - r) < 0.001:
                already_found = True
                break

        if not already_found:
            roots.append(root)
            selected.append((a, b))

    return selected


# ==================================================
# 3(a)
# 2x^3 - 6x - 1 = 0
# ==================================================

f3a = lambda x: 2*x**3 - 6*x - 1

intervals = find_intervals(f3a)
intervals = choose_intervals(f3a, intervals)

print("3(a)  2x^3 - 6x - 1 = 0")

for a, b in intervals:
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
# 3(b)
# e^(x-2) + x^3 - x = 0
# ==================================================

f3b = lambda x: math.exp(x - 2) + x**3 - x

intervals = find_intervals(f3b)
intervals = choose_intervals(f3b, intervals)

print("\n3(b)  e^(x-2) + x^3 - x = 0")

for a, b in intervals:
    root = bisection(f3b, a, b)
    print(f"Interval [{a}, {b}] -> Root = {root:.6f}")


# Plot 3(b)

x = [i / 100 for i in range(-300, 301)]
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
# 3(c)
# 1 + 5x - 6x^3 - e^(2x) = 0
# ==================================================

f3c = lambda x: 1 + 5*x - 6*x**3 - math.exp(2*x)

intervals = find_intervals(f3c)
intervals = choose_intervals(f3c, intervals)

print("\n3(c)  1 + 5x - 6x^3 - e^(2x) = 0")

for a, b in intervals:
    root = bisection(f3c, a, b)
    print(f"Interval [{a}, {b}] -> Root = {root:.6f}")


# Plot 3(c)

x = [i / 100 for i in range(-300, 301)]
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

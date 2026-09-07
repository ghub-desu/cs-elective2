import math


# ==========================================================
# 5. g(x) = cos^2(x)
# ==========================================================


def g(x):
    return math.cos(x) ** 2


# Initial guess
x = 1

# Six correct decimal places
tolerance = 0.5e-6


print("================================================")
print("5. g(x) = cos^2(x)")
print("================================================")

print("Iteration        x_n                 Error")
print("-----------------------------------------------")

print(f"{0:<17}{x:<20.10f}-")


for n in range(1, 1000):

    x_new = g(x)

    error = abs(x_new - x)

    print(f"{n:<17}{x_new:<20.10f}{error:.10f}")

    if error < tolerance:
        print("-----------------------------------------------")
        print(f"Fixed Point: {x_new:.6f}")
        print(f"Iterations: {n}")
        break

    x = x_new


# ==========================================================
# Theorem 1.6
# ==========================================================

# g(x) = cos^2(x)
#
# g'(x) = -2 sin(x) cos(x)
#
#      = -sin(2x)

r = x_new

derivative = -math.sin(2 * r)

S = abs(derivative)


print("\n================================================")
print("Theorem 1.6 - Local Convergence")
print("================================================")

print(f"Fixed point r = {r:.6f}")
print(f"g'(r) = {derivative:.6f}")
print(f"S = |g'(r)| = {S:.6f}")

if S < 1:
    print("Since S < 1, Fixed-Point Iteration converges locally.")
else:
    print("Since S >= 1, Fixed-Point Iteration does not converge locally.")

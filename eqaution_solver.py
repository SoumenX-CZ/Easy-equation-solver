from sympy.solvers import solve
from sympy import Symbol

x = Symbol("x")
print(solve(x ** 2 - 1, x))
print(solve(x ** 3 + x ** 2 + x + 1, x))
print(solve(x ** 3 - 0 * x ** 2 + 4 * x - 5, x))
# def a():
#     import numpy as np

#     x = np.array([0, 1, 2, 3, 4])
#     p = np.array([0.40, 0.35, 0.15, 0.08, 0.02])

#     EX = np.sum(x * p)
#     VarX = np.sum((x - EX)**2 * p)
#     sigma = np.sqrt(VarX)

#     print("E(X) =", EX)
#     print("Var(X) =", VarX)
#     print("σ =", sigma)

from scipy.stats import binom

n = 20
p = 0.25

result = binom.pmf(5, n, p)
print(result)
prob = 1 - binom.cdf(2, n, p)
print(prob)

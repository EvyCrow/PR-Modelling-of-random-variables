import random as rn
import numpy as np
import matplotlib.pyplot as plt


# distribution
def erlang_distribution(b: float = 1.5, c: int = 6):
    p = np.prod([rn.random() for _ in range(c)])
    return -b * np.log(p)


alpha = 10
# distribution parameters
b = 1.5
c = 6

# number of realizations
num_realization_x = np.arange(1100, 1300, 10)


# the function generates alpha realisations of a random variable,
# after which it returns the sample (selective) mean
def dependence(alpha):
    random_var = np.zeros(alpha)
    for i in range(alpha):
        random_var[i] = erlang_distribution()
    sel_mean = np.sum(random_var) / alpha
    return sel_mean


# arrays for variance (dispersion), sample variance (selective dispersion),
# sample mean and mathematical expectation values
dispersion_y = []
sel_dispersion_y = []
sel_mean_y = []
math_exp = []

# filling arrays with values for the above selected range of realisations
for i in num_realization_x:
    dispersion_y.append(b ** 2 * c)
    math_exp.append(b*c)
    sel_dispersion_y.append((i/(i-1))*(b**2*c))
    sel_mean_y.append(dependence(i))

# visual block
plt.plot(num_realization_x, dispersion_y, color="orange", marker="o", label="dispersion")
plt.plot(num_realization_x, sel_dispersion_y, color="sienna", marker="o", label="selective dispersion")
plt.plot(num_realization_x, sel_mean_y, color="mediumvioletred", marker="o", label="selective mean")
plt.plot(num_realization_x, math_exp, color="crimson", marker="o", label="mathematical expectation")
plt.xlabel("number of realizations")
plt.legend()
plt.grid()
plt.show()

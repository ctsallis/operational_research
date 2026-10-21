"""Coursework Part A: worked solutions in Python (new in the October 2026 review).

Not part of the original module material: written so that every question of the 2025/26 brief has a worked
Python answer. Plain-script version of `part_a_solutions.ipynb`; run it with `python part_a_solutions.py`.
The `# %%` lines mark the notebook cells (VS Code can run them one by one).
"""


# %% [markdown]
# ## Set-up
#
# Load Pyomo, NumPy and Matplotlib, and create the HiGHS solver once. `appsi_highs` is the HiGHS solver that comes
# with the `highspy` package, so it works on the course website and on your computer without installing anything else.

# %%
import itertools

import matplotlib.pyplot as plt
import numpy as np
from pyomo.environ import (Binary, ConcreteModel, Constraint, NonNegativeReals, Objective,
                           SolverFactory, Var, maximize, minimize, value)

solver = SolverFactory("appsi_highs")  # HiGHS, installed with highspy
print("Solver available:", solver.available())

# %% [markdown]
# ## Question 1: a two-variable linear programme
#
# maximise $x + 3y$ subject to $x + 2y \le 20$, $3x + y \le 30$, $x + 10y \le 80$, $x, y \ge 0$.
#
# ### 1a) Graph and basic solutions
#
# With two variables every corner of the feasible region is where **two** constraint lines meet. There are five
# lines (three constraints plus $x = 0$ and $y = 0$), so there are $\binom{5}{2} = 10$ pairs. The cell below solves each
# pair as simultaneous equations, checks whether the point satisfies *all* constraints (a **basic feasible
# solution**) and evaluates the objective there. The best feasible corner is the optimum.

# %%
# Each constraint as (a, b, rhs) meaning a*x + b*y <= rhs. Non-negativity is written as -x <= 0 and -y <= 0.
q1_lines = {
    "x + 2y <= 20":  (1, 2, 20),
    "3x + y <= 30":  (3, 1, 30),
    "x + 10y <= 80": (1, 10, 80),
    "x >= 0":        (-1, 0, 0),
    "y >= 0":        (0, -1, 0),
}

def q1_objective(x, y):
    return x + 3 * y

print(f"{'pair of lines':34s} {'x':>8s} {'y':>8s}  feasible  {'x + 3y':>8s}")
corners = []
for (name1, (a1, b1, c1)), (name2, (a2, b2, c2)) in itertools.combinations(q1_lines.items(), 2):
    matrix = np.array([[a1, b1], [a2, b2]], dtype=float)
    if abs(np.linalg.det(matrix)) < 1e-12:  # parallel lines never meet
        print(f"{name1 + ' & ' + name2:34s} {'parallel':>8s}")
        continue
    x, y = np.linalg.solve(matrix, [c1, c2])  # where the two lines cross
    feasible = all(a * x + b * y <= c + 1e-9 for a, b, c in q1_lines.values())
    x, y = x + 0.0, y + 0.0  # turn -0.0 into 0.0 for printing
    print(f"{name1 + ' & ' + name2:34s} {x:8.3f} {y:8.3f}  {str(feasible):8s}  {q1_objective(x, y):8.3f}")
    if feasible:
        corners.append((q1_objective(x, y), x, y))

best_z, best_x, best_y = max(corners)
print(f"\nBest basic feasible solution: x = {best_x:g}, y = {best_y:g}, objective = {best_z:g}")

# %% [markdown]
# The plot shows the three constraint lines, the feasible region (shaded) and the objective line $x + 3y = 27.5$
# through the optimal corner. Moving the objective line further up-right would leave the feasible region.

# %%
xs = np.linspace(0, 12, 400)
fig, ax = plt.subplots(figsize=(6, 5))
ax.plot(xs, (20 - xs) / 2, label="x + 2y = 20")
ax.plot(xs, 30 - 3 * xs, label="3x + y = 30")
ax.plot(xs, (80 - xs) / 10, label="x + 10y = 80")
ax.plot(xs, (best_z - xs) / 3, "k--", label=f"x + 3y = {best_z:g} (objective)")
upper = np.minimum.reduce([(20 - xs) / 2, 30 - 3 * xs, (80 - xs) / 10])  # top edge of the region
ax.fill_between(xs, 0, upper, where=upper >= 0, alpha=0.25, label="feasible region")
ax.plot(best_x, best_y, "ko")
ax.annotate(f"optimum ({best_x:g}, {best_y:g})", (best_x, best_y), textcoords="offset points", xytext=(8, 8))
ax.set_xlim(0, 12); ax.set_ylim(0, 12); ax.set_xlabel("x"); ax.set_ylabel("y")
ax.set_title("Question 1: feasible region and optimum")
ax.legend(loc="upper right", fontsize=8)
plt.show()

# %% [markdown]
# ### 1b) Binding constraints
#
# A constraint is **binding** when it holds with equality at the optimum (its slack is zero). Compute the slack of
# each constraint at $(5, 7.5)$.

# %%
for name, (a, b, c) in list(q1_lines.items())[:3]:
    slack = c - (a * best_x + b * best_y)  # unused amount of the right-hand side
    print(f"{name:15s} slack = {slack:5.2f}  ->  {'binding' if abs(slack) < 1e-9 else 'not binding'}")

# %% [markdown]
# ### 1c) Matrix form
#
# "minimise $c^T x$ subject to $Ax \le b$, $x \ge 0$": a maximisation becomes a minimisation by changing the sign of
# the objective, so
#
# $$c = \begin{pmatrix}-1\\-3\end{pmatrix},\quad A = \begin{pmatrix}1 & 2\\ 3 & 1\\ 1 & 10\end{pmatrix},\quad b = \begin{pmatrix}20\\30\\80\end{pmatrix}.$$
#
# ### 1d) Solve in Python
#
# The model is built **directly from** $c$, $A$ and $b$, so the code is the matrix form. The minimum of $c^T x$ is
# $-27.5$, i.e. the maximum of $x + 3y$ is $27.5$, the same corner as in 1a.

# %%
c = [-1, -3]
A = [[1, 2],
     [3, 1],
     [1, 10]]
b = [20, 30, 80]

m1 = ConcreteModel()
m1.J = range(len(c))      # variables: 0 = x, 1 = y
m1.I = range(len(b))      # constraints: one per row of A
m1.v = Var(m1.J, domain=NonNegativeReals)
m1.obj = Objective(expr=sum(c[j] * m1.v[j] for j in m1.J), sense=minimize)          # c^T x
m1.rows = Constraint(m1.I, rule=lambda m, i: sum(A[i][j] * m.v[j] for j in m.J) <= b[i])  # A x <= b
solver.solve(m1)

print(f"x = {value(m1.v[0]):g}, y = {value(m1.v[1]):g}")
print(f"minimum of c^T x = {value(m1.obj):g}  ->  maximum of x + 3y = {-value(m1.obj):g}")

# %% [markdown]
# ## Question 2: investing £10,000 in three funds
#
# ### 2a) The model
#
# Decision variables (in £): $x$ = Toy Town, $y$ = C&G, $z$ = Pixel Ltd.
#
# $$\max\ 0.06x + 0.07y + 0.10z$$
#
# subject to
#
# - $x + y + z \le 10000$ (no more than the money available),
# - $x \ge 2y$ (at least twice as much in Toy Town as in C&G),
# - $z \le 2000$ (limit on the high-risk fund),
# - $x, y, z \ge 0$.
#
# ### 2b) Solve it

# %%
m2 = ConcreteModel()
m2.x = Var(domain=NonNegativeReals)  # Toy Town (£)
m2.y = Var(domain=NonNegativeReals)  # C&G (£)
m2.z = Var(domain=NonNegativeReals)  # Pixel Ltd (£)
m2.ret = Objective(expr=0.06 * m2.x + 0.07 * m2.y + 0.10 * m2.z, sense=maximize)  # expected return (£)
m2.budget = Constraint(expr=m2.x + m2.y + m2.z <= 10000)  # money available
m2.low_risk = Constraint(expr=m2.x >= 2 * m2.y)            # Toy Town at least twice C&G
m2.high_risk = Constraint(expr=m2.z <= 2000)               # cap on Pixel Ltd
solver.solve(m2)

for name, var in [("Toy Town", m2.x), ("C&G", m2.y), ("Pixel Ltd", m2.z)]:
    print(f"{name:10s} £{value(var):10,.2f}")
print(f"Expected return: £{value(m2.ret):,.2f} ({value(m2.ret) / 10000:.2%} of £10,000)")

# %% [markdown]
# ### 2c) Two decision variables
#
# Every fund has a positive return, so all £10,000 is invested and $z = 10000 - x - y$. Substituting:
#
# - objective: $0.06x + 0.07y + 0.10(10000 - x - y) = 1000 - 0.04x - 0.03y$, so maximising it means
#   **minimising $0.04x + 0.03y$**;
# - $z \le 2000 \iff x + y \ge 8000$; $\ z \ge 0 \iff x + y \le 10000$; and still $x \ge 2y$.
#
# The two-variable model gives the same plan:

# %%
m2b = ConcreteModel()
m2b.x = Var(domain=NonNegativeReals)  # Toy Town (£)
m2b.y = Var(domain=NonNegativeReals)  # C&G (£); Pixel gets the rest, z = 10000 - x - y
m2b.cost = Objective(expr=0.04 * m2b.x + 0.03 * m2b.y, sense=minimize)  # return given up vs. all in Pixel
m2b.pixel_cap = Constraint(expr=m2b.x + m2b.y >= 8000)    # z <= 2000
m2b.pixel_nonneg = Constraint(expr=m2b.x + m2b.y <= 10000)  # z >= 0
m2b.low_risk = Constraint(expr=m2b.x >= 2 * m2b.y)          # Toy Town at least twice C&G
solver.solve(m2b)

x2, y2 = value(m2b.x), value(m2b.y)
print(f"Toy Town £{x2:,.2f}, C&G £{y2:,.2f}, Pixel £{10000 - x2 - y2:,.2f}")
print(f"Expected return = 1000 - (0.04x + 0.03y) = £{1000 - value(m2b.cost):,.2f}")

# %% [markdown]
# **What this tells you.** The objective contains no measure of risk: the model simply prefers the highest return.
# So it puts the maximum allowed, £2,000, into Pixel Ltd, and the remaining £8,000 is split exactly 2 : 1 between
# Toy Town and C&G, because C&G pays more than Toy Town and only the 2 : 1 rule stops more going into C&G. Both
# self-imposed rules are binding and fix the answer completely, so it can be found by hand:
# $8000 \times \tfrac{2}{3} = £5{,}333.33$ and $8000 \times \tfrac{1}{3} = £2{,}666.67$. The "risk" in the problem is
# handled only through the constraints the investor chose.

# %% [markdown]
# ## Question 3: the rucksack problem
#
# ### 3a) The integer programme
#
# Let $x_i = 1$ if item $i$ is taken and $0$ otherwise ($i = 1,\dots,10$), with weight $w_i$, volume $v_i$ and value $p_i$:
#
# $$\max \sum_{i=1}^{10} p_i x_i \quad \text{s.t.} \quad \sum_i w_i x_i \le 15,\quad \sum_i v_i x_i \le 30,\quad x_i \in \{0, 1\}.$$
#
# ### 3b) Solve the ILP

# %%
items = range(1, 11)
weight = dict(zip(items, [3.5, 2.4, 0.9, 2.5, 3.1, 4.2, 5.1, 3.5, 4.5, 2.9]))  # kg
volume = dict(zip(items, [4, 4, 5, 2, 11, 9, 11, 8, 11, 8]))                 # litres
worth  = dict(zip(items, [5, 2, 3, 1, 11, 7, 5, 2, 5, 7]))                   # £

MAX_WEIGHT, MAX_VOLUME = 15, 30  # the rucksack's limits (kg, litres)

def rucksack(integer=True, max_weight=MAX_WEIGHT, max_volume=MAX_VOLUME):
    m = ConcreteModel()
    m.x = Var(items, domain=Binary if integer else NonNegativeReals, bounds=(0, 1))  # share of item i taken
    m.value = Objective(expr=sum(worth[i] * m.x[i] for i in items), sense=maximize)
    m.weight = Constraint(expr=sum(weight[i] * m.x[i] for i in items) <= max_weight)  # weight limit
    m.volume = Constraint(expr=sum(volume[i] * m.x[i] for i in items) <= max_volume)  # volume limit
    solver.solve(m)
    return {i: value(m.x[i]) for i in items}, value(m.value)

def describe(x, max_weight=MAX_WEIGHT, max_volume=MAX_VOLUME):
    w = sum(weight[i] * x[i] for i in items)
    v = sum(volume[i] * x[i] for i in items)
    p = sum(worth[i] * x[i] for i in items)
    ok = w <= max_weight + 1e-9 and v <= max_volume + 1e-9
    return f"weight {w:.2f} kg, volume {v:.2f} l, value £{p:.2f}, feasible: {ok}"

x_ilp, z_ilp = rucksack(integer=True)
print("ILP: take items", [i for i in items if x_ilp[i] > 0.5])
print("    ", describe(x_ilp))

# %% [markdown]
# ### 3c) Relax the integer constraints
#
# Allow $0 \le x_i \le 1$ (any fraction of an item). The LP can take part of item 6, so its value is higher.

# %%
x_lp, z_lp = rucksack(integer=False)
print("LP relaxation:", {i: round(x_lp[i], 4) for i in items if x_lp[i] > 1e-9})
print("    ", describe(x_lp))

# %% [markdown]
# ### 3d) Round the LP solution and compare

# %%
rounded_down = {i: np.floor(x_lp[i] + 1e-9) for i in items}
rounded_up = {i: np.ceil(x_lp[i] - 1e-9) for i in items}
nearest = {i: np.round(x_lp[i]) for i in items}
print("Rounded down:", [i for i in items if rounded_down[i]], "|", describe(rounded_down))
print("Rounded up:  ", [i for i in items if rounded_up[i]], "|", describe(rounded_up))
print("Nearest:     ", [i for i in items if nearest[i]], "|", describe(nearest))
print(f"\nILP £{z_ilp:g}  <=  LP relaxation £{z_lp:.4f}")

# %% [markdown]
# **What this shows.** The LP relaxation gives an *upper bound* (£28.44) on the best integer value. Rounding its
# answer is not a reliable way to solve an integer programme:
#
# - rounding item 6 **up** (it is also the nearest integer, 0.78 → 1) needs 32 litres, more than the 30 available: infeasible;
# - rounding **down** is feasible but worth only £23, well below the true integer optimum;
# - the true optimum (£27) takes items 1, 3, 4, 5 and 10, a different set (it swaps item 6 for items 3 and 4), which
#   no rounding of the LP answer would find.
#
# So integer problems need an integer method (branch and bound, as the solver uses); the LP relaxation is useful as a
# bound and a starting point, not as the answer.

# %% [markdown]
# ### Try it
#
# Which limit really restricts the rucksack? In a new cell, run `describe(rucksack(max_weight=16)[0])` and then
# `describe(rucksack(max_volume=32)[0], max_volume=32)`. What do you notice?
#
# <details><summary>Answer</summary>
#
# An extra kilogram changes nothing: the optimal items use only 12.9 kg, so the weight limit is **not** binding.
# Two extra litres change the answer to items 1, 5, 6, 10 worth £30, exactly the "rounded up" LP solution, which
# now fits. The volume limit is the binding one.
# </details>

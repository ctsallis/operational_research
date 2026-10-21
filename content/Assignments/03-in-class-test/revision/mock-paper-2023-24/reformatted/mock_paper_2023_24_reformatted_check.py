"""Mock paper 2023/24 (reformatted): code check of the written solutions (new in the October 2026 review).

Not part of the original module material. Plain-script version of `mock_paper_2023_24_reformatted_check.ipynb`;
run it with `python mock_paper_2023_24_reformatted_check.py`.
The `# %%` lines mark the notebook cells (VS Code can run them one by one).
"""


# %% [markdown]
# ## Set-up

# %%
import numpy as np
import pandas as pd
from pyomo.environ import (ConcreteModel, Constraint, NonNegativeReals, Objective, SolverFactory, Var,
                           maximize, minimize, value)

solver = SolverFactory("appsi_highs")  # HiGHS, installed with highspy

# %% [markdown]
# ## Question 1: forecasting with additive and multiplicative models
#
# Fit on periods 1–12, validate on 13–16. The 4-period moving average of periods 1–4 sits between periods 2 and 3,
# so it is shown at period 2 (as in the practice-paper solutions); the **centred** moving average (CMA) at period $t$
# is the mean of the 4-MAs shown at $t-1$ and $t$. With 12 periods the CMA exists for periods 3–10.

# %%
sales = [1013, 1025, 1002, 1021, 1053, 1067, 1042, 1060, 1093, 1106, 1083, 1101, 1134, 1147, 1123, 1139]
seasons = ["Spring", "Summer", "Autumn", "Winter"]
df = pd.DataFrame({"t": range(1, 17), "season": [seasons[i % 4] for i in range(16)], "sales": sales})

fit = df[df["t"] <= 12].copy()                                        # fitting sample only
fit["ma4"] = fit["sales"].rolling(4).mean().shift(-2)                 # MA of t-1..t+2, shown at t
fit["cma"] = (fit["ma4"].shift(1) + fit["ma4"]) / 2                   # centred at t
print(fit[["t", "season", "sales", "ma4", "cma"]].to_string(index=False))

# %% [markdown]
# **Correction to the written solutions, part (a).** The table there lists, for periods 3–10, CMA values 1015.625,
# 1024.625, 1037.125, 1050.750, 1065.875, 1078.875, 1091.375, 1101.000 (and 4-MA values that are wrong from period 5
# on). The correct CMA values are the ones above: 1020.250, 1030.500, 1040.750, 1050.625, 1060.500, 1070.375, 1080.375,
# 1090.625. The trend line, seasonal indices and forecasts in the written solutions were computed from these
# **correct** values, so everything after the table is right, as the next cells show.

# %%
cma_rows = fit.dropna(subset=["cma"]).copy()
slope, intercept = np.polyfit(cma_rows["t"], cma_rows["cma"], 1)      # straight line through the CMAs
print(f"Trend: T = {intercept:.3f} + {slope:.3f} t")

cma_rows["add"] = cma_rows["sales"] - cma_rows["cma"]                 # additive seasonal variation
cma_rows["mult"] = cma_rows["sales"] / cma_rows["cma"]                # multiplicative seasonal ratio
add_idx = cma_rows.groupby("season")["add"].mean()
add_idx -= add_idx.mean()                                             # additive indices sum to 0
mult_idx = cma_rows.groupby("season")["mult"].mean()
mult_idx /= mult_idx.mean()                                           # multiplicative indices average 1
print(pd.DataFrame({"additive": add_idx.round(3), "multiplicative": mult_idx.round(5)}).loc[seasons])

# %%
val = df[df["t"] >= 13].copy()
trend = intercept + slope * val["t"]
val["additive"] = trend + val["season"].map(add_idx)                  # trend + seasonal index
val["multiplicative"] = trend * val["season"].map(mult_idx)           # trend x seasonal index
val["add_AE"] = (val["sales"] - val["additive"]).abs()
val["mult_AE"] = (val["sales"] - val["multiplicative"]).abs()
print(val.round(3).to_string(index=False))
print(f"MAD additive = {val['add_AE'].mean():.3f},  MAD multiplicative = {val['mult_AE'].mean():.3f}")

future = pd.DataFrame({"t": range(17, 21), "season": seasons})
future["forecast"] = (intercept + slope * future["t"]) * future["season"].map(mult_idx)
print(future.round(3).to_string(index=False))

# %% [markdown]
# ## Question 2: warehouse simulation with the paper's random numbers
#
# Each week: look up deliveries and demand from the cumulative probabilities, add deliveries to the stock carried
# over, pay £10 per warehouse space and £20 per car above capacity, sell what demand allows, carry the rest over.

# %%
def lookup(rn, values, probs):
    # first value whose cumulative probability exceeds the random number
    return values[int(np.searchsorted(np.cumsum(probs), rn, side="right"))]

delivery_rn = [0.086, 0.237, 0.801, 0.582, 0.094, 0.433, 0.479, 0.160, 0.735, 0.114, 0.391, 0.517]
demand_rn = [0.431, 0.587, 0.738, 0.956, 0.284, 0.649, 0.696, 0.293, 0.001, 0.973, 0.298, 0.314]

def simulate(capacity):
    stock, rows = 0, []
    for week in range(12):
        delivered = lookup(delivery_rn[week], [7, 8, 9, 10], [0.10, 0.20, 0.50, 0.20])
        demand = lookup(demand_rn[week], [6, 7, 8, 9, 10, 11], [0.05, 0.20, 0.30, 0.10, 0.20, 0.15])
        start = stock + delivered                       # cars on hand at the start of the week
        overflow = max(start - capacity, 0)             # cars in rented spaces
        cost = 10 * capacity + 20 * overflow            # weekly cost (£)
        sold = min(start, demand)
        stock = start - sold                            # carried into next week
        rows.append((week + 1, delivered, demand, start, sold, stock, overflow, cost))
    return pd.DataFrame(rows, columns=["week", "delivered", "demand", "start", "sold", "end", "overflow", "cost"])

print(simulate(9).to_string(index=False))
for capacity in (7, 8, 9, 10):
    print(f"capacity {capacity:2d}: average weekly cost £{simulate(capacity)['cost'].mean():.2f}")

# %% [markdown]
# ## Question 3: transportation and transhipment

# %%
supply = {"A": 100, "B": 100, "C": 100}
demand = {"X": 70, "Y": 80, "Z": 150}
cost = {("A", "X"): 8, ("A", "Y"): 7, ("A", "Z"): 5,
        ("B", "X"): 12, ("B", "Y"): 3, ("B", "Z"): 9,
        ("C", "X"): 10, ("C", "Y"): 11, ("C", "Z"): 7}

def transport(forbid=(), at_least=None):
    m = ConcreteModel()
    m.x = Var(list(cost), domain=NonNegativeReals)                     # units warehouse -> shop
    m.obj = Objective(expr=sum(cost[a] * m.x[a] for a in cost), sense=minimize)
    m.supply = Constraint(list(supply), rule=lambda m, i: sum(m.x[i, j] for j in demand) <= supply[i])
    m.demand = Constraint(list(demand), rule=lambda m, j: sum(m.x[i, j] for i in supply) == demand[j])
    for arc in forbid:
        m.x[arc].fix(0)                                                  # route not allowed
    if at_least:
        arc, amount = at_least
        m.minimum = Constraint(expr=m.x[arc] >= amount)                  # minimum on one route
    solver.solve(m)
    return value(m.obj), {a: value(m.x[a]) for a in cost if value(m.x[a]) > 1e-9}

print("(b) direct shipping:", transport())
print("(c) no B->Y, A->Z at least 5:", transport(forbid=[("B", "Y")], at_least=(("A", "Z"), 5)))

# %% [markdown]
# Several plans can reach the same minimum cost; compare the **cost**, and check that your own plan meets every
# supply and demand constraint. Part (d): all flow goes warehouse → distribution point → shop.

# %%
to_hub = {("A", "D1"): 4, ("A", "D2"): 5, ("B", "D1"): 3, ("B", "D2"): 2, ("C", "D1"): 6, ("C", "D2"): 4}
from_hub = {("D1", "X"): 4, ("D1", "Y"): 5, ("D1", "Z"): 2, ("D2", "X"): 2, ("D2", "Y"): 4, ("D2", "Z"): 4}
hubs = ["D1", "D2"]

t = ConcreteModel()
t.x = Var(list(to_hub), domain=NonNegativeReals)                       # warehouse -> hub
t.y = Var(list(from_hub), domain=NonNegativeReals)                     # hub -> shop
t.obj = Objective(expr=sum(to_hub[a] * t.x[a] for a in to_hub) + sum(from_hub[a] * t.y[a] for a in from_hub))
t.supply = Constraint(list(supply), rule=lambda m, i: sum(m.x[i, k] for k in hubs) <= supply[i])
t.balance = Constraint(hubs, rule=lambda m, k: sum(m.x[i, k] for i in supply) == sum(m.y[k, j] for j in demand))
t.demand = Constraint(list(demand), rule=lambda m, j: sum(m.y[k, j] for k in hubs) == demand[j])
solver.solve(t)
print("(d) transhipment cost:", value(t.obj))
print({a: value(t.x[a]) for a in to_hub if value(t.x[a]) > 1e-9})
print({a: value(t.y[a]) for a in from_hub if value(t.y[a]) > 1e-9})

# %% [markdown]
# ## Question 4: linear programming

# %%
def production(linked=False):
    m = ConcreteModel()
    m.x = Var(domain=NonNegativeReals)                     # units of X per week
    m.y = Var(domain=NonNegativeReals)                     # units of Y per week
    m.profit = Objective(expr=36 * m.x + 34 * m.y, sense=maximize)  # £k
    m.material_a = Constraint(expr=4 * m.x + 3 * m.y <= 40)
    m.material_b = Constraint(expr=0.2 * m.x + 0.3 * m.y <= 3)
    if linked:
        m.link = Constraint(expr=m.y == 3 * m.x)            # 3 units of Y for every unit of X
    solver.solve(m)
    slack_a = round(40 - value(4 * m.x + 3 * m.y), 9) + 0.0   # unused raw material A
    slack_b = round(3 - value(0.2 * m.x + 0.3 * m.y), 9) + 0.0  # unused raw material B
    return value(m.x), value(m.y), value(m.profit), slack_a, slack_b

x, y, z, sa, sb = production()
print(f"(b) x = {x:.4f}, y = {y:.4f} (= 20/3), profit = {z:.2f}; (c) unused A = {sa:.4f}, unused B = {sb:.4f}")
x2, y2, z2, _, _ = production(linked=True)
print(f"(e) x = {x2:.4f} (= 30/11), y = {y2:.4f} (= 90/11), profit = {z2:.2f}; reduction = {z - z2:.2f}")

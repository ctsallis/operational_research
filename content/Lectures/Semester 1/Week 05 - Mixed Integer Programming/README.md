# Week 5: Mixed Integer Programming

This README is your guide to Week 5 if you are studying on your own. It tells you what to open, in which
order, what each file is for, and what result you should get at every step. It also explains the key
ideas, so you can go through the week with nothing but this page, the slides and the notebooks.

**What you will learn this week**

- What a *mixed-integer linear program* (MILP) is, and why rounding an LP answer is not enough.
- What a *binary* (0/1) variable is and how it models yes/no decisions.
- Three classic models: the **knapsack problem**, the **set covering problem** and a **purchasing problem**
  with minimum order sizes.
- How to model rules such as "if you order an item, order at least 6 kg", "order at most 2 different
  items" and "not both item 1 and item 4".
- How to write and solve all of these in Python with **Pyomo** and the **HiGHS** solver.

**What you need from earlier weeks**

- Week 3: writing a linear program (LP) and solving it with Pyomo; the Icki-Toffee candy problem.
- Week 4: turning a word problem into variables, an objective and constraints.

If Pyomo is new to you, re-run a Week 3 demo first. This week uses the same structure in every notebook.

---

## Contents

1. [How to open the files](#1-how-to-open-the-files)
2. [What is in this folder](#2-what-is-in-this-folder)
3. [Your plan for the week](#3-your-plan-for-the-week)
4. [The key ideas, explained](#4-the-key-ideas-explained)
5. [Lecture: slide-by-slide guide with the demo notebooks](#5-lecture-slide-by-slide-guide-with-the-demo-notebooks)
6. [Tutorial: questions, hints and how to check your answers](#6-tutorial-questions-hints-and-how-to-check-your-answers)
7. [How to read the Pyomo and HiGHS output](#7-how-to-read-the-pyomo-and-highs-output)
8. [If something goes wrong](#8-if-something-goes-wrong)
9. [Check your understanding](#9-check-your-understanding)
10. [Checklist: have you finished the week?](#10-checklist-have-you-finished-the-week)
11. [Assumptions](#11-assumptions)

---

## 1. How to open the files

### Notebooks (`.ipynb`): run them in your browser

The course website runs Python **inside your web browser**. You install nothing, and you need no account.

1. Open the course site: <https://ctsallis.github.io/operational_research/>
   Use a recent **Chrome, Edge or Firefox**.
2. In the file list on the left, double-click your way to
   `Lectures` → `Semester 1` → `Week 05 - Mixed Integer Programming`.
3. Open a sub-folder (for example `2 Lecture Demos`) and double-click a notebook to open it.
4. **Run the first code cell first.** It installs Pyomo and HiGHS into the open browser tab. The first
   time, this takes about a minute.
5. Then choose *Run → Run All Cells* from the menu, or run the cells one by one with **Shift + Enter**
   while you read.

You can also open each notebook directly with the links in [section 5](#5-lecture-slide-by-slide-guide-with-the-demo-notebooks)
and [section 6](#6-tutorial-questions-hints-and-how-to-check-your-answers).

If this is your first session on the site, open `00_START_HERE.ipynb` (at the top of the file list) and run
all its cells. If every cell prints `OK`, all the course examples will run in your browser.

> **Save your work.** Changes you make to a notebook on the site are kept **only in this browser**.
> Clearing browser data, using a private window or switching computer loses them. Before you leave,
> right-click the notebook in the file list → **Download**.

### Slides and Word documents (`.pptx`, `.docx`): download and open them

The website cannot display PowerPoint or Word files. Download them and open them in **PowerPoint** and
**Word**. They contain equations, so open them in those programs to see everything correctly.

- **Lecture slides:** [download `Week 5 - Mixed Integer Programming.pptx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/1%20Lecture/Week%205%20-%20Mixed%20Integer%20Programming.pptx)
- **Tutorial sheet:** [download `Week 5 - Mixed Integer Programming Tutorial.docx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/3%20Tutorial/Week%205%20-%20Mixed%20Integer%20Programming%20Tutorial.docx)
- **Tutorial answers:** [download `Week 5 - Mixed Integer Programming Tutorial - Answers.docx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/4%20Tutorial%20Answers/Week%205%20-%20Mixed%20Integer%20Programming%20Tutorial%20-%20Answers.docx)

Another way to get them: on the course site, right-click the file in the file list → **Download**.

**Slide numbers** in this README are the numbers PowerPoint shows in the slide list on the left. Slide 3
is a hidden, empty slide. PowerPoint skips it in a slide show, but it still counts in the numbering.

---

## 2. What is in this folder

| Folder | File | What it is | When to use it |
| --- | --- | --- | --- |
| `1 Lecture` | `Week 5 - Mixed Integer Programming.pptx` | The lecture slides (32 slides) | Read first, alongside the demos |
| `2 Lecture Demos` | `1 Integer LP.ipynb` | Integer LP from slides 5–9: why rounding fails | With slides 4–9 |
| | `2 Knapsack problem.ipynb` | 7-item knapsack, capacity 10 kg | With slides 12–14 |
| | `3 Fire stations - set covering.ipynb` | Fire stations for 6 cities | With slides 15–21 |
| | `4 Purchasing - basic model.ipynb` | Purchasing problem as an ordinary LP | With slides 24–25 |
| | `5 Purchasing - binary variables.ipynb` | Adds "at least 6 kg if ordered" | With slides 26–28 |
| | `6 Purchasing - order at most two items.ipynb` | Adds "at most 2 different items" | With slides 29–30 |
| | `7 Purchasing - item 1 or item 4.ipynb` | Adds "not both item 1 and item 4" | With slides 31–32 |
| | `8 Minimum vertex cover.ipynb` | Extra example, not on the slides; a preview of Week 6 | After demo 3 (optional) |
| `3 Tutorial` | `Week 5 - Mixed Integer Programming Tutorial.docx` | The tutorial sheet: Q1 (a, b, c), Q2, Q3 | After the lecture |
| `4 Tutorial Answers` | `Week 5 - Mixed Integer Programming Tutorial - Answers.docx` | Worked formulations and results | After you have tried the tutorial |
| | `Q1a`, `Q1b`, `Q1c Desert island knapsack.ipynb` | Code answers for Q1 | After trying Q1 |
| | `Q2 Fire stations - set covering.ipynb` | Code answer for Q2 | After trying Q2 |
| | `Q3 Icki-Toffee - binary variables.ipynb` | Code answer for Q3 | After trying Q3 |
| `5 Source Files` | `Python/*.py` (13 scripts) | The original scripts the notebooks were made from | Not needed (see below) |
| | `MATLAB/*.m` (5 scripts) | The tutorial answers in MATLAB | Only if you use MATLAB |

**About `5 Source Files`.** You do not need these files: every one of them has a notebook version in
`2 Lecture Demos` or `4 Tutorial Answers`, and the notebook says which script it came from.

- The Python scripts use the GLPK solver, which you would have to install on your own computer. To run one
  on your computer with HiGHS instead, change `SolverFactory('glpk')` to `SolverFactory('appsi_highs')`
  and install the packages with `pip install pyomo highspy`.
- The MATLAB scripts need MATLAB with the Optimization Toolbox (`optimvar`, `intlinprog`).
- The code pictures on the slides show the original scripts, which use `SolverFactory('glpk')`. The
  notebooks use `SolverFactory('appsi_highs')`. Everything else in the models is the same.

---

## 3. Your plan for the week

Work through these steps in order. Tick them off in [section 10](#10-checklist-have-you-finished-the-week).

| Step | What to do | Material |
| --- | --- | --- |
| 1 | Run `00_START_HERE.ipynb` once to check that the site works in your browser | Course site |
| 2 | Read [section 4](#4-the-key-ideas-explained) of this README for the ideas behind the week | This README |
| 3 | Go through the slides, and run each demo notebook when [section 5](#5-lecture-slide-by-slide-guide-with-the-demo-notebooks) tells you to | `1 Lecture`, `2 Lecture Demos` |
| 4 | Answer each demo's **"What do you notice?"** or **"Try it"** question *before* you open its answer | Last cell of each demo |
| 5 | Do the tutorial on paper first: write each formulation (variables, objective, constraints) | `3 Tutorial` |
| 6 | Solve your formulations in Python, by copying and changing a demo notebook | `2 Lecture Demos` |
| 7 | Check your formulations and results against the answers | `4 Tutorial Answers` |
| 8 | Answer the questions in [section 9](#9-check-your-understanding) | This README |

**Tip for step 6.** In the course site's file list, right-click a demo notebook → **Duplicate**. Rename
the copy, then change its data and constraints. The demo that is closest to each tutorial question is
named in [section 6](#6-tutorial-questions-hints-and-how-to-check-your-answers).

---

## 4. The key ideas, explained

### 4.1 Mixed-integer linear programs (slides 4–5)

A **linear program (LP)** has a linear objective, linear constraints, and variables that can take any real
value (such as 2.37). A **mixed-integer linear program (MILP)** is the same, except that **some or all of the
variables must be whole numbers** (integers). If *all* variables must be integers, it is also called an
**integer linear program (ILP)**.

Slide 5 shows both cases for the same problem:

$$\max\ P = 2x + 3.5y \quad \text{s.t.}\quad 3x + 2y \le 14,\quad 2x + 3y \le 12.5,\quad -x + y \le 1,\quad x, y \ge 0$$

- with $x, y \in \mathbb{Z}$ (both whole numbers): an integer program;
- with only $x \in \mathbb{Z}$ ($y$ may be fractional): a *mixed*-integer program.

### 4.2 Why you cannot just round the LP answer (slides 6–9)

Without the whole-number rule, the best point is $(x, y) = (1.9, 2.9)$ with $P = 13.95$. Rounding gives
the nearby whole-number points:

| Point | Feasible? | $P$ |
| --- | --- | --- |
| $(1, 2)$ | yes | 9 |
| $(1, 3)$ | no: $-1 + 3 = 2 > 1$ | – |
| $(2, 2)$ | yes | 11 |
| $(2, 3)$ | no: $2 \cdot 2 + 3 \cdot 3 = 13 > 12.5$ | – |

The true integer optimum is $(3, 2)$ with $P = 13$, which is **not** one of the rounded points. Rounding can
give an infeasible point, or a feasible one that is far from the best. A MILP solver finds the true integer
optimum. HiGHS does this by *branch and bound*: it solves LPs and splits the problem on variables that come
out fractional.

### 4.3 Binary variables (slides 10–11)

A **binary variable** can only be 0 or 1. It is an integer variable with bounds $0 \le x \le 1$. It models a
**yes/no decision**: take the item or not, build the station or not, order the product or not.

In Pyomo you choose the type of a variable with `within=` (or `domain=`):

| Pyomo | Meaning |
| --- | --- |
| `NonNegativeReals` | any real number $\ge 0$ (ordinary LP variable) |
| `NonNegativeIntegers` | a whole number $\ge 0$: 0, 1, 2, … |
| `Binary` | 0 or 1 |

### 4.4 The knapsack problem (slides 12–14)

You have $n$ items. Item $i$ has a weight $w_i$ and a value $v_i$. Your bag holds at most $W$. Choose
the items that give the largest total value. Let $x_i = 1$ if you take item $i$, and $0$ if not:

$$\max \sum_{i=1}^{n} v_i x_i \quad \text{s.t.} \quad \sum_{i=1}^{n} w_i x_i \le W, \qquad x_i \in \lbrace 0, 1\rbrace$$

Because each $x_i$ is 0 or 1, $v_i x_i$ is "the value of item $i$ if taken, otherwise 0". The best choice is
the best **combination** that fits, which is not necessarily the most valuable single items.

### 4.5 The set covering problem (slides 15–23)

You must **cover** a set of things (cities, edges, elements) using as few "sets" as possible. Each set
covers some of the things. Let $x_s = 1$ if you choose set $s$:

$$\min \sum_{s} x_s \quad \text{s.t.} \quad \sum_{s \text{ that cover } e} x_s \ge 1 \ \text{ for every thing } e, \qquad x_s \in \lbrace 0, 1\rbrace$$

Each constraint says "at least one chosen set covers this thing".

**The fire-station example (slides 15–21).** There are six cities, and the table on slide 15 gives the driving
times between them. A station in city $i$ covers city $j$ if the drive takes **15 minutes or less**. You
choose where to build stations ($x_i = 1$). For each city you write one constraint: the sum of the $x_i$
for every city whose station can reach it within 15 minutes must be at least 1. For example, city 1 can be
reached from city 1 (0 min) and city 2 (10 min), so $x_1 + x_2 \ge 1$.

> **How to build a covering constraint:** take one row of the table (one city), circle every entry that is
> 15 or less, and add up the $x$ of those columns. The diagonal entry is 0, so a city always covers itself.

Slides 22–23 give the general form and a small example with four sets $s_1 = \lbrace 1,2,5\rbrace$,
$s_2 = \lbrace 2,3\rbrace$, $s_3 = \lbrace 4,5\rbrace$ and $s_4 = \lbrace 3,4\rbrace$. Two sets,
$\lbrace s_1, s_4\rbrace$, are enough to cover $\lbrace 1,2,3,4,5\rbrace$.

### 4.6 Linking a quantity to a yes/no decision (slides 24–28)

In the purchasing problem, $x_i$ is the **amount** (kg) of item $i$, a real number. The new rule is:
*if you order an item, order at least 6 kg and at most 10 kg of it.*

Writing $x_i \ge 6$ is wrong (slide 26): it forces you to order **every** item. Instead, add a binary
variable $\delta_i$ (1 if item $i$ is ordered) and link the two:

$$x_i \le 10\,\delta_i \quad (1) \qquad\qquad x_i \ge 6\,\delta_i \quad (2)$$

- If $\delta_i = 0$: (1) gives $x_i \le 0$ and (2) gives $x_i \ge 0$, so $x_i = 0$ (not ordered).
- If $\delta_i = 1$: (1) gives $x_i \le 10$ and (2) gives $x_i \ge 6$, so $6 \le x_i \le 10$.

This **pattern is the most important tool of the week**:

> **lower limit × δ ≤ amount ≤ upper limit × δ**

It switches a continuous amount "off" (forced to 0) or "on" (forced into a range). You will need it in
tutorial Q3. In the code, $\delta_i$ is called `b[i]` (demos 5–7) or `xb[i]` (tutorial Q3).

### 4.7 Logical rules with binary variables (slides 29–32)

Once each yes/no decision has its own $\delta_i$, rules about the decisions become simple linear
constraints:

| Rule | Constraint |
| --- | --- |
| at most 2 different items | $\sum_i \delta_i \le 2$ |
| at least 6 different items | $\sum_i \delta_i \ge 6$ |
| not both item 1 and item 4 (one, the other, or neither) | $\delta_1 + \delta_4 \le 1$ |
| exactly one of item 1 and item 4 | $\delta_1 + \delta_4 = 1$ |

The slides' rule "either item 1 or item 4, not both" uses $\le 1$, which also allows ordering neither.
Use $= 1$ only when exactly one must be chosen.

### 4.8 Python counts from 0

In every notebook, item 1 is `x[0]`, item 2 is `x[1]`, and so on. When the output says `x[6] = 1`, it
means **item 7**. Keep this in mind whenever you compare code output with the slides or the tutorial.

---

## 5. Lecture: slide-by-slide guide with the demo notebooks

Read the slides in order. When you reach a demo, open the notebook, read its first cell, run it, and
compare your output with the **expected result** below. Each notebook ends with a question. Answer it
yourself before you click **Answer** to reveal the solution.

| Slides | Topic | Run this demo | Expected result |
| --- | --- | --- | --- |
| 1–2 | Title, contents | – | – |
| 4–9 | Review: MILP, LP optimum (1.9, 2.9), rounding, integer solution | [`1 Integer LP`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/1%20Integer%20LP.ipynb) | `x[0] = 3`, `x[1] = 2`, objective **13** |
| 10–11 | Binary variables | – | – |
| 12–14 | Knapsack: 7 items, 10 kg | [`2 Knapsack problem`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/2%20Knapsack%20problem.ipynb) | Value **170**: items 5 and 7 (`x[4]`, `x[6]` = 1), 9 kg |
| 15–21 | Set covering: fire stations, 6 cities | [`3 Fire stations - set covering`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/3%20Fire%20stations%20-%20set%20covering.ipynb) | **2 stations**, cities 2 and 4 (`x[1]`, `x[3]` = 1) |
| (extra) | Minimum vertex cover, 6 vertices and 5 edges | [`8 Minimum vertex cover`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/8%20Minimum%20vertex%20cover.ipynb) (optional) | **3 vertices**, e.g. 2, 4 and 5 |
| 22–23 | General set covering problem | – | – |
| 24–25 | Purchasing problem, basic LP | [`4 Purchasing - basic model`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/4%20Purchasing%20-%20basic%20model.ipynb) | Profit **84.44**: 10 kg of item 1, 1.11 kg of item 3, 10 kg of item 4 |
| 26–28 | Minimum order 6 kg with binary variables | [`5 Purchasing - binary variables`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/5%20Purchasing%20-%20binary%20variables.ipynb) | Profit **81.6**: 6 kg of item 1, 6 kg of item 3, 9.2 kg of item 4 |
| 29–30 | At most 2 different items | [`6 Purchasing - order at most two items`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/6%20Purchasing%20-%20order%20at%20most%20two%20items.ipynb) | Profit **80**: 10 kg each of items 1 and 4; £150 spent |
| 31–32 | Item 1 or item 4, not both | [`7 Purchasing - item 1 or item 4`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/7%20Purchasing%20-%20item%201%20or%20item%204.ipynb) | Profit **76.67**: 10 kg of item 1, 6.67 kg of item 3 |

**Things to notice as you go**

- **Demo 2:** item 4 + item 7 also gives £170. If your output shows that choice instead, it is equally
  correct. A problem can have several optimal solutions with the same objective value.
- **Demo 3:** compare the model with your own reading of the table on slide 15, using the tip in
  [section 4.5](#45-the-set-covering-problem-slides-1523). The slides found the same answer, cities 2 and 4,
  "by inspection" (slide 16).
- **Demos 4 → 5 → 6 → 7:** every new rule can only keep the profit the same or lower it
  (84.44 → 81.6 → 80; demo 7 replaces demo 6's rule, giving 76.67). A rule removes options; it never adds
  better ones.
- **Demo 8** is not on the slides. It is the same kind of covering model, applied to the edges of a graph.
  Week 6 returns to it.

---

## 6. Tutorial: questions, hints and how to check your answers

Open the tutorial sheet (`3 Tutorial`). The sheet marks the hardest question with `**`: this week that is
**Q3**. For each question:

1. **On paper:** define the decision variables, write the objective, then write the constraints.
2. **In Python:** duplicate the demo named below, change the data and constraints, and solve.
3. **Check:** open the hints below only if you are stuck, then compare with the answers document and the
   answer notebook.

### Q1. Desert-island knapsack

Eight items with weights and survival values (Table 1); you can carry 15 kg.
(a) maximise survival value; (b) you may take an item more than once; (c) ignoring (b), take at least 5 items.

- **Closest demo:** `2 Knapsack problem`.
- **What changes between the parts:** (a) is a knapsack exactly as in section 4.4. In (b), $x_i$ becomes "how
  many of item $i$", so it is no longer binary (look at the variable types in section 4.3). In (c), add one
  constraint that counts the items, using the fact that a sum of binary variables counts how many are 1.

<details><summary>Check Q1: formulations and results</summary>

Let $s_i$ = survival value, $w_i$ = weight, $x_i$ = number of times item $i$ is packed.

- **(a)** $\max \sum_{i=1}^{8} s_i x_i$ s.t. $\sum_i w_i x_i \le 15$, $x_i \in \lbrace 0,1\rbrace$.
  Result **270**: items 4, 5 and 7 (exactly 15 kg).
- **(b)** same objective and capacity, $x_i \ge 0$ and integer. Result **350**: five of item 7 (15 kg).
- **(c)** as (a), plus $\sum_i x_i \ge 5$. Result **250**: items 1, 2, 3, 7 and 8 (15 kg).

Notebooks: [`Q1a`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/4%20Tutorial%20Answers/Q1a%20Desert%20island%20knapsack.ipynb),
[`Q1b`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/4%20Tutorial%20Answers/Q1b%20Desert%20island%20knapsack.ipynb),
[`Q1c`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/4%20Tutorial%20Answers/Q1c%20Desert%20island%20knapsack.ipynb).
</details>

### Q2. Fire stations (set covering)

Table 2 lists, for each of 7 cities, which cities a station built there would cover. Build as few stations as
possible so that every city is covered.

- **Closest demo:** `3 Fire stations - set covering`.
- **Hint:** you need one constraint **per city** being covered. For city $j$, add up $x_i$ for every station
  $i$ whose "Covers" list contains $j$. (In this table, "station $i$ covers city $j$" and "station $j$ covers
  city $i$" always go together, so you can also read city $j$'s own row.)

<details><summary>Check Q2: formulation and result</summary>

$\min \sum_{i=1}^{7} x_i$ subject to

| City | Constraint |
| --- | --- |
| 1 | $x_1 + x_2 + x_3 \ge 1$ |
| 2 | $x_1 + x_2 + x_4 \ge 1$ |
| 3 | $x_1 + x_3 \ge 1$ |
| 4 | $x_2 + x_4 + x_5 \ge 1$ |
| 5 | $x_4 + x_5 + x_6 \ge 1$ |
| 6 | $x_5 + x_6 + x_7 \ge 1$ |
| 7 | $x_6 + x_7 \ge 1$ |

and $x_i \in \lbrace 0,1\rbrace$. Result: **3 stations**. Several choices are optimal: the notebook shows
cities 1, 2 and 6, and the answers document shows cities 3, 4 and 7. Any 3 stations that cover every city
are correct.

Notebook: [`Q2 Fire stations - set covering`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/4%20Tutorial%20Answers/Q2%20Fire%20stations%20-%20set%20covering.ipynb).
</details>

### Q3. Icki-Toffee with binary variables (hard, `**`)

This is the candy-selection problem from Weeks 3–4 (Table 3: fat, calories, weight and cost of 12 candies).
Minimise the total cost. Keep the four rules from before: weight at least 320 g, fat at most 45% of the
weight, at most 2850 calories, weight at most 1.5 × 320 g. Then add three new rules: at least 6 different
candies, at least 3 of each candy chosen, and at most 6 of each candy chosen.

- **Closest demo:** `5 Purchasing - binary variables` (the same linking idea).
- **Hints:**
  - $x_i$ is the **number** of candy $i$, a whole number. Add a binary $\delta_i$ = 1 if candy $i$ is in the
    selection.
  - "At least 3 and at most 6 of each chosen candy, none of the others" is exactly the pattern in
    [section 4.6](#46-linking-a-quantity-to-a-yesno-decision-slides-2428), with 3 and 6 instead of 6 and 10.
  - "At least 6 different candies" is a counting rule, as in [section 4.7](#47-logical-rules-with-binary-variables-slides-2932).
  - The fat rule has a sum on both sides: $\sum_i F_i x_i \le 0.45 \sum_i W_i x_i$. This is still linear.
  - A `-` in the fat column of Table 3 means 0 g of fat.

<details><summary>Check Q3: formulation and result</summary>

$$\min \sum_i C_i x_i$$

subject to

- $\sum_i W_i x_i \ge 320$ and $\sum_i W_i x_i \le 480$
- $\sum_i K_i x_i \le 2850$
- $\sum_i F_i x_i \le 0.45 \sum_i W_i x_i$
- $\sum_i \delta_i \ge 6$
- $x_i \ge 3\,\delta_i$ and $x_i \le 6\,\delta_i$ for every candy $i$
- $x_i \ge 0$ and integer, $\delta_i \in \lbrace 0,1\rbrace$

Result: cost **310**. More than one selection costs 310:

- notebook: 3 each of Buttery butterscotch, Caramel softie, Lemon sorbet and Lime sherbet, 6 Rose-water posy,
  5 Grape bunch (321 g);
- answers document: the same first four, 4 Rose-water posy and 6 Grape bunch (320 g).

Any selection that costs 310 and meets every constraint is correct. Without the three variety rules, the
cheapest selection (Week 3) costs 268, so variety adds 42 to the cost.

Notebook: [`Q3 Icki-Toffee - binary variables`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/4%20Tutorial%20Answers/Q3%20Icki-Toffee%20-%20binary%20variables.ipynb).
</details>

### About the answers document

The answers document (`4 Tutorial Answers`) shows the formulations and screenshots of **MATLAB** output:

- `sol` is the list of variable values, in item order (item 1 first).
- `fval` is the objective value. For the maximisation problems in Q1 it is **negative** (−270, −350, −250),
  because MATLAB's `intlinprog` always minimises, so the code minimises minus the survival value. The survival
  values are 270, 350 and 250.
- In Q3, the left column is the $x_i$ values and the right column the $\delta_i$ values.

---

## 7. How to read the Pyomo and HiGHS output

Each notebook prints three things:

1. **`model.pprint()`**, the model with your data filled in. Check every constraint against your formulation.
   This is the best place to catch typing mistakes.
2. **The HiGHS log.** In the browser, HiGHS prints its progress even when the code says `tee=False`. You
   can skip most of it. Look for the **Solving report** near the end: `Status Optimal` means the solver
   proved it found the best answer.
3. **`model.display()`**, the results:
   - under **Variables**, the `Value` column gives each variable's value (remember: `x[0]` is item 1);
   - under **Objectives**, `Value` is the optimal objective;
   - under **Constraints**, `Body` is the left-hand side at the optimum, shown next to its `Lower` and/or
     `Upper` limit. If `Body` equals the limit, the constraint is *binding* (it limits the answer).

**Small number effects.** A value printed as `-0.0` is zero. A value such as `0.9999999` or `1e-10` is the
solver's rounding: read it as 1 or 0.

**Different but equal answers.** If your objective value matches the expected one but the chosen items
differ, check that your choice satisfies every constraint. If it does, it is also optimal. This happens in
demo 2, demo 8, Q2 and Q3.

---

## 8. If something goes wrong

| Problem | What to do |
| --- | --- |
| `ModuleNotFoundError: No module named 'pyomo'` | Run the **first code cell** of the notebook again. The install lasts only for the open tab. |
| Nothing happens for a long time when you first run a cell | The first run downloads Python and the packages. Wait about a minute. If nothing has changed after that, reload the page and run the first cell again. |
| `NameError: name 'model' is not defined` (or similar) | You skipped a cell. Use *Run → Run All Cells*. |
| `ApplicationError: No executable found for solver 'glpk'` | Use `SolverFactory('appsi_highs')`. GLPK and CBC do not run in the browser. |
| The objective matches but the items differ from the expected result | See "Different but equal answers" in [section 7](#7-how-to-read-the-pyomo-and-highs-output). |
| Your own model gives a different objective | Compare `model.pprint()` with your paper formulation line by line. Check the variable types (`Binary`, `NonNegativeIntegers` or `NonNegativeReals`) and that item 1 is index 0. |
| `RuntimeError: A feasible solution was not found, so no solution can be loaded` | The model has no optimal solution. Scroll up to the HiGHS log and read its status. **Infeasible**: your constraints cannot all hold at once, so check the directions (`<=` or `>=`) and the right-hand sides. **Unbounded**: something can grow without limit, so a capacity, budget or upper-limit constraint is probably missing. |
| Your edits disappeared | Edits are kept only in the browser you used. Next time, download the notebook before you leave (section 1). |
| The `.pptx` or `.docx` does not open on the site | Download it and open it in PowerPoint or Word (section 1). |
| The site will not load at all | Try another browser (Chrome, Edge or Firefox). The notebooks also run in Google Colab or Anaconda Jupyter: the first cell installs the packages there too. |

---

## 9. Check your understanding

Try to answer each question in a sentence or two before you open the answer.

<details><summary>1. Why can the best integer solution not always be found by rounding the LP solution?</summary>

Rounded points can break a constraint, such as (2, 3) and (1, 3) on slide 7. The feasible ones can be far
from the best: (2, 2) gives 11, while the integer optimum (3, 2) gives 13. The integer optimum need not be
next to the LP optimum.
</details>

<details><summary>2. What is the difference between <code>Binary</code> and <code>NonNegativeIntegers</code> in Pyomo?</summary>

`Binary` allows only 0 or 1. `NonNegativeIntegers` allows any whole number 0, 1, 2, …. Q1a uses binary
variables (take an item or not), and Q1b uses non-negative integers (take several copies).
</details>

<details><summary>3. In the fire-station example, why is the constraint for city 2 written as x₁ + x₂ + x₆ ≥ 1?</summary>

Only cities 1 (10 min), 2 (0 min) and 6 (10 min) are within 15 minutes of city 2. At least one of them must
have a station.
</details>

<details><summary>4. Why is "xᵢ ≥ 6" the wrong way to model a minimum order of 6 kg?</summary>

It forces you to order at least 6 kg of every item, even ones you do not want. With
$6\delta_i \le x_i \le 10\delta_i$, the minimum applies only when $\delta_i = 1$ (the item is ordered).
</details>

<details><summary>5. How would you write "order exactly 3 different items"? And "if you order item 2, you must also order item 5"?</summary>

$\sum_i \delta_i = 3$. For the second rule, $\delta_2 \le \delta_5$: if $\delta_2 = 1$ then $\delta_5$ must be 1,
and if $\delta_2 = 0$ there is no restriction on item 5.
</details>

<details><summary>6. Adding the rule "at most 2 different items" lowered the profit from 81.6 to 80. Could adding a rule ever raise it?</summary>

No. A new constraint only removes options from the feasible region, so the best value can stay the same or
get worse, never better.
</details>

---

## 10. Checklist: have you finished the week?

- [ ] I ran `00_START_HERE.ipynb` and every cell printed `OK`.
- [ ] I read all the slides (1–32) and ran demos 1–7; my results match the table in section 5.
- [ ] I answered the "What do you notice?" / "Try it" question at the end of each demo before I looked
      at its answer.
- [ ] *(Optional)* I ran demo 8, minimum vertex cover.
- [ ] I wrote the formulations for Q1a, Q1b, Q1c, Q2 and Q3 on paper.
- [ ] I solved them in Python and got 270, 350, 250, 3 stations and a cost of 310.
- [ ] I compared my formulations with the answers document and the answer notebooks.
- [ ] I can explain the linking pattern $L\delta_i \le x_i \le U\delta_i$ and the counting rule
      $\sum_i \delta_i \le k$ in my own words.
- [ ] I downloaded any notebooks I changed and want to keep.

**Next week (Week 6)** continues with integer programming: fire stations with building costs, security
cameras as a vertex cover, and assignment problems.

---

## 11. Assumptions

These points are not stated in the course material for this week. This README assumes them:

1. **Order of work:** the slides and demos come before the tutorial, and the tutorial comes before the
   answers. The answer notebooks say "Release after the practical", but they are already in this folder, so
   a student working alone is trusted to attempt each question first.
2. **Demo 8 is optional.** It is not on the slides, and its notebook calls it a preview of Week 6.
3. **The `5 Source Files` folder is not required.** Every script in it has a notebook version.
4. **Slide numbers** count every slide in the `.pptx`, including the hidden empty slide 3.
5. **No time estimates or deadlines** are given, because the course material does not state them.
6. **Next week's topics** (end of section 10) are taken from the Week 6 demo notebook names, not from a
   timetable.
7. **The download links** in section 1 point to the files on the repository's `main` branch.

# Week 9: The Travelling Salesman Problem (TSP)

A salesman has to visit a list of cities, **each exactly once**, and come back to where he started. Which
order of cities gives the **shortest total journey**? That is the Travelling Salesman Problem. It sounds
simple, but it is one of the most famous hard problems in mathematics and computing.

This week you will learn:

| Topic | Slides | What you should be able to do afterwards |
| --- | --- | --- |
| Counting tours | 3–6 | Work out how many different tours *n* cities have, and explain why trying them all is hopeless |
| Why the TSP is hard | 7–8 | Explain in plain words what NP, NP-complete and NP-hard mean |
| Where the TSP appears | 9–11 | Give real examples (delivery routes, drilling circuit boards) |
| The TSP as a MILP | 12–14 | Write the first model and explain why it fails (*subtours*) |
| The MTZ constraints | 15–19 | Explain how the Miller–Tucker–Zemlin constraints remove subtours, and check them on a small tour |
| Solving it in Python | 20 | Run the Pyomo model and read its output |
| Heuristics | 21 | Explain what a genetic algorithm does and why it gives no guarantee |

The week has **one slide deck, one notebook to run and one answers notebook**. There is no separate
tutorial sheet: the tutorial tasks are on **slide 22**, and you do them in the notebook.

## Contents

1. [Before you start](#1-before-you-start)
2. [How to open the files](#2-how-to-open-the-files)
3. [What is in this folder](#3-what-is-in-this-folder)
4. [Your plan for the week](#4-your-plan-for-the-week)
5. [The key ideas, explained](#5-the-key-ideas-explained)
6. [Lecture guide: slide by slide](#6-lecture-guide-slide-by-slide)
7. [The demo notebook, cell by cell](#7-the-demo-notebook-cell-by-cell)
8. [Tutorial (slide 22): tasks, hints and how to check your answers](#8-tutorial-slide-22-tasks-hints-and-how-to-check-your-answers)
9. [How to read the answers notebook](#9-how-to-read-the-answers-notebook)
10. [If something goes wrong](#10-if-something-goes-wrong)
11. [Check your understanding](#11-check-your-understanding)
12. [Checklist: have you finished the week?](#12-checklist-have-you-finished-the-week)
13. [What comes next](#13-what-comes-next)
14. [Assumptions](#14-assumptions)

---

## 1. Before you start

You will use these ideas from earlier weeks. If one of them is unclear, look back before you begin.

| You need | Where it was taught |
| --- | --- |
| Binary variables (a variable that can only be 0 or 1) and mixed-integer linear programs (MILP) | Weeks 05 and 06 |
| Reading and running a Pyomo model: `Var`, `Objective`, `Constraint`, `SolverFactory` | Weeks 03–06 |
| Networks: cities as vertices, roads as edges with a weight (distance or cost) | Week 08 |

You do **not** need to install anything. Everything runs in your web browser.

---

## 2. How to open the files

The course site is **https://ctsallis.github.io/operational_research/**. On the left it shows a file
browser with the course folders. This week's folder is

`Lectures/Semester 1/Week 09 - Travelling Salesman Problem`

### The slides (`.pptx`): download them

The course site cannot display PowerPoint files. To open the slides:

1. In the file browser, open the folder `1 Lecture`.
2. **Right-click** `Travelling Salesman Problem.pptx` → **Download**.
3. Open the downloaded file in **PowerPoint**.

The links on slides 11, 21, 22 and 23 open web pages and videos. Click them in PowerPoint (in *Slide
Show* mode, a single click; in the normal editing view, **Ctrl + click**).

### The notebooks (`.ipynb`): run them in your browser

1. In the file browser, open the folder `2 Lecture Demos` and **double-click** `1 TSP with Pyomo.ipynb`.
   (Or use the direct link: [open the demo notebook on the course site](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2009%20-%20Travelling%20Salesman%20Problem/2%20Lecture%20Demos/1%20TSP%20with%20Pyomo.ipynb).
   Slide 22 has the same link.)
2. Choose the menu **Run → Run All Cells**.
3. Wait. The **first code cell installs Pyomo and the HiGHS solver**, which can take up to a minute the
   first time. While a cell is running, its left margin shows `[*]`. When it has finished, the star
   becomes a number, e.g. `[3]`.
4. The notebook is finished when **every code cell shows a number** and the last plot has appeared.

The notebooks were saved **without results**: you see output only after you run them.

> **Your changes are kept only in this browser.** Clearing your browser data, using a private window or
> moving to another computer loses them. To keep your work: right-click the notebook in the file
> browser → **Download**. You can also run a downloaded notebook in Google Colab or Anaconda Jupyter.

### This README

On the course site: right-click `README.md` → **Open With → Markdown Preview**.

---

## 3. What is in this folder

| Folder | File | What it is | When to use it |
| --- | --- | --- | --- |
| `1 Lecture` | `Travelling Salesman Problem.pptx` | The lecture: 23 slides | First. Section 6 below guides you through it |
| `2 Lecture Demos` | `1 TSP with Pyomo.ipynb` | The TSP model in Pyomo on 4 and 20 cities, and a genetic algorithm on 35 cities. **This is also where you do the tutorial** | After slide 20 |
| `4 Tutorial Answers` | `Tutorial answers (slide 22).ipynb` | Full answers to the slide 22 tasks: solve times for 5 to 35 cities, five genetic-algorithm settings compared, answers to the research questions | **Only after** you have tried the tutorial yourself |

There is no `3 Tutorial` folder. The tutorial tasks are on slide 22 (and in section 8 below).

---

## 4. Your plan for the week

Work through these steps in order. The times are rough guides.

1. **Read section 5.1** (the words you need), 5 minutes.
2. **Slides 1–11** with sections 5.2–5.5: the problem, counting tours, why it is hard, applications.
   About 40 minutes. Do the 4-city count in section 5.3 with pen and paper.
3. **Slides 12–19** with sections 5.6–5.7: the MILP model, subtours and the MTZ constraints. About 1 hour.
   This is the core of the week; take your time and check the worked example in section 5.7 yourself.
4. **Slide 20 and the demo notebook** (section 7): run it and compare every result with the expected
   ones. About 30 minutes.
5. **Slide 21** with section 5.8: heuristics and the genetic algorithm. 15 minutes.
6. **The tutorial, slide 22** (section 8): the experiments in the notebook and the three research
   questions. About 1.5 hours.
7. **Check your answers** with the answers notebook (section 9).
8. **Test yourself** with section 11 and tick off the checklist in section 12.
9. Optional: watch the video on slide 23 (Bill Cook, about one hour).

---

## 5. The key ideas, explained

### 5.1 Words you need this week

| Word | Meaning |
| --- | --- |
| **City** | A place that must be visited. In the model the cities are numbered 1, 2, …, *n* |
| **Cost** $c_{ij}$ | The cost (or distance, or time) of going from city *i* to city *j* |
| **Symmetric** | Going from *i* to *j* costs the same as going from *j* to *i*: $c_{ij} = c_{ji}$. All examples this week are symmetric |
| **Tour** | A route that visits every city exactly once and returns to the start, e.g. 1 → 2 → 4 → 3 → 1 |
| **Subtour** | A closed loop that visits only *some* of the cities, e.g. 2 → 3 → 2 |
| **Brute force** | Trying every possible tour and keeping the shortest |
| **Polynomial time** | The work grows like a power of *n*, such as $n^2$ or $n^3$. Considered "fast" |
| **MILP** | Mixed-integer linear program: a linear program in which some variables must be whole numbers (here, 0 or 1) |
| **MTZ constraints** | The Miller–Tucker–Zemlin constraints, which stop the model from choosing subtours |
| **Heuristic** | A method that finds a *good* answer quickly but does not prove it is the best |
| **Genetic algorithm (GA)** | A heuristic that imitates evolution: good tours are combined and changed at random, and the best survive |

### 5.2 The problem (slide 2)

You are given *n* cities and the cost $c_{ij}$ of travelling between each pair. Find the cheapest way to
visit all the cities and return to the starting point.

### 5.3 How many tours are there? (slides 3–6)

Fix the starting city (it does not matter which one: a tour is a loop). With 4 cities A, B, C, D and
start A:

- there are 3 choices for the second city,
- then 2 choices for the third,
- then 1 choice for the last,

so $3 \times 2 \times 1 = 3! = 6$ orders. But **A–B–C–D–A and A–D–C–B–A are the same loop driven in
opposite directions**. When the costs are symmetric they cost the same, so each tour has been counted
twice. The number of different tours is

$$\frac{(n-1)!}{2}$$

| Cities *n* | Different tours $(n-1)!/2$ |
| --- | --- |
| 4 | 3 |
| 5 | 12 |
| 10 | 181,440 |
| 20 | about $6.1 \times 10^{16}$ |
| 22 | 25,545,471,085,854,720,000 (about $2.6 \times 10^{19}$, slide 6) |
| 40 | about $10^{46}$ |

**Try it by hand (the 4-city example from the notebook).** The costs are:

| | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| **1** | – | 10 | 15 | 20 |
| **2** | 10 | – | 35 | 25 |
| **3** | 15 | 35 | – | 30 |
| **4** | 20 | 25 | 30 | – |

The 3 different tours starting at city 1 are:

| Tour | Length |
| --- | --- |
| 1 → 2 → 3 → 4 → 1 | 10 + 35 + 30 + 20 = 95 |
| 1 → 2 → 4 → 3 → 1 | 10 + 25 + 30 + 15 = **80** (shortest) |
| 1 → 3 → 2 → 4 → 1 | 15 + 35 + 25 + 20 = 95 |

The notebook should find 80 (section 7).

**Slide 6.** A newspaper claimed a laptop would need 1,000 years to find the best route between 22
cities. That is only true for brute force. Good solvers do **not** try every tour (section 5.4), so
the claim is "partly right".

### 5.4 Why the TSP is hard: P, NP, NP-complete, NP-hard (slides 7–8)

These words describe how the work needed grows as the problem gets bigger. They are easy to mix up, so
read slowly.

- **Yes/no version.** Instead of "find the shortest tour", ask: *"Is there a tour of length at most L?"*
- **NP** (Nondeterministic Polynomial time) is the class of yes/no problems where a proposed answer can
  be **checked** quickly (in polynomial time). For the TSP: if someone hands you a tour, you can add up
  its length and compare it with L in a few steps. NP does **not** mean "non-polynomial".
- **NP-complete** means: in NP, *and* among the hardest problems in NP. If anyone found a fast
  (polynomial-time) algorithm for one NP-complete problem, every problem in NP would have one. The yes/no
  TSP is NP-complete. So is Sudoku (on $n^2 \times n^2$ grids).
- **NP-hard** means at least as hard as every problem in NP, whether or not it is in NP itself. **Finding
  the shortest tour is NP-hard.**
- **P = NP?** Nobody knows whether fast algorithms exist for these problems. It is one of the seven
  Millennium Prize Problems, with a prize of one million dollars (slide 8). Most experts believe the answer is no.

What this means in practice: no known method solves **every** TSP quickly. Good methods still solve
**many** TSPs with thousands of cities, as you will see.

### 5.5 Where the TSP appears (slides 9–11)

Delivery and bus routes, engineers' service calls, and drilling holes in a circuit board (the drill must
visit every hole once, as fast as possible). Slide 10 shows a newspaper article about Santa's route.
Slide 11 introduces William Cook, an expert on the TSP; his website is linked on the slide.

### 5.6 The TSP as a MILP, first attempt (slides 12–14)

**Decision variables.** For every pair of different cities *i* and *j*:

$$x_{ij} = \begin{cases} 1 & \text{if the tour goes directly from city } i \text{ to city } j \\ 0 & \text{otherwise} \end{cases}$$

The arc from *i* to *j* and the arc from *j* to *i* are separate variables. $E$ is the set of all
pairs $(i, j)$ with $i \neq j$.

**Model.**

$$
\begin{aligned}
\min \quad & \sum_{(i,j) \in E} c_{ij}\, x_{ij} && \text{total length of the arcs used} \\
\text{s.t.} \quad & \sum_{j \neq i} x_{ij} = 1 && \text{for every city } i \text{ (leave each city exactly once)} \\
& \sum_{j \neq i} x_{ji} = 1 && \text{for every city } i \text{ (enter each city exactly once)} \\
& x_{ij} \in \lbrace 0, 1 \rbrace
\end{aligned}
$$

**Why it is wrong (slides 13–14).** Every city now has exactly one arc in and one arc out, but nothing
says the arcs form **one** loop. The solution can split into several small loops, called **subtours**.
For example, with 5 cities: 1 → 2 → 1 and 3 → 4 → 5 → 3. Every city is entered once and left once,
yet the salesman never gets from city 2 to city 3.

Because subtours are often *shorter* than a real tour, the solver happily chooses them. In the notebook,
the 20-city problem without the extra constraints gives 10 two-city loops with total length 373.11,
shorter than the real optimal tour (407.97).

### 5.7 The Miller–Tucker–Zemlin (MTZ) constraints (slides 15–19)

**Idea.** Give every city except city 1 a number $u_i$ that records **when** the city is visited. If the
tour goes from *i* to *j*, then *j* is visited after *i*, so we want $u_j \geq u_i + 1$.

**The constraint**, for every pair of cities *i*, *j* in $\lbrace 2, \dots, n \rbrace$ with $i \neq j$:

$$u_i - u_j + 1 \leq (n - 1)(1 - x_{ij})$$

Read it in two cases:

| Case | Right-hand side | What the constraint says |
| --- | --- | --- |
| $x_{ij} = 1$ (arc used) | $(n-1) \times 0 = 0$ | $u_i - u_j + 1 \leq 0$, i.e. $u_j \geq u_i + 1$: *j* comes after *i* |
| $x_{ij} = 0$ (arc not used) | $n - 1$ | $u_i - u_j \leq n - 2$: always true when the $u$ values are visit positions (they differ by at most $n-2$), so it does nothing |

The number $n - 1$ is a "big number" that switches the constraint off when the arc is not used.

**Why subtours become impossible.** Take any loop that does **not** contain city 1, say
$k_1 \to k_2 \to \dots \to k_m \to k_1$. MTZ applies to every arc in it:

$$u_{k_2} \geq u_{k_1} + 1,\quad u_{k_3} \geq u_{k_2} + 1,\quad \dots,\quad u_{k_1} \geq u_{k_m} + 1$$

Add all *m* inequalities: the $u$'s cancel and you get $0 \geq m$, which is impossible. So **every loop
must pass through city 1**. Each city has only one way in and one way out, so there can be only one
loop through city 1, and it must contain every city: a single tour. (Slide 16 shows the smallest case:
$x_{ij} = x_{ji} = 1$ would need $u_j \geq u_i + 1$ and $u_i \geq u_j + 1$ at the same time.)

**Why city 1 is left out.** The tour has to come back to city 1 at the end. If city 1 had a $u$ value
too, the last arc back to city 1 would demand that city 1 comes *after* the last city, which
contradicts it being the first. Leaving city 1 out of MTZ allows exactly that one "return" arc
(slide 18).

**Worked check (do it yourself).** Take the 4-city optimal tour 1 → 2 → 4 → 3 → 1, so $n = 4$ and
$n - 1 = 3$. Give the cities after city 1 their positions: $u_2 = 2$, $u_4 = 3$, $u_3 = 4$.

| Pair | Arc used? | Constraint | With the numbers | OK? |
| --- | --- | --- | --- | --- |
| 2 → 4 | yes | $u_2 - u_4 + 1 \leq 0$ | $2 - 3 + 1 = 0 \leq 0$ | ✔ |
| 4 → 3 | yes | $u_4 - u_3 + 1 \leq 0$ | $3 - 4 + 1 = 0 \leq 0$ | ✔ |
| 3 → 2 | no | $u_3 - u_2 + 1 \leq 3$ | $4 - 2 + 1 = 3 \leq 3$ | ✔ |
| 2 → 3 | no | $u_2 - u_3 + 1 \leq 3$ | $2 - 4 + 1 = -1 \leq 3$ | ✔ |
| 3 → 4 | no | $u_3 - u_4 + 1 \leq 3$ | $4 - 3 + 1 = 2 \leq 3$ | ✔ |
| 4 → 2 | no | $u_4 - u_2 + 1 \leq 3$ | $3 - 2 + 1 = 2 \leq 3$ | ✔ |

All six MTZ constraints hold, so the real tour is allowed. (The arcs 1 → 2 and 3 → 1 touch city 1, so
they have no MTZ constraint.)

**The full MTZ model (slide 19)** is the model of section 5.6 plus the MTZ constraints, with
$u_i$ any real number for $i = 2, \dots, n$. Many textbooks also add the bounds $2 \leq u_i \leq n$. They
are not needed for correctness, and the notebook does not use them, which is why its $u$ values can
look odd (section 7).

**Size.** For *n* cities the model has $n^2$ variables $x_{ij}$ (the notebook also creates $x_{ii}$ and
fixes it to 0), $n - 1$ variables $u_i$, and $(n-1)(n-2)$ MTZ constraints. For 20 cities: 400 binary
variables, 19 real ones and 342 MTZ constraints.

### 5.8 Heuristics and the genetic algorithm (slide 21)

When the exact model takes too long, we can settle for a **good** tour instead of the **best** one. A
heuristic does that. The demo uses a **genetic algorithm**:

1. **Population.** Start with many random tours (100 in the demo). A tour is stored as a list of city
   numbers, e.g. `[3, 1, 4, 2]`.
2. **Fitness.** Measure each tour's length. Here *smaller is better*.
3. **Selection (tournament).** Pick 5 tours at random; the shortest becomes a parent. Repeat to get
   enough parents.
4. **Crossover** (with probability `crossover_rate`). Combine two parents into two children: each child
   keeps a piece of one parent and fills in the missing cities in the order they appear in the other
   parent, so every child is still a valid tour.
5. **Mutation** (with probability `mutation_rate`). Swap two cities in a child, to try something new.
6. **Survival.** Keep the best 100 tours among parents and children. Repeat from step 3 for a number of
   **generations** (200 in the demo).

The GA always returns a tour, quickly, even for hundreds of cities. But it gives **no guarantee**: it
cannot tell you how far its tour is from the shortest one. The MILP is the opposite: it proves its tour
is the shortest, but becomes very slow as *n* grows.

---

## 6. Lecture guide: slide by slide

| Slides | Title | What to take from it | Explained in |
| --- | --- | --- | --- |
| 1–2 | Travelling Salesman Problem; The Problem | The problem statement | 5.2 |
| 3–5 | Complexity | $(n-1)!/2$ tours; brute force is of order $n!$ | 5.3 |
| 6 | Some Numbers… | 22 cities have $2.6 \times 10^{19}$ tours; brute force is not the only method | 5.3 |
| 7 | NP-Complete | NP means "answers can be checked quickly", not "non-polynomial" | 5.4 |
| 8 | P = NP? | The one-million-dollar Millennium Prize question | 5.4 |
| 9–11 | Applications; TSP in the news; William Cook | Where the TSP appears; an expert to follow | 5.5 |
| 12 | MILP | Variables $x_{ij}$; one arc out and one arc in per city. The question "why is this wrong?" | 5.6 |
| 13–14 | MILP; Subtour example | The answer: subtours (red = one tour, blue = three subtours; both obey the in/out constraints) | 5.6 |
| 15 | Solution | The $u_i$ variables and the MTZ constraint | 5.7 |
| 16–18 | Why does this work? | Arc used ⇒ $u_j \geq u_i + 1$; the $u$'s increase along the tour; the last arc returns to city 1 | 5.7 |
| 19 | Miller-Tucker-Zemlin (MTZ) Formulation | The complete model | 5.7 |
| 20 | Pyomo Code | Run the demo notebook now | 7 |
| 21 | Heuristics | Good, not necessarily optimal, solutions; a visualisation video | 5.8 |
| 22 | Tutorial | Your tasks | 8 |
| 23 | A must watch video | Bill Cook's public lecture (optional) | – |

On slide 14 the formula is a picture and is written "$\lbrace 1, \dots\, n \rbrace$" without the comma
before *n*. It means the same as $\lbrace 1, \dots, n \rbrace$ on the other slides.

---

## 7. The demo notebook, cell by cell

`2 Lecture Demos/1 TSP with Pyomo.ipynb`. Run it with **Run → Run All Cells** (section 2). After the
install, the whole notebook takes well under a minute. **Run the cells in order**: later cells use
functions defined in earlier ones.

| Cell (heading above it) | What it does | What you should see |
| --- | --- | --- |
| First code cell (no heading) | Installs Pyomo and HiGHS; adapts Pyomo to the browser | A short install message, or nothing. No error |
| *The TSP model with the Miller–Tucker–Zemlin (MTZ) constraints* | Builds the MTZ model for the 4 cities of section 5.3 and solves it | See below |
| *20 random cities, with and without the MTZ constraints* | 20 random cities: solves with MTZ, then switches MTZ off and solves again | Three plots, see below |
| *A heuristic: genetic algorithm on 35 cities* | Runs the genetic algorithm on 35 random cities | `Best fitness: 599.2423493491926` and a plot |
| *What do you notice?* and *Try it* | Questions. Click **Answer** to reveal each answer | – |

### Reading the 4-city output

The cell prints a lot: first the solver's progress log (`tee=True`), then the whole model
(`model.pprint()`), then the values (`model.display()`). **Scroll to the very end** of the output. The last
lines are the answer:

```
Node 1 -> Node 2
Node 2 -> Node 4
Node 3 -> Node 1
Node 4 -> Node 3
Optimal distance: 80.0
```

Each line is one arc with $x_{ij} = 1$. To read the tour, start at node 1 and follow the arrows:
1 → 2, then 2 → 4, then 4 → 3, then 3 → 1. The tour is **1 → 2 → 4 → 3 → 1, length 80**, as you found
by hand in section 5.3. (On another computer the solver may print the same tour in the opposite
direction, 1 → 3 → 4 → 2 → 1. It has the same length.)

In the `model.display()` part, the values of `u` may be, for example, `0, 2, 1` for cities 2, 3, 4,
not `2, 4, 3` as in the worked check of section 5.7. Both are correct. The model puts no bounds on
$u$, so only the **order** matters: along the tour 2 → 4 → 3 the values increase (0 < 1 < 2).

### Reading the three 20-city plots

1. **Cities**: 20 red dots, numbered. `np.random.seed(0)` makes them the same every time.
2. **TSP Solution** (with MTZ): **one** closed loop through all 20 cities, total length **407.97** (the
   length is not printed; section 8 shows how to print it). In order:
   1 – 3 – 17 – 15 – 8 – 18 – 13 – 9 – 14 – 16 – 12 – 4 – 7 – 10 – 11 – 20 – 5 – 6 – 2 – 19 – 1.
3. **TSP Solution** again, after `model.mtz_subtour_elimination.deactivate()`: **10 separate pairs**,
   each a two-city loop (go to a neighbour and straight back): 1–12, 2–19, 3–17, 4–16, 5–6, 7–10, 8–15,
   9–14, 11–20, 13–18. Total length 373.11. Shorter, but not a tour. This is the subtour problem of
   section 5.6, made visible.

The second and third plots have the same title; only the second is a real tour.

### The genetic algorithm output

`Best solution:` is the best tour found (a list of 35 city numbers in visiting order) and `Best fitness:`
its length, **599.24**. The shortest tour for these 35 cities is 518.52, so the GA's tour is 15.6 %
longer. The line `random.seed(1)` makes the random choices the same on every run. Delete it, or change
the 1, to see how much the result varies from run to run.

---

## 8. Tutorial (slide 22): tasks, hints and how to check your answers

Slide 22 asks you to:

1. Use the notebook to investigate the TSP:
   - (a) try out the problem;
   - (b) increase the problem size: when does it become unreasonable to solve?
   - (c) change the genetic algorithm's settings (mutation, crossover, population). Can it solve larger
     problems than the MILP can?
2. Research the TSP:
   - (a) Why is it hard to solve?
   - (b) What is NP-hard?
   - (c) What is combinatorial optimisation?

Do everything in the demo notebook, **after** running all its cells once. Write your answers down
(on paper or in a new Markdown cell) **before** you open the answers notebook.

### Task 1(a): try out the problem

Run the demo and check every result against section 7. Then change something small and predict the
result before you run it. For example, in the 4-city cell change the cost of (2, 4) **and** (4, 2) from
25 to 40, run the cell again, and check the answer by hand with the table of section 5.3.

<details><summary>Answer for the changed cost</summary>

The three tours now have lengths 95, 10 + 40 + 30 + 15 = 95, and 15 + 35 + 40 + 20 = 110. Two tours
tie at 95, so the solver prints 95 with either 1 → 2 → 3 → 4 → 1 or 1 → 2 → 4 → 3 → 1 (or one of them
in reverse). Set the costs back to 25 afterwards.
</details>

### Task 1(b): when does the MILP become unreasonable?

**Step 1.** Click the last cell of the notebook, then click the **+** button in the notebook's toolbar: it
adds an empty cell below. Paste this code into it and run it (**Shift + Enter**):

```python
import time

for n in [5, 10, 15, 20, 25, 30]:
    cities = generate_random_points(n)
    model_n = create_tsp_model(n, compute_distance_matrix(cities))
    start = time.perf_counter()
    solve_tsp(model_n)
    seconds = time.perf_counter() - start
    print(n, "cities: shortest tour", round(value(model_n.obj), 2), "found in", round(seconds, 1), "s")
```

It uses the functions defined earlier in the notebook, and takes about 15 seconds in the browser.

**Step 2.** Add 35 to the list and run it again (35 cities alone take about 20–30 seconds).

**Step 3.** Write down how the time grows. Is it smooth? When would you call it "unreasonable"?

**Hints.**
- `generate_random_points(n)` always uses the same seed, so the first 20 cities of every run are the
  demo's 20 cities. Your lengths should match the table below exactly; your times will not (they depend
  on your computer and browser).
- **Do not try 40 or more cities in the browser** unless you are ready to wait several minutes. If a cell
  runs much too long, choose **Kernel → Restart Kernel**. Then make the slow cell smaller (or delete it:
  select it and press `D` twice) **before** you run the notebook again from the top (**Run → Run All Cells**);
  otherwise *Run All* starts the same slow calculation again.

<details><summary>Check your numbers</summary>

| Cities | Shortest tour | Typical time in the browser |
| --- | --- | --- |
| 5 | 158.71 | under 1 s |
| 10 | 343.89 | about 1 s |
| 15 | 381.58 | about 2 s |
| 20 | 407.97 | about 3 s |
| 25 | 475.37 | about 1–2 s |
| 30 | 511.32 | about 6–8 s |
| 35 | 518.52 | about 20–30 s |
| 40 | (not in the table) | several minutes |

A desktop Python installation is several times faster (35 cities: about 3 seconds).

**What to conclude.** The time does not grow smoothly (25 cities can be faster than 20, because the
difficulty depends on where the cities are, not only on how many), but the trend is steep: every few
extra cities can multiply the time. In the browser, with this model, "unreasonable" starts at around
35–40 cities. Note that the solver does **not** try all tours: 35 cities have about $1.5 \times 10^{38}$
tours, yet the solver needs only seconds, because branch and bound rules out most tours without
looking at them.
</details>

### Task 1(c): the genetic algorithm's settings

The settings are in the last code cell of the demo, just above `random.seed(1)`:

```python
population_size = 100
num_generations = 200
tournament_size = 5
crossover_rate = 0.7
mutation_rate = 0.2
```

**Step 1.** Change **one** setting at a time, run the cell, and write down `Best fitness`. Try:
`crossover_rate = 0.0`, then `mutation_rate = 0.8`, then `population_size = 300`, then
`num_generations = 1000`. Put each one back before changing the next.

**Step 2.** For each run, work out how far it is above the shortest tour (518.52):

$$\text{gap} = 100 \times \frac{\text{GA length} - 518.52}{518.52} \ \%$$

**Step 3.** Try a size the MILP cannot handle in the browser. Insert a new cell at the end and run:

```python
n = 60
cities = generate_random_points(n)
distances = compute_distance_matrix(cities)
random.seed(1)
tour, length = genetic_algorithm(n, distances, 100, 200, 5, 0.7, 0.2)
print("Genetic algorithm,", n, "cities: length", round(length, 2))
plot_tsp_solution_ga(cities, tour)
```

It takes a few seconds and prints a length of **1137.27**. Look at the plot: do the lines cross? (A tour
whose lines cross can always be shortened by "uncrossing" them, so crossings show the tour is not
optimal.)

**Hint.** Each run uses one seed. A different seed gives different numbers, so to compare settings
fairly you would run each several times.

<details><summary>Check your numbers</summary>

| Population | Generations | Crossover | Mutation | Length | Above the shortest tour |
| --- | --- | --- | --- | --- | --- |
| 100 | 200 | 0.7 | 0.2 | 599.24 | 15.6 % (the demo's settings) |
| 100 | 200 | 0.0 | 0.2 | 703.56 | 35.7 % |
| 100 | 200 | 0.7 | 0.8 | 573.02 | 10.5 % |
| 300 | 200 | 0.7 | 0.2 | 577.83 | 11.4 % |
| 100 | 1000 | 0.7 | 0.2 | 593.08 | 14.4 % |

**What to conclude.**
- Without crossover the result is much worse: crossover combines good pieces of different tours.
- More mutation helps here. A larger population also helps but takes about three times as long.
- Many more generations hardly help: the tours in the population become nearly identical, and only
  mutation still changes them.
- **Can it solve larger problems than the MILP?** It always returns a tour quickly, for 60 or 100 cities
  as easily as for 35. But "solve" needs care: it never proves its tour is the best, and even on 35
  cities its best result was still 10 % longer than the optimum that the MILP found and proved. For
  very large problems, heuristics are the practical choice; for problems the MILP can handle, the MILP
  gives the guaranteed answer.
</details>

### Task 2: research questions

Use sections 5.3 and 5.4, slides 3–8, and your own reading. Answer each question in 3–6 sentences in
your own words.

**Hints.**
- (a) Why hard: think about how fast $(n-1)!/2$ grows, and whether any known method avoids an
  exponential amount of work in the worst case.
- (b) NP-hard: explain NP first (checking an answer is quick), then what "hard" adds. Say how the yes/no
  TSP and the "find the shortest tour" TSP fit.
- (c) Combinatorial optimisation: what kind of choices are being made (orders, subsets, assignments)?
  Give examples from earlier weeks: knapsack and set covering (Week 05), assignment (Week 06), job shop
  scheduling (Week 07), shortest paths and spanning trees (Week 08).

Then compare your answers with section 2 of the answers notebook.

### How to mark your own work

- **Numbers** (tour lengths, gaps): must match the tables to 2 decimal places. If they don't, you
  probably changed a setting and forgot to change it back, or ran cells out of order. Restart and run
  everything from the top.
- **Times**: will differ from the tables. Only the pattern matters.
- **Written answers**: check that you used the key words correctly: NP is about **checking** answers
  quickly; NP-hard means **at least as hard** as every problem in NP; a heuristic gives **no guarantee**.

---

## 9. How to read the answers notebook

`4 Tutorial Answers/Tutorial answers (slide 22).ipynb`
([open it on the course site](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2009%20-%20Travelling%20Salesman%20Problem/4%20Tutorial%20Answers/Tutorial%20answers%20%28slide%2022%29.ipynb)).
Run it with **Run → Run All Cells**. It takes about a minute and a half in the browser.

| Part | What it shows |
| --- | --- |
| First code cell | Installs Pyomo and HiGHS, as in the demo |
| *The model and the cities* | The demo's functions, copied so this notebook runs on its own. Nothing is printed |
| *1(a)* | A table: cities, shortest tour, solve time, for 5 to 35 cities (about 40 seconds), then the written answer |
| *1(b)* | A table: population, generations, crossover, mutation, length, % above the optimum, time; then the written answer |
| *2. Research questions* | Model answers to the three questions |

The **lengths** must match the tables in section 8 exactly; the **times** will differ.

---

## 10. If something goes wrong

| Problem | What to do |
| --- | --- |
| The `.pptx` shows an error or strange characters on the site | The site cannot display PowerPoint files. Right-click → **Download** and open it in PowerPoint |
| `ModuleNotFoundError: No module named 'pyomo'` | Run the first code cell (the install cell) again. Installs last only while the browser tab is open |
| `NameError: name 'create_tsp_model' is not defined` (or another name) | You ran a cell before the cells above it. Choose **Run → Run All Cells**, or run the cells from the top in order |
| A cell shows `[*]` for a long time | It is still working. The install cell can take a minute; 35 cities take up to half a minute. If it is far longer than the times in section 8: **Kernel → Restart Kernel**, then **Run → Run All Cells** |
| The 4-city cell prints pages of text | That is normal (the solver log and the whole model). Scroll to the end for the tour and the length |
| My tour is printed in the other direction | Same tour, same length. Correct |
| My `u` values are not 2, 3, 4 | Correct: only their order matters (section 7) |
| My GA numbers differ from the tables | Check that `random.seed(1)` is still there and that you changed only one setting. Restart the kernel and run all cells again |
| My notebook changes have disappeared | Changes are stored only in the browser you used. Download your copy before you leave (section 2) |
| The course site does not work at all | Download the notebook (from the site, or from the GitHub repository `ctsallis/operational_research`) and open it in Google Colab or Anaconda Jupyter. The first cell installs what is needed |

---

## 11. Check your understanding

Try each question first, then click to see the answer.

**Q1.** How many different tours are there for 6 cities with symmetric costs?

<details><summary>Answer</summary>

$(6-1)!/2 = 120/2 = 60$.
</details>

**Q2.** Why do we divide by 2 when counting tours?

<details><summary>Answer</summary>

Each tour can be travelled in two directions, A–B–C–D–A and A–D–C–B–A. With symmetric costs both have
the same length, so they are the same tour and would otherwise be counted twice.
</details>

**Q3.** True or false: "NP means the problem cannot be solved in polynomial time."

<details><summary>Answer</summary>

False. NP means a proposed answer can be **checked** in polynomial time. Whether every NP problem can
also be **solved** in polynomial time is exactly the open question P = NP.
</details>

**Q4.** With 6 cities, the first model (without MTZ) returns 1 → 2 → 1 and 3 → 4 → 5 → 6 → 3. Which
constraints of the first model does this satisfy, and which MTZ constraints does it break?

<details><summary>Answer</summary>

Every city has exactly one arc out and one arc in, so it satisfies all the constraints of the first
model. The loop 3 → 4 → 5 → 6 → 3 does not contain city 1, so MTZ applies to all four arcs:
$u_4 \geq u_3 + 1$, $u_5 \geq u_4 + 1$, $u_6 \geq u_5 + 1$, $u_3 \geq u_6 + 1$. Adding them gives
$0 \geq 4$, impossible. So no values of $u$ make this solution feasible.
</details>

**Q5.** For 4 cities and the tour 1 → 3 → 2 → 4 → 1, choose values for $u_2, u_3, u_4$ and check the MTZ
constraint for the arc 2 → 4 (used) and for 4 → 2 (not used).

<details><summary>Answer</summary>

Use visit positions: $u_3 = 2$, $u_2 = 3$, $u_4 = 4$. Arc 2 → 4 is used:
$u_2 - u_4 + 1 = 3 - 4 + 1 = 0 \leq 0$ ✔. Arc 4 → 2 is not used: $u_4 - u_2 + 1 = 4 - 3 + 1 = 2 \leq n - 1 = 3$ ✔.
</details>

**Q6.** Why does city 1 have no $u$ variable and no MTZ constraints?

<details><summary>Answer</summary>

The tour must end by returning to city 1. If city 1 were in the MTZ constraints, that last arc would
require city 1 to come after the last city, contradicting it being first. Leaving it out allows that
single return arc.
</details>

**Q7.** In the MTZ constraint, what is the job of the factor $(n-1)$?

<details><summary>Answer</summary>

It is a "big number". When $x_{ij} = 0$ the right-hand side becomes $n - 1$, which is large enough that
the constraint holds for any sensible $u$ values, so it has no effect. When $x_{ij} = 1$ the right-hand
side is 0 and the constraint forces $u_j \geq u_i + 1$.
</details>

**Q8.** Without MTZ, why does the 20-city solution consist of two-city loops?

<details><summary>Answer</summary>

The model then only asks for one arc in and one arc out of every city. The cheapest way to do that is to
go from each city to a close neighbour and straight back. That gives pairs (total 373.11), which is
shorter than any real tour (407.97).
</details>

**Q9.** The genetic algorithm found a 35-city tour of length 599.24. Can you tell from the GA alone how
close this is to the shortest tour?

<details><summary>Answer</summary>

No. A heuristic gives no bound on how far it is from the optimum. We only know it is 15.6 % longer
because the MILP found and proved the shortest tour, 518.52.
</details>

**Q10.** Why does the notebook test `value(model.x[i, j]) > 0.5` instead of `== 1`?

<details><summary>Answer</summary>

Solvers work with decimal numbers and may return 0.9999999 instead of exactly 1. Comparing with 0.5
treats anything close to 1 as "arc used" and anything close to 0 as "not used".
</details>

---

## 12. Checklist: have you finished the week?

- [ ] I can explain the TSP in one sentence.
- [ ] I can work out $(n-1)!/2$ for a small *n* and explain each part of the formula.
- [ ] I can explain NP, NP-complete and NP-hard without saying "non-polynomial".
- [ ] I can write the first MILP model and explain why it allows subtours.
- [ ] I can write the MTZ constraint, explain both cases ($x_{ij} = 0$ and $1$), and check it on a small tour.
- [ ] I can explain why city 1 is left out of MTZ.
- [ ] I have run the demo notebook and my results match section 7 (80; 407.97; 10 pairs, 373.11; 599.24).
- [ ] I have done tutorial tasks 1(a), 1(b) and 1(c) and compared my numbers with section 8.
- [ ] I have written answers to the three research questions and compared them with the answers notebook.
- [ ] I can explain the difference between an exact method (MILP) and a heuristic (genetic algorithm).

---

## 13. What comes next

**Week 10 (Vehicle Routing Problem)** uses this week's TSP model and MTZ constraints directly: several
vehicles share the cities instead of one salesman. Its notebook (`Week 10 - Vehicle Routing
Problem/2 Lecture Demos/1 TSP and VRP with Pyomo.ipynb`) starts with the TSP of this week in section 1.
Make sure section 5.7 is clear before you start Week 10.

Further, optional: William Cook's TSP pages (https://www.math.uwaterloo.ca/tsp/) and the video on
slide 23.

---

## 14. Assumptions

These points are not stated in the course material; this README assumes them.

- **Time estimates** in section 4 are suggestions, not official figures.
- **Browser times** in sections 2, 7, 8 and 9 come from test runs of the notebooks with the same Python
  engine (Pyodide) the course site uses. Your browser and computer may be faster or slower; the tour
  lengths do not change.
- **Stopping a long run.** The README tells you to use *Kernel → Restart Kernel*. It assumes the
  *Interrupt* (■) button may not stop a running solve on the course site.
- **Week 10 link.** Section 13 assumes Week 10 is taught after this week, as in the module handbook's
  list of weeks.
- **Assessment.** This README does not say whether or how the TSP is assessed. Check the assessment
  briefs and the module handbook.
- **The changed-cost exercise** (task 1(a)) and the **60-city GA run** (task 1(c), step 3) are
  suggestions added in this README; they are not on slide 22. Their answers were checked by running the
  code.

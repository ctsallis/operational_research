# Week 6: Integer Linear Programming – Further Problems

This README is your guide to Week 6 if you are studying on your own. It tells you what to open, in which
order, what each file is for, and what result you should get at every step. It also explains the key
ideas, so you can go through the week with nothing but this page, the slides and the notebooks.

**What you will learn this week**

- The **set covering problem** in general form, and the **costed** version where each set has a price.
- Three ways to write the same Pyomo model: constraints typed by hand, an **incidence matrix**, and
  **sets with dictionaries and rules**.
- Problems on **graphs** (vertices joined by edges): **edge cover**, **vertex cover**, **matching**,
  **perfect matching** and **maximum weight matching**.
- The **balanced assignment problem**: give each worker exactly one job so that the total time is as
  small as possible.
- How to write and solve all of these in Python with **Pyomo** and the **HiGHS** solver.

**What you need from earlier weeks**

- Week 5: binary (0/1) variables, and the set covering model of the fire stations
  ([Week 5 demo 3](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/3%20Fire%20stations%20-%20set%20covering.ipynb)).
- Week 5 demo 8, *Minimum vertex cover*, is a short preview of this week's vertex cover
  ([open it](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/8%20Minimum%20vertex%20cover.ipynb)).
- Weeks 3–4: building a Pyomo model (variables, objective, constraints) and solving it.

If binary variables are new to you, read the Week 5 README first. Every notebook this week uses them.

---

## Contents

1. [How to open the files](#1-how-to-open-the-files)
2. [What is in this folder](#2-what-is-in-this-folder)
3. [Your plan for the week](#3-your-plan-for-the-week)
4. [The key ideas, explained](#4-the-key-ideas-explained)
5. [Lecture: slide-by-slide guide with the demo notebooks](#5-lecture-slide-by-slide-guide-with-the-demo-notebooks)
6. [Tutorial: tasks, hints and how to check your answers](#6-tutorial-tasks-hints-and-how-to-check-your-answers)
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
   `Lectures` → `Semester 1` → `Week 06 - Integer Linear Programming - Further Problems`.
3. Open a sub-folder (for example `2 Lecture Demos`) and double-click a notebook to open it.
4. **Run the first code cell first.** It installs Pyomo and HiGHS into the open browser tab. The first
   time, this takes about a minute.
5. Then choose *Run → Run All Cells* from the menu, or run the cells one by one with **Shift + Enter**
   while you read.

You can also open each notebook directly with the links in [section 5](#5-lecture-slide-by-slide-guide-with-the-demo-notebooks)
and [section 6](#6-tutorial-tasks-hints-and-how-to-check-your-answers).

If this is your first session on the site, open `00_START_HERE.ipynb` (at the top of the file list) and run
all its cells. If every cell prints `OK`, all the course examples will run in your browser.

> **Save your work.** Changes you make to a notebook on the site are kept **only in this browser**.
> Clearing browser data, using a private window or switching computer loses them. Before you leave,
> right-click the notebook in the file list → **Download**.

### Slides and PDFs: download and open them

The website cannot display PowerPoint files. Download the slides and open them in **PowerPoint**. They
contain equations, so open them in PowerPoint to see everything correctly.

- **Lecture slides (start here):** [download `Week 6 - Integer Linear Programming - Further Problems.pptx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/1%20Lecture/Week%206%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems.pptx)
- **Annotated lecture, optional:** [download `Week 6 - Integer Linear Programming - Further Problems (annotated).pdf`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/1%20Lecture/Week%206%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems%20%28annotated%29.pdf)
- **Further reading, optional:** [download `How-Vodafone-Uses-Optimization.pdf`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/6%20Further%20Reading/How-Vodafone-Uses-Optimization.pdf)

Another way to get them: on the course site, right-click the file in the file list → **Download**.

**Slide numbers** in this README are the numbers PowerPoint shows in the slide list on the left. Slide 2
is a hidden, empty slide. PowerPoint skips it in a slide show, but it still counts in the numbering.

**There is no separate tutorial sheet this week.** The tutorial is the last slide of the lecture (slide 28).
[Section 6](#6-tutorial-tasks-hints-and-how-to-check-your-answers) goes through it task by task.

---

## 2. What is in this folder

| Folder | File | What it is | When to use it |
| --- | --- | --- | --- |
| `1 Lecture` | `Week 6 - Integer Linear Programming - Further Problems.pptx` | The lecture slides (28 slides); slide 28 is the tutorial | Read first, alongside the demos |
| | `Week 6 - Integer Linear Programming - Further Problems (annotated).pdf` | The slides as used in an earlier (2023) lecture, with the lecturer's handwritten notes | Optional, after the slides |
| `2 Lecture Demos` | `1 Costed fire stations.ipynb` | Costed set cover, every constraint typed by hand | With slides 7–9 |
| | `2 Costed fire stations - incidence matrix.ipynb` | The same model, constraints built from a 0/1 table | After demo 1 (also answers tutorial task 2) |
| | `3 Costed fire stations - sets and dictionaries.ipynb` | The same model, written with named data and a rule | After demo 2 |
| | `4 Security cameras - vertex cover.ipynb` | Minimum vertex cover: cameras in a school | With slides 15–18 |
| | `5 Balanced assignment.ipynb` | Four workers, four jobs | With slides 23–26 |
| | `6 Balanced assignment - named.ipynb` | The same model with named index sets | After demo 5 |
| | `7 Balanced assignment - sets and dictionaries.ipynb` | The same model with a dictionary and rules | After demo 6 |
| `4 Tutorial Answers` | `Q5 Maximum set cover, edge cover and independent set.ipynb` | Answer to tutorial task 5 | After you have tried task 5 |
| `5 Source Files` | `Python/*.py` (7 scripts) | The original scripts the demo notebooks were made from | Not needed (see below) |
| | `Week 6 - … (annotated).pptx` | An older (2020) version of the slides, with handwriting | Not needed |
| | `Staff Notes/Notes for 2526.txt` | A one-line note for the teaching staff | Not for students |
| `6 Further Reading` | `How-Vodafone-Uses-Optimization.pdf` | A talk by Rolf Bardeli (Vodafone GmbH) on how a telecoms company uses graph models and integer programming | Optional, at the end of the week |

**About the annotated PDF.** Page *N* of the PDF shows slide *N*, but it is an **older version** of the
slides. Some wording and notation differ from the `.pptx`. Where they disagree, the `.pptx` is correct. Two
known slips in the PDF: on page 28 "Maximum Edge Cover" should read **Minimum** Edge Cover, and on page 27
the right-hand graph labels all three students `s1` (they are s1, s2 and s3).

**About `5 Source Files`.** You do not need these files. Every Python script has a notebook version in
`2 Lecture Demos`, and the first cell of each notebook names the script it came from.

- The scripts use the GLPK solver, which you would have to install on your own computer. To run one on
  your computer with HiGHS instead, change `SolverFactory('glpk')` to `SolverFactory('appsi_highs')` and
  install the packages with `pip install pyomo highspy`.
- The notebooks use `SolverFactory('appsi_highs')`. Everything else in the models is the same.

---

## 3. Your plan for the week

Work through these steps in order. Tick them off in [section 10](#10-checklist-have-you-finished-the-week).

| Step | What to do | Material |
| --- | --- | --- |
| 1 | Run `00_START_HERE.ipynb` once to check that the site works in your browser | Course site |
| 2 | Read [section 4](#4-the-key-ideas-explained) of this README for the ideas behind the week | This README |
| 3 | Go through the slides, and run each demo notebook when [section 5](#5-lecture-slide-by-slide-guide-with-the-demo-notebooks) tells you to | `1 Lecture`, `2 Lecture Demos` |
| 4 | Answer each demo's **"What do you notice?"** or **"Try it"** question *before* you open its answer | Last cell of each demo |
| 5 | Do the tutorial on slide 28: tasks 1–5 | Slide 28, [section 6](#6-tutorial-tasks-hints-and-how-to-check-your-answers) |
| 6 | Check task 2 against demo 2 and task 5 against the answer notebook | `2 Lecture Demos`, `4 Tutorial Answers` |
| 7 | Answer the questions in [section 9](#9-check-your-understanding) | This README |
| 8 | *(Optional)* Look through the annotated PDF and the Vodafone talk | `1 Lecture`, `6 Further Reading` |

**Tip for writing your own models.** In the course site's file list, right-click a demo notebook →
**Duplicate**. Rename the copy, then change its data and constraints. Keep the first code cell: it installs
Pyomo and HiGHS.

---

## 4. The key ideas, explained

### 4.1 Words you need this week

| Word | Meaning |
| --- | --- |
| **Graph** $G = (V, E)$ | A set of **vertices** $V$ (dots, also called nodes) and a set of **edges** $E$ (lines), each edge joining two vertices |
| **Endpoint** | One of the two vertices an edge joins. Edge $\lbrace u, v\rbrace$ has endpoints $u$ and $v$ |
| **Bipartite graph** | A graph whose vertices form two groups (for example workers and jobs) where every edge joins one group to the other |
| **Cover** | A choice that "reaches" everything that must be reached: every element, every edge, or every vertex |
| **Incidence matrix** | A table of 0s and 1s: entry (row, column) is 1 if that row's item is touched by that column's item |
| $n!$ ("$n$ factorial") | $n \times (n-1) \times \dots \times 1$. For example $4! = 24$ |

### 4.2 The general set covering problem (slides 4–6)

You have a collection $S$ of **sets**. Together they contain all the **elements** of $U$. Choose as few sets
as possible so that every element is in at least one chosen set. Let $x_t = 1$ if you choose set $t$, and
$0$ if not:

$$\min \sum_{t \in S} x_t \quad \text{s.t.} \quad \sum_{t:\ e \in t} x_t \ge 1 \ \text{ for every element } e \in U, \qquad x_t \in \lbrace 0,1\rbrace$$

Read the constraint as: "for element $e$, add up the $x$ of every set that contains $e$; at least one of
them must be chosen". There is **one constraint per element**, and $N = |S|$ is the number of sets.

**The example on slides 5–6.** $a = \lbrace 1,2,5\rbrace$, $b = \lbrace 2,3\rbrace$, $c = \lbrace 4,5\rbrace$,
$d = \lbrace 3,4\rbrace$, $U = \lbrace 1,2,3,4,5\rbrace$.

| Element | Sets that contain it | Constraint |
| --- | --- | --- |
| 1 | $a$ | $x_a \ge 1$ |
| 2 | $a, b$ | $x_a + x_b \ge 1$ |
| 3 | $b, d$ | $x_b + x_d \ge 1$ |
| 4 | $c, d$ | $x_c + x_d \ge 1$ |
| 5 | $a, c$ | $x_a + x_c \ge 1$ |

Element 1 forces $a$. Set $a$ covers 1, 2 and 5, so 3 and 4 remain, and $d$ covers both. The minimum
set cover is $\lbrace a, d\rbrace$: **2 sets**. One set cannot be enough, because no set contains all five
elements.

### 4.3 Costed set cover: fire stations with running costs (slides 7–9)

Now each set has a **cost** $c_t$, and you minimise the total cost instead of the number of sets:

$$\min \sum_{t \in S} c_t x_t \quad \text{s.t.} \quad \sum_{t:\ e \in s_t} x_t \ge 1 \ \text{ for every city } e \in U, \qquad x_t \in \lbrace 0,1\rbrace$$

Here the "sets" are four possible fire stations $a, b, c, d$, and the elements are five cities 0–4.
$s_t$ is the set of cities that station $t$ covers:

| Station $t$ | Covers cities $s_t$ | Running cost $c_t$ |
| --- | --- | --- |
| $a$ | 0, 2 | 12 |
| $b$ | 1, 2, 3 | 7 |
| $c$ | 1, 4 | 10 |
| $d$ | 4 | 5 |

The constraints, one per city (slide 8): city 0: $x_a \ge 1$; city 1: $x_b + x_c \ge 1$; city 2:
$x_a + x_b \ge 1$; city 3: $x_b \ge 1$; city 4: $x_c + x_d \ge 1$.

**Optimal answer (slide 9): stations $a$, $b$ and $d$, cost $12 + 7 + 5 = 24$.** You can see why: cities 0
and 3 each have only one station that covers them, so $a$ and $b$ must be run. They cover cities 0–3. City 4
needs $c$ (cost 10) or $d$ (cost 5), and $d$ is cheaper.

> **How to build a covering constraint:** pick one element (city), list every set (station) that contains
> it, and add up their $x$. Write "$\ge 1$". Repeat for every element.

### 4.4 Three ways to write the same model (demos 1–3)

Demos 1, 2 and 3 solve **the same problem** and get **the same answer** (cost 24). Only the code style changes.

| Demo | Style | How the constraints are made | Good for |
| --- | --- | --- | --- |
| 1 | Typed by hand | One line of code per city: `model.city0 = Constraint(expr=model.x[0] >= 1)` | Small problems; easy to compare with the slides |
| 2 | Incidence matrix | A 0/1 table `A` with one **row per city** and one **column per station**; a loop builds one constraint per row | Data that arrives as a table |
| 3 | Sets and dictionaries | Named stations `'A'`…`'D'`, a dictionary `covers` of the cities each one covers, and a **rule** that Pyomo calls once per city | Larger problems; the data can change without touching the model |

The incidence matrix of demo 2, with rows = cities 0–4 and columns = stations $a, b, c, d$:

| | $a$ | $b$ | $c$ | $d$ |
| --- | --- | --- | --- | --- |
| city 0 | 1 | 0 | 0 | 0 |
| city 1 | 0 | 1 | 1 | 0 |
| city 2 | 1 | 1 | 0 | 0 |
| city 3 | 0 | 1 | 0 | 0 |
| city 4 | 0 | 0 | 1 | 1 |

Row $e$ gives the constraint $\sum_t A_{et}\, x_t \ge 1$. The 0 entries add nothing, so each row gives
exactly the constraint you would type by hand.

### 4.5 Edge cover (slides 10–11)

An **edge cover** is a set of **edges** that touches **every vertex**: each vertex is an endpoint of at least
one chosen edge (slide 10). A **minimum edge cover** uses as few edges as possible (slide 11). In slide 11's
right-hand graph, 3 edges are enough for its 6 vertices. Each edge touches only 2 vertices, so a graph
with $n$ vertices needs at least $n/2$ edges in any edge cover.

The slides do not write a model for edge cover. Writing it is part of tutorial task 5 (section 6).

### 4.6 Vertex cover and the security cameras (slides 12–18)

A **vertex cover** is a set of **vertices** that includes at least one endpoint of **every edge** (slide 13).
A **minimum vertex cover** uses as few vertices as possible. With $x_u = 1$ if vertex $u$ is chosen:

$$\min \sum_{u \in V} x_u \quad \text{s.t.} \quad x_u + x_v \ge 1 \ \text{ for every edge } \lbrace u, v\rbrace \in E, \qquad x_u \in \lbrace 0,1\rbrace$$

There is **one constraint per edge**: "at least one end of this edge is chosen". Compare it with set covering:
each vertex "covers" the edges that touch it, and every edge must be covered.

**Security cameras (slides 15–18).** A school has 8 corridor corners (vertices 1–8) and 10 corridors (edges):
1–2, 1–8, 2–3, 2–5, 3–4, 4–5, 5–6, 5–8, 6–7 and 7–8. A camera at a corner watches every corridor that ends
there. Watch every corridor with as few cameras as possible.

- Slide 16 shows the graph and the 10 constraints, $x_1 + x_2 \ge 1$, …, $x_7 + x_8 \ge 1$.
- **The minimum is 4 cameras.** There are two optimal answers: corners **2, 4, 6, 8** (slide 17, "Solver
  Solution") and corners **1, 3, 5, 7** (slide 18, "Another possibility").
- Why 3 cameras cannot be enough: corridors 1–2, 3–4, 5–6 and 7–8 share no corner, so no single camera
  watches two of them. Each needs its own camera.

Slides 14 and 16 show a picture with "Node variables $x_u$" (one variable per vertex) and "Edge variables
$x_{uv}$" (one variable per edge). Vertex cover uses node variables; matching (next section) uses edge
variables. The same pictures appear in the Vodafone talk in `6 Further Reading`.

### 4.7 Matchings (slides 19–22)

- A **matching** is a set of edges with **no vertex in common** (slide 20).
- A **maximum matching** is a matching with as many edges as possible (slide 20).
- A **perfect matching** is a matching that touches **every vertex** (slide 21). It can exist only if the
  number of vertices is even.
- A **maximum weight matching** gives each edge a weight $w_{uv}$ and chooses a matching with the largest
  total weight (slide 22). With $x_{uv} = 1$ if edge $\lbrace u, v\rbrace$ is chosen:

$$\max \sum_{\lbrace u,v\rbrace \in E} w_{uv}\, x_{uv} \quad \text{s.t.} \quad \sum_{v:\ \lbrace u,v\rbrace \in E} x_{uv} \le 1 \ \text{ for every vertex } u \in V, \qquad x_{uv} \in \lbrace 0,1\rbrace$$

The constraint says "at most one chosen edge at each vertex": exactly the rule "no vertex in common".

### 4.8 The balanced assignment problem (slides 23–27)

Four workers must do four jobs, **one job each**, and each job needs **exactly one** worker. The table gives
the time worker $u$ needs for job $v$:

| | Job 1 | Job 2 | Job 3 | Job 4 |
| --- | --- | --- | --- | --- |
| Worker 1 | 9 | 2 | 7 | 8 |
| Worker 2 | 6 | 4 | 3 | 7 |
| Worker 3 | 5 | 8 | 1 | 8 |
| Worker 4 | 7 | 6 | 9 | 4 |

As a graph (slide 23), workers and jobs are the two groups of a **bipartite graph**, and a full assignment is
a **perfect matching** in it. In the table, it is **one cell in every row and every column** (slide 25).
There are $4! = 24$ possible assignments; with $n$ workers there are $n!$.

With $x_{uv} = 1$ if worker $u$ does job $v$, and $c_{uv}$ the time (slide 25):

$$\min \sum_{u \in W} \sum_{v \in J} c_{uv} x_{uv} \quad \text{s.t.} \quad \sum_{v \in J} x_{uv} = 1 \ \ \forall u \in W, \qquad \sum_{u \in W} x_{uv} = 1 \ \ \forall v \in J, \qquad x_{uv} \in \lbrace 0,1\rbrace$$

The first group of constraints is "each worker does exactly one job" (one per **row**). The second is "each
job gets exactly one worker" (one per **column**). Note the "$= 1$", not "$\ge 1$" or "$\le 1$".

- **Slide 24:** one possible assignment, worker 1 → job 2, 2 → 4, 3 → 1, 4 → 3, takes $2 + 7 + 5 + 9 = 23$.
- **Slide 26:** the optimal assignment, worker 1 → job 2, 2 → 1, 3 → 3, 4 → 4, takes
  $2 + 6 + 1 + 4 = \mathbf{13}$. It is the only assignment with total 13.
- **Slide 27:** the same idea with 3 students and 3 dissertation projects. The left graph shows every
  possible student–project pair. The right graph highlights one assignment: s1 → p2, s2 → p1, s3 → p3.
  The slide gives no costs, so this is an example of a valid assignment, not an optimum.

### 4.9 Python counts from 0, and the demos number things differently

The slides, the tables above and the demos do not all number things the same way. Always check the
numbering before you compare results:

| Demo | In the code | On the slides |
| --- | --- | --- |
| 1, 2 | `x[0]`, `x[1]`, `x[2]`, `x[3]` | stations $a$, $b$, $c$, $d$ |
| 3 | `x['A']` … `x['D']`; cities **1–5** | stations $a$–$d$; cities **0–4** (city 1 in the code = city 0 on the slides) |
| 4 | `x[0]` … `x[7]` | corners 1–8 (`x[1]` = corner 2) |
| 5, 6 | `x[0,1]` | worker 1, job 2 |
| 7 | `x[1,2]` | worker 1, job 2 (numbered from 1, like the table) |

---

## 5. Lecture: slide-by-slide guide with the demo notebooks

Read the slides in order. When you reach a demo, open the notebook, read its first cell, run it, and
compare your output with the **expected result** below. Each notebook ends with a question. Answer it
yourself before you click **Answer** to reveal the solution.

| Slides | Topic | Run this demo | Expected result |
| --- | --- | --- | --- |
| 1 | Title | – | – |
| 3–6 | Minimum set cover: the general model and a small example | – | 2 sets: $\lbrace a, d\rbrace$ (section 4.2) |
| 7–9 | Costed set cover: fire stations | [`1 Costed fire stations`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/1%20Costed%20fire%20stations.ipynb) | Cost **24**: stations $a$, $b$, $d$ (`x[0]`, `x[1]`, `x[3]` = 1) |
| 7–9 | The same, with an incidence matrix | [`2 Costed fire stations - incidence matrix`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/2%20Costed%20fire%20stations%20-%20incidence%20matrix.ipynb) | Cost **24**: `x[0]`, `x[1]`, `x[3]` = 1 |
| 7–9 | The same, with sets and dictionaries | [`3 Costed fire stations - sets and dictionaries`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/3%20Costed%20fire%20stations%20-%20sets%20and%20dictionaries.ipynb) | Cost **24**: `x[A]`, `x[B]`, `x[D]` = 1 |
| 10–11 | Edge cover, minimum edge cover | – (tutorial task 5) | – |
| 12–14 | Vertex cover: definition and model | – | – |
| 15–18 | Security cameras | [`4 Security cameras - vertex cover`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/4%20Security%20cameras%20-%20vertex%20cover.ipynb) | **4 cameras**: corners 2, 4, 6, 8 (`x[1]`, `x[3]`, `x[5]`, `x[7]` = 1) |
| 19–22 | Matching, perfect matching, maximum weight matching | – | – |
| 23–26 | Balanced assignment: 4 workers, 4 jobs | [`5 Balanced assignment`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/5%20Balanced%20assignment.ipynb) | Total time **13**: `x[0,1]`, `x[1,0]`, `x[2,2]`, `x[3,3]` = 1 |
| 23–26 | The same, with named index sets | [`6 Balanced assignment - named`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/6%20Balanced%20assignment%20-%20named.ipynb) | Total time **13**: same variables as demo 5 |
| 23–26 | The same, with sets and dictionaries | [`7 Balanced assignment - sets and dictionaries`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/7%20Balanced%20assignment%20-%20sets%20and%20dictionaries.ipynb) | Total time **13**: `x[1,2]`, `x[2,1]`, `x[3,3]`, `x[4,4]` = 1 |
| 27 | Assignment of 3 students to 3 projects | – | – |
| 28 | **Tutorial** | see [section 6](#6-tutorial-tasks-hints-and-how-to-check-your-answers) | – |

**Things to notice as you go**

- **Demos 1 → 2 → 3:** the printed model (`model.pprint()`) has the same five constraints each time; only
  their names change. Compare them with slide 8.
- **Demo 4:** the slides call 2, 4, 6, 8 the "Solver Solution". If your output shows 1, 3, 5, 7 instead, it
  is equally correct: both use 4 cameras. (The original script in `5 Source Files`, run with GLPK, gives
  1, 3, 5, 7.)
- **Demo 4's matrix `A`** has a 1 only above the diagonal (row $i$, column $j$ with $i < j$), so each corridor
  appears once and gives one constraint. Count the 1s: there are ten, one per corridor.
- **Demo 5's "Try it"** shows something special about the assignment problem: even if the variables may take
  fractional values, the best answer is still whole-numbered (0s and 1s).
- **Demos 5 → 6 → 7:** only names and numbering change; the answer is 13 every time.

---

## 6. Tutorial: tasks, hints and how to check your answers

The tutorial is **slide 28**. It has five numbered tasks. Task 5 asks you to code three problems that
are named under it: *Maximum Set Cover*, *Minimum Edge Cover* and *Maximum Independent Set*.

| Task | What it asks | Answer provided? |
| --- | --- | --- |
| 1 | Study the models and understand the Python code | Self-check: the questions at the end of each demo, and [section 9](#9-check-your-understanding) |
| 2 | Code the costed fire stations in Pyomo using an incidence matrix | Yes: demo 2 |
| 3 | Look at the Gurobi modelling examples | No (reading task) |
| 4 | Pick one Gurobi example and code it in Pyomo | No (your own choice); see how to check it below |
| 5 | Code maximum set cover, minimum edge cover and maximum independent set | Yes: `4 Tutorial Answers/Q5 …` |

### Task 1. Study the models and the code

For each demo, make sure you can say, without looking: what the variables mean, what the objective is, and
what **one** constraint means in words. Then answer the demo's last question before you open its answer.

### Task 2. Costed fire stations with an incidence matrix

- **Start from:** a copy of `1 Costed fire stations`.
- **Hint:** make a list of lists `A` with **one row per city** (5 rows) and **one column per station**
  (4 columns). Put a 1 where the station covers the city. Then replace the five hand-typed constraints with a
  loop over the rows: for each city, $\sum_{\text{station}} A[\text{city}][\text{station}] \cdot x[\text{station}] \ge 1$.
  Use a `ConstraintList` to collect them.
- **Check:** your answer must be cost **24**, stations $a$, $b$, $d$.

<details><summary>Check task 2: the answer</summary>

The answer is demo 2,
[`2 Costed fire stations - incidence matrix`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/2%20Lecture%20Demos/2%20Costed%20fire%20stations%20-%20incidence%20matrix.ipynb).
Its matrix is the table in section 4.4. Compare your `model.pprint()` with demo 2's: the five constraints must
be the same.
</details>

### Tasks 3 and 4. The Gurobi examples

Open the Gurobi page on slide 28:
<https://www.gurobi.com/resource/modeling-examples-using-the-gurobi-python-api-in-jupyter-notebook/>.
It lists optimisation examples as Jupyter notebooks, grouped by level (introductory, beginner, intermediate,
advanced).

- **Task 3:** read a few. For each, find the decision variables, the objective and the constraints.
- **Task 4:** pick an **introductory or beginner** example whose data is written in the notebook itself, and
  rewrite it in Pyomo in a copy of one of this week's demos.

The Gurobi examples use Gurobi's own Python package, `gurobipy`. It does **not** run on the course site, so
read the Gurobi notebook and translate it:

| Gurobi (`gurobipy`) | Pyomo |
| --- | --- |
| `m = gp.Model()` | `model = ConcreteModel()` |
| `x = m.addVars(I, vtype=GRB.BINARY)` | `model.x = Var(I, within=Binary)` |
| `x = m.addVars(I)` (continuous, $\ge 0$) | `model.x = Var(I, within=NonNegativeReals)` |
| `m.addConstr(expression)` | `model.c1 = Constraint(expr=expression)` |
| `m.addConstrs(expression for i in I)` | `model.c = Constraint(I, rule=...)` (as in demos 3 and 7) |
| `gp.quicksum(...)` | `sum(...)` |
| `m.setObjective(expression, GRB.MAXIMIZE)` | `model.obj = Objective(expr=expression, sense=maximize)` |
| `m.optimize()` | `SolverFactory('appsi_highs').solve(model)` |
| `x[i].X` (value after solving) | `value(model.x[i])` |

**How to check task 4 on your own:** the Gurobi notebook shows its optimal objective value. Your Pyomo model
must give the **same objective value**. The chosen variables may differ if the problem has several optimal
answers (see [section 7](#7-how-to-read-the-pyomo-and-highs-output)).

### Task 5. Maximum set cover, minimum edge cover, maximum independent set

The slide only names the three problems; you choose the data. The answer notebook uses this week's two
examples, so try them on the same data:

- **(a) Maximum set cover** on the fire stations (section 4.3): open **at most $k = 2$** stations (ignore the
  costs) and cover **as many cities as possible**.
- **(b) Minimum edge cover** on the security-camera graph (section 4.6): choose as few **corridors** as
  possible so that every **corner** touches a chosen corridor.
- **(c) Maximum independent set** on the same graph: choose as many **corners** as possible so that **no
  two chosen corners are joined by a corridor**.

**Hints**

- **(a)** You need two kinds of binary variable: $x_t$ (station $t$ is opened) and $y_e$ (city $e$ counts as
  covered). Maximise $\sum_e y_e$. A city may count only if an opened station covers it, so link $y_e$ to the
  stations that cover city $e$. Add one constraint that limits the number of opened stations to $k$.
- **(b)** Here the variables are on the **edges**, one per corridor, and there is one constraint per
  **vertex**. It is vertex cover with the roles of vertices and edges swapped.
- **(c)** Start from demo 4. Change the objective direction and change "$\ge 1$" to "$\le 1$". Think about
  what "$x_u + x_v \le 1$" means for the two ends of a corridor.
- **Expected values:** (a) 4 cities; (b) 4 corridors; (c) 4 corners. Each part has several optimal choices.

<details><summary>Check task 5: formulations and results</summary>

- **(a) Maximum set cover.** $\max \sum_{e \in U} y_e$ s.t. $y_e \le \sum_{t:\ e \in s_t} x_t$ for every city
  $e$, $\sum_{t \in S} x_t \le k$, all variables binary. Result **4 of the 5 cities**. No two stations cover
  all five: city 0 needs $a$ and city 3 needs $b$, and $a$ + $b$ miss city 4. The pairs $a$ + $b$, $a$ + $c$,
  $b$ + $c$ and $b$ + $d$ all reach 4. The notebook prints $a$ + $c$ (cities 0, 1, 2, 4).
- **(b) Minimum edge cover.** With $z_{uv} = 1$ if corridor $\lbrace u, v\rbrace$ is chosen:
  $\min \sum_{\lbrace u,v\rbrace \in E} z_{uv}$ s.t. $\sum_{\text{edges at } w} z_{uv} \ge 1$ for every
  vertex $w$, $z_{uv} \in \lbrace 0,1\rbrace$. Result **4 corridors**: each corridor touches 2 of the 8
  corners, so at least 4 are needed. The notebook prints 1–8, 2–3, 4–5, 6–7; 1–2, 3–4, 5–6, 7–8 also works.
  Four corridors that touch all 8 corners share no corner, so they are also a **perfect matching**.
- **(c) Maximum independent set.** $\max \sum_{u \in V} x_u$ s.t. $x_u + x_v \le 1$ for every edge
  $\lbrace u, v\rbrace$, $x_u \in \lbrace 0,1\rbrace$. Result **4 corners**: 1, 3, 5, 7 (what the notebook
  prints) or 2, 4, 6, 8.

The answer notebook ends with a "What do you notice?" question that links (c) with the vertex cover of demo 4.

Notebook: [`Q5 Maximum set cover, edge cover and independent set`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/4%20Tutorial%20Answers/Q5%20Maximum%20set%20cover%2C%20edge%20cover%20and%20independent%20set.ipynb).
</details>

---

## 7. How to read the Pyomo and HiGHS output

Each demo prints three things:

1. **`model.pprint()`**, the model with your data filled in. Check every constraint against your formulation.
   This is the best place to catch typing mistakes.
2. **The HiGHS log.** In the browser, HiGHS prints its progress even when the code says `tee=False`. You
   can skip most of it. Look for the **Solving report** near the end: `Status Optimal` means the solver
   proved it found the best answer.
3. **`model.display()`**, the results:
   - under **Variables**, the `Value` column gives each variable's value. A variable with two indices is
     shown as `(0, 1)`, which is `x[0,1]`;
   - under **Objectives**, `Value` is the optimal objective;
   - under **Constraints**, `Body` is the left-hand side at the optimum, shown next to its `Lower` and/or
     `Upper` limit.

The answer notebook for task 5 does not use `display()`. It prints short summaries such as
`Cities covered: 4.0` instead.

**Small number effects.** A value printed as `-0.0` is zero. A value such as `0.9999999` or `1e-10` is the
solver's rounding: read it as 1 or 0.

**Different but equal answers.** If your objective value matches the expected one but the chosen items
differ, check that your choice satisfies every constraint. If it does, it is also optimal. This happens in
demo 4 and in all three parts of task 5. It does **not** happen in demos 1–3 or 5–7: their optimal answers
are unique.

---

## 8. If something goes wrong

| Problem | What to do |
| --- | --- |
| `ModuleNotFoundError: No module named 'pyomo'` | Run the **first code cell** of the notebook again. The install lasts only for the open tab. |
| Nothing happens for a long time when you first run a cell | The first run downloads Python and the packages. Wait about a minute. If nothing has changed after that, reload the page and run the first cell again. |
| `NameError: name 'model' is not defined` (or similar) | You skipped a cell. Use *Run → Run All Cells*. |
| `ApplicationError: No executable found for solver 'glpk'` | Use `SolverFactory('appsi_highs')`. GLPK and CBC do not run in the browser. |
| `ModuleNotFoundError: No module named 'gurobipy'` | Gurobi does not run on the course site. Translate the model to Pyomo (task 4 in section 6). |
| A constraint error after you change the data, e.g. `KeyError` | A name or number in your data does not match the index set. Check that every key in your dictionaries (for example `'E'` or `(5, 5)`) is also in the list of stations, cities, workers or jobs. |
| The objective matches but the items differ from the expected result | See "Different but equal answers" in [section 7](#7-how-to-read-the-pyomo-and-highs-output). |
| Your own model gives a different objective | Compare `model.pprint()` with your paper formulation line by line. Check the direction of each constraint (`>=`, `<=` or `==`), the objective sense (`minimize` or `maximize`), and the numbering (section 4.9). |
| `RuntimeError: A feasible solution was not found, so no solution can be loaded` | The model has no optimal solution. Scroll up to the HiGHS log and read its status. **Infeasible**: your constraints cannot all hold at once; for example, `== 1` constraints with more workers than jobs. **Unbounded**: something can grow without limit, so a limit constraint is probably missing. |
| Your edits disappeared | Edits are kept only in the browser you used. Next time, download the notebook before you leave (section 1). |
| The `.pptx` does not open on the site | Download it and open it in PowerPoint (section 1). |
| The site will not load at all | Try another browser (Chrome, Edge or Firefox). The notebooks also run in Google Colab or Anaconda Jupyter: the first cell installs the packages there too. |

---

## 9. Check your understanding

Try to answer each question in a sentence or two before you open the answer.

<details><summary>1. In the costed fire-station example, which stations must be run whatever the costs are, and why?</summary>

Stations $a$ and $b$. City 0 is covered only by $a$ ($x_a \ge 1$) and city 3 only by $b$ ($x_b \ge 1$). The
solver's only real choice is how to cover city 4: $c$ (10) or $d$ (5).
</details>

<details><summary>2. Write the column for station b in the incidence matrix of demo 2. What does it tell you?</summary>

Reading cities 0 to 4 from top to bottom: 0, 1, 1, 1, 0. Station $b$ covers cities 1, 2 and 3, which is
$s_b = \lbrace 1,2,3\rbrace$. A **row** lists the stations that cover one city (one constraint); a **column**
lists the cities one station covers.
</details>

<details><summary>3. What is the difference between a vertex cover and an edge cover?</summary>

A vertex cover chooses **vertices** so that every **edge** has a chosen endpoint (one constraint per edge). An
edge cover chooses **edges** so that every **vertex** is an endpoint of a chosen edge (one constraint per
vertex).
</details>

<details><summary>4. Why do the security cameras need at least 4 cameras?</summary>

Corridors 1–2, 3–4, 5–6 and 7–8 share no corner, so a camera can watch at most one of them. Each of the four
needs its own camera. A set of edges with no common vertex is a matching, and every vertex cover needs at least
as many vertices as any matching has edges.
</details>

<details><summary>5. Why are the assignment constraints "= 1" and not "≥ 1"?</summary>

"Balanced" means every worker does **exactly one** job and every job gets **exactly one** worker. With
"$\ge 1$", a worker could take two jobs or a job could get two workers. With "$\le 1$" only, the cheapest choice
would be to assign nobody, at total time 0.
</details>

<details><summary>6. How many possible assignments are there with 5 workers and 5 jobs? With 10?</summary>

$5! = 120$ and $10! = 3\,628\,800$. Checking them one by one quickly becomes impossible, which is why we let
an integer programming solver search instead.
</details>

<details><summary>7. In the slides' example, why is the assignment on slide 24 (total 23) not optimal?</summary>

It is a valid perfect matching (one cell per row and column), but the solver found one with total 13
(slide 26). Valid is not the same as optimal.
</details>

<details><summary>8. Demo 4 needs 4 cameras out of 8 corners, and task 5(c) finds 4 corners with no corridor between them. Is that a coincidence?</summary>

No. A set of vertices is independent exactly when the **other** vertices form a vertex cover: an edge with no
end in the cover would have both ends in the independent set. So the largest independent set plus the smallest
vertex cover equals the number of vertices: $4 + 4 = 8$.
</details>

---

## 10. Checklist: have you finished the week?

- [ ] I ran `00_START_HERE.ipynb` and every cell printed `OK`.
- [ ] I read all the slides (1–28) and ran demos 1–7; my results match the table in section 5.
- [ ] I answered the "What do you notice?" / "Try it" question at the end of each demo before I looked
      at its answer.
- [ ] I can write the set covering, costed set covering, vertex cover and assignment models on paper.
- [ ] Task 2: I wrote the costed fire stations with an incidence matrix and got cost 24.
- [ ] Tasks 3–4: I read some Gurobi examples and rewrote one in Pyomo with the same objective value.
- [ ] Task 5: I coded maximum set cover, minimum edge cover and maximum independent set, and got 4, 4 and 4.
- [ ] I answered the questions in section 9.
- [ ] I downloaded any notebooks I changed and want to keep.

**Next week (Week 7)** is *Flow Shop and Job Shop Scheduling*.

---

## 11. Assumptions

These points are not stated in the course material for this week. This README assumes them:

1. **Order of work:** the slides and demos come before the tutorial, and the tutorial comes before the
   answers. The answers are already in this folder, so a student working alone is trusted to attempt each
   task first.
2. **Task 5's data:** slide 28 only names the three problems. This README uses the same data as the answer
   notebook (the fire stations with $k = 2$, and the security-camera graph). Other data is also acceptable.
3. **Tasks 3 and 4 have no answer.** The README suggests checking task 4 by matching the Gurobi notebook's
   objective value; the course material does not say how it is marked or checked.
4. **The Gurobi page** and the layout described in section 6 are as they were when this README was written.
5. **The annotated PDF and the Vodafone talk are optional.** Nothing in the week depends on them. The years
   given for the two annotated versions (2023 for the PDF, 2020 for the `.pptx` in `5 Source Files`) come
   from the files' saved dates, not from a statement in the material.
6. **Slide numbers** count every slide in the `.pptx`, including the hidden empty slide 2.
7. **No time estimates or deadlines** are given, because the course material does not state them.
8. **Next week's topic** (end of section 10) is taken from the Week 7 folder name, not from a timetable.
9. **The download links** in section 1 point to the files on the repository's `main` branch.

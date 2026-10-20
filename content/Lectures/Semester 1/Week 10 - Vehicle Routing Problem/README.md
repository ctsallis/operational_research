# Week 10 – Vehicle Routing Problem

This README guides you through Week 10 on your own, from start to finish. It covers what to open, in what order, what you should see, and how to check that you have understood. Each step tells you what to look at and what to do. The answers to every question are on this page, hidden under **▸ Answer** until you click.

---

## Contents

1. [What this week is about](#1-what-this-week-is-about)
2. [Before you start](#2-before-you-start)
3. [What is in this folder](#3-what-is-in-this-folder)
4. [How to open each file](#4-how-to-open-each-file)
5. [Study plan, step by step](#5-study-plan-step-by-step)
6. [The key ideas in one place](#6-the-key-ideas-in-one-place)
7. [The demo notebook: what it does and what you should see](#7-the-demo-notebook-what-it-does-and-what-you-should-see)
8. [Practice exercises (with answers)](#8-practice-exercises-with-answers)
9. [Self-test](#9-self-test)
10. [Troubleshooting](#10-troubleshooting)
11. [Glossary](#11-glossary)
12. [Checklist: have you finished the week?](#12-checklist-have-you-finished-the-week)
13. [Assumptions made in this README](#13-assumptions-made-in-this-readme)

---

## 1. What this week is about

A delivery company has one **depot** and several **customers**. Each customer needs some amount of goods (its **demand**). The company has a few **vehicles**, and each can carry at most a fixed amount (its **capacity**). The **Vehicle Routing Problem (VRP)** asks: which customers should each vehicle visit, and in what order?

The week builds the VRP step by step from last week's Travelling Salesman Problem (TSP):

1. **TSP with the MTZ constraint.** One vehicle visits every city once. The Miller–Tucker–Zemlin (MTZ) constraint stops the model from returning several small separate loops (**subtours**) instead of one tour.
2. **Several tours from the depot.** Relax the constraints at city 1 (the depot) so that $m$ tours can start and end there.
3. **VRP, minimise total distance.** Add demands and a vehicle capacity using a **flow** variable (the load on the vehicle). With positive demands, the flow also removes subtours.
4. **VRP, minimise the longest route.** Give every vehicle its own copy of the network and minimise the length $C_{Max}$ of the longest route. This is a **minimax** model: all deliveries finish as early as possible.
5. **Heuristics.** TSP and VRP are NP-hard, so large instances are solved approximately, for example with the nearest-neighbour rule.

**By the end of the week you should be able to:**

- explain why the "one arc in, one arc out" constraints alone allow subtours;
- write the MTZ constraint, and explain why city 1 is excluded from it and why $M = n-1$ is big enough;
- change a TSP model so that $m$ tours leave the depot;
- write the VRP model with demand, capacity and flow, and explain why it needs no MTZ constraint when all demands are positive;
- write the minimax VRP model with one set of variables per vehicle, and explain each constraint;
- build and solve these models in Pyomo with the HiGHS solver, and read the results;
- describe the nearest-neighbour heuristic and its main weakness.

---

## 2. Before you start

**You need:**

- a web browser (to read the notes and run the notebook on the course site; nothing needs installing);
- Microsoft PowerPoint (to view the lecture slides, a `.pptx` file);
- about the Week 09 material: what a TSP tour is and what the binary variable $x_{ij}$ means. Slides 3–5 of this week's deck recap it, so you can manage without Week 09, but it helps.

**Notation used all week**

| Symbol | Meaning |
|---|---|
| $V$ | set of locations; **city 1 is the depot** |
| $n$ | number of locations (the size of $V$) |
| $V \setminus \{1\}$ | all locations except the depot, i.e. $\{2, \dots, n\}$ |
| $c_{ij}$ | distance (cost) from $i$ to $j$ |
| $x_{ij} \in \{0,1\}$ | 1 if a vehicle drives directly from $i$ to $j$ |
| $u_i$ | a number that orders the cities along a tour (MTZ variable) |
| $m$ | number of vehicles (number of routes that may leave the depot) |
| $q_i$ | demand of customer $i$ |
| $Q$ | capacity of each vehicle |
| $f_{ij}$ | flow: the load on the vehicle as it drives from $i$ to $j$ ("what is in the van at that point") |
| $K$ | set of vehicles, $k \in K$ (minimax model) |
| $x_{ijk}$, $f_{ijk}$ | the same as $x_{ij}$, $f_{ij}$, but for vehicle $k$ |
| $C_{Max}$ | length of the longest route (minimax model) |

---

## 3. What is in this folder

| Folder / file | What it is | Do you need it? |
|---|---|---|
| [`1 Lecture/Vehicle Routing Problem.pptx`](1%20Lecture/Vehicle%20Routing%20Problem.pptx) | The lecture slides (36 slides) | **Yes**: main material |
| [`1 Lecture/Notes/Routing Problems - Lecture Notes.md`](1%20Lecture/Notes/Routing%20Problems%20-%20Lecture%20Notes.md) | Written lecture notes: the same models with full explanations, Pyomo code and pictures | **Yes**: read alongside the slides |
| `1 Lecture/Notes/assets/` | The 11 pictures used by the notes | Opened automatically by the notes |
| [`2 Lecture Demos/1 TSP and VRP with Pyomo.ipynb`](2%20Lecture%20Demos/1%20TSP%20and%20VRP%20with%20Pyomo.ipynb) | Demo notebook: solves the TSP and both VRP models on one small example and draws the routes | **Yes**: run it |
| `5 Source Files/` | Staff material: HTML exports of the notes, an earlier draft of the notes, staff notes on slides 27 and 33 | **No**: everything you need is in the files above |
| [`6 Further Reading/Miller, Tucker and Zemlin (1960) - Integer Programming Formulation of TSP.pdf`](6%20Further%20Reading/Miller%2C%20Tucker%20and%20Zemlin%20%281960%29%20-%20Integer%20Programming%20Formulation%20of%20TSP.pdf) | The original 4-page paper that introduced the MTZ constraint | Optional |
| [`6 Further Reading/Christofides (1976) - The Vehicle Routing Problem.pdf`](6%20Further%20Reading/Christofides%20%281976%29%20-%20The%20Vehicle%20Routing%20Problem.pdf) | A 16-page survey of exact and heuristic methods for the VRP | Optional |

There is **no separate tutorial sheet** this week. The practice is the "What do you notice?" and "Try it" sections at the end of the demo notebook, plus [Section 8](#8-practice-exercises-with-answers) and [Section 9](#9-self-test) of this README.

---

## 4. How to open each file

### The course site

The course runs in your browser at **https://ctsallis.github.io/operational_research/**. In the file browser on the left, open `Lectures` → `Semester 1` → `Week 10 - Vehicle Routing Problem`.

The demo notebook also opens directly from this link (the last slide of the deck has the same link):
<https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2010%20-%20Vehicle%20Routing%20Problem/2%20Lecture%20Demos/1%20TSP%20and%20VRP%20with%20Pyomo.ipynb>

### The slides (`.pptx`)

The browser cannot show PowerPoint files, so download the deck and open it in PowerPoint:

- **On the course site:** right-click `Vehicle Routing Problem.pptx` in `1 Lecture` → **Download**.
- **Or on GitHub:** open the file and use the download button.

Slide numbers in this README are the numbers PowerPoint shows.

### The lecture notes (`.md`)

On the course site, **right-click** `Routing Problems - Lecture Notes.md` → **Open With** → **Markdown Preview**. This shows the formatted text, the equations and the pictures. A plain double-click opens the raw text with the LaTeX code instead, which is hard to read.

### The demo notebook (`.ipynb`)

Double-click it on the course site. It runs entirely in your browser. To run a cell, click it and press **Shift + Enter**. Section 7 explains what each part does and what you should see.

**Tip:** to experiment without losing the original, right-click the notebook → **Duplicate** and work on the copy.

### The further-reading PDFs

Double-click to view in the browser, or download them.

---

## 5. Study plan, step by step

Work through the steps in order. Each step lists **what to open**, **what to look for**, and a **checkpoint** question. If you can't answer a checkpoint, re-read that part before moving on. Every checkpoint has a hidden answer.

### Step 1: Recap the TSP and see the problem of subtours (slides 1–5)

- **Slide 2** (*Disclaimer/Invite*): the models this week are MILPs (mixed-integer linear programmes) that a solver handles when they are small; real companies use heuristics and their own software. The lecturer invites anyone interested in researching this area to get in touch.
- **Slides 3–4**: the TSP with only two kinds of constraint. Each city is left exactly once ($\sum_j x_{ij} = 1$) and entered exactly once ($\sum_j x_{ji} = 1$).
- **Slide 5**: two pictures. Both a single tour (red) and several small loops (blue) obey these constraints.

> **Checkpoint 1.** Why do "one arc in and one arc out of every city" not guarantee a single tour?
>
> <details><summary>▸ Answer</summary>
>
> A set of separate small loops (subtours) also gives every city exactly one arc in and one arc out. Nothing in those constraints says that the loops must be joined into one. Because a set of short loops is usually cheaper than one long tour, the solver will often return subtours.
> </details>

### Step 2: The MTZ constraint (slides 6–13; notes "Explaining the MTZ Subtour Constraint")

- **Slides 6–8.** Each city $i$ gets a number $u_i$ that orders the cities along the tour (only the order matters, not the values). If the tour goes from $i$ straight to $j$ ($x_{ij}=1$), we want $u_j \ge u_i + 1$. Written with a "big $M$":
  $$u_i - u_j + 1 \le M(1 - x_{ij})$$
  - If $x_{ij}=1$, the right side is 0, which gives $u_j \ge u_i + 1$.
  - If $x_{ij}=0$, the right side is $M$, which is large enough that the constraint does nothing.
- **Slides 9–10.** Why city 1 is left out. Along a tour, the $u$ values must keep increasing. A tour has to come back to its start, and that would need the start's $u$ to be bigger than itself, which is impossible. So the constraint is written only for $i, j \ne 1$. City 1 is then free to start the chain $r_2, r_3, \dots, r_n$ and to receive the arc back from $r_n$. (Here $r_k$ means "the city visited $k$-th".)
- **Slides 11–12.** Choosing $M$. The chain has $n-1$ cities after city 1, so $u_{r_n} - u_{r_2} \ge n - 2$. For the pair $r_n \to r_2$ (not used), the constraint needs $M \ge u_{r_n} - u_{r_2} + 1 \ge n - 1$. So **$M = n - 1$ is enough**, and that is the value always used.
- **Slide 13.** The complete TSP model in set notation.

**Read in the notes:** "Travelling Salesman Problem (TSP)" up to "Extending the TSP to Allow Multiple Tours". The notes give the same argument in more detail and show Pyomo code.

> **Checkpoint 2.** For a 5-city problem, what is the MTZ constraint for the arc $3 \to 4$, and what does it say when $x_{34}=1$ and when $x_{34}=0$?
>
> <details><summary>▸ Answer</summary>
>
> With $n = 5$, $M = n - 1 = 4$: $\;u_3 - u_4 + 1 \le 4(1 - x_{34})$.
> If $x_{34} = 1$: $u_3 - u_4 + 1 \le 0$, so $u_4 \ge u_3 + 1$ (city 4 comes after city 3).
> If $x_{34} = 0$: $u_3 - u_4 + 1 \le 4$, i.e. $u_3 - u_4 \le 3$. If the $u$ values of cities 2–5 are set to their positions 1–4 along the tour, they differ by at most 3, so this always holds: it never rules out a real tour.
> </details>

### Step 3: Several tours from the depot (slides 14–17; notes "Extending the TSP to Allow Multiple Tours")

- Drop the "left once" and "entered once" constraints **for city 1 only**, and add $\sum_{j \ne 1} x_{1j} = m$. Then $m$ arcs leave city 1 (and, by the other constraints, $m$ come back).
- **Slide 16.** The MTZ constraint now allows several increasing chains instead of one. Each chain is joined to city 1 at both ends, giving $m$ tours that all start and end at the depot.
- **Slide 17.** An example with two chains: $1 \to 7 \to 3 \to 1$ and $1 \to 5 \to \dots \to 10 \to 1$.

> **Checkpoint 3.** Which constraints change when we go from one tour to $m$ tours, and which stay the same?
>
> <details><summary>▸ Answer</summary>
>
> - **Change:** "left exactly once" and "entered exactly once" now hold only for $i \in V \setminus \{1\}$, and a new constraint fixes the number of arcs leaving city 1 at $m$.
> - **Same:** the MTZ constraint (still only for $i, j \ne 1$), the binary $x_{ij}$, and the objective.
> </details>

### Step 4: The basic VRP and its weakness (slides 18–24)

- **Slides 18–20.** The VRP in words: route a fleet of $m$ vehicles to serve the customers. With $m = 1$ it is the TSP. The word "optimal" is ambiguous, so two objectives are compared: **total distance** or **longest route**. Demand and capacity are still missing from the model.
- **Slides 21–22.** Minimise total distance with **at most** $m$ routes ($\sum_{j \ne 1} x_{1j} \le m$).
- **Slide 23.** Without capacity, if the distances obey the triangle inequality (going direct is never longer than a detour), a single vehicle (the TSP tour) is always one of the best solutions. Every extra route has to drive out of the depot and back again.
- **Slide 24.** Once demand and capacity are added, minimising total distance can still give some long routes and some short ones. A company that wants deliveries done quickly may not like that.

> **Checkpoint 4.** Why does minimising the total distance tend to use as few vehicles as possible?
>
> <details><summary>▸ Answer</summary>
>
> Every route has to leave the depot and come back to it. Merging two routes into one saves at least one trip out and one trip back, so with the triangle inequality, fewer, longer routes have a smaller (or equal) total distance. The model therefore uses only as many vehicles as the capacity forces it to.
> </details>

### Step 5: VRP with demand, capacity and flow (slides 25–28; notes "Vehicle Routing Problem (VRP)" → "Model 1")

The model (slide 26):

$$
\begin{aligned}
\text{Minimise } & \sum_{i \in V} \sum_{j \in V: j \ne i} c_{ij} x_{ij} \\
\text{subject to } & \sum_{j \ne i} x_{ij} = 1 && \forall i \in V \setminus \{1\} && \text{(each customer left once)}\\
& \sum_{i \ne j} x_{ij} = 1 && \forall j \in V \setminus \{1\} && \text{(each customer entered once)}\\
& \sum_{j} x_{1j} \le m && && \text{(at most } m \text{ vehicles leave the depot)}\\
& \sum_{j} f_{ji} - \sum_{j} f_{ij} = q_i && \forall i \in V \setminus \{1\} && \text{(flow conservation)}\\
& 0 \le f_{ij} \le Q\,x_{ij} && \forall i \ne j && \text{(load only on used arcs, at most } Q)\\
& x_{ij} \in \{0,1\}
\end{aligned}
$$

How to read the flow constraints:

- A vehicle leaves the depot carrying the whole demand of its route.
- At each customer, the load drops by exactly that customer's demand: load in − load out $= q_i$.
- The load on an arc can be positive only if the arc is used ($x_{ij} = 1$), and it never exceeds $Q$. So each route's total demand is at most $Q$.

**Slide 27: why no MTZ constraint is needed.** Take a subtour that misses the depot, $r_i \to r_j \to \dots \to r_p \to r_i$. Write flow conservation at each of its cities and add the equations: every flow appears once with + and once with −, so you get
$$0 = q_{r_i} + q_{r_j} + \dots + q_{r_p}.$$
If every demand is positive this is impossible, so **positive demands rule out subtours**.

**Slide 28.** If some demands are zero or negative (pick-ups), the demands on a subtour can add up to 0. Then subtours can appear, and you add the MTZ constraint. The notes show a "cooked-up" example with and without it.

> **Checkpoint 5.** A vehicle drives $1 \to 8 \to 2 \to 3 \to 1$ with demands $q_8 = 5$, $q_2 = 4$, $q_3 = 3$. What is the flow on each arc?
>
> <details><summary>▸ Answer</summary>
>
> It leaves the depot with the whole route demand, $5 + 4 + 3 = 12$, and drops each customer's demand on the way:
> $f_{1,8} = 12$, $f_{8,2} = 12 - 5 = 7$, $f_{2,3} = 7 - 4 = 3$, $f_{3,1} = 3 - 3 = 0$.
> Check flow conservation at city 8: in − out $= 12 - 7 = 5 = q_8$. ✔ All loads are at most $Q$ if $Q \ge 12$.
> </details>

### Step 6: Minimise the longest route (slides 29–33; notes "Model 2")

- **Slide 29.** "Deliver all orders as quickly as possible" becomes "minimise the length of the longest route": a **minimax** objective.
- **Slide 30.** To know each route's length, imagine one **copy of the network per vehicle** and track which arcs each vehicle uses.
- **Slides 32–33.** The full model. Variables $x_{ijk}$ and $f_{ijk}$ for every vehicle $k \in K$, plus $C_{Max}$:

| Constraint | Meaning |
|---|---|
| Minimise $C_{Max}$ | Make the longest route as short as possible |
| $\sum_{k}\sum_{j \ne i} x_{ijk} = 1$, $\forall i \ne 1$ | A single vehicle leaves each customer |
| $\sum_{k}\sum_{i \ne j} x_{ijk} = 1$, $\forall j \ne 1$ | A single vehicle enters each customer |
| $\sum_{j \ne i} x_{jik} = \sum_{j \ne i} x_{ijk}$, $\forall i \ne 1, \forall k$ | If vehicle $k$ enters customer $i$, **the same vehicle** leaves it |
| $\sum_k \sum_j x_{1jk} \le m$ | No more than $m$ vehicles leave the depot |
| $\sum_{i}\sum_{j \ne i} c_{ij} x_{ijk} \le C_{Max}$, $\forall k$ | Each vehicle's route length is at most $C_{Max}$ |
| $\sum_k\sum_j f_{jik} - \sum_k\sum_j f_{ijk} = q_i$, $\forall i \ne 1$ | Flow conservation: each customer gets its demand |
| $0 \le f_{ijk} \le Q\,x_{ijk}$ | Vehicle $k$ carries load only on arcs it uses, at most $Q$ |
| (optional) $u_{ik} - u_{jk} + 1 \le (n-1)(1 - x_{ijk})$ | MTZ for each vehicle; add only if subtours appear |

The "same vehicle enters and leaves" constraint is **required**. Without it, vehicle 1 could drive into a customer and vehicle 2 drive out. Each vehicle's "route" would then be only part of a real route, so $C_{Max}$ would be too small and the answer meaningless.

> **Checkpoint 6.** Why can't the minimax model use the variables $x_{ij}$ of the first VRP model?
>
> <details><summary>▸ Answer</summary>
>
> $x_{ij}$ only says that *some* vehicle uses arc $i \to j$, not *which* one. To bound each vehicle's route length by $C_{Max}$ you have to add up the distances of the arcs used by that vehicle alone, so every vehicle needs its own variables $x_{ijk}$.
> </details>

### Step 7: Subgraphs, heuristics and the wrap-up (slides 34–36; notes "Limitations of the Model", "NP-Hard Problems and Heuristic Solutions")

- **Slide 34.** If the vehicles only need to visit a subset $S$ of the locations, compute the shortest path between every pair of locations in $S$ first. Then solve the VRP on $S$ alone, using those shortest-path distances.
- **Notes, limitations.** The model assumes one vehicle per customer, identical vehicles and no time windows. Each of these can be modelled, but it makes the problem harder.
- **Notes, heuristics.** TSP and VRP are NP-hard: no known algorithm solves every instance quickly and optimally. Common heuristics are nearest neighbour, Clarke–Wright savings, simulated annealing and genetic algorithms.
  - **Nearest neighbour for the VRP:** each vehicle in turn starts at the depot. It repeatedly moves to the nearest unvisited location whose demand still fits in the remaining capacity, then returns to the depot.
  - Its weakness: it can end up collecting far-away demand. One fix is to set a maximum distance from the depot.
  - Exercise 3 in Section 8 lets you try it.
- **Slide 36** links to the demo notebook: go to Step 8.

### Step 8: Run the demo notebook

Follow [Section 7](#7-the-demo-notebook-what-it-does-and-what-you-should-see). Then do its **"What do you notice?"** and **"Try it"** sections. Their answers are inside the notebook, under **Answer** / **Answers**; try first, then click to check.

### Step 9: Test yourself

Do the [practice exercises](#8-practice-exercises-with-answers) and the [self-test](#9-self-test), then tick off the [checklist](#12-checklist-have-you-finished-the-week).

### Step 10 (optional): Further reading

- **Miller, Tucker and Zemlin (1960)**: the paper the MTZ constraint is named after. Their "base city" is numbered **0** (ours is city 1), and they also allow the salesman to return to the base several times, like the $m$ tours of Step 3.
- **Christofides (1976)**: a survey of VRP solution methods, exact (Section 3.1) and heuristic (Section 3.3, including the Clarke–Wright "savings" method mentioned in the notes).

---

## 6. The key ideas in one place

| Idea | One-line summary |
|---|---|
| Subtour | A closed loop that does not include every city (or does not pass through the depot) |
| MTZ constraint | $u_i - u_j + 1 \le (n-1)(1 - x_{ij})$ for $i, j \ne 1$: if $i \to j$ is used, $u_j \ge u_i + 1$, so no loop can avoid city 1 |
| Why exclude city 1 | A tour returns to its start, which would need the start's $u$ to exceed itself |
| Why $M = n-1$ | The $u$ values along a chain of $n - 1$ cities span at least $n - 2$; one more gives $n - 1$ |
| $m$ tours | Relax the in/out constraints at city 1; $\sum_{j \ne 1} x_{1j} = m$ (or $\le m$) |
| Flow $f_{ij}$ | Load on the vehicle on arc $i \to j$; drops by $q_i$ at customer $i$; at most $Q x_{ij}$ |
| Flow removes subtours | Adding flow conservation round a subtour gives $0 = $ sum of its demands, impossible if all $q_i > 0$ |
| Minimise total distance | Fewest, fullest vehicles; some routes may be much longer than others |
| Minimax | Minimise $C_{Max} \ge$ every vehicle's route length; balances the routes, usually at a higher total distance |
| Per-vehicle variables | Needed to measure each vehicle's route; "same vehicle enters and leaves" is required |
| Feasibility check | You need $m \cdot Q \ge \sum_{i \ne 1} q_i$, otherwise no solution exists |
| Heuristics | Fast, not optimal; e.g. nearest neighbour |

---

## 7. The demo notebook: what it does and what you should see

**File:** `2 Lecture Demos/1 TSP and VRP with Pyomo.ipynb` ([open on the course site](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2010%20-%20Vehicle%20Routing%20Problem/2%20Lecture%20Demos/1%20TSP%20and%20VRP%20with%20Pyomo.ipynb)).

**The example.**
- One depot (node 1) at (50, 50) and 7 customers (nodes 2–8).
- Total demand is 30; there are 3 vehicles of capacity 15.
- Distances are straight-line distances, rounded to one decimal.

**How to run it.** Run the cells from top to bottom with **Shift + Enter**, one at a time, or use **Run → Run All Cells**.

- **Cell 1** installs Pyomo (the modelling library) and HiGHS (the solver). It takes about a minute the first time. Its extra lines only adapt Pyomo to the browser; you don't need to understand them.
- The rest takes about 15 seconds, most of it for model 3.

| Section | What it builds | What you should see |
|---|---|---|
| Data and helpers | Coordinates, demands, distances; functions to read and draw routes | `7 customers, total demand 30, 3 vehicles x capacity 15 = 45` |
| 1. TSP with MTZ | Solves the TSP twice: MTZ switched off, then on | Without MTZ: length **233.4**, four two-city loops. With MTZ: length **281.4**, tour `1 -> 8 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 1` |
| 2. VRP, minimise total distance | Flow model (Step 5) | Total distance **327.6**: two routes, each with load 15, lengths **172.8** and **154.8** |
| 3. VRP, minimise the longest route | Minimax model (Step 6) | Longest route **137.4**; three routes of length 114.2, 110.9 and 137.4 (loads 9, 9, 12); total **362.5** |

Each section also draws its routes, one colour per vehicle.

- A route may print in the opposite direction (e.g. `1 -> 7 -> 6 -> 1` instead of `1 -> 6 -> 7 -> 1`), and routes may come out in a different order. The lengths are what matter.
- In model 3, only the longest route is optimised. The two shorter routes can therefore differ between runs or computers while $C_{Max}$ stays 137.4.

**Two small differences from slide 33** (both explained in the notebook):
1. Each vehicle may leave the depot **at most once**, so no vehicle makes two trips.
2. The flow is kept **per vehicle**.

The longest route is the same (137.4).

**After running it:**
- **"What do you notice?"** Compare the plots of models 2 and 3, and explain why model 2 leaves a vehicle at the depot.
- **"Try it"** has four experiments:
  - set `capacity = 12`;
  - set `num_vehicles = 2` and `capacity = 14`;
  - add a customer 9;
  - compare the total distance of models 2 and 3.

  Change the data cell, re-run everything below it, and compare with the answers in the notebook. **Set the data back afterwards.**
- In the second experiment, the model-2 cell stops with `RuntimeError: A feasible solution was not found…`. That error **is** the expected answer (the fleet cannot carry the demand), not a bug.

**Want to run the code from the notes?** The notes contain Pyomo code for the TSP and for both VRP models.
1. Add new cells at the end of the demo notebook, after running it from the top. Cell 1 must have run first.
2. Paste the TSP code as it is. It solves its own 4-city example.
3. For the two VRP code blocks, first run a cell with `num_cities = n` and `distance_matrix = dist`. The notes' code then uses the notebook's data (`demand`, `capacity`, `num_vehicles` already exist).
4. The VRP code from the notes prints the arcs it uses, `i -> j`. With the notebook's data, the first VRP model gives the same two routes as model 2 (total 327.6).
5. The minimax code from the notes defines the model without solving it. Add `SolverFactory('appsi_highs').solve(model)` and `print(value(model.Cmax))` at the end; you should get 137.4.

---

## 8. Practice exercises (with answers)

Do these on paper. They use only this week's ideas.

**Exercise 1: MTZ by hand.** Four cities, tour $1 \to 3 \to 2 \to 4 \to 1$, $n = 4$.
(a) Give values of $u_2, u_3, u_4$ that satisfy all MTZ constraints.
(b) Check the constraint for the unused arc $4 \to 3$.
(c) Show that the subtour $2 \to 3 \to 2$ breaks MTZ.

<details><summary>▸ Answer</summary>

(a) Order along the tour after city 1: 3, 2, 4. Take $u_3 = 1$, $u_2 = 2$, $u_4 = 3$.
Used arcs: $3 \to 2$: $u_3 - u_2 + 1 = 0 \le 0$ ✔; $2 \to 4$: $u_2 - u_4 + 1 = 0 \le 0$ ✔. The arcs $1 \to 3$ and $4 \to 1$ touch city 1, so they have no MTZ constraint.

(b) $x_{43} = 0$: $u_4 - u_3 + 1 = 3 \le (n-1)(1-0) = 3$ ✔. It holds with equality, which shows that $M = n - 1$ is exactly big enough here.

(c) $x_{23} = x_{32} = 1$ gives $u_2 - u_3 + 1 \le 0$ and $u_3 - u_2 + 1 \le 0$. Adding them: $2 \le 0$, impossible. So the subtour cannot occur.
</details>

**Exercise 2: How many vehicles?** Demands of the notebook: total 30.
(a) With capacity 15, what is the smallest number of vehicles?
(b) With capacity 12?
(c) With 2 vehicles of capacity 14?

<details><summary>▸ Answer</summary>

You need $m \cdot Q \ge 30$, so at least $\lceil 30 / Q \rceil$ vehicles.

- (a) $\lceil 30/15 \rceil = 2$. Model 2 in the notebook uses exactly 2, both full.
- (b) $\lceil 30/12 \rceil = 3$. With `capacity = 12`, model 2 must use all 3 vehicles (total 362.5).
- (c) $2 \times 14 = 28 < 30$: no feasible solution, which is why the notebook stops with a `RuntimeError`.

This count is only a lower bound. Demands cannot be split between vehicles, so sometimes even more vehicles are needed.
</details>

**Exercise 3: Nearest neighbour by hand.** Use the notebook's example: capacity 15, demands $q_2=4, q_3=3, q_4=5, q_5=4, q_6=6, q_7=3, q_8=5$. If two locations are equally near, take the one with the lower number. The distances you need are:

| from \ to | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **1** | – | 42.4 | 42.7 | 46.1 | 41.2 | 39.1 | 36.4 | 36.4 |
| **2** | 42.4 | – | 18.0 | 60.2 | 72.8 | 81.4 | 68.0 | 40.3 |
| **3** | 42.7 | 18.0 | – | 45.3 | 62.6 | 80.6 | 75.2 | 53.9 |
| **4** | 46.1 | 60.2 | 45.3 | – | 26.9 | 65.2 | 80.6 | 79.1 |
| **5** | 41.2 | 72.8 | 62.6 | 26.9 | – | 42.7 | 67.3 | 77.6 |
| **6** | 39.1 | 81.4 | 80.6 | 65.2 | 42.7 | – | 35.4 | 63.2 |
| **7** | 36.4 | 68.0 | 75.2 | 80.6 | 67.3 | 35.4 | – | 35.4 |
| **8** | 36.4 | 40.3 | 53.9 | 79.1 | 77.6 | 63.2 | 35.4 | – |

Build the routes vehicle by vehicle and compare the total with the optimum of model 2 (327.6).

<details><summary>▸ Answer</summary>

- **Vehicle 1:** from 1, the nearest are 7 and 8 (36.4); take 7 (load 3). From 7, the nearest are 6 and 8 (35.4); take 6 (load 9). From 6, the nearest is 5 (42.7), load 13. Remaining capacity is 2 and every unvisited demand is larger, so it returns.
  Route $1 \to 7 \to 6 \to 5 \to 1$, length $36.4 + 35.4 + 42.7 + 41.2 = 155.7$.
- **Vehicle 2:** from 1 the nearest unvisited is 8 (36.4), load 5. Then 2 (40.3), load 9. Then 3 (18.0), load 12. Customer 4 (demand 5) does not fit, so it returns.
  Route $1 \to 8 \to 2 \to 3 \to 1$, length $36.4 + 40.3 + 18.0 + 42.7 = 137.4$.
- **Vehicle 3:** only 4 is left. Route $1 \to 4 \to 1$, length $46.1 + 46.1 = 92.2$.

Total $155.7 + 137.4 + 92.2 = 385.3$, against the optimum 327.6, i.e. about 18 % longer. It also uses three vehicles where two suffice. Customer 4 is left to the end and served alone: this is the "picks up far-away demand" weakness from the notes.
</details>

**Exercise 4: Write a constraint.** In the minimax model, write the constraint "each vehicle leaves the depot at most once", which the notebook adds.

<details><summary>▸ Answer</summary>

$$\sum_{j \in V \setminus \{1\}} x_{1jk} \le 1 \quad \forall k \in K$$

In the notebook: `mm.depot = pyo.Constraint(K, rule=lambda m, k: sum(m.x[1, j, k] for j in C) <= 1)`, where `C` is the list of customers.
</details>

---

## 9. Self-test

Answer each question in one or two sentences, then open the answer.

**Q1.** What is a subtour, and why does the TSP model need extra constraints to avoid them?
<details><summary>▸ Answer</summary>A closed loop that does not visit all the cities. The "one arc in, one arc out" constraints are also satisfied by several separate loops, so on their own they do not force a single tour.</details>

**Q2.** In $u_i - u_j + 1 \le (n-1)(1 - x_{ij})$, what does $u_i$ represent, and does its value have to equal the position of city $i$?
<details><summary>▸ Answer</summary>It orders the cities along the tour. Only the order matters: any increasing values work, not necessarily 1, 2, 3, ….</details>

**Q3.** For which $i, j$ is the MTZ constraint written, and why?
<details><summary>▸ Answer</summary>For all $i \ne j$ with $i, j \in V \setminus \{1\}$. Including city 1 would make every tour impossible, because the tour must return to its start.</details>

**Q4.** How do you change the TSP so that exactly $m$ routes leave city 1?
<details><summary>▸ Answer</summary>Apply the "left once" and "entered once" constraints only to cities $2, \dots, n$, and add $\sum_{j \ne 1} x_{1j} = m$.</details>

**Q5.** Without demand and capacity, why does minimising total distance usually give a single tour?
<details><summary>▸ Answer</summary>If the distances obey the triangle inequality, merging routes never increases the total (it saves trips to and from the depot), so a single tour is always among the best solutions.</details>

**Q6.** What does $f_{ij} \le Q\,x_{ij}$ do?
<details><summary>▸ Answer</summary>Two things: no load can travel on an unused arc ($x_{ij} = 0 \Rightarrow f_{ij} = 0$), and the load on a used arc is at most the vehicle capacity $Q$.</details>

**Q7.** Why does the flow model need no MTZ constraint when all demands are positive? When would you add it?
<details><summary>▸ Answer</summary>Adding flow conservation round a subtour that misses the depot gives 0 = the sum of its demands, which is impossible if every $q_i > 0$. Add MTZ if some demands are zero or negative (pick-ups), because then a subtour's demands can sum to 0.</details>

**Q8.** What is $C_{Max}$, and why is minimising it called a minimax model?
<details><summary>▸ Answer</summary>An upper bound on every vehicle's route length. Minimising it minimises the maximum route length, so the longest route is as short as possible.</details>

**Q9.** Why is "if vehicle $k$ enters location $i$, it must leave $i$" required in the minimax model?
<details><summary>▸ Answer</summary>Without it, one vehicle could arrive at a customer and another leave. Each vehicle's arcs would not form a real route, its "length" would be too small, and $C_{Max}$ would be meaningless.</details>

**Q10.** In the notebook, model 2 has total distance 327.6 and longest route 172.8; model 3 has 362.5 and 137.4. What does balancing the routes cost and gain?
<details><summary>▸ Answer</summary>It costs 34.9 more total distance (about +10.7 %) and makes the longest route 35.4 shorter (about −20.5 %): deliveries finish sooner, at the price of more driving.</details>

**Q11.** What must hold for a VRP with $m$ vehicles of capacity $Q$ to be feasible at all?
<details><summary>▸ Answer</summary>$m \cdot Q \ge \sum_{i \ne 1} q_i$: the fleet must be able to carry the total demand. This is necessary but not always sufficient, because each customer is served by one vehicle and demands cannot be split.</details>

**Q12.** Why are heuristics used for real VRPs, and what is one weakness of nearest neighbour?
<details><summary>▸ Answer</summary>The VRP is NP-hard, so exact solvers become too slow for large instances. Nearest neighbour is fast but short-sighted: it can leave far-away customers to the end and serve them with long extra trips.</details>

---

## 10. Troubleshooting

| Problem | What to do |
|---|---|
| The `.pptx` opens as strange text or does not open on the course site | The browser cannot show PowerPoint files. Right-click → **Download**, then open it in PowerPoint (Section 4). |
| The notes show LaTeX code such as `$$\begin{align*}` | You opened the raw file. Right-click → **Open With** → **Markdown Preview**. |
| `ModuleNotFoundError: No module named 'pyomo'` (or `highspy`) | Run cell 1 (the `%pip install` cell) first, and wait until it finishes. |
| `NameError` (e.g. `name 'dist' is not defined`) | A cell was run before the cells above it. Use **Run → Run All Cells**, or run every cell from the top in order. |
| `RuntimeError: A feasible solution was not found…` | The data has no feasible solution (e.g. total capacity below total demand). In the "Try it" experiment this is the expected answer. Otherwise check `capacity`, `num_vehicles` and `demand`. |
| A route prints backwards, or in a different order | Normal: the length is the same. |
| In model 3 the two shorter routes differ from Section 7 | Normal: only the longest route (137.4) is optimised; the others can vary. |
| The notebook is stuck or behaves strangely after many changes | **Kernel → Restart Kernel**, then run all cells from the top. |
| You changed the notebook and want the original values back | The data cell's original values are: `capacity = 15`, `num_vehicles = 3`, and the `coords`/`demand` of nodes 1–8 in Section 7. Better: experiment on a duplicate (right-click → **Duplicate**). |

---

## 11. Glossary

| Term | Meaning |
|---|---|
| **Arc / edge** | A direct connection $i \to j$ between two locations |
| **Depot** | The base where every vehicle starts and ends; city (node) 1 |
| **Tour / route** | A closed path that starts and ends at the depot |
| **Subtour** | A closed loop that does not go through the depot (or does not cover all cities) |
| **MTZ constraint** | Miller–Tucker–Zemlin subtour-elimination constraint, using order variables $u_i$ |
| **Big $M$** | A constant large enough that a constraint does nothing when a binary variable is 0 |
| **Demand $q_i$** | The amount customer $i$ needs delivered |
| **Capacity $Q$** | The most a vehicle can carry |
| **Flow $f_{ij}$** | The load on a vehicle as it drives $i \to j$ |
| **Flow conservation** | Load in − load out at a customer = its demand |
| **Minimax** | Minimise the largest of several quantities (here, route lengths) |
| **MILP** | Mixed-integer linear programme: a linear model with some integer (here binary) variables |
| **NP-hard** | A class of problems for which no fast exact algorithm is known for all instances |
| **Heuristic** | A fast method that gives a good, but not necessarily optimal, solution |
| **Triangle inequality** | $c_{ik} \le c_{ij} + c_{jk}$: going direct is never longer than a detour |
| **Pyomo** | A Python library for writing optimisation models |
| **HiGHS** (`appsi_highs`) | The open-source solver the notebook uses; it runs in the browser |

---

## 12. Checklist: have you finished the week?

- [ ] I read slides 1–36 in PowerPoint.
- [ ] I read the lecture notes in Markdown Preview, at least the TSP, multiple-tours and VRP Model 1 and Model 2 sections.
- [ ] I answered Checkpoints 1–6 in Section 5.
- [ ] I ran the demo notebook from top to bottom and got 281.4, 327.6 and 137.4.
- [ ] I did the notebook's "What do you notice?" and all four "Try it" experiments, then put the data back.
- [ ] I did Exercises 1–4 in Section 8.
- [ ] I can answer Q1–Q12 in Section 9 without looking.
- [ ] (Optional) I looked at the MTZ paper and the Christofides survey.

---

## 13. Assumptions made in this README

These points are not stated in the course files themselves. Please check them if anything looks different:

1. **Course-site address and menus.** The site address (`https://ctsallis.github.io/operational_research/`) is taken from the link on slide 36 of the deck.
   - The menu names (**Download**, **Open With → Markdown Preview**, **Duplicate**, **Run → Run All Cells**, **Kernel → Restart Kernel**) are those of the standard JupyterLab interface the site uses. Their exact wording may differ slightly.
2. **No tutorial this week.** The folder contains no tutorial sheet or answers. Section 8 and the self-test were written for this README from the lecture material and the notebook's example. Every number in them was checked by running the notebook's data.
3. **Prerequisite.** Section 2 assumes that Week 09 (Travelling Salesman Problem) comes before this week. The folder numbering suggests this, and the deck recaps the TSP on slides 3–5.
4. **Timings.** "About a minute" for the first cell and "about 15 seconds" for the rest come from the notebook itself. They depend on your connection and computer.
5. **Tie rule in Exercise 3.** The notes' nearest-neighbour description does not say what to do when two locations are equally near. "Take the lower number" is a choice made for this exercise.
6. **Notes code in the browser.** Running the notes' code inside the demo notebook (Section 7) is a suggestion, not part of the course material. It was checked with the same browser Python engine the site uses.
7. **`5 Source Files`.** These are treated as staff material that students do not need, because their content is either in the student files or concerns preparing the slides.

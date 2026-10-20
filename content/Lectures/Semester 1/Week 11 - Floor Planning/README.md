# Week 11 – Floor Planning

This week is about **packing rectangles**: placing tables, machines or boxes on a floor so that they do not overlap, while making the floor as small as possible, fitting in as many items as possible, or keeping connected items close together. All of these become **mixed-integer linear programs (MILPs)**. The key trick is the same in every model: binary variables and a large number $M$ that switch constraints on and off.

This README is written so that you can do the whole week on your own. Work through the sections in order.

## Contents

1. [What you will be able to do](#1-what-you-will-be-able-to-do)
2. [What is in this folder](#2-what-is-in-this-folder)
3. [Before you start](#3-before-you-start)
4. [Your plan for the week](#4-your-plan-for-the-week)
5. [The ideas, step by step](#5-the-ideas-step-by-step)
6. [The four notebooks](#6-the-four-notebooks)
7. [Answers to the questions on the slides](#7-answers-to-the-questions-on-the-slides)
8. [Check yourself](#8-check-yourself)
9. [If something goes wrong](#9-if-something-goes-wrong)
10. [Words used this week](#10-words-used-this-week)
11. [Assumptions made in this README](#11-assumptions-made-in-this-readme)

---

## 1. What you will be able to do

By the end of the week you should be able to:

- write the **non-overlap constraints** for two rectangles, and explain why only one of the four needs to hold;
- use **two binary variables and a big-M** to choose which of the four constraints holds;
- write a **minimax** objective (the smallest square that holds all items);
- add **rotation** (turning an item through 90°) with one binary variable per item;
- change the objective to **fit as many items as possible**, **cover as much area as possible**, or **keep connected items close** (rectilinear distance with absolute values);
- explain why these models get slow quickly as the number of items grows.

There is **no tutorial sheet this week**. Your practice is the four notebooks (their *What do you notice?* and *Try it* cells, which include answers) and the questions in [section 8](#8-check-yourself).

---

## 2. What is in this folder

```
Week 11 - Floor Planning/
├── README.md                          ← this file
├── 1 Lecture/
│   └── Week 11 - Floor Planning.pptx  ← the slides (35 slides)
├── 2 Lecture Demos/                   ← the notebooks; run them in number order
│   ├── 1 Floor planning - minimise area.ipynb
│   ├── 2 Floor planning - maximise number of items.ipynb
│   ├── 3 Floor planning - maximise placed area.ipynb
│   └── 4 Connected floor planning - minimise distance.ipynb
└── 5 Source Files/                    ← originals; you do not need these
    ├── HTML Exports/Floor Planning - Pyomo Model.html
    ├── MATLAB/  (3 .m files)
    └── Python/  (model.py, Floor Planning - Pyomo Model.md)
```

| File | What it is | Do you need it? |
| --- | --- | --- |
| [`1 Lecture/Week 11 - Floor Planning.pptx`](1%20Lecture/Week%2011%20-%20Floor%20Planning.pptx) | The lecture slides | **Yes.** Open in PowerPoint. |
| [`2 Lecture Demos/1 …minimise area.ipynb`](2%20Lecture%20Demos/1%20Floor%20planning%20-%20minimise%20area.ipynb) | Smallest square for 6 items, with rotation | **Yes** |
| [`2 Lecture Demos/2 …maximise number of items.ipynb`](2%20Lecture%20Demos/2%20Floor%20planning%20-%20maximise%20number%20of%20items.ipynb) | Most items on a 4 × 5 floor | **Yes** |
| [`2 Lecture Demos/3 …maximise placed area.ipynb`](2%20Lecture%20Demos/3%20Floor%20planning%20-%20maximise%20placed%20area.ipynb) | Most area covered on a 10 × 10 floor | **Yes** |
| [`2 Lecture Demos/4 Connected …minimise distance.ipynb`](2%20Lecture%20Demos/4%20Connected%20floor%20planning%20-%20minimise%20distance.ipynb) | Keep connected tables close on a fixed floor | **Yes** |
| `5 Source Files/MATLAB/*.m` | The lecturer's original MATLAB models (notebooks 1–3 are Python versions) | No. Optional; they need MATLAB with the Optimization Toolbox. |
| `5 Source Files/Python/model.py` and `Floor Planning - Pyomo Model.md` | The original Python script behind notebook 1 (same code; the `.md` shows it as text) | No. It uses the GLPK solver, which does not run in the browser. |
| `5 Source Files/HTML Exports/…html` | A web-page copy of the `.md` above | No |

---

## 3. Before you start

### Background you need

- **Mixed-integer programming and big-M constraints.** If "binary variable" or "big-M" is unfamiliar, revise [Week 05 – Mixed Integer Programming](../Week%2005%20-%20Mixed%20Integer%20Programming/) first. Slides 2–4 of this week also give a quick recap.
- **Either/or constraints** were also used for scheduling in [Week 07 – Flow Shop and Job Shop Scheduling](../Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/). Floor planning uses the same idea in two dimensions.
- **Basic Pyomo:** `ConcreteModel`, `Var`, `Constraint`, `Objective`, `SolverFactory`. Every line of the notebooks is explained, so you can follow them even if you are rusty.

### How to open the notebooks

The notebooks run **inside your web browser** on the course site (JupyterLite). Nothing has to be installed.

1. Open the course site in Chrome, Edge or Firefox: <https://ctsallis.github.io/operational_research/> (see [assumption A1](#11-assumptions-made-in-this-readme)).
2. If this is your first session, open `00_START_HERE.ipynb` in the top folder and choose *Run → Run All Cells*. If every check prints `OK`, the notebooks of this week will run too.
3. In the file browser on the left, go to `Lectures` → `Semester 1` → `Week 11 - Floor Planning` → `2 Lecture Demos` and double-click a notebook.
4. Run the cells **from the top, in order**. The **first code cell** installs Pyomo and the HiGHS solver; it is needed every time you open a notebook, and the first time it can take a minute. The quickest way to run everything is *Run → Run All Cells*.
5. While a cell runs it shows `[*]` on its left; when it finishes the star becomes a number.

To read this README on the site: right-click `README.md` → *Open With* → *Markdown Preview*.

### How to get the slides

On the site, go to `1 Lecture`, right-click `Week 11 - Floor Planning.pptx` → **Download**, and open it in PowerPoint. (The site cannot show a `.pptx` itself.)

### Saving your work

Notebooks you change on the site are stored **only in that browser**. Clearing browser data, a private window or another computer loses them. To keep a copy, right-click the notebook in the file browser → **Download**.

When a *Try it* asks you to change a line, the original line is given in this README, so you can always type it back.

---

## 4. Your plan for the week

Tick each step when you finish it.

- [ ] **Step 1 – Recap (slides 1–4).** A small linear program and the same problem with $x$ forced to be an integer. Check that you understand why the optimum moves from $(1.9, 2.9)$ with $P^* = 13.95$ to $(2, 2.833)$ with $P^* = 13.917$.
- [ ] **Step 2 – The basic packing model (slides 5–19).** Read slowly; [section 5](#5-the-ideas-step-by-step) explains each step again. Make sure you can fill in the big-M table on slide 15 yourself.
- [ ] **Step 3 – Rotation (slides 20–23).**
- [ ] **Step 4 – Notebook 1.** Run it and compare `v` with the six-item result on slide 19 (12). Then do its *What do you notice?* and *Try it* cells; *Try it* 2 reproduces the four-table results of slides 19 (12) and 23 (11).
- [ ] **Step 5 – The cost of binary variables (slides 32–34).** Read these now: they explain why notebook 2 is slow.
- [ ] **Step 6 – Notebooks 2 and 3.** Two new objectives on a fixed floor.
- [ ] **Step 7 – Connected items (slides 24–29), then notebook 4.**
- [ ] **Step 8 – A real application (slides 30–31)** and the conclusion (slide 35).
- [ ] **Step 9 – [Check yourself](#8-check-yourself).** Answer the questions before opening the answers.

---

## 5. The ideas, step by step

Slide numbers refer to the `.pptx`.

### 5.1 The data (slides 6–7)

Each item (the slides call them tables) $t_i$ has a width $w_i$ and a height $h_i$. Its position is the **bottom-left corner** $(x_i, y_i)$, so it covers $x_i \le x \le x_i + w_i$ and $y_i \le y \le y_i + h_i$.

The four tables of the slides:

| Table | $t_1$ | $t_2$ | $t_3$ | $t_4$ |
| --- | --- | --- | --- | --- |
| $(w, h)$ | (4, 5) | (3, 7) | (6, 4) | (7, 7) |

### 5.2 Non-overlap: "at least one of four" (slides 8–13)

Two rectangles do **not** overlap exactly when one of them lies completely to one side of the other. For tables 1 and 2 that gives four possibilities:

| Constraint | Meaning |
| --- | --- |
| C1: $x_1 + w_1 \le x_2$ | $t_1$ is to the **left** of $t_2$ |
| C2: $x_2 + w_2 \le x_1$ | $t_2$ is to the **left** of $t_1$ |
| C3: $y_1 + h_1 \le y_2$ | $t_1$ is **below** $t_2$ |
| C4: $y_2 + h_2 \le y_1$ | $t_2$ is **below** $t_1$ |

At least one of them must hold. A linear program cannot say "at least one of", because all of its constraints must hold at the same time. That is why we need binary variables.

### 5.3 Two binaries and big-M choose the constraint (slides 14–15)

Give the pair two binary variables $x_{12}, y_{12} \in \{0, 1\}$ and a large number $M$, and write:

$$
\begin{aligned}
x_1 + w_1 &\le x_2 + M(x_{12} + y_{12}) &&\text{C1}\\
x_2 + w_2 &\le x_1 + M(1 - x_{12} + y_{12}) &&\text{C2}\\
y_1 + h_1 &\le y_2 + M(1 + x_{12} - y_{12}) &&\text{C3}\\
y_2 + h_2 &\le y_1 + M(2 - x_{12} - y_{12}) &&\text{C4}
\end{aligned}
$$

The four values of $(x_{12}, y_{12})$ add $0$ to exactly one constraint and $M$ or $2M$ to the other three:

| $(x_{12}, y_{12})$ | added to C1 | C2 | C3 | C4 | The constraint that must hold |
| --- | --- | --- | --- | --- | --- |
| (0, 0) | 0 | $M$ | $M$ | $2M$ | C1 |
| (1, 0) | $M$ | 0 | $2M$ | $M$ | C2 |
| (0, 1) | $M$ | $2M$ | 0 | $M$ | C3 |
| (1, 1) | $2M$ | $M$ | $M$ | 0 | C4 |

Adding $M$ to the right-hand side makes a constraint **always true** ("switched off"), as long as $M$ is larger than any value the left-hand side minus the rest of the right-hand side can reach. The solver chooses $(x_{12}, y_{12})$, and so chooses the side.

**Careful with the names:** $x_i, y_i$ (one index) are **positions**; $x_{ij}, y_{ij}$ (two indices) are the **binary variables** of a pair. They are different variables.

Every pair $i < j$ gets its own four constraints and two binaries. With $n$ items there are $\binom{n}{2} = \frac{n(n-1)}{2}$ pairs, so $4\binom{n}{2}$ non-overlap constraints (slide 16).

### 5.4 The objective: the smallest square (slides 17–18)

Add one variable $A^*$ and require every item to end at or before $A^*$ in both directions:

$$x_i + w_i \le A^*, \qquad y_i + h_i \le A^* \qquad \text{for every item } i.$$

Then **minimise $A^*$**. $A^*$ is the **side** of the smallest square that holds every item; its area is $(A^*)^2$. This is a **minimax** problem: we minimise the largest of the values $x_i + w_i$ and $y_i + h_i$. In the notebooks $A^*$ is called `v`.

The full model (slide 18):

$$
\begin{aligned}
\text{minimise } & A^* \\
\text{subject to } & x_i + w_i \le A^*,\quad y_i + h_i \le A^* && \text{for all } i\\
& \text{the four constraints of 5.3} && \text{for all pairs } i < j\\
& x_{ij}, y_{ij} \in \{0,1\},\quad x_i, y_i \ge 0
\end{aligned}
$$

Slide 19 shows the result: $A^* = 12$, both for the four tables and for a six-item example.

### 5.5 Rotation (slides 20–23)

Turning an item through 90° swaps its width and height. Add one binary per item, $r_i = 1$ if item $i$ is rotated and $0$ if not. Then

$$\text{width of } i = (1 - r_i)\,w_i + r_i\,h_i, \qquad \text{height of } i = (1 - r_i)\,h_i + r_i\,w_i.$$

Check: with $r_i = 0$ the width is $w_i$; with $r_i = 1$ it is $h_i$. Now replace every $w_i$ and $h_i$ in the model by these two expressions. Both are still linear, because $w_i$ and $h_i$ are numbers.

The full model with rotation is on slide 32. It also lists $r_i \in \{0,1\}$ with the other binary variables.

With rotation the four tables fit in an **11 × 11** square (slide 23) instead of 12 × 12.

### 5.6 Other objectives on a fixed floor (notebooks 2 and 3, slide 26)

If the floor is fixed at $W \times H$, the minimax constraints become **boundary constraints**:

$$x_i + \text{width}_i \le W, \qquad y_i + \text{height}_i \le H.$$

If not every item fits, give each item a binary $u_i$ (1 = placed, 0 = left out) and release the constraints of left-out items with more big-M terms:

- the boundary constraints get $+M(1 - u_i)$ on the right-hand side;
- each non-overlap constraint gets $+M(2 - u_i - u_j)$, so it is switched off when either item is left out.

Then:

- **notebook 2** maximises the **number** of items placed, $\sum_i u_i$;
- **notebook 3** maximises the **area** placed, $\sum_i u_i\, w_i h_i$.

### 5.7 Keeping connected items close (slides 24–29, notebook 4)

Some items are connected (think of machines joined by pipes) and should be near each other on a fixed $W \times H$ floor. Measure the distance between the **centres** of two connected items $i$ and $j$:

$$D^x_{ij} = \Big(x_i + \tfrac{\text{width}_i}{2}\Big) - \Big(x_j + \tfrac{\text{width}_j}{2}\Big), \qquad D^y_{ij} = \Big(y_i + \tfrac{\text{height}_i}{2}\Big) - \Big(y_j + \tfrac{\text{height}_j}{2}\Big).$$

These can be negative. We want the **rectilinear** (city-block) distance $|D^x_{ij}| + |D^y_{ij}|$. An absolute value is not linear, so add two variables $R_{ij}$ and $B_{ij}$ with

$$D^x_{ij} \le R_{ij},\quad -D^x_{ij} \le R_{ij},\qquad D^y_{ij} \le B_{ij},\quad -D^y_{ij} \le B_{ij},$$

and **minimise $\sum (R_{ij} + B_{ij})$** over the connected pairs.

The constraints only say $R_{ij} \ge |D^x_{ij}|$. Because we minimise, the solver pushes $R_{ij}$ down until it equals $|D^x_{ij}|$; the same holds for $B_{ij}$. This trick works only when the absolute value is being minimised.

Slide 29 shows the result on three floors: 20 × 20, 8 × 20 and 10 × 15.

### 5.8 Why these models get slow (slides 32–34)

Each pair of items has two binaries, so there are $2\binom{n}{2}$ of them and $2^{2\binom{n}{2}}$ combinations of their values:

- for 7 items: $2^{42} \approx 4.4 \times 10^{12}$;
- for 10 items: $2^{90}$, which at one combination per millisecond would take about $3.9 \times 10^{16}$ years;
- rotation adds $n$ more binaries, a further factor $2^n$.

The solver does not try every combination (branch and bound skips most of them), but the growth is still why the *Mums Know Best!* puzzle (slide 33) took MATLAB about 10 minutes. Problems like this are **NP-hard** (slide 35): no known method solves every case quickly as the size grows.

---

## 6. The four notebooks

Each notebook starts with a cell that states the problem, how to run it and the expected result. Every code cell has a short explanation above it, and the last cells are *What do you notice?* and *Try it*, with answers hidden under **Answer** (click to open). Try each question before opening its answer.

**Different pictures are normal.** Many layouts are equally good, so your positions, rotations and pictures may differ from the slides and from another computer. The number that matters, such as the side `v`, the number of items or the area, is the same.

### Notebook 1 – Smallest square (slides 17–23)

- **Problem:** six items with rotation allowed; find the smallest square that holds them. The six items are:

  | Item | 1 | 2 | 3 | 4 | 5 | 6 |
  | --- | --- | --- | --- | --- | --- | --- |
  | $(w, h)$ | (4,5) | (3,7) | (6,4) | (7,6) | (3,3) | (2,4) |

  Items 1–3 are the slides' tables $t_1$–$t_3$. Item 4 is 7 × 6 here (7 × 7 in the four-table example). Items 1–6 are the six items of slide 19.
- **Expected result:** `v= 12.0` (a 12 × 12 square), then a plot of the layout.
- **Long output:** `model.display()` and `model.pprint()` print every variable and constraint. Scroll past them to the results.
- **Try it:** in the data cell the original lines are

  ```python
  w = np.array([4,3,6,7,3,2])
  h = np.array([5,7,4,6,3,4])
  ```

  Expected answers (also in the notebook):
  - rotation off → `v = 12`;
  - the four tables → `v = 11` with rotation, `v = 12` without;
  - the *Mums Know Best!* pieces → `v = 5`. That solve takes about half a minute in the browser, so wait for the `[*]` to turn into a number.

### Notebook 2 – Fit as many items as possible

- **Problem:** seven pieces must go on a 4 × 5 floor. Their sizes $(w, h)$ are $(4,1), (3,1), (3,1), (3,1), (2,2), (2,1), (2,1)$. These are the *Mums Know Best!* pieces (slide 33) without one 2 × 1 piece; 7 items is the number used on slide 34.
- **Expected result:** `Status: optimal` and `Objective: 6.0`. Six of the seven fit, and the list shows which item was left out (this can differ between runs).
- **⚠️ The solve cell is slow:** allow **2–4 minutes** in the browser. This is the point of the notebook: the area argument ($21 > 20$) shows at once that 7 cannot fit, but the solver does not know that argument and has to prove it branch by branch.
- **Try it:** adding an area constraint makes the solve take under a second (still 6 items). With `W, H = 5, 5` all 7 fit. The original line is `W, H = 4, 5      # floor size`.

### Notebook 3 – Cover as much floor area as possible

- **Problem:** the six items of notebook 1 (total area 124) on a 10 × 10 floor (area 100).
- **Expected result:** `Status: optimal`, `Objective: 100.0`, and item 3 (6 × 4) left out. The whole floor is covered.
- **Try it:** with `W, H = 10, 12` the answer is **115**, with item 5 left out. The original line is `W, H = 10, 10    # floor size`.

### Notebook 4 – Keep connected tables close (slides 24–29)

- **Problem:** the four tables of the slides on a 20 × 20 floor, rotation allowed. Five pairs are connected: $t_1$–$t_2$, $t_1$–$t_3$, $t_1$–$t_4$, $t_2$–$t_3$ and $t_3$–$t_4$, read from the diagram on slide 25. The objective is the smallest total rectilinear distance between the centres of connected tables.
- **Expected result:** `Status: optimal` and a total distance (see [assumption A2](#11-assumptions-made-in-this-readme)), then:
  - one line per table with its corner and rotation;
  - one line per connected pair with its across and up/down distance;
  - a plot showing the tables inside the dashed floor outline, with each connection drawn as an L-shaped path between the centres.
- **How to check your result yourself:**
  - in the plot, all four tables lie inside the dashed outline and do not overlap;
  - for each connected pair, the across plus up/down distances printed add up, over all five pairs, to the total distance;
  - in the *Try it* (floors 8 × 20 and 10 × 15), the total distance is never smaller than on 20 × 20.
- **Try it:** the original line is `W, H = 20, 20      # floor size (first picture on the Results slide)`.

---

## 7. Answers to the questions on the slides

**Slide 19: "Can it be improved? What is the issue?"**
<details><summary>Answer</summary>

The model never turns a table. Some tables would fit better turned through 90°. Allowing rotation (slides 20–22) brings the four tables down from a 12 × 12 to an 11 × 11 square (slide 23). Rotation does not always help: for the six items of notebook 1 the answer stays 12 (notebook 1, *Try it* 1).
</details>

**Slide 23: "Can it be improved? This is dependent on your desired objective!"**
<details><summary>Answer</summary>

11 × 11 is the best **square** for the four tables. The solver proves it, and there is no better square. "Better" can mean something else, though:

- a fixed floor with as many items as possible (notebook 2);
- as much area used as possible (notebook 3);
- connected items as close as possible (slides 24–29, notebook 4).

Each is a different objective, and each gives a different "best" layout.
</details>

**Slides 33–34: why did the computer take 10 minutes on a puzzle a person solves in 20 seconds?**
<details><summary>Answer</summary>

The solver has to **prove** that no better answer exists. Slide 33 says the optimal layout was found after 0.6 seconds, and the rest of the time went on proof. The number of combinations of binary values grows as $2^{2\binom{n}{2}}$ (slide 34). A person uses insight, for example about area, that the model does not have. Notebook 2's *Try it* shows that giving the model such an insight as an extra constraint makes it fast.
</details>

---

## 8. Check yourself

Answer each question on paper first, then open the answer.

**Q1.** Six items. How many non-overlap constraints are there, and how many pair binaries $x_{ij}, y_{ij}$? How many binaries in total with rotation?
<details><summary>Answer</summary>

$\binom{6}{2} = 15$ pairs, so $4 \times 15 = 60$ non-overlap constraints and $2 \times 15 = 30$ pair binaries. Rotation adds $r_1, \dots, r_6$: 36 binaries in total.
</details>

**Q2.** For tables 1 and 2 the solver chooses $x_{12} = 1$, $y_{12} = 0$. Which constraint must hold, and what does it say about the layout?
<details><summary>Answer</summary>

C2: $x_2 + w_2 \le x_1 + M(1 - 1 + 0) = x_1$. Table 2 lies completely to the left of table 1. The other three constraints get $+M$ or $+2M$ and are switched off.
</details>

**Q3.** The four tables cover $20 + 21 + 24 + 49 = 114$ square units. What lower bound does that give for the side $A^*$? Is the bound reached?
<details><summary>Answer</summary>

The square must have area at least 114, so $A^* \ge \sqrt{114} \approx 10.68$. The bound is not reached: the best square with rotation is 11 × 11 (area 121). Area gives a bound, but the shapes also have to fit together.
</details>

**Q4.** Table 3 is $(w, h) = (6, 4)$. Write its width and height with the rotation variable $r_3$, and check both values of $r_3$.
<details><summary>Answer</summary>

Width $= (1 - r_3)\cdot 6 + r_3 \cdot 4$ and height $= (1 - r_3)\cdot 4 + r_3 \cdot 6$. With $r_3 = 0$: 6 wide and 4 high. With $r_3 = 1$: 4 wide and 6 high.
</details>

**Q5.** In the connected model, why is it enough to write $R_{ij} \ge D^x_{ij}$ and $R_{ij} \ge -D^x_{ij}$ instead of $R_{ij} = |D^x_{ij}|$? When would this trick fail?
<details><summary>Answer</summary>

The two constraints mean $R_{ij} \ge |D^x_{ij}|$. Since $R_{ij}$ appears in the objective that is minimised, the solver makes it as small as allowed, which is exactly $|D^x_{ij}|$. The trick fails if you **maximise** the distance: then nothing stops $R_{ij}$ from growing beyond $|D^x_{ij}|$, and the model is unbounded.
</details>

**Q6.** In notebook 2, item 5 is left out ($u_5 = 0$). Why does the boundary constraint $x_5 + \text{width}_5 \le W + M(1 - u_5)$ not force item 5 onto the floor?
<details><summary>Answer</summary>

With $u_5 = 0$ the right-hand side is $W + M$, which is larger than any value the left-hand side needs, so the constraint is always satisfied. With $u_5 = 1$ it is the normal boundary constraint $\le W$.
</details>

**Q7.** Why can $M$ not be too small, and why is a huge $M$ (like 9999) not ideal either?
<details><summary>Answer</summary>

- **Too small:** a constraint that should be switched off still restricts the layout, so good layouts are wrongly forbidden.
- **Very large:** solvers work with limited precision. Answers can come out as `11.999999` instead of `12`, and the LP relaxation becomes weaker, which can slow the solve.

This is why notebooks 2–4 use the smallest value that is still safe: $W + H$ plus the longest item side. Notebook 1 keeps the original $M = 9999$, and on a desktop it may print `v= 11.999999` for that reason.
</details>

**Q8.** Using the numbers on slide 34, how many combinations of pair binaries are there for 7 items?
<details><summary>Answer</summary>

$2\binom{7}{2} = 42$ binaries, so $2^{42} \approx 4.4 \times 10^{12}$ combinations.
</details>

---

## 9. If something goes wrong

| What you see | What to do |
| --- | --- |
| `ModuleNotFoundError: No module named 'pyomo'` | Run the **first code cell** (the install cell) again. Installs last only for the open browser tab. |
| The first cell runs for a long time | The first run downloads Python and the packages. Give it a minute; if nothing happens, reload the page and run again. |
| Notebook 2 shows `[*]` for minutes | Expected: allow 2–4 minutes. Do not restart it. |
| `v= 11.999999` or positions like `4.999999` | Rounding caused by the large $M$; the answer is 12 (or that whole number). This happens mainly outside the browser. |
| `-0.0` or `-0` in the output | It is 0. |
| Your layout differs from the slides or from a friend's | Normal: many layouts are equally good. Compare the objective value, not the picture. |
| `r[ 5 ]= 0.0` in notebook 1 but item 5 looks "unrotated" | Item 5 is a 3 × 3 square, so rotating it changes nothing. |
| A cell fails with `NameError` | An earlier cell has not run. Choose *Run → Run All Cells*. |
| You changed a line in a *Try it* and want the original back | Copy the original line from [section 6](#6-the-four-notebooks). |
| Nothing works on the site | Use Chrome, Edge or Firefox. As a fallback the notebooks also run in Google Colab or Anaconda Jupyter (the install cell uses `pip` there). |

---

## 10. Words used this week

| Word | Meaning |
| --- | --- |
| **Floor planning / bin packing** | Placing rectangles in a region without overlap, with some goal (smallest region, most items, …) |
| **MILP** | Mixed-integer linear program: a linear program in which some variables must be integers (here: binaries) |
| **Binary variable** | A variable that can only be 0 or 1, used for yes/no decisions |
| **Big-M** | A large constant $M$ added to a constraint so that a binary variable can switch the constraint off |
| **Non-overlap constraints** | The four "left of / right of / below / above" constraints of each pair |
| **Minimax** | Minimising the largest of several values, here the furthest edge $x_i + w_i$ or $y_i + h_i$ |
| **Rotation variable $r_i$** | 1 if item $i$ is turned through 90° (width and height swapped), else 0 |
| **Placement variable $u_i$** | 1 if item $i$ is placed on the floor, 0 if left out (notebooks 2 and 3) |
| **Rectilinear distance** | Distance measured across plus up/down, like walking along city blocks: $\lvert \Delta x \rvert + \lvert \Delta y \rvert$ |
| **Relaxation** | The same model with binaries allowed to take any value between 0 and 1; the solver uses it to get bounds |
| **Optimal** | The solver has **proved** that no better solution exists |
| **NP-hard** | A class of problems for which no method is known that is fast for every large instance |
| **HiGHS** | The open-source solver the notebooks use (`SolverFactory('appsi_highs')`) |
| **GLPK** | The solver the original script `model.py` used; it cannot run in the browser |

---

## 11. Assumptions made in this README

- **A1 – Site address.** The address <https://ctsallis.github.io/operational_research/> is the default GitHub Pages address for this repository. The site's deployment workflow publishes to GitHub Pages, but the address itself was not confirmed in the repository files. If the course gives you a different link, use that one.
- **A2 – Notebook 4 numbers.** Notebook 4 passes the repository's automatic browser test, so it runs to the end. Its total distance for each floor was not recorded when this README was written. The README therefore gives checks you can make yourself instead of numbers.
- **A3 – Running times.** "About half a minute" (notebook 1, *Mums* puzzle) and "2–4 minutes" (notebook 2) come from the automatic browser test and the notebooks' own notes. Your browser and computer may be faster or slower.
- **A4 – Connections in notebook 4.** The five connected pairs were read from the diagram on slide 25. The code behind the pictures on slide 29 is not in the course files, so those pictures may use slightly different settings.
- **A5 – No tutorial.** This week has no tutorial sheet or answers in the course files. The practice questions here and in the notebooks replace them.
- **A6 – Background weeks.** Weeks 05 and 07 are suggested for revision from their titles (mixed-integer programming, job shop scheduling). This README does not describe their content.

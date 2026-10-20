# Week 03 – Linear Programming 2

This week you move from solving linear programmes (LPs) with SciPy's `linprog` to writing them in
**Pyomo**, a modelling language in which a model looks almost like the maths on paper. You will:

- write a large LP compactly with **summation notation** ($\sum_i c_i x_i$) and turn it into code;
- see what happens when an LP has **no optimum** (it is *unbounded*) and how to fix the model;
- meet **integer** programmes (ILP) and **mixed-integer** programmes (MILP), where some or all
  variables must be whole numbers, and see why rounding an LP answer is not enough.

This README is written so that you can do the whole week on your own. Read it from top to bottom
once, then follow **Section 5 (Step-by-step plan)** and tick the boxes as you go.

---

## Contents

1. What you should be able to do by the end
2. What you need before you start
3. How to open each kind of file
4. Every file in this folder
5. Step-by-step plan
6. The lecture, slide by slide
7. The demo notebooks
8. The tutorial, question by question
9. Answers to check against
10. Common mistakes
11. If something goes wrong
12. Key words
13. Test yourself
14. Checklist: have you finished?
15. Assumptions made in this README

---

## 1. What you should be able to do by the end

1. Write an LP with indexed variables and summation notation, and say in words what each symbol means.
2. Build and solve an LP in Pyomo: variables, objective, constraints, solver, and reading the output.
3. Recognise an **unbounded** LP from the solver's message, explain why it happened, and add
   constraints that fix it.
4. Explain the difference between LP, ILP and MILP, and why, for a maximisation problem,
   LP optimum ≥ MILP optimum ≥ ILP optimum.
5. Explain, with an example, why rounding an LP solution does not always give the best integer solution.
6. Model a constraint written as a percentage ("fat at most 45% of the weight") as a linear constraint.

---

## 2. What you need before you start

**Knowledge from Week 02.** This week reuses Week 02 material and assumes you can:

- draw the feasible region of a two-variable LP and find the best corner point;
- write an LP in matrix form ($\max\ c^T x$ subject to $Ax \le b$, $x \ge 0$);
- use SciPy's `linprog` (and remember that it only *minimises*).

Two Week 02 tutorial questions come back in this week's lecture: **Q5** (the manufacturing
problem with products X, Y and Z) and **Q6** (the diet problem with 10 foods). If you have not
done them, read them on the Week 02 tutorial sheet first.

**Software.**

- A recent **Chrome, Edge or Firefox** browser, to open the course site and run the notebooks.
  Nothing needs installing: Python runs inside the browser.
- **PowerPoint** for the slides (`.pptx`) and **Word** for the tutorial sheets (`.docx`).
- An internet connection the first time you run each notebook: its first cell downloads the
  Pyomo and HiGHS packages into the browser tab.
- *Optional:* MATLAB, only if you want to look at the MATLAB versions in `5 Source Files`.

**Before your first notebook,** open `00_START_HERE.ipynb` at the top of the course site and run
it (*Run → Run All Cells*). If every cell prints `OK`, this week's notebooks will run too.

---

## 3. How to open each kind of file

All files live on the course site: <https://ctsallis.github.io/operational_research/>. In the file
browser on the left, open `Lectures` → `Semester 1` → `Week 03 - Linear Programming 2`.

| File type | How to open it |
| --- | --- |
| Notebook (`.ipynb`) | Double-click it. It opens in the browser and runs there. |
| Slides (`.pptx`), tutorial sheet (`.docx`) | Right-click the file → **Download**, then open the downloaded file in PowerPoint or Word. The site cannot display them itself. |
| This README (`.md`) | Right-click → **Open With** → **Markdown Preview**. |
| Scripts in `5 Source Files` (`.py`, `.m`) | Double-click to read them in the browser. They are not meant to be run on the site (see Section 4). |

**Running a notebook.** Always run the **first code cell first**: it installs Pyomo and the HiGHS
solver into the tab. The first time this takes about a minute; wait until the cell's `[*]` turns
into a number. Then use **Run → Run All Cells**, or click into each cell and press
**Shift + Enter** to run it and move to the next one.

**Saving your work.** Anything you change or create on the site is stored **only in this browser**.
Clearing browser data, using a private window or changing computer loses it. To keep a notebook:
right-click it in the file browser → **Download**.

**Experimenting safely.** Before changing a demo notebook, make a copy (right-click → **Duplicate**)
and work in the copy, so the original stays as it was.

**Slide numbers.** Slide numbers in this README are the numbers PowerPoint shows in the slide list
on the left. Slide 3 is a hidden blank slide: you will see it faded in the list, and it is skipped
when you play the slideshow. It has no content; ignore it.

---

## 4. Every file in this folder

| Folder | File | What it is | Do you need it? |
| --- | --- | --- | --- |
| `1 Lecture` | `Week 3 - Linear Programming 2.pptx` | The lecture slides (27 slides). | **Yes** |
| `1 Lecture` | `Simplex Method 2 Variable Graphical Demo.pptx` | 12 slides that step through the simplex method on a small LP, one corner point at a time. The lecture's *Contents* slide calls this the *Simplex Method Demonstration*. The same file is in Week 02. | Recommended |
| `2 Lecture Demos` | `1 LP with Pyomo.ipynb` | Week 02's lecture LP rewritten in Pyomo. | **Yes** |
| `2 Lecture Demos` | `2 Diet problem 6a - minimise cost.ipynb` | Diet problem: cheapest diet. | **Yes** |
| `2 Lecture Demos` | `3 Diet problem 6b - unbounded.ipynb` | Diet problem: most attractive diet, which turns out to be unbounded. | **Yes** |
| `2 Lecture Demos` | `4 Diet problem 6c - the fix.ipynb` | Diet problem with upper and lower limits, which fixes the unboundedness. | **Yes** |
| `2 Lecture Demos` | `5 Integer LP.ipynb` | A two-variable integer programme (ILP). | **Yes** |
| `2 Lecture Demos` | `6 Mixed-integer LP.ipynb` | The same problem with only one integer variable (MILP). | **Yes** |
| `3 Tutorial` | `Week 3 - Linear Programming 2 - Tutorial.docx` | The tutorial sheet: Q1 (LP, ILP, MILP) and Q2 (Icki-Toffee candies). | **Yes** |
| `4 Tutorial Answers` | `Week 3 - Linear Programming 2 - Tutorial - Answers.docx` | The answer sheet: the formulation for Q2a and the solver output for each question. | After you try the tutorial |
| `4 Tutorial Answers` | `Q1 LP, ILP and MILP.ipynb` | Worked answer to Q1, with a plot of the feasible region. | After you try Q1 |
| `4 Tutorial Answers` | `Q2b Icki-Toffee - minimise cost.ipynb` | Worked answer to Q2b. | After you try Q2b |
| `4 Tutorial Answers` | `Q2c Icki-Toffee - maximise popularity.ipynb` | Worked answer to Q2c, including the weight of the selection. | After you try Q2c |
| `5 Source Files/Python` | `linprog_pyomo.py`, `Week2_question_5a/5b/5c_pyomo.py`, `intlinprog_pyomo.py`, `milp_pyomo.py`, `week3_icki_toffee_q2b.py`, `week3_icki_toffee_q2c.py` | The original scripts that the notebooks were made from. Despite the `5a/5b/5c` in their names, the three diet scripts are demos 2–4 (Week 02 Q6). They use the GLPK solver, which does not work in the browser. | No |
| `5 Source Files/Python/Old Q1 (previous tutorial version)` | `week3_q1a_…py`, `week3_q1b_…py` | Answers to an **older** version of Q1 (a different LP). Do not compare your Q1 with these. | No |
| `5 Source Files/MATLAB` | `week3_icki_toffee_q2b.m`, `week3_icki_toffee_q2c.m` | MATLAB versions of the Q2b and Q2c answers. | No (only if you use MATLAB) |
| `5 Source Files/MATLAB/Old Q1 (previous tutorial version)` | `week3_q1a_…m`, `week3_q1b_…m` | MATLAB answers to the **older** Q1. | No |

> **Why do the diet notebooks say 6a, 6b, 6c?** The diet problem is **Q6** on the Week 02 tutorial
> sheet, parts (a), (b) and (c). The slides and notebooks use that numbering. The script names in
> `5 Source Files` still use an older numbering (5a/5b/5c); they are the same problems.

---

## 5. Step-by-step plan

Work through these in order. Each step says what to open and what you should have at the end.

**Part A: the lecture**

- [ ] **A1.** Download and open `1 Lecture/Week 3 - Linear Programming 2.pptx`. Read slides 1–7
  (review of Week 02: the LP *maximise* $5x + 7y$, its matrix form, and solving it in Python).
- [ ] **A2.** Download and open `1 Lecture/Simplex Method 2 Variable Graphical Demo.pptx` and
  click through all 12 slides. *You should be able to say:* the simplex method starts at a corner,
  moves to the neighbouring corner with the best objective value, and stops when no neighbour is
  better (here at C = (4, 1.5), P = 26).
- [ ] **A3.** Run demo `1 LP with Pyomo` (it goes with slide 7). *Result:* $x = 41.14$, $y = 10.29$, $P = 277.71$.
- [ ] **A4.** Read slides 8–12 (diet problem: from a table to summation notation), then run demo
  `2 Diet problem 6a`. *Result:* minimum cost **93.25**.
- [ ] **A5.** Read slides 13–14, then run demo `3 Diet problem 6b`. *Result:* `Termination condition: unbounded`.
- [ ] **A6.** Read slides 15–16, then run demo `4 Diet problem 6c`. *Result:* attractiveness **149.66**.
- [ ] **A7.** Read slides 17–20 (manufacturing problem: why rounding is not enough). No notebook goes with these.
- [ ] **A8.** Read slides 21–24, then run demo `5 Integer LP`. *Result:* $x = 3$, $y = 2$, $P = 13$.
- [ ] **A9.** Read slides 25–26, then run demo `6 Mixed-integer LP`. *Result:* $x = 2$, $y = 2.833$, $P = 13.917$.
- [ ] **A10.** In each demo, do the *What do you notice?* or *Try it* cell at the end **before** you
  open its hidden answer.

**Part B: the tutorial**

- [ ] **B1.** Download and open `3 Tutorial/Week 3 - Linear Programming 2 - Tutorial.docx`.
- [ ] **B2.** Do **Q1** in your own notebook (Section 8 shows how to start one), then check it with Section 9.
- [ ] **B3.** Do **Q2a** on paper (the formulation).
- [ ] **B4.** Do **Q2b** and **Q2c** in your own notebook.
- [ ] **B5.** Write a few sentences for **Q2d** (there is no single right answer; see Section 8).

**Part C: check and consolidate**

- [ ] **C1.** Compare with `4 Tutorial Answers` (the Word answer sheet and the three notebooks) and Section 9.
- [ ] **C2.** Answer the questions in Section 13 without looking, then check.
- [ ] **C3.** Go through the checklist in Section 14.
- [ ] **C4.** Download any notebook you wrote, so you don't lose it.

---

## 6. The lecture, slide by slide

| Slides | Topic | What to take from it |
| --- | --- | --- |
| 1–2 | Title and contents | — |
| 3 | Hidden blank slide | Ignore. |
| 4–5 | Review: an LP and its canonical (matrix) form | maximise $P = 5x + 7y$ subject to $3x + 2y \le 144$, $x \ge 4y$, $x, y \ge 0$. To fit $Ax \le b$, the constraint $x \ge 4y$ is rewritten as $-x + 4y \le 0$. |
| 6 | Solution with Python (`linprog`) | `linprog` minimises, so to maximise $5x + 7y$ you give it $c = [-5, -7]$ and change the sign of the answer back. |
| 7 | Solution with Pyomo | The same model in Pyomo; you can write `sense=maximize` directly. → demo 1 |
| 8–11 | Diet problem (Week 2 Tutorial Q6a) | From the data table to one constraint per nutrient, written out in full and then in summation notation. Read the symbol list on slide 11 carefully. |
| 12 | 6a solution via Pyomo | The summation model in code. → demo 2 |
| 13–14 | Diet problem (Week 2 Tutorial Q6b) | Same constraints, but *maximise* attractiveness: **unbounded**. → demo 3 |
| 15–16 | Fix, and 6c solution via Pyomo | Add a maximum to every vitamin and a minimum to fat (maximum = minimum + 20%). → demo 4 |
| 17 | Introduction to MILP | Section heading. |
| 18–20 | Manufacturing problem (Week 2 Q5c, adapted: profit of X is £11.5 here) | LP answer $(x, y, z) = (8.89, 0, 20)$, $P = 262.22$. Rounding up, (9, 0, 20), needs 100.5 hours: infeasible. Rounding down, (8, 0, 20), gives £252. But (8, 2, 20) gives £262. **Rounding does not necessarily give the best integer solution.** |
| 21 | Desmos demonstration | maximise $P = 2x + 3.5y$ subject to $3x + 2y \le 14$, $2x + 3y \le 12.5$, $-x + y \le 1$, $x, y \ge 0$. LP optimum $(1.9, 2.9)$, $P = 13.95$. |
| 22–23 | Rounded solutions | The integer points next to $(1.9, 2.9)$ are either infeasible or poor ($P = 9$ or $11$). The best integer point, $(3, 2)$ with $P = 13$, is somewhere else. |
| 24 | Integer solution via Pyomo | $x, y \in \mathbb{Z}$ (whole numbers). → demo 5 |
| 25–26 | Mixed-integer program | Only $x \in \mathbb{Z}$: optimum $(2, 2.833)$, $P = 13.917$. → demo 6 |
| 27 | Demos | Where the notebooks are on the course site. |

**Reading summation notation (slides 11–16).** $x_i$ is the number of units of food $i$, and
$v^A_i$ is the amount of vitamin A in one unit of food $i$. So $\sum_i v^A_i x_i$ means
"for every food, multiply the amount of vitamin A in one unit by the number of units, then add up
over all foods", which is the total vitamin A in the diet. $\sum_i v^A_i x_i \ge 100$ says this total must be at
least 100. "$x_i \ge 0,\ \forall i$" means "$x_i \ge 0$ for every food $i$".

**Note on the code pictures in the slides.** Slides 7, 24 and 26 show code that uses the GLPK solver
(`SolverFactory('glpk')`). The notebooks use **HiGHS** (`SolverFactory('appsi_highs')`) instead,
because GLPK cannot run in a browser. The models and the answers are the same.

---

## 7. The demo notebooks

All six are in `2 Lecture Demos`. Each one starts with the problem, how to run it and the expected
result, explains every code cell above it, and ends with a question whose answer is hidden under
*Answer* (click to open it).

| Notebook | Slides | The problem | Expected result |
| --- | --- | --- | --- |
| `1 LP with Pyomo` | 7 | max $5x + 7y$; $3x + 2y \le 144$, $x \ge 4y$ | $x = 41.14$, $y = 10.29$, $P = 277.71$ (both constraints binding) |
| `2 Diet problem 6a - minimise cost` | 8–12 | min cost, vitamin minimums, fat ≤ 300 | cost **93.25**: food 2 = 9.09, food 5 = 1.43, food 10 = 2.27 units |
| `3 Diet problem 6b - unbounded` | 13–14 | max attractiveness, same constraints | `Termination condition: unbounded` (no optimum) |
| `4 Diet problem 6c - the fix` | 15–16 | max attractiveness, min and max limits | attractiveness **149.66**, using foods 1, 6, 7, 8 and 10 |
| `5 Integer LP` | 21–24 | max $2x + 3.5y$, $x, y$ whole numbers | $x = 3$, $y = 2$, $P = 13$ |
| `6 Mixed-integer LP` | 25–26 | same, only $x$ a whole number | $x = 2$, $y = 2.833$, $P = 13.917$ |

**Index numbers.** Python counts from 0, so in demos 2–4 `x[0]` is food 1 and `x[9]` is food 10.

**Reading Pyomo's output.** `model.display()` prints:

- **Variables:** the *Value* column is the solution.
- **Objectives:** the optimal objective value.
- **Constraints:** *Body* is the left-hand side at the solution, shown next to its *Lower* and
  *Upper* bounds. If *Body* equals a bound, that constraint is **binding** (it has no spare).

Values such as `120.00000000000001`, `-3.55e-14` or `49.99999999999984` are tiny rounding errors
in the computer's arithmetic. Read them as 120, 0 and 50.

**Solver log.** In the browser, HiGHS prints its log (lines such as `Running HiGHS …`, `Presolving
model`) whether `tee` is `True` or `False`. This is normal; the answer is printed after it.

---

## 8. The tutorial, question by question

Open the tutorial sheet in Word next to this README. Questions marked `*` are medium and `**` are
hard. The sheet also links to an external Pyomo example (*Notebook (jckantor.github.io)*), which
you can use as extra reading.

### Starting your own notebook

1. On the course site, open the `3 Tutorial` folder in the file browser (so your notebook is saved there).
2. **File → New → Notebook**. If asked to choose a kernel, choose **Python (Pyodide)**.
3. Open any demo notebook, click in its **first code cell** (it starts `# Run this cell first.`),
   copy the whole cell (Ctrl + A inside the cell, then Ctrl + C; on a Mac, Cmd instead of Ctrl) and paste it into the first cell of
   your notebook. Run it. This installs Pyomo and HiGHS and makes Pyomo work in the browser.
4. In the next cell, type `from pyomo.environ import *` and build your model as in the demos.
5. Rename your notebook (right-click it → **Rename**) and download it when you finish.

### Q1 – LP, ILP and MILP

maximise $12x + 18y$ subject to $2x + 4y \le 55$, $2x + y \le 25$, $x, y \ge 0$.

- **Q1:** solve the LP with Pyomo. Start from demo `1 LP with Pyomo` and change the numbers.
- **Q1a:** $x$ and $y$ integers (ILP). Use `domain=NonNegativeIntegers`, as in demo 5.
- **Q1b** `*`: $x$ real, $y$ integer (MILP). Give each variable its own domain, as in demo 6.
- **Check graphically**, as the sheet suggests. Draw both lines: $2x + 4y = 55$ meets the axes at
  $(27.5, 0)$ and $(0, 13.75)$, and $2x + y = 25$ at $(12.5, 0)$ and $(0, 25)$. Work out the objective at each
  corner of the feasible region. You can draw it by hand or with an online graphing tool such as
  Desmos (<https://www.desmos.com/calculator>), as on slide 21.

*Hint:* for a maximisation problem, adding "must be a whole number" can only keep the optimum the
same or make it lower. So expect ILP ≤ MILP ≤ LP.

### Q2 – Icki-Toffee candies

Choose how many of each of 12 candies to put in a selection. The selection must weigh **at least
320 g**, have **at most 2850 calories**, and its fat must be **at most 45% of its weight**.
Tables 1 and 2 on the sheet give each candy's fat, calories, weight, cost and popularity.

**Q2a** `*` – Formulate the model with summation notation, minimising cost. Let $x_i$ be the number
of candy $i$; $F_i$, $K_i$, $W_i$, $C_i$ are its fat, calories, weight and cost.

- Write the objective, then one constraint for each requirement.
- The tricky one is fat. "Total fat at most 45% of total weight" is
  $\sum_i F_i x_i \le 0.45 \sum_i W_i x_i$. It is still **linear**: you can move everything to one
  side, $\sum_i (F_i - 0.45\,W_i)\,x_i \le 0$.
- You cannot sell part of a candy, so $x_i$ must be a non-negative **whole number**.

**Q2b** `**` – Solve Q2a with Pyomo. To save typing, these lists hold the data from Tables 1 and 2,
in the sheet's order (index 0 = Buttery butterscotch, …, index 11 = Grape bunch). A `-` in the table
is 0.

```python
fat    = [20, 16, 10, 7, 6, 5, 13, 15, 18, 0, 19, 0]              # F_i, grams
cals   = [100, 100, 80, 50, 60, 40, 80, 90, 80, 145, 120, 120]  # K_i
weight = [24, 22, 15, 12, 10, 10, 14, 17, 20, 8, 20, 15]        # W_i, grams
cost   = [12, 12, 12, 15, 13, 13, 16, 16, 15, 10, 18, 20]       # C_i
pop    = [10, 10, 8, 9, 5, 6, 7, 8, 10, 3, 8, 4]                # P_i, popularity
```

Check the lists against the sheet before you rely on them. Use `domain=NonNegativeIntegers` and
`sense=minimize`.

**Q2c** `**` – Keep the constraints, but maximise total popularity $\sum_i P_i x_i$. Then work out the
**weight** of the selection: $\sum_i W_i x_i$ for your answer. You can also read it as the *Body* of
the weight constraint in `model.display()`.

**Q2d** – Are these good selections? Would you be happy? The sheet leaves this for you to think
about; there is no official answer. Questions to guide you:

- In Q2b, which candies are chosen, and how popular are they (Table 2)?
- In Q2c, how many candies are in the box, and are they the most popular ones?
- Is "total popularity" (popularity × number of candies, added up) really what a customer would
  call a popular selection? What happens to it if you simply add more cheap candies?

The hidden answers at the end of the Q2b and Q2c answer notebooks discuss this, and Week 04's
tutorial Q1 looks at better objectives for the same problem.

---

## 9. Answers to check against

Try each question first. These are the results of the answer notebooks in `4 Tutorial Answers`.

| Question | Answer |
| --- | --- |
| Q1 (LP) | $x = 7.5$, $y = 10$, objective **270** |
| Q1a (ILP) | $x = 7$, $y = 10$, objective **264** |
| Q1b (MILP) | $x = 7.5$, $y = 10$, objective **270** (the LP answer already has a whole-number $y$, so nothing changes) |
| Q2a | minimise $\sum_i C_i x_i$ subject to $\sum_i W_i x_i \ge 320$, $\sum_i K_i x_i \le 2850$, $\sum_i F_i x_i \le 0.45 \sum_i W_i x_i$, $x_i \ge 0$ and $x_i \in \mathbb{Z}$ for every $i$ |
| Q2b | minimum cost **268**. **More than one selection** achieves it, e.g. 9 Caramel softie + 10 Rose-water posy + 3 Grape bunch (answer sheet) or 9 Caramel softie + 8 Rose-water posy + 4 Grape bunch (the answer notebook). Any selection that costs 268 and meets all three constraints is correct. |
| Q2c | maximum popularity **365**: 5 Coconut Ice + 50 Lime sherbet + 5 Grape bunch. Weight $5 \times 12 + 50 \times 10 + 5 \times 15 =$ **635 g**. |
| Q2d | No single answer (see Section 8). |

**If your Q2b answer differs from both selections above,** check it yourself: work out its cost,
weight, calories and fat by hand. If the cost is 268 and all three constraints hold, you are right.

---

## 10. Common mistakes

| Mistake | What happens | Fix |
| --- | --- | --- |
| Skipping the first code cell | `ModuleNotFoundError: No module named 'pyomo'`, or errors when printing the model | Run the first cell (Section 3), wait for it to finish, then run the rest. |
| Forgetting `sense=maximize` | Pyomo minimises by default, so a maximisation problem returns 0 or a wrong answer | Write `sense=maximize` in the `Objective`. |
| Giving `linprog` the objective without minus signs | `linprog` minimises, so you get the smallest value, not the largest | Pass $-c$ and change the sign of the result back (slide 6). |
| Writing `<` or `>` in a Pyomo constraint | Pyomo stops with an error: strict inequalities are not allowed | Use `<=` or `>=`. |
| Using `NonNegativeReals` for an integer question | You get fractions such as 7.5 when whole numbers were asked for | Use `NonNegativeIntegers` for the variables that must be whole numbers. |
| Mixing up food (or candy) numbers | Data shifted by one place | Python counts from 0: `x[0]` is item 1 in the table. |
| Treating `-` in a table as missing | Lists of different lengths, or the wrong numbers | `-` means 0; every list needs one entry per food or candy. |
| Comparing your Q1 with the scripts in `Old Q1 (previous tutorial version)` | Different numbers (e.g. 212.5) | Those scripts solve an older version of Q1. Use Section 9. |
| Expecting the exact Q2b mix from the answer sheet | A different selection appears | Q2b has several optimal selections; compare the **cost**. |
| Rounding an LP answer to get an integer answer | Infeasible or worse than the best | Solve the integer problem itself (slides 18–23). |
| Reading `-3.55e-14` or `49.99999999999984` as real values | Confusion about tiny fractions | These are rounding errors: 0 and 50. |

---

## 11. If something goes wrong

| Problem | What to do |
| --- | --- |
| The first cell runs for a long time | The first run downloads Python and the packages. Wait a minute. If nothing happens after that, reload the page and run the first cell again. |
| `ModuleNotFoundError` | Run the first code cell again. Packages installed in one tab do not carry over to another tab or to a reloaded page. |
| The kernel dies, or "table index is out of bounds" | You used SciPy's `linprog`/`milp` **and** Pyomo with HiGHS in the same notebook. The browser cannot load both. Use separate notebooks, or reload the page and run only one of them. |
| You changed a demo and want the original back | If you made a copy first (Section 3), close it and open the original. |
| A `.pptx` or `.docx` file shows nothing on the site | This is expected: download it and open it in PowerPoint or Word. |
| The solver says `unbounded` | Your model lets the objective grow forever. Check for a missing constraint or a `>=` that should be `<=` (as in demo 3). |
| The solver says `infeasible` | No point satisfies every constraint. Check each constraint's direction (`<=` or `>=`) and right-hand side against the question. |
| You lost a notebook | Work kept only in the browser is lost if browser data is cleared. Download notebooks before you leave (Section 3). |
| The site does not work in your browser | Use a recent Chrome, Edge or Firefox. |

---

## 12. Key words

| Word | Meaning |
| --- | --- |
| **Pyomo** | A Python package for writing optimisation models in a form close to the maths. |
| **HiGHS** | The open-source solver that finds the answer to the model (`SolverFactory('appsi_highs')`). |
| **Decision variable** | A quantity you choose, e.g. $x_i$, the number of units of food $i$. |
| **Summation notation** | $\sum_i a_i x_i$ means $a_1 x_1 + a_2 x_2 + \dots$, added over all $i$. |
| **Binding constraint** | A constraint that holds with equality at the optimum: it has no spare. |
| **Unbounded** | The objective can be improved forever without breaking any constraint, so there is no optimum. |
| **Infeasible** | No point satisfies all the constraints. |
| **ILP (integer linear programme)** | An LP in which every variable must be a whole number. |
| **MILP (mixed-integer linear programme)** | An LP in which some variables must be whole numbers and the others need not be. |
| **$\mathbb{Z}$** | The set of whole numbers (integers); $x \in \mathbb{Z}$ means "$x$ is a whole number". |
| **Branch and bound** | The method HiGHS uses for integer variables: it solves LPs and splits the problem on fractional values. |
| **Simplex method** | The method that moves from corner to corner of the feasible region, always to a better one, until none is better. |

---

## 13. Test yourself

Answer each question before you open its answer.

**1.** `linprog` minimises. How do you use it to maximise $5x + 7y$?

<details><summary>Answer</summary>

Minimise $-5x - 7y$, i.e. pass `c = [-5, -7]`. The maximum is minus the minimum that `linprog` reports.
</details>

**2.** In the diet problem, why is minimising cost fine but maximising attractiveness unbounded,
with exactly the same constraints?

<details><summary>Answer</summary>

When minimising, buying food costs money, so the solver buys as little as possible, and the vitamin
minimums stop it going to zero. When maximising, nothing stops it buying more: the vitamin
constraints are only minimums, and the fat limit does not involve the fat-free foods. So the
attractiveness can grow forever. Adding maximum vitamin limits fixes this.
</details>

**3.** Put these in order from largest to smallest for a maximisation problem: the ILP optimum,
the LP optimum and the MILP optimum. Why?

<details><summary>Answer</summary>

LP ≥ MILP ≥ ILP. Each step adds a restriction (some variables, then all variables, must be whole
numbers), and adding a restriction can never improve the optimum. In demos 5 and 6:
13.95 ≥ 13.917 ≥ 13.
</details>

**4.** The LP optimum of the manufacturing problem is $(8.89, 0, 20)$. Why not simply round to $(9, 0, 20)$?

<details><summary>Answer</summary>

$(9, 0, 20)$ needs $4.5 \times 9 + 3 \times 20 = 100.5$ hours, more than the 100 available: it is
infeasible. Rounding down to $(8, 0, 20)$ is feasible but earns £252, less than the £262 of
$(8, 2, 20)$.
</details>

**5.** Write "total fat at most 45% of total weight" as a linear constraint.

<details><summary>Answer</summary>

$\sum_i F_i x_i \le 0.45 \sum_i W_i x_i$, or equivalently $\sum_i (F_i - 0.45\,W_i)\,x_i \le 0$.
</details>

**6.** In `model.display()`, a constraint shows *Lower* 120, *Body* 120.00000000000001 and no
*Upper*. What does that tell you?

<details><summary>Answer</summary>

The left-hand side equals its lower bound (the extra digits are rounding), so the constraint is
binding: it is one of the constraints that decide the optimum.
</details>

**7.** In the simplex demo, the method moves A → B → C and then stops. Why does it stop at C?

<details><summary>Answer</summary>

Both neighbours of C, B (P = 25) and D (P = 23.5), have a lower objective value than C (P = 26).
No neighbouring corner is better, so C is optimal.
</details>

---

## 14. Checklist: have you finished?

- [ ] I have read all the lecture slides and clicked through the simplex demo.
- [ ] I have run all six demo notebooks and got the expected results in Section 7.
- [ ] I have answered every *What do you notice?* / *Try it* question before opening its answer.
- [ ] I have solved Q1, Q1a and Q1b in Pyomo and checked them graphically.
- [ ] I have written the Q2a model in summation notation, including the 45% fat constraint.
- [ ] I have solved Q2b (cost 268) and Q2c (popularity 365, weight 635 g) in Pyomo.
- [ ] I have written my own answer to Q2d.
- [ ] I can answer every question in Section 13 without looking.
- [ ] I have downloaded the notebooks I wrote.

---

## 15. Assumptions made in this README

- **Time.** The README does not say how long the week takes; no time estimate is given in the material.
- **Order.** The plan in Section 5 assumes you read the lecture before the tutorial and run each demo
  right after its slides, as slide 27 and the notebooks' slide references suggest.
- **When to open the answers.** The answer notebooks say "Release after the practical". For a student
  working alone, this README assumes that means "after you have tried the questions yourself".
- **Software.** It assumes you can open `.pptx` and `.docx` files in PowerPoint and Word, and that the
  course site works in your browser as described in `00_START_HERE.ipynb`.
- **Site menus.** The menu names (*File → New → Notebook*, *Duplicate*, *Download*, *Open With →
  Markdown Preview*, the *Python (Pyodide)* kernel) are those of the JupyterLite version the site uses at
  the time of writing; they may change slightly in a later version.
- **Q2d.** There is no official answer to Q2d in the material. The guiding questions in Section 8
  are prompts, not a model answer.
- **External links.** The jckantor.github.io Pyomo example (linked from the tutorial sheet) and Desmos
  are outside the course; they are optional and may change.
- **MATLAB.** The `.m` files are not needed this week; this README does not explain how to run them.

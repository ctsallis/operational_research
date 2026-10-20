# Week 02 – Linear Programming 1

This week you learn to **write a decision problem as a linear programme (LP)**, solve a two-variable LP
**by drawing it**, put it in **matrix (canonical) form**, and solve it **on a computer** with Python's
`linprog` and with Excel Solver.

This page tells you everything you need to work through the week on your own: what each file is, how to
open it, the order to use them in, and how to check your answers.

---

## Contents

1. [What you will be able to do](#1-what-you-will-be-able-to-do)
2. [What you need before you start](#2-what-you-need-before-you-start)
3. [The files in this folder](#3-the-files-in-this-folder)
4. [How to open each kind of file](#4-how-to-open-each-kind-of-file)
5. [Step-by-step plan for the week](#5-step-by-step-plan-for-the-week)
6. [The tutorial, question by question](#6-the-tutorial-question-by-question)
7. [Check your answers](#7-check-your-answers)
8. [Common mistakes](#8-common-mistakes)
9. [If something goes wrong](#9-if-something-goes-wrong)
10. [Key words](#10-key-words)
11. [Test yourself](#11-test-yourself)
12. [Checklist: have you finished the week?](#12-checklist-have-you-finished-the-week)
13. [Assumptions made in this README](#13-assumptions-made-in-this-readme)

---

## 1. What you will be able to do

By the end of the week you should be able to:

- turn a short word problem into an LP: **decision variables**, an **objective** to maximise or minimise,
  and **constraints**, including non-negativity;
- draw the **feasible region** of a two-variable LP and find the optimum by checking its **vertices**
  (corners);
- recognise a **binding** constraint, an **infeasible** LP, an **unbounded** LP and an LP with
  **infinitely many** optimal solutions;
- write an LP in **canonical form**: maximise **c**ᵀ**x** subject to **Ax** ≤ **b**, **x** ≥ **0**;
- solve an LP with SciPy's `linprog` in Python, remembering that `linprog` **minimises**;
- solve the same LP with Excel Solver;
- explain the idea of the **simplex method**: move from vertex to neighbouring vertex while the
  objective improves.

---

## 2. What you need before you start

| You need | Why | Notes |
| --- | --- | --- |
| A computer with a recent **Chrome, Edge or Firefox** | Runs the course site, where the Python notebooks work | Nothing to install. Safari works but is slow. |
| **Microsoft PowerPoint** | Opens the slides (`.pptx`) | Download the file first (section 4). |
| **Microsoft Word** | Opens the tutorial sheet and the written answers (`.docx`) | Download the file first. |
| **Desktop Microsoft Excel with the Solver add-in** | Tutorial Question 4 and the Excel demo | How to switch Solver on: section 4. |
| Paper, pencil and a ruler (or graph paper) | Tutorial Question 1 is solved by drawing | |
| Week 01 | Basic vectors and matrices (matrix × vector) | Used for the canonical form. |

You do **not** need to know any Python beyond what Week 01 used. Every notebook explains each step.

---

## 3. The files in this folder

The folder is `Lectures/Semester 1/Week 02 - Linear Programming 1/`.

### `1 Lecture/`: the slides

| File | What it is |
| --- | --- |
| [Week 2 - Linear Programming 1.pptx](1%20Lecture/Week%202%20-%20Linear%20Programming%201.pptx) | **Main lecture, 27 slides.** Everything you need for the tutorial. |
| [Simplex Method 2 Variable Graphical Demo.pptx](1%20Lecture/Simplex%20Method%202%20Variable%20Graphical%20Demo.pptx) | **12 slides.** A step-by-step picture of how the simplex method walks from corner to corner. Use **Slide Show** mode: the slides build up one step at a time. |

What the main lecture covers, slide by slide:

| Slides | Topic |
| --- | --- |
| 3–9 | The **introductory example**: a factory makes products X and Y on one machine. X takes 3 hours and earns £5; Y takes 2 hours and earns £7; there are 144 hours a week. Constraints, feasible region, objective, and why the best point is a vertex. |
| 10 | Observations: the optimum was at a vertex. |
| 11–13 | **Is the answer sensible?** X and Y are chairs and tables, so a new constraint is added: x ≥ 4y (at least 4 chairs for each table). |
| 14–15 | **Binding constraints**: constraints that hold with equality at the optimum. |
| 16 | **Infeasible** LP: no point satisfies all the constraints. |
| 17 | **Unbounded** LP: the objective can grow for ever. |
| 18 | **Infinitely many solutions**: the objective is parallel to a constraint. |
| 19 | **Optimality**: an optimum, if it exists, is always found at a vertex (a *basic feasible solution*). |
| 20 | The same idea with 3 variables (a cube). |
| 21–23 | **Canonical form** with matrices: **c**, **x**, **A**, **b**. |
| 24 | Maximising **c**ᵀ**x** gives the same best point as minimising −**c**ᵀ**x**. |
| 25–26 | Solving the example with Python's `linprog`. |
| 27 | What the tutorial asks you to do. |

> **Watch the letters A and B.** On slides 5–8, A = (48, 0) and B = (0, 72). From slide 12 onwards, after
> the chairs-and-tables constraint is added, B is a **different** point: (41.14, 10.29). Always read
> the coordinates next to the letter.

Slide 7 links to an **interactive Desmos graph** of the example
(<https://www.desmos.com/calculator/qlrpn3qn0i>). Move the profit line and watch where it leaves the
feasible region.

### `2 Lecture Demos/`: the lecture example on a computer

| File | What it is | Expected result |
| --- | --- | --- |
| [1 LP with SciPy linprog.ipynb](2%20Lecture%20Demos/1%20LP%20with%20SciPy%20linprog.ipynb) | The chairs-and-tables LP solved in Python. Ends with "What do you notice?" and "Try it" exercises with hidden answers. | `x[1] = 41.14`, `x[2] = 10.29`, `fval = -277.71`, so the profit is **£277.71** |
| [2 LP with Excel Solver.xlsx](2%20Lecture%20Demos/2%20LP%20with%20Excel%20Solver.xlsx) | The same LP set up for Excel Solver. Cell A12 says how to run it. | X = 41.14, Y = 10.29, total in F10 = **277.71** |

### `3 Tutorial/`: the questions

| File | What it is |
| --- | --- |
| [Week 2 - Linear Programming - Tutorial.docx](3%20Tutorial/Week%202%20-%20Linear%20Programming%20-%20Tutorial.docx) | **Tutorial sheet, 6 questions (2 pages).** One star (\*) marks a medium question, two stars (\*\*) a hard one. |

### `4 Tutorial Answers/`: the answers (open these **after** you have tried)

| File | Answers question |
| --- | --- |
| [Week 2 - Linear Programming - Tutorial Answers.docx](4%20Tutorial%20Answers/Week%202%20-%20Linear%20Programming%20-%20Tutorial%20Answers.docx) | **All questions**, written out with the models and the solver output. |
| [Q3 LP with linprog.ipynb](4%20Tutorial%20Answers/Q3%20LP%20with%20linprog.ipynb) | Q3 |
| [Q4 LP with Excel Solver.xlsx](4%20Tutorial%20Answers/Q4%20LP%20with%20Excel%20Solver.xlsx) | Q4 |
| [Q5a Manufacturing - products X and Y.ipynb](4%20Tutorial%20Answers/Q5a%20Manufacturing%20-%20products%20X%20and%20Y.ipynb) | Q5a |
| [Q5b Manufacturing - add product Z.ipynb](4%20Tutorial%20Answers/Q5b%20Manufacturing%20-%20add%20product%20Z.ipynb) | Q5b |
| [Q5c Manufacturing - faster X.ipynb](4%20Tutorial%20Answers/Q5c%20Manufacturing%20-%20faster%20X.ipynb) | Q5c |
| [Q6 Diet problem - parts a, b and c.ipynb](4%20Tutorial%20Answers/Q6%20Diet%20problem%20-%20parts%20a,%20b%20and%20c.ipynb) | Q6a, Q6b and Q6c |

The screenshots in the answers `.docx` show the output of the original solution: `x` as a column and
4 decimal places. The notebooks print **the same numbers** as `x[1] = …`, `fval = …`, rounded to
2 decimal places.

### `5 Source Files/Python/`: you do not need these

These are the original Python scripts that the notebooks were made from. They are kept for reference
only. Their names follow an **older numbering** of the tutorial sheet:

| Script | Is now |
| --- | --- |
| `linprog_lecture_eg.py` | Lecture demo 1 |
| `Question_3.py` | Q3 |
| `Question_4a.py`, `Question_4b.py`, `Question_4c.py` | Q5a, Q5b, Q5c |
| `Question_5.py` | Q6 |

---

## 4. How to open each kind of file

### Notebooks (`.ipynb`): run in your browser

1. Go to the course site: <https://ctsallis.github.io/operational_research/lab/index.html>.
   The first visit takes a minute while Python loads.
2. **Once per session**, open `00_START_HERE.ipynb` (top of the file list) and choose
   **Run → Run All Cells**. If every cell prints `OK`, the course examples will run.
3. In the file list on the left, double-click `Lectures`, then `Semester 1`, then
   `Week 02 - Linear Programming 1`, then the folder you need.
4. Double-click a notebook to open it.
5. Run it with **Run → Run All Cells**, or click a cell and press **Shift + Enter** to run one cell at a
   time while you read. Nothing to install: SciPy is already built into the browser's Python.
6. Answers to "What do you notice?" and "Try it" are hidden. Click the **▸ Answer** line to show them.

**Your changes are saved only in this browser.** Clearing browser data, using a private window or
changing computer loses them. Before you leave, right-click the notebook in the file list →
**Download**.

**To write your own notebook** (Q3, Q5 and Q6): in the week's folder choose **File → New → Notebook**,
and pick the **Python (Pyodide)** kernel if asked. Or right-click
`2 Lecture Demos/1 LP with SciPy linprog.ipynb` → **Duplicate**, and edit the copy.

### Slides, Word and Excel files (`.pptx`, `.docx`, `.xlsx`): download, then open

These do **not** open inside the course site. Download them first, either way:

- **On the course site:** right-click the file in the file list → **Download**.
- **On GitHub:** click the file name in the tables above, then the **Download raw file** button (↓) at
  the top right of the file view.

Then open the `.pptx` in PowerPoint, the `.docx` in Word and the `.xlsx` in Excel. If Office shows a
yellow **Protected View** bar, click **Enable Editing**. Excel needs this before Solver will run.

### Switching on Excel Solver (once per computer)

- **Windows:** **File → Options → Add-ins**. At the bottom, *Manage: Excel Add-ins* → **Go…** →
  tick **Solver Add-in** → **OK**.
- **Mac:** **Tools → Excel Add-ins…** → tick **Solver Add-in** → **OK**.

**Solver** now appears at the right-hand end of the **Data** tab.

---

## 5. Step-by-step plan for the week

Work in this order. Each step says what you should see before you move on.

| Step | Do this | You are ready to move on when… |
| --- | --- | --- |
| 1 | Read the **main lecture slides 1–10**. Open the Desmos link on slide 7 and move the profit line. | You can explain why the best profit (£504 at x = 0, y = 72) is at a corner. |
| 2 | Read **slides 11–18**. | You can name and sketch each case: binding, infeasible, unbounded, infinitely many solutions. |
| 3 | Read **slides 19–24**. | You can write the chairs-and-tables LP as **c**, **A**, **b**. |
| 4 | Read **slides 25–26**, then run **`2 Lecture Demos/1 LP with SciPy linprog.ipynb`**. Do its "What do you notice?" and "Try it" parts before opening the answers. | You get `fval = -277.71` and understand why it is negative. |
| 5 | Open **`2 Lecture Demos/2 LP with Excel Solver.xlsx`**. Follow the note in cell A12 and run Solver. | F10 shows 277.71. |
| 6 | Go through the **Simplex demo** slides in Slide Show mode. | You can say which corner the method visits next, and why it stops at C. |
| 7 | Do the **tutorial**, Q1 to Q6 (section 6). Try each question **before** looking at its answer. | Your answers match section 7. |
| 8 | Do **Test yourself** (section 11) and the **checklist** (section 12). | Every box ticked. |

Question 6 is hard on purpose. The tutorial sheet says you are **not expected** to finish it yet; the
Week 03 lecture starts by discussing it. Try it, then study the answer carefully.

---

## 6. The tutorial, question by question

Open the tutorial sheet (`3 Tutorial/…Tutorial.docx`) alongside this section.

### Q1: Solve graphically
Maximise 5x + 17y subject to 2x + 3y ≤ 60, x + y ≤ 25, x, y ≥ 0.

1. Draw both constraints as lines. A quick way is to find where each line crosses the axes: put x = 0,
   then y = 0.
2. Shade the region that satisfies **all** the constraints. That is the feasible region.
3. List its corners. Find each one by solving the two equations of the lines that meet there.
4. Work out 5x + 17y at every corner. The largest value is the optimum (lecture slides 8 and 19).

### Q2: Matrix form
Write Q1 as maximise **c**ᵀ**x** subject to **Ax** ≤ **b**, **x** ≥ **0**. Write down **c**, **x**,
**A** and **b** (lecture slides 21–23). There is one row of **A** per constraint, and one column per
variable.

### Q3: Python
Solve Q1 with `linprog` in a new notebook (section 4). Start from the lecture demo notebook and change
`c`, `A_ub` and `b_ub`. Remember that `linprog` **minimises**, so use `c = [-5, -17]`.

### Q4: Excel
Solve Q1 with Excel Solver. Copy the layout of the lecture workbook: two cells for x and y, one cell for
the objective, and one formula cell for the left-hand side of each constraint. Then in Solver:

- **Set Objective:** the objective cell; select **Max**.
- **By Changing Variable Cells:** the x and y cells.
- **Subject to the Constraints:** **Add** each constraint as *left-hand side cell* `<=` *right-hand side
  cell*.
- Tick **Make Unconstrained Variables Non-Negative**.
- **Select a Solving Method:** **Simplex LP**. Then click **Solve**, and **OK** to keep the solution.

### Q5 (\*): Manufacturing
Write the model on paper first: variables, objective, constraints. Then solve it with `linprog`.

- **a)** Two products, X and Y, on machine A (100 hours a week). X takes 5 hours and earns £12; Y takes
  2 hours and earns £5.
- **b)** Add product Z: 3 hours, £8 profit, and at most 20 a week. You now have 3 variables, so every
  row of `A_ub` has 3 numbers. The limit "at most 20 of Z" is a row of its own: `[0, 0, 1]` with
  right-hand side 20.
- **c)** As b), but X now takes 4.5 hours. Look at the answer: can a factory make 22.22 products? What
  happens if you round it?

**Hint:** compare the profit **per machine hour** of each product (profit ÷ hours).

### Q6 (\*\*): Diet problem
Ten foods; Table 1 gives the nutrient limits and Table 2 the content, cost and attractiveness of one
unit of each food. Let xᵢ = the number of units of food i (i = 1, …, 10).

- **a)** Minimise the cost. "At least" (≥) constraints must be turned into ≤ for `linprog`: multiply
  both sides by −1. A "–" in Table 2 means 0.
- **b)** Maximise the attractiveness, with the same constraints. Read `linprog`'s message carefully:
  what kind of LP is this?
- **c)** Give every nutrient both a minimum and a maximum, where maximum = minimum + 20%:
  - vitamins: between the minimum and 1.2 × the minimum;
  - fat: the table gives only the **maximum** (300), so the minimum is 300 ÷ 1.2 = **250**.

  Each nutrient now needs **two** rows in `A_ub`. Solve with both objectives (attractiveness and cost).

---

## 7. Check your answers

Compare with these only after you have tried. The full working is in the answers `.docx` and the answer
notebooks.

| Q | Answer |
| --- | --- |
| 1 | Corners and values: (0, 0) → 0; (25, 0) → 125; (15, 10) → 245; (0, 20) → **340**. Optimum **x = 0, y = 20, value 340**. |
| 2 | **c** = (5, 17), **A** = [[2, 3], [1, 1]], **b** = (60, 25), **x** = (x, y) ≥ **0**. |
| 3 | `x[1] = 0.00`, `x[2] = 20.00`, `fval = -340.00` (that is, a maximum of 340). |
| 4 | Solver gives x = 0, y = 20, objective 340, the same as Q1–Q3. |
| 5a | x = 0, y = 50, profit **£250** (`fval = -250.00`). Y earns £2.50 per hour, X only £2.40. |
| 5b | x = 0, y = 20, z = 20, profit **£260** (`fval = -260.00`). |
| 5c | x = 22.22, y = 0, z = 0, profit **£266.67** (`fval = -266.67`). You cannot make 0.22 of a product. Rounding down to x = 22 earns only £264, but x = 20, y = 2, z = 2 uses exactly 100 hours and earns **£266**. X and Z now both earn £8/3 per hour, so other plans also reach £266.67 (e.g. z = 20, x = 8.89), and a solver may report any of them. Week 03 shows how to ask for whole numbers directly. |
| 6a | Minimum cost **93.25** with x₂ = 9.09, x₅ = 1.43, x₁₀ = 2.27, all other foods 0. |
| 6b | **Unbounded.** Foods with no fat (1, 2, 4, 5, 9, 10) can be increased without limit, so the attractiveness grows for ever. |
| 6c | Maximum attractiveness **149.66** (`fval = -149.66`), with x₁ = 0.19, x₆ = 7.63, x₇ = 0.86, x₈ = 5.93, x₁₀ = 7.16. With the cost objective under the same limits, the minimum cost rises from 93.25 to **136.52**. |

Your numbers may differ in the last decimal place. Other solvers (or Excel) may print a **different
optimal point with the same objective value** when there are several optima (as in 5c). That is still
correct.

---

## 8. Common mistakes

| Mistake | Fix |
| --- | --- |
| Forgetting that `linprog` **minimises** | To maximise, negate every entry of `c`; the printed `fval` is then **minus** the maximum. |
| Typing a ≥ constraint directly into `A_ub` | `A_ub` only takes ≤ rows. Multiply the whole row and its right-hand side by −1: x ≥ 4y becomes −x + 4y ≤ 0. |
| Adding rows for x ≥ 0, y ≥ 0 | Not needed: `linprog` assumes every variable is ≥ 0 unless told otherwise. |
| Writing `A_ub = [5, 2]` for a single constraint | `A_ub` is a list of rows, even with one row: `[[5, 2]]`, with `b_ub = [100]`. |
| Rows of `A_ub` and entries of `b_ub` out of step | Row k of `A_ub` goes with entry k of `b_ub`. Check you have the same number of each. |
| Treating "–" in the diet table as missing | It means 0. Every row of `A_ub` must have 10 numbers. |
| Q6c fat minimum as 300 × 0.8 = 240 | Maximum = minimum + 20%, so minimum = 300 ÷ 1.2 = 250. |
| Excel Solver gives a non-linear or odd answer | Choose **Simplex LP**, and tick **Make Unconstrained Variables Non-Negative**. |
| Reading a rounded LP answer as the best whole-number plan | Rounding can lose profit (Q5c). Integer programming (Week 03 onwards) handles this properly. |

---

## 9. If something goes wrong

| Problem | What to do |
| --- | --- |
| The site keeps loading, or the kernel stays busy | The first run downloads Python. Wait a minute; if nothing happens, reload the page. Use Chrome, Edge or Firefox. |
| `ModuleNotFoundError` | Run `00_START_HERE.ipynb` again (**Run → Run All Cells**). Installs only last for the open tab. |
| My edited notebook has disappeared | Edits live only in that browser. Always **Download** your work before leaving (section 4). |
| A `.pptx`, `.docx` or `.xlsx` does not open on the site | That is expected: download it and open it in PowerPoint, Word or Excel (section 4). |
| No **Solver** button in Excel | Switch the add-in on (section 4). Click **Enable Editing** if the file opened in Protected View. |
| The kernel dies with "table index is out of bounds" | You used SciPy's `linprog` **and** Pyomo in the same notebook. Keep them in separate notebooks. (This week only uses `linprog`.) |
| `linprog` says *The problem is infeasible* or *unbounded* | That may be the right answer (as in Q6b). If you didn't expect it, check the signs of your ≥ rows and the `c` signs. |
| Nothing else works | Every notebook also runs in Google Colab or Anaconda Jupyter. |

---

## 10. Key words

| Term | Meaning |
| --- | --- |
| Decision variables | The quantities you choose, e.g. x = number of chairs, y = number of tables. |
| Objective function | What you maximise or minimise, e.g. profit P = 5x + 7y. |
| Constraint | A limit the variables must satisfy, e.g. 3x + 2y ≤ 144 machine hours. |
| Non-negativity | x ≥ 0, y ≥ 0: you cannot make a negative amount. |
| Feasible region | All points that satisfy every constraint. |
| Vertex / basic feasible solution (BFS) | A corner of the feasible region, where boundary lines meet. If an LP has an optimum, one is always at a vertex. |
| Binding constraint | A constraint that holds with **equality** at the optimum (its slack is 0). |
| Slack | How much of a ≤ constraint is unused: right-hand side minus left-hand side. |
| Infeasible | No point satisfies all the constraints together. |
| Unbounded | The objective can be improved for ever. |
| Canonical form | Maximise **c**ᵀ**x** subject to **Ax** ≤ **b**, **x** ≥ **0**. With m constraints and n variables, **A** is m × n. |
| Simplex method | Starts at a vertex and moves to a neighbouring vertex with a better objective, until no neighbour is better. |

---

## 11. Test yourself

Try each one, then click to check.

<details><summary>1. Why is the optimum of an LP always at a vertex, if an optimum exists?</summary>

The objective is a straight line (a plane in higher dimensions) that you slide across the feasible
region. The last point it touches before leaving is a corner. If the line is parallel to an edge, it
touches a whole edge, and that edge's end points are still corners (slides 18–19).
</details>

<details><summary>2. In the chairs-and-tables LP, which constraints are binding at the optimum (41.14, 10.29)?</summary>

Both: 3(41.14) + 2(10.29) = 144, and x = 4y (41.14 ≈ 4 × 10.29). Slide 15.
</details>

<details><summary>3. Write x ≥ 60 as a row for <code>linprog</code>'s <code>A_ub</code> in an LP with variables (x, y).</summary>

−x ≤ −60, so the row is `[-1, 0]` and the right-hand side is `-60`.
</details>

<details><summary>4. <code>linprog</code> prints <code>fval = -504.00</code> for a maximisation. What is the maximum?</summary>

504. You passed the negated objective, so the minimum of −P is −504, and the maximum of P is 504.
</details>

<details><summary>5. For an LP with 3 constraints and 2 variables, what are the sizes of c, A and b?</summary>

**c** has 2 entries, **A** is 3 × 2, **b** has 3 entries (slide 23: m = 3, n = 2).
</details>

<details><summary>6. In the simplex demo, why does the method stop at C?</summary>

C = (4, 1.5) has P = 26. Its neighbours are B (P = 25) and D (P = 23.5). Neither is better, so C is
optimal.
</details>

---

## 12. Checklist: have you finished the week?

- [ ] I have read all 27 lecture slides and gone through the simplex demo.
- [ ] I ran the lecture demo notebook and got `fval = -277.71`.
- [ ] I ran the Excel demo with Solver and got 277.71.
- [ ] Q1: I drew the feasible region and found the optimum (0, 20), value 340.
- [ ] Q2: I wrote **c**, **A** and **b**.
- [ ] Q3: my own notebook gives `fval = -340.00`.
- [ ] Q4: my own spreadsheet gives 340.
- [ ] Q5a–c: I wrote each model, solved it, and can explain why 5c's answer cannot be used as it is.
- [ ] Q6: I tried it and then studied the answer notebook, including why 6b is unbounded.
- [ ] I can answer all six questions in section 11 without looking.
- [ ] I downloaded any notebook I edited.

**Next week (Week 03 – Linear Programming 2)** starts from Q6 and writes LPs in a friendlier way
(Pyomo). It also introduces whole-number (integer) variables, which fix the problem you saw in Q5c.

---

## 13. Assumptions made in this README

These points are not stated in the course files; this README assumes them. Tell your lecturer if any
are wrong for you.

1. **Course site address:** <https://ctsallis.github.io/operational_research/lab/index.html> (the
   repository's GitHub Pages site).
2. **Software:** you have desktop Microsoft PowerPoint, Word and Excel, and you may install Excel's
   Solver add-in. Excel for the web and other spreadsheet programs are not covered.
3. **Office menus:** the Solver and Protected View steps match current Microsoft 365 for Windows and
   Mac; older versions may name the menus slightly differently.
4. **Links:** the file links in section 3 and the Contents links at the top work when this page is
   viewed on GitHub. On the course site, if a link does not work, scroll to the section, or open the
   file from the file list on the left.
5. **Hidden answers:** the "▸" lines in section 11 and in the notebooks expand when clicked, both on
   GitHub and in the site's Markdown Preview.
6. **No deadline or marks** are attached to this week's tutorial; no hand-in is mentioned in the course
   files.
7. **Time needed** is not given in the course files, so this README does not estimate it.
8. **Next week:** the description of Week 03 is taken from that week's folder (its notebooks use Pyomo,
   the diet problem and integer LPs).

# Semester 1 · Week 1 – Introduction to Operational Research

This page is your guide to Week 1. It tells you what to do, in what order, how to open and run
each file, what results you should get, and what to do if something goes wrong. You can complete
the whole week on your own using only this page and the files in this folder.

**This week you will:**

1. find out what Operational Research (OR) is, where it is used and what this module covers;
2. revise the maths the rest of the module is built on: linear equations, systems of equations,
   matrices, determinants, linear inequalities and feasible regions;
3. learn to do this maths in Python with NumPy, and to draw it with Matplotlib and Desmos.

**What you need:** a computer with a recent version of Chrome, Edge or Firefox, PowerPoint (for the
slides), and pen and paper. You do not need to install Python.

---

## Contents

1. [The files in this folder](#1-the-files-in-this-folder)
2. [Before you start: how the course site works](#2-before-you-start-how-the-course-site-works)
3. [Step 1 – The lecture slides](#3-step-1--the-lecture-slides)
4. [Step 2 – The NumPy notebook](#4-step-2--the-numpy-notebook)
5. [Step 3 – The tutorial](#5-step-3--the-tutorial)
6. [Step 4 – Check your answers](#6-step-4--check-your-answers)
7. [The maths of this week on one page](#7-the-maths-of-this-week-on-one-page)
8. [If something goes wrong](#8-if-something-goes-wrong)
9. [Glossary](#9-glossary)
10. [Checklist](#10-checklist)

---

## 1. The files in this folder

Work through them in this order. Ignore `5 Source Files` (see the last row).

| Step | Folder | File | What it is |
| --- | --- | --- | --- |
| 1 | `1 Lecture` | `Week 1 - Introduction to Operations Research.pptx` | The lecture slides (31 slides). Open in PowerPoint. |
| 2 | `2 Lecture Demos` | `1 Vectors and matrices in NumPy.ipynb` | A short notebook that teaches vectors, matrices, determinants and solving equations in Python. |
| 3 | `3 Tutorial` | `Week 1 Tutorial - Introduction to OR.ipynb` | This week's exercises (Exercises 1–8). |
| 4 | `4 Tutorial Answers` | `Week 1 Tutorial - Answers.ipynb` | Worked answers to Exercises 1–8. Open it only **after** you have tried the exercises. |
| – | `5 Source Files` | `Week 1 - Tutorial.docx` | An older version of the tutorial written for MATLAB. **You do not need it.** The notebook in `3 Tutorial` replaces it. |

The module handbook is in the course's `Handbook` folder (go up three levels from this folder):
`Handbook/Module Handbook Operational Research (5CM522) 2526.pdf`.

---

## 2. Before you start: how the course site works

The course runs on a website that runs Python **inside your web browser** (it is a *JupyterLite*
site). Nothing is installed on your computer and your code is not sent anywhere.

### Open the site and find this week

1. Go to **<https://ctsallis.github.io/operational_research/>**.
2. The left-hand panel is the **file browser**. Double-click the folders
   `Lectures` → `Semester 1` → `Week 01 - Introduction to Operational Research`.
3. To read a `README.md` (like this one) on the site: right-click it → **Open With** →
   **Markdown Preview**.

The first time the site starts Python it downloads it into your browser. This can take a minute.
Wait until the notebook stops showing "busy" before you run anything.

### Run a notebook

- **Open** a notebook: double-click the `.ipynb` file. If the site asks you to choose a kernel,
  choose the Python (Pyodide) one.
- **Run one cell:** click inside it and press **Shift+Enter**. The output appears under the cell
  and the cursor moves to the next cell.
- **Run everything from the top:** menu **Run → Run All Cells**.
- **Start again from a clean state:** menu **Kernel → Restart Kernel and Run All Cells…**.
- **Always run cells from top to bottom.** A cell can use something made in an earlier cell
  (for example `np`, created by `import numpy as np`). If you skip that earlier cell, you get an
  error such as `NameError: name 'np' is not defined`.
- **Read the maths in a text cell:** text cells use LaTeX for formulas. Double-click a text cell to
  see the LaTeX; press Shift+Enter to show it formatted again.

### Save your work (important)

Notebooks you edit on the site are stored **only in this browser on this computer**. Clearing your
browser data, using a private window or moving to another computer loses them.

- Before you change a notebook, make your own copy: right-click it in the file browser →
  **Duplicate**. Work in the copy, so the original stays clean.
- Before you leave, download your copy: right-click it in the file browser → **Download**.

### Download the slides

The slides are a PowerPoint file, so they do not open on the site. In the file browser, open
`1 Lecture`, right-click `Week 1 - Introduction to Operations Research.pptx` → **Download**, then
open the downloaded file in PowerPoint.

---

## 3. Step 1 – The lecture slides

**File:** `1 Lecture/Week 1 - Introduction to Operations Research.pptx` (open in PowerPoint).

The slides have two parts. Slides 1–14 explain what OR is. Slides 15–31 revise the maths you need
for the rest of the module; read these carefully, because the tutorial uses them.

| Slides | Topic | What to do |
| --- | --- | --- |
| 1–3 | Title, module handbook, reading and software | Read the module handbook (see [Section 1](#1-the-files-in-this-folder)). Slide 3 says the module uses the Python libraries Pyomo and SimPy, and Excel. |
| 4–5 | What is OR? The OR Society | Watch the video on slide 4 (it plays in PowerPoint when you are online; it is also at <https://www.youtube.com/watch?v=0oMVVx81kCs>). Visit <https://www.theorsociety.com/about-or/>. |
| 6–9 | Why OR is useful, fields and applications | Read. Slide 9 links to real case studies. |
| 10 | **Task:** a business case study | See *Task A* below. |
| 11–12 | What this module will do for you; careers | Read. |
| 13 | **Task:** your interests and career | See *Task B* below. |
| 14 | History of OR | Watch the video (also at <https://www.youtube.com/watch?v=ILWbaWrjgU4>). |
| 15–17 | Linear equations in 1, 2, 3 and *n* dimensions | Point, line, plane, hyperplane. |
| 18 | Solving a system of two equations by substitution | Follow every line of the working with pen and paper. Answer: $(x, y) = (1, 2)$. |
| 19–20 | Row picture and column picture of the same system | Two ways to "see" the solution $(1, 2)$. |
| 21 | Matrix form, the inverse of a 2 × 2 matrix, the determinant | **Learn the two formulas on this slide.** You need them in Exercises 1 and 3. |
| 22–25 | When there is no solution, or infinitely many | Parallel lines (determinant 0), underdetermined and overdetermined systems, and a summary on slide 25. |
| 26 | Systems in 3 dimensions | Watch the video at <https://www.youtube.com/watch?v=WAzUwzV1F3g>. It shows how three planes can meet in one point, a line, or not at all. |
| 27–28 | Linear inequalities and half-spaces | One inequality cuts space in two. |
| 29 | A system of inequalities and its **feasible region** | Exercise 6 asks you to draw one of these. |
| 30 | Writing a system of inequalities in matrix form $A\mathbf{x} \le \mathbf{b}$ | You will use this form in almost every later week. |
| 31 | Polygon, polyhedron, polytope; convexity | Read. |

**Task A (slide 10).** Open the OR Society's business case studies,
<https://www.theorsociety.com/ORS/About-OR/Business-case-studies.aspx>, and pick one case. Write
short answers: What is the problem? Who are the stakeholders? What are the constraints (resources,
time, budget, …)? What are the objectives or performance measures (cost, time, quality, customer
satisfaction, …)? What methods were used? What outcomes were achieved (cost savings, time
reductions, service improvement, …)? In class this is done in pairs and reported to the class;
working alone, write your answers down in a few lines each.

**Task B (slide 13).** Answer the six questions on slide 13 for yourself (what interests you, what
career, which industries, which skills, what impact, what excites you most). There are no right
answers; write a few lines.

The maths from slides 15–31 is summarised in [Section 7](#7-the-maths-of-this-week-on-one-page).

---

## 4. Step 2 – The NumPy notebook

**File:** `2 Lecture Demos/1 Vectors and matrices in NumPy.ipynb`

**Why:** the tutorial asks you to finish this notebook first. It shows every Python command the
tutorial needs.

**How:** open it and run every cell from top to bottom with Shift+Enter. Read the text above each
cell before you run it. Nothing needs to be installed.

**What you should see** (in order):

| Section | Result you should get |
| --- | --- |
| Scalar, element-wise and dot product of $\mathbf{a} = (1,2,3)$ and $\mathbf{b} = (4,5,6)$ | `[ 5 10 15]`, `[ 4 10 18]`, `32` |
| A word on dimensions | `(3,)` for a plain array, `(3, 1)` for a true column vector |
| Matrix multiplication $M\mathbf{a}$ | `[14 32]` (or the same numbers as a column) for `np.matmul`, `np.dot` and `@` |
| Dimension error | Two `ValueError` messages are printed. **This is intended:** a 3 × 2 matrix cannot multiply a vector of length 3. |
| Inverse of the matrix `[[1, 2], [3, 4]]` | `[[-2.   1. ]` / `[ 1.5 -0.5]]` |
| Inverse of the singular matrix `[[1, 2], [3, 6]]` | On the site: a matrix of `nan` ("not a number"). In other Python installations: `LinAlgError: Singular matrix`. Both mean the same thing: **this matrix has no inverse.** |
| Its determinant | `0.0` |
| Solving $x + 2y = 1$, $3x + 4y = 3$ | `[1. 0.]`, i.e. $x = 1$, $y = 0$ |

The notebook also has a **"Try it"** cell: change the singular matrix to
$\begin{pmatrix}1&2\\3&5\end{pmatrix}$ and run the inverse and determinant cells again. The answer
is in the same cell, under the question.

**The commands you will reuse in the tutorial:**

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])      # a matrix: a list of rows
b = np.array([1, 3])        # the right-hand side

np.linalg.det(A)            # determinant of A
np.linalg.inv(A)            # inverse of A (only if the determinant is not 0)
np.dot(np.linalg.inv(A), b) # solution of A x = b, using the inverse
np.linalg.solve(A, b)       # the same solution, computed without the inverse
```

---

## 5. Step 3 – The tutorial

**File:** `3 Tutorial/Week 1 Tutorial - Introduction to OR.ipynb`

**Before you start:**

1. Make your own copy (right-click → **Duplicate**) and open the copy.
2. **Run the first cell once.** It contains `%pip install ipywidgets`, which installs the slider used
   in Exercise 8. You need to run it again each time you reopen the notebook or restart the kernel.
3. Open <https://www.desmos.com/calculator> in another browser tab for Exercises 5 and 6.
4. Have pen and paper ready for Exercises 1, 3 a–b and 6.

The notebook already contains some plots. These are pictures of the **example** systems in the
starter code, not the answers to the exercises.

### Exercise 1 – Determinants by hand (pen and paper)

Find the determinants of
$\begin{pmatrix}1&2\\3&4\end{pmatrix}$,
$\begin{pmatrix}1&-2\\3&4\end{pmatrix}$ and
$\begin{pmatrix}2&6\\4&12\end{pmatrix}$, then say what each one tells you about a system of
equations with that matrix.

**How:** for $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ the determinant is $ad - bc$ (slide 21). Watch
the signs: $b$ is $-2$ in the second matrix. Then use the rule from slides 21–25:

- determinant **not 0** → the matrix has an inverse and the system has **exactly one** solution;
- determinant **0** → the matrix is **singular** (no inverse) and the system has either **no**
  solution or **infinitely many**.

### Exercise 2 – Determinants in Python

Check your three answers to Exercise 1 in the code cell. Type each matrix with `np.array([[…], […]])`
and print `np.linalg.det(...)` for each.

**Tip:** the computer may print `-2.0000000000000004` instead of `-2`. This is a normal rounding
error. Use `round(np.linalg.det(A), 10)` to hide it.

### Exercise 3 – Solve $3x + y = 11$, $x + 4y = 11$

- **a) By hand.** Use substitution, as on slide 18: rearrange one equation for one unknown,
  substitute it into the other equation, solve, then substitute back.
- **b) In matrix form.** Write the system as $A\mathbf{x} = \mathbf{b}$. Find
  $A^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ and multiply:
  $\mathbf{x} = A^{-1}\mathbf{b}$ (slide 21).
- **c) In Python.** Use `np.dot(np.linalg.inv(A), b)` or `np.linalg.solve(A, b)`.

All three methods must give the same answer. If they don't, look for a sign or arithmetic error in
your hand working.

### Exercise 4 – Plot the Exercise 3 solution in Python

The starter cell solves and plots the example system $x + 2y = 1$, $3x + 4y = 3$. It rewrites each
equation $a_{i1}x + a_{i2}y = b_i$ as $y = (b_i - a_{i1}x)/a_{i2}$, draws the two lines, and marks
the solution with a black dot.

**What to do:** change only the lines `A = np.array(...)` and `b = np.array(...)` to the Exercise 3
system, then run the cell. **Check:** the two lines must cross exactly at the black dot, and the dot
must be at your answer to Exercise 3.

### Exercise 5 – Plot the Exercise 3 solution on Desmos

In <https://www.desmos.com/calculator> type `3x+y=11` on the first line and `x+4y=11` on the
second. Click the point where the lines cross: Desmos shows its coordinates. They must match
Exercise 3.

### Exercise 6 – Draw a feasible region by hand, then check on Desmos

Draw the region where all of these hold: $x + y \le 2$, $x + 3y \le 3$, $x \ge 0$, $y \ge 0$.

**How (pen and paper):**

1. Draw each boundary line by turning $\le$ into $=$. A quick way: find where the line meets the
   axes. Put $x = 0$ to get the $y$-intercept, and $y = 0$ to get the $x$-intercept.
2. Decide which side of each line is allowed. Test the point $(0, 0)$: if it satisfies the
   inequality, shade the side containing $(0, 0)$; otherwise shade the other side.
3. $x \ge 0$ and $y \ge 0$ keep you in the top-right quarter (the first quadrant).
4. The **feasible region** is where all the shadings overlap (slide 29). Mark its corners. To find
   a corner where two lines cross, solve the two equations together (as in Exercise 3).

**Check on Desmos:** type `x+y<=2`, `x+3y<=3`, `x>=0` and `y>=0` on four lines. The area where all
four shadings overlap must match your drawing.

### Exercise 7 – A 3 × 3 system in Python

Solve $2x + 3y - 2z = 3$, $x - 2y + 4z = 0$, $2x - 3y + z = 1$.

**How:** each equation is one **row** of $A$ (its coefficients of $x$, $y$, $z$, in that order) and
one entry of $\mathbf{b}$ (its right-hand side). Write a missing term as `0` and a lone variable as
`1` or `-1`. Then solve exactly as in Exercise 3 c).

**Check your answer:** compute `A @ x`. It must give back `b` (up to tiny rounding errors).

### Exercise 8 – Draw the three planes of Exercise 7

The first starter cell solves and draws an **example** 3 × 3 system. It rewrites each equation as
$z = (b_i - a_{i1}x - a_{i2}y)/a_{i3}$ on a grid of points and draws the three planes.

**What to do:** change `A` and `b` to your Exercise 7 system and run the cell. The line
`ax.view_init(0, 0)` sets the viewing angle: the first number tilts the view up or down (elevation)
and the second turns it round (azimuth), both in degrees. Try other values, for example
`ax.view_init(20, 30)`.

The second cell is an **interactive** version: it shows two sliders, `elev` and `azim`, and the
black dot is the solution. Change `A` and `b` **inside the function** too, run the cell, then drag
the sliders. **Check:** the three planes meet at one point, the black dot.

If the sliders do not appear, run the first cell of the notebook (`%pip install ipywidgets`) again,
then run this cell again. If they still do not work, use the first cell and change the numbers in
`view_init` by hand instead; you see the same picture.

---

## 6. Step 4 – Check your answers

**File:** `4 Tutorial Answers/Week 1 Tutorial - Answers.ipynb`

Open it only after you have tried every exercise. Run it with **Run → Run All Cells**. It gives the
full working for Exercises 1–8, with plots for Exercises 4, 6 and 8, and one more question ("What do
you notice?") with its answer.

To check a single result quickly, open the matching box below.

<details>
<summary>Exercise 1 and 2 – the three determinants</summary>

$-2$, $10$ and $0$. The first two matrices have an inverse, so a system with either matrix has
exactly one solution. The third is singular (its second row is twice its first), so a system with
it has no solution or infinitely many.

</details>

<details>
<summary>Exercises 3, 4 and 5 – the 2 × 2 system</summary>

$(x, y) = (3, 2)$. The determinant is $3 \cdot 4 - 1 \cdot 1 = 11$, and
$\begin{pmatrix}x\\y\end{pmatrix} = \frac{1}{11}\begin{pmatrix}4&-1\\-1&3\end{pmatrix}\begin{pmatrix}11\\11\end{pmatrix} = \begin{pmatrix}3\\2\end{pmatrix}$.
In Exercise 4 the lines cross at $(3, 2)$, and Desmos labels the crossing point $(3, 2)$.

</details>

<details>
<summary>Exercise 6 – the feasible region</summary>

A four-sided region with corners $(0, 0)$, $(2, 0)$, $(1.5, 0.5)$ and $(0, 1)$. The line
$x + y = 2$ meets the axes at $(2, 0)$ and $(0, 2)$; the line $x + 3y = 3$ meets them at $(3, 0)$
and $(0, 1)$; the two lines cross at $(1.5, 0.5)$.

</details>

<details>
<summary>Exercises 7 and 8 – the 3 × 3 system</summary>

$A = \begin{pmatrix}2&3&-2\\1&-2&4\\2&-3&1\end{pmatrix}$, $\mathbf{b} = \begin{pmatrix}3\\0\\1\end{pmatrix}$,
$\det A = 39$.
Solution: $x = 38/39 \approx 0.974$, $y = 11/39 \approx 0.282$, $z = -4/39 \approx -0.103$.
In Exercise 8 the three planes meet at this point.

</details>

---

## 7. The maths of this week on one page

**Linear equations** (slides 16–17): $ax = b$ is a point on a line, $ax + by = c$ is a line in the
plane, $ax + by + cz = d$ is a plane in space, and $a_1x_1 + a_2x_2 + \dots + a_nx_n = b$ is a
**hyperplane** in $n$ dimensions.

**A system of equations** is several equations that must all hold at once. For
$3x + 2y = 7$, $2x + 4y = 10$ (slides 18–21):

- **row picture:** each equation is a line; the solution is where the lines cross, $(1, 2)$;
- **column picture:** $x\begin{pmatrix}3\\2\end{pmatrix} + y\begin{pmatrix}2\\4\end{pmatrix} = \begin{pmatrix}7\\10\end{pmatrix}$:
  the solution says how much of each column to add to reach the right-hand side;
- **matrix form:** $A\mathbf{x} = \mathbf{b}$ with
  $A = \begin{pmatrix}3&2\\2&4\end{pmatrix}$, $\mathbf{x} = \begin{pmatrix}x\\y\end{pmatrix}$,
  $\mathbf{b} = \begin{pmatrix}7\\10\end{pmatrix}$, so $\mathbf{x} = A^{-1}\mathbf{b}$.

**The 2 × 2 formulas** (slide 21): for $A = \begin{pmatrix}a&b\\c&d\end{pmatrix}$,

$$|A| = ad - bc, \qquad A^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}.$$

If $|A| = 0$ you would divide by zero: the matrix is **singular** and has no inverse (slide 22).

**How many solutions?** With $n$ unknowns and $m$ equations (slides 22–25):

| Case | Name | Solutions |
| --- | --- | --- |
| $m < n$ | underdetermined | infinitely many, but there may be none |
| $m = n$ | square | exactly one if $\det A \ne 0$; otherwise none or infinitely many |
| $m > n$ | overdetermined | usually none, but there can be one |

In 3 dimensions each equation is a plane; three planes can meet in one point, along a line, or
not at all (slide 26).

**Linear inequalities** (slides 27–28): $ax \le b$, $ax + by \le c$, $ax + by + cz \le d$. In
general $a_1x_1 + \dots + a_nx_n \le b$ (with not all $a_i$ zero) is a **closed half-space**:
everything on one side of a hyperplane, including the hyperplane itself.

**Systems of inequalities** (slides 29–30): the points that satisfy all the inequalities form the
**feasible region**. To write a system as $A\mathbf{x} \le \mathbf{b}$, turn every $\ge$ into
$\le$ by multiplying both sides by $-1$. For example, $x_1 \ge 0$ becomes $-x_1 \le 0$:

$$
\begin{aligned}
-x_1 + x_2 &\le 1\\
3x_1 + 2x_2 &\le 12\\
2x_1 + 3x_2 &\le 12\\
x_1 &\ge 0\\
x_2 &\ge 0
\end{aligned}
\quad\Longrightarrow\quad
\begin{pmatrix}-1&1\\3&2\\2&3\\-1&0\\0&-1\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}
\le
\begin{pmatrix}1\\12\\12\\0\\0\end{pmatrix}
$$

The half-spaces cut out a **polygon** in 2 dimensions, a **polyhedron** in 3 and a **polytope** in
$n$ dimensions; these shapes are **convex** (slide 31). You will meet $A\mathbf{x} \le \mathbf{b}$
and feasible regions again in Week 2 (Linear Programming 1).

---

## 8. If something goes wrong

| What you see | What it means | What to do |
| --- | --- | --- |
| The notebook says "busy" or nothing happens for a while | The site is downloading Python into your browser (first run only). | Wait about a minute. If nothing happens after that, reload the page. |
| `NameError: name 'np' is not defined` (or another name) | A cell was run before the cell that creates that name. | Menu **Kernel → Restart Kernel and Run All Cells…**, or run the cells from the top. |
| `ModuleNotFoundError: No module named 'ipywidgets'` | The install cell was not run in this session. | Run the tutorial's first cell (`%pip install ipywidgets`), then the cell again. |
| `ValueError: matmul: …` or `shapes (3,2) and (3,) not aligned` | The matrix and vector sizes don't fit: the number of **columns** of the matrix must equal the length of the vector. | Check that you typed every row of `A` with the same number of entries, and that `b` has one entry per row of `A`. In the NumPy notebook these two errors are intended. |
| A matrix full of `nan`, or `LinAlgError: Singular matrix` | The matrix has determinant 0, so it has no inverse. | In the NumPy notebook this is intended. In an exercise, check your matrix: one row may have been typed wrong. |
| Numbers like `2.22e-16`, `-0.` or `-2.0000000000000004` | Tiny rounding errors in the computer's arithmetic. `2.22e-16` means $2.22 \times 10^{-16}$, which is 0 for our purposes; `-0.` is also 0. | Round, for example `np.round(x, 10)`. |
| A plot shows lines that do not cross at the black dot | `A` and `b` do not describe the same system, or a coefficient is wrong. | Compare each row of `A` and each entry of `b` with the equations. |
| `divide by zero` warning or missing plane in Exercise 8 | The code divides by each equation's $z$-coefficient; it fails if one is 0. | Not a problem in Exercise 7 (its $z$-coefficients are $-2$, $4$ and $1$). |
| My changes disappeared | The site stores your work only in this browser. | Download your notebooks before you leave (right-click → **Download**). |
| The site does not work at all | — | Use a recent Chrome, Edge or Firefox. Every notebook also runs in Google Colab or Anaconda Jupyter (upload the downloaded `.ipynb`). |

---

## 9. Glossary

| Term | Meaning |
| --- | --- |
| Operational Research (OR) | Using mathematical models and methods to make better decisions (slides 4–9). |
| Linear equation | An equation like $a_1x_1 + \dots + a_nx_n = b$: unknowns appear only multiplied by numbers and added. |
| Hyperplane | The set of points satisfying one linear equation in $n$ dimensions (a line in 2-D, a plane in 3-D). |
| System of equations | Several equations that must all hold at the same time. |
| Matrix, vector | A rectangular table of numbers; a vector is a matrix with one column (or one row). |
| Determinant $\lvert A\rvert$ | A number computed from a square matrix; for 2 × 2 it is $ad - bc$. |
| Inverse $A^{-1}$ | The matrix with $A^{-1}A = I$, where $I$ is the identity matrix (1s on the diagonal, 0s elsewhere); it exists only if $\lvert A\rvert \ne 0$. |
| Singular matrix | A square matrix with determinant 0; it has no inverse. |
| Underdetermined / overdetermined | Fewer / more equations than unknowns. |
| Dot product | $\mathbf{a}\cdot\mathbf{b} = a_1b_1 + a_2b_2 + \dots$, one number. |
| Element-wise (Hadamard) product | $\mathbf{a}\circ\mathbf{b}$: multiply matching entries, giving a vector. |
| Linear inequality | Like a linear equation but with $\le$ or $\ge$. |
| Closed half-space | All points satisfying one linear inequality (one side of a hyperplane, including it). |
| Feasible region | The points that satisfy every inequality of a system. |
| Polygon / polyhedron / polytope | The shape cut out by half-spaces in 2 / 3 / $n$ dimensions. |
| Convex | A shape is convex if the straight segment between any two of its points stays inside it. |
| Notebook, cell, kernel | A notebook (`.ipynb`) is made of text cells and code cells; the kernel is the Python that runs the code. |
| NumPy, Matplotlib | Python libraries for arrays and matrices (NumPy) and for plots (Matplotlib). |
| Desmos | A free online graphing calculator: <https://www.desmos.com/calculator>. |

---

## 10. Checklist

You have finished Week 1 when you can tick every box.

- [ ] I read the module handbook and slides 1–31, and watched the three videos (slides 4, 14 and 26).
- [ ] I wrote my answers to Task A (a business case) and Task B (my interests and career).
- [ ] I ran the NumPy notebook from top to bottom and got the results in [Section 4](#4-step-2--the-numpy-notebook).
- [ ] Exercise 1: three determinants by hand, and what each one means for a system of equations.
- [ ] Exercise 2: the same determinants in Python.
- [ ] Exercise 3: the 2 × 2 system solved by hand, in matrix form and in Python, with the same answer.
- [ ] Exercises 4 and 5: the two lines cross at my answer, in Python and on Desmos.
- [ ] Exercise 6: the feasible region drawn by hand with its corners, and checked on Desmos.
- [ ] Exercise 7: the 3 × 3 system solved in Python, and `A @ x` gives back `b`.
- [ ] Exercise 8: the three planes meet at the black dot.
- [ ] I compared all my answers with `4 Tutorial Answers` and understand any differences.
- [ ] I downloaded my edited notebooks.
- [ ] Without notes, I can: compute a 2 × 2 determinant and inverse; say when a system has one, none
      or infinitely many solutions; draw a feasible region; and write a system of inequalities as
      $A\mathbf{x} \le \mathbf{b}$.

**Next week:** Week 2 – Linear Programming 1 (folder `Week 02 - Linear Programming 1`).

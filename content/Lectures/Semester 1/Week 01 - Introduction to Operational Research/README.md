# Semester 1 · Week 01 – Introduction to Operational Research

What OR is, where it is used, and a refresher on vectors, matrices and linear (in)equalities in Python.

| Folder | What is in it | When |
| --- | --- | --- |
| `1 Lecture` | Slides (PDF) and lecture notes | The lecture |
| `2 Lecture Demos` | Notebooks and spreadsheets shown in the lecture, numbered in teaching order | Run live in the lecture |
| `3 Tutorial` | Tutorial / practical sheet and any starter files | The practical |
| `4 Tutorial Answers` | Worked answers and answer notebooks | **Release after the practical** |
| `5 Source Files` | Editable originals (.pptx, .docx, .md), the scripts the notebooks came from, MATLAB, older versions, staff notes | Staff only |

## Before you start

- **Maths:** solving two equations in two unknowns (school algebra). Everything else is introduced this week.
- **Python:** none needed. The notebooks explain each step.
- **Set-up:** open the course site and run `00_START_HERE.ipynb` once (see `Lectures/Semester 1/README.md`, section 1).

## Work through this week in order

| Step | File | What it is for |
| --- | --- | --- |
| 1 | `1 Lecture/Week 1 - Introduction to Operations Research.pdf` | What OR is and where it is used (slides 1–14); the maths for the rest of the module: linear equations, systems of equations, inequalities and feasible regions (slides 15–30) |
| 2 | `2 Lecture Demos/1 Vectors and matrices in NumPy.ipynb` | Run every cell: vectors, matrix products, inverse, determinant and solving $Ax = b$ in NumPy. **Do this before the tutorial.** |
| 3 | `3 Tutorial/Week 1 Tutorial - Introduction to OR.ipynb` | Exercises 1–8: determinants and systems by hand and in Python, plots of the solutions, a feasible region. Exercises 5 and 6 also use [desmos.com](https://www.desmos.com/calculator). Keep the step 2 notebook open for reference. |
| 4 | `4 Tutorial Answers/Week 1 Tutorial - Answers.ipynb` | Worked answers to Exercises 1–8. Check your work after you have tried them. |

The `(PDF version)` files are printable copies of the notebooks, for reading offline (printed Oct 2026 from
the current notebooks with their saved outputs). Run the `.ipynb` files to see every result.

## By the end of this week you can

- explain what Operational Research is and name some places it is used;
- solve a system of two linear equations by substitution and with the matrix inverse;
- calculate a 2 × 2 determinant and say what a zero determinant (a singular matrix) means;
- recognise systems with one solution, no solution and infinitely many solutions (parallel lines,
  more variables than equations, more equations than variables);
- use NumPy to multiply matrices, find inverses and determinants, and solve $Ax = b$;
- write a system of linear inequalities in matrix form $Ax \le b$ and sketch its feasible region.

**Next:** Week 02 (Linear Programming 1) uses the matrix form and the feasible region from this week.

## 1 Lecture

- `Week 1 - Introduction to Operations Research.pdf`

## 2 Lecture Demos

- `1 Vectors and matrices in NumPy (PDF version).pdf`
- `1 Vectors and matrices in NumPy.ipynb` (notebook)

## 3 Tutorial

- `Week 1 Tutorial - Introduction to OR (PDF version).pdf`
- `Week 1 Tutorial - Introduction to OR.ipynb` (notebook)

## 4 Tutorial Answers

- `Week 1 Tutorial - Answers.ipynb` (notebook): Ex 1 determinants −2, 10, 0; Ex 3 $(x, y) = (3, 2)$;
  Ex 6 corners $(0, 0), (2, 0), (1.5, 0.5), (0, 1)$; Ex 7 $(x, y, z) = (38/39,\ 11/39,\ -4/39)$.

## Notes for staff

- The NumPy notebook's two deliberate error examples are caught and printed, so *Run All* runs to the end.
- **Tutorial answers were added in Oct 2026** (`4 Tutorial Answers`). Before that no answers existed for Week 1.
  Exercise 7's answer is fractional (det = 39); the answer notebook checks it by substituting back.
- `5 Source Files/Week 1 - Tutorial.docx` is the earlier MATLAB version of the tutorial; the Python notebook in `3 Tutorial` replaces it. The exercises are the same, numbered differently:
  .docx Q1 = Ex 1, Q2 = Ex 2, Q3 (solve, matrix form, MATLAB, plot, Desmos) = Ex 3–5, Q4 = Ex 6, Q5 = Ex 7, Q6 = Ex 8.
  Corrected Oct 2026: Q2 now says "check your answers to Q1" (it said Q2); "it's determinant" → "its".
- The tutorial notebook gained a first cell, `%pip install ipywidgets`.
- The tutorial notebook's saved outputs were regenerated: two example plots, a widget placeholder and three placeholder prints are stored.
- The two `(PDF version)` files were re-printed in Oct 2026 from the current notebooks (saved outputs only, nothing re-run).
  The NumPy notebook stores no outputs, so its print shows code without results.
- The NumPy notebook's note that the browser returns a matrix of `nan` instead of raising `LinAlgError` was added during the move.
- The tutorial notebook's introduction now names the NumPy notebook by its current file and title (it used the old name *Basic Vector and Matrix Operations in NumPy*).
- **Corrections (Oct 2026), notebooks.** NumPy notebook: the `.dot()` / `M @` output labels were swapped
  and `answer3`/`answer4` used `np.matmul` where the comment said `.dot`; the singular-matrix paragraph
  was an unfinished sentence; the line "It should also help for Peter's module" was removed; typos.
  Both notebooks: the comment "solve … using the `np.linalg.det()` function" now says `np.linalg.inv()`.
  Tutorial: Exercises 4 and 8 now name the exercise they plot (3 and 7); the empty last cell was removed;
  typos ("Write your code", "library"); the opening cell now says how to run the notebook and what
  students should end up with; the interactive Exercise 8 cell's comment "Data for three-dimensional
  scattered points" now reads "Grid of (x, y) points on which the three planes are drawn". NumPy notebook:
  $\mathbf{a} \circ \mathbf{b}$ and $\mathbf{a} \cdot \mathbf{b}$ in bold like the rest of the notebook, "NumPy" spelling,
  and a *Try it* cell (with its answer) after the determinant cell. No code or printed numbers changed.
- **Corrections (Oct 2026), slides.** The `.pptx` in `5 Source Files` was corrected and the PDF in `1 Lecture`
  re-exported from it in PowerPoint:
  - slide 24: the equation now reads $x - y = 1$, which is the line the graph has always drawn (it crosses
    the other two at (1.8, 0.8) and (2.333, 1.333)); the slide said $x - y = 0$. The last line now reads
    "i.e. no point solves all three equations simultaneously!" (it said "something that solves…");
  - slide 18: "Sub (3) into (2)" (it said "Sub (1) into (2)");
  - slide 2: "Let's start" (it said "Let' start");
  - slide 29 (PDF page 28): the graph labels `x₁ ≥ 0` and `x₂ ≥ 0` were swapped (`x₂ ≥ 0` sat on the vertical
    axis, which is the line x₁ = 0). The two labels have exchanged places, so each sits on its own boundary line.
  - Not changed: slide 3 says "Simpy" for SimPy, but that text is part of a picture.
  - Edit and export the deck in PowerPoint only. Some equation boxes also store a fallback picture, which only
    other programs (LibreOffice, Google Slides) show, so those programs may show old text.
- Slide 25 of the `.pptx` is hidden and not in the PDF. It says that as many equations as unknowns always
  gives a unique solution and more equations than unknowns always gives none; both are false in general.
  Keep it hidden or correct it before showing it.
- **Review (19 Oct 2026, second pass).** All three notebooks were checked in Pyodide 314.0.0, on desktop Python and
  against the original notebooks: same printed results (in the browser the Exercise 7 check may print `-0.`).
  Text and comments only; no code, saved output or printed number changed:
  - NumPy notebook: the opening cell says how to run it and what you end up with; a short Markdown cell
    explains the `np.dot()` error example; "The number of columns … the number of rows"; "We can write it
    in matrix form".
  - Tutorial: Exercises 4 and 8 explain what the example code does and what to replace, with comments on
    the line and plane formulas; the slider cell says how to use it; Exercise 1 asks again what the
    determinants say about the systems (as the .docx Q1 does); Exercise 5 names Exercise 3; "P.S. … LaTeX".
  - Answers: Exercise 1 adds that a and b give exactly one solution; a comment on the browser's `-0.`.
  - Both `(PDF version)` files were re-printed from the edited notebooks (saved outputs, nothing re-run).
  - Slides (`.pptx`; the PDF in `1 Lecture` was re-exported from it in PowerPoint): slide 16 now reads
    $(x, y) \in \mathbb{R}^2$, $(x, y, z) \in \mathbb{R}^3$ and $(x_1, \dots, x_n) \in \mathbb{R}^n$ (it said $x \in$ each time);
    slide 23 "e.g. two parallel planes" (it said "e.g 2"). The first slide 16 edit put "(x,y)" and "(x,y,z)" in
    one math run each, and PowerPoint drew them without the letters, as "(,)" and "(,,)"; it was redone with
    one character per run, as PowerPoint itself stores equations. If you edit equations outside PowerPoint,
    keep to that.
  - Not changed: the 3D picture on slide 27 (linear inequality) shows a plane, not a half-space; it is an image.
    The tutorial's two saved example plots have a dark background (saved under a dark theme).

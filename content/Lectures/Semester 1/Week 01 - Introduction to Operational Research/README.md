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
| 1 | `1 Lecture/Week 1 - Introduction to Operations Research.pdf` | What OR is and where it is used (pages 1–14); the maths for the rest of the module: linear equations, systems of equations, inequalities and feasible regions (pages 15–30) |
| 2 | `2 Lecture Demos/1 Vectors and matrices in NumPy.ipynb` | Run every cell: vectors, matrix products, inverse, determinant and solving $Ax = b$ in NumPy. **Do this before the tutorial.** |
| 3 | `3 Tutorial/Week 1 Tutorial - Introduction to OR.ipynb` | Exercises 1–8: determinants and systems by hand and in Python, plots of the solutions, a feasible region. Exercises 5 and 6 also use [desmos.com](https://www.desmos.com/calculator). Keep the step 2 notebook open for reference. |
| 4 | `4 Tutorial Answers/Week 1 Tutorial - Answers.ipynb` | Worked answers to Exercises 1–8. Check your work after you have tried them. |

The `(PDF version)` files are printable copies of the notebooks, for reading offline, printed with the notebooks'
saved outputs. Run the `.ipynb` files to see every result.

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

- **Slides.** `1 Lecture/Week 1 - Introduction to Operations Research.pdf` is exported in PowerPoint from
  `5 Source Files/Week 1 - Introduction to Operations Research.pptx`. Edit and export the deck in PowerPoint only:
  some equation boxes also store a fallback picture, which other programs show instead, so they may show old text.
  When editing an equation outside PowerPoint's equation editor, keep one character per math run, as PowerPoint
  stores it; a run holding several characters, such as "(x,y)", is drawn without its letters.
- Slide 25 of the `.pptx` is hidden and not in the PDF, so from slide 26 on the PDF page is the slide number
  minus 1 (slide 29 = PDF page 28). It says that as many equations as unknowns always gives a unique solution and
  more equations than unknowns always gives none; both are false in general. Keep it hidden or correct it before
  showing it.
- Text inside pictures, which cannot be edited: slide 3 says "Simpy" for SimPy; the 3D picture on slide 27
  (linear inequality) shows a plane, not a half-space.
- **Tutorial.** `5 Source Files/Week 1 - Tutorial.docx` is the earlier MATLAB version of the tutorial; the Python
  notebook in `3 Tutorial` replaces it. The exercises are the same, numbered differently:
  .docx Q1 = Ex 1, Q2 = Ex 2, Q3 (solve, matrix form, MATLAB, plot, Desmos) = Ex 3–5, Q4 = Ex 6, Q5 = Ex 7, Q6 = Ex 8.
- **Answers.** `4 Tutorial Answers/Week 1 Tutorial - Answers.ipynb` is the only set of worked answers for Week 1
  (the .docx has none). Exercise 7's answer is fractional (det = 39); the notebook checks it by substituting back.
- **Running in the browser.** All three notebooks run top to bottom in Pyodide 314.0.0 (the version the site
  loads) and print the same results as desktop Python, with two expected differences: the NumPy notebook's
  singular-matrix cell prints a matrix of `nan` instead of `LinAlgError: Singular matrix` (its text says so), and
  the answers' Exercise 7 check may print `-0.` for 0. The NumPy notebook's two deliberate error examples are
  caught and printed, so *Run All* runs to the end. The tutorial's first cell installs `ipywidgets` for the
  Exercise 8 slider.
- **Saved outputs.** The tutorial notebook stores its two example plots (dark background), the slider placeholder
  and the three placeholder prints; the answers notebook stores all its results and plots; the NumPy notebook
  stores none, so its `(PDF version)` shows code without results.
- **PDF versions.** The two `(PDF version)` files are printed from the notebooks with their saved outputs (nothing
  re-run). Re-print them after editing a notebook, with code-cell line wrap on so long lines are not cut off.
- The NumPy and tutorial notebooks come from the Colab notebooks *Basic Vector and Matrix Operations in NumPy*
  and *OR Week 1 Tutorial - Introduction to OR*, and print the same results. The versions here add the opening
  "How to use this notebook" cells, explanations, comments and the *Try it* cell, catch the two error examples,
  and start the tutorial with `%pip install ipywidgets`.

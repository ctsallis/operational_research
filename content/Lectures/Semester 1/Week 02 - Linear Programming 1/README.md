# Semester 1 · Week 02 – Linear Programming 1

Formulating linear programmes, solving them graphically, and solving them with SciPy's `linprog` and Excel Solver.

| Folder | What is in it | When |
| --- | --- | --- |
| `1 Lecture` | Slides (PowerPoint) | The lecture |
| `2 Lecture Demos` | Notebooks and spreadsheets shown in the lecture, numbered in teaching order | Run live in the lecture |
| `3 Tutorial` | Tutorial sheet (Word) | The practical |
| `4 Tutorial Answers` | Worked answers (Word), answer notebooks and a workbook | **Release after the practical** |
| `5 Source Files` | The scripts the notebooks came from | Staff only |

## Before you start

- **Maths:** Week 01's matrix form $Ax \le b$ and sketching a feasible region from linear inequalities.
- **Python:** none needed beyond Week 01. The notebooks are short and commented.
- **Excel:** desktop Excel with the **Solver** add-in (*File → Options → Add-ins → Excel Add-ins → Solver*),
  for the Excel demo and Tutorial Q4. Excel does not run on the course site.
- **PowerPoint and Word:** the slides, tutorial sheet and answers are `.pptx` and `.docx` files. On the course
  site, right-click → *Download*, then open them in PowerPoint or Word.

## Work through this week in order

| Step | File | What it is for |
| --- | --- | --- |
| 1 | `1 Lecture/Week 2 - Linear Programming 1.pptx` | The lecture example (two products, one machine), the feasible region, the objective line, optimal vertices, binding constraints, infeasible, unbounded and multiple-optimum LPs, the canonical (matrix) form, and the switch from maximising to minimising |
| 2 | `2 Lecture Demos/1 LP with SciPy linprog.ipynb` | Run every cell: the lecture LP solved with `linprog`; the answer $(41.14, 10.29)$, profit £277.71, is slide 12's point B |
| 3 | `2 Lecture Demos/2 LP with Excel Solver.xlsx` | The same LP in Excel: download it, open *Data → Solver* and press *Solve* |
| 4 | `1 Lecture/Simplex Method 2 Variable Graphical Demo.pptx` | Optional: how the simplex method walks from vertex to vertex (A → B → C) |
| 5 | `3 Tutorial/Week 2 - Linear Programming - Tutorial.docx` | Q1 graphically, Q2 in matrix form, Q3 in Python (copy the step 2 notebook and change `c`, `A_ub`, `b_ub`), Q4 in Excel (copy the step 3 workbook), Q5 manufacturing (medium), Q6 diet problem (hard; it is discussed at the start of Week 03) |
| 6 | `4 Tutorial Answers/` | Check your work after you have tried the questions: the Word file for Q1–Q6, a notebook for Q3, Q5a, Q5b, Q5c and Q6, and a workbook for Q4 |

## By the end of this week you can

- turn a short word problem into a linear programme: decision variables, objective, constraints, non-negativity;
- draw the feasible region of a two-variable LP and find the optimum by moving the objective line, or by
  checking the vertices;
- say which constraints are binding at a solution;
- recognise infeasible and unbounded LPs and LPs with many optimal solutions;
- write an LP in canonical form ($\max c^T x$ subject to $Ax \le b$, $x \ge 0$) and turn a maximisation into
  a minimisation by negating $c$;
- solve an LP with SciPy's `linprog` and with Excel Solver, and read the result (`linprog` prints
  $-$profit when you maximise).

**Next:** Week 03 (Linear Programming 2) solves the lecture LP and the Q6 diet problem again in Pyomo, then
adds integer variables. Tutorial Q5c already shows why whole-number answers need a different method.

## 1 Lecture

- `Simplex Method 2 Variable Graphical Demo.pptx`
- `Week 2 - Linear Programming 1.pptx`

## 2 Lecture Demos

- `1 LP with SciPy linprog.ipynb` (notebook)
- `2 LP with Excel Solver.xlsx`

## 3 Tutorial

- `Week 2 - Linear Programming - Tutorial.docx`

## 4 Tutorial Answers

- `Q3 LP with linprog.ipynb` (notebook): $(x, y) = (0, 20)$, maximum 340 (also Q1).
- `Q4 LP with Excel Solver.xlsx`: the Q1 problem in the demo workbook's layout, with Solver set up; same answer.
- `Q5a Manufacturing - products X and Y.ipynb` (notebook): 50 of Y, profit £250.
- `Q5b Manufacturing - add product Z.ipynb` (notebook): 20 of Y and 20 of Z, profit £260.
- `Q5c Manufacturing - faster X.ipynb` (notebook): 22.22 of X, profit £266.67; the best whole-number plan
  earns £266.
- `Q6 Diet problem - parts a, b and c.ipynb` (notebook): (a) minimum cost £93.25; (b) unbounded;
  (c) maximum attractiveness 149.66, and minimum cost £136.52 under the same limits. Lists the binding
  constraints.
- `Week 2 - Linear Programming - Tutorial Answers.docx`

## Notes for staff

- **No PDF copies.** Students use the `.pptx` and `.docx` files directly, so there is nothing to re-export after
  an edit. Edit the decks in PowerPoint only: every text box that contains an equation also stores a fallback
  picture, which other programs show instead, so they may show old text.
- Text inside pictures, which cannot be edited: the code on slide 25 still has the comment "to minimise we need
  the negatives" (the notebooks say: `linprog` minimises, so to maximise we pass the negatives).
- **Question numbers.** The scripts were written for an earlier numbering of the sheet: `Question_4a–c.py`
  answer **Q5a–c** and `Question_5.py` answers **Q6a–c**. The notebooks use the sheet's numbering. Week 03's
  slides and demos still use the old numbers (see `Lectures/Semester 1/README.md`, section 5).
- **Tutorial and answers.** The answers' output screenshots are MATLAB's; the values match the notebooks. Each "Please see the notebook" names
  a notebook in `4 Tutorial Answers`. Q4's answer is `Q4 LP with Excel Solver.xlsx`, made from the demo workbook
  (same layout and Solver set-up).
- **Q6 notebook.** Beyond `Question_5.py`, it lists the binding constraints after (a) and (c) (rows 1–3, and 2,
  4, 5, 8, 10, as in the screenshots). It also solves (c) with the cost objective (£136.52), because the
  question asks about both solutions.
- **Several optimal solutions.** Q5c (X and Z both earn £8/3 per machine hour) and the demo's *Try it* 2
  (objective parallel to $3x + 2y = 144$) have many optimal solutions. `linprog` reports one vertex; another
  solver may report a different one with the same value.
- **Running in the browser.** All six notebooks run top to bottom in Pyodide 314.0.0 (the version the site
  loads). They print the same results as desktop Python and as the original scripts in `5 Source Files/Python`,
  from which the `@author` staff ID line was removed. SciPy is built into the browser's Python, so the notebooks
  have no install cell.
- **Saved outputs.** The demo notebook stores its result; the five answer notebooks store none (students see the
  results when they run them).
- **Excel.** Both workbooks need desktop Excel with the Solver add-in; they do not run on the site.

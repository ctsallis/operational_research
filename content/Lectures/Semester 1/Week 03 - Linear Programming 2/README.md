# Semester 1 · Week 03 – Linear Programming 2

Pyomo modelling, the diet problem, and a first look at integer and mixed-integer programmes.
Work through the folders in number order.

| Folder | What is in it | When |
| --- | --- | --- |
| `1 Lecture` | Slides and the 2-variable simplex demo (PowerPoint) | The lecture |
| `2 Lecture Demos` | Six notebooks, numbered in the order the slides use them | Run live in the lecture |
| `3 Tutorial` | Tutorial sheet (Word) | The practical |
| `4 Tutorial Answers` | Worked answers (Word) and answer notebooks | **Release after the practical** |
| `5 Source Files` | The scripts the notebooks came from (and older Q1 scripts), MATLAB versions | Staff only |

## Before you start

- **Week 02:** the lecture LP (maximise $5x + 7y$), its graphical solution, and the diet problem (Week 02
  tutorial Q6). This week solves both again in Pyomo.
- **Maths:** summation notation, $\sum_i c_i x_i$ (the lecture introduces it with the diet problem).
- **Python:** lists, `for` loops and `sum(...)`. Each notebook's first cell installs Pyomo and the HiGHS
  solver; run it first.
- **PowerPoint and Word:** the slides, tutorial sheet and answers are `.pptx` and `.docx` files. On the course
  site, right-click → *Download*, then open them in PowerPoint or Word.

## Work through this week in order

Slide numbers are those of the `.pptx` (slide 3 is hidden, so the slide show skips it).

| Step | File | What it is for |
| --- | --- | --- |
| 1 | `1 Lecture/Week 3 - Linear Programming 2.pptx`, slides 1–6 | Review of Week 02: the LP model, canonical (matrix) form, the `linprog` solution |
| 2 | `1 Lecture/Simplex Method 2 Variable Graphical Demo.pptx` | Optional: how the simplex method walks from vertex to vertex (the same demo as Week 02) |
| 3 | `2 Lecture Demos/1 LP with Pyomo.ipynb` | Slide 7: the same LP in Pyomo; $(41.14, 10.29)$, $P = 277.71$ |
| 4 | `2 Lecture Demos/2 Diet problem 5a - minimise cost.ipynb` | Slides 8–12: the diet problem in summation notation and Pyomo; minimum cost 93.25 |
| 5 | `2 Lecture Demos/3 Diet problem 5b - unbounded.ipynb` | Slides 13–14: maximise attractiveness; the solver reports *unbounded*, and why |
| 6 | `2 Lecture Demos/4 Diet problem 5c - the fix.ipynb` | Slides 15–16: minimum and maximum limits give a sensible diet; attractiveness 149.66 |
| 7 | Lecture slides 17–23 | Manufacturing problem and the Desmos demo: rounding an LP answer is not the same as the best whole-number answer |
| 8 | `2 Lecture Demos/5 Integer LP.ipynb` | Slide 24: integer variables; $(3, 2)$, $P = 13$ |
| 9 | `2 Lecture Demos/6 Mixed-integer LP.ipynb` | Slides 25–26: one integer and one continuous variable; $(2, 2.833)$, $P = 13.917$ |
| 10 | `3 Tutorial/Week 3 - Linear Programming 2 - Tutorial.docx` | Q1 (LP, ILP and MILP: copy demo 5 or 6 and change the numbers), Q2 Icki-Toffee (medium/hard: copy demo 2's structure, with integer variables) |
| 11 | `4 Tutorial Answers/` | Check your work after you have tried the questions: the Word file for Q1–Q2, and three notebooks |

Each notebook starts with the problem, how to run it and the expected result, explains every code cell,
and ends with a short *What do you notice?* or *Try it* question with a hidden answer.

## By the end of this week you can

- write an LP in Pyomo: a `ConcreteModel`, variables with a domain, an objective and constraints, solved
  with `SolverFactory('appsi_highs')`;
- read Pyomo's output: variable values, the objective, and which constraints are binding;
- write a model with summation notation ($\sum_i c_i x_i$) and code it with `sum(...)` over lists of data;
- recognise an unbounded LP from the solver's message, explain why it happens, and fix the model by
  adding the missing limits;
- explain why rounding an LP solution may be infeasible or not optimal;
- solve integer (ILP) and mixed-integer (MILP) programmes by changing the variables' domain, and compare
  LP ≥ MILP ≥ ILP for a maximisation.

**Next:** Week 04 (Mathematical Programming: Modelling) uses the Icki-Toffee model again to compare
objectives (Q2d's question: is maximising total popularity the right aim?) and adds slack variables.

## 1 Lecture

- `Simplex Method 2 Variable Graphical Demo.pptx` (the same file as in Week 02)
- `Week 3 - Linear Programming 2.pptx`

## 2 Lecture Demos

| Notebook | Slides | Shows |
| --- | --- | --- |
| `1 LP with Pyomo` | 7 | The lecture LP written in Pyomo |
| `2 Diet problem 5a - minimise cost` | 8–12 | Week 2 tutorial Q6a (the slides' Q5a) in Pyomo |
| `3 Diet problem 5b - unbounded` | 13–14 | Maximising attractiveness: the solver reports *unbounded* |
| `4 Diet problem 5c - the fix` | 15–16 | Adding limits on fat and vitamins gives a sensible diet |
| `5 Integer LP` | 24 | Same constraints, integer variables |
| `6 Mixed-integer LP` | 25–26 | One integer and one continuous variable |

## 3 Tutorial

- `Week 3 - Linear Programming 2 - Tutorial.docx`

## 4 Tutorial Answers

| Notebook | Question | Answer |
| --- | --- | --- |
| `Q1 LP, ILP and MILP` | Q1, Q1a, Q1b | LP 270 at (7.5, 10); ILP 264 at (7, 10); MILP 270 at (7.5, 10) |
| `Q2b Icki-Toffee - minimise cost` | Q2b | Minimum cost 268 (several selections reach it) |
| `Q2c Icki-Toffee - maximise popularity` | Q2c | 5 Coconut Ice, 50 Lime sherbet, 5 Grape bunch; weight 635 g |

- `Week 3 - Linear Programming 2 - Tutorial - Answers.docx`: Q1–Q2, with Pyomo output.

## Notes for staff

- **No PDF copies.** Students use the `.pptx` and `.docx` files directly, so
  there is nothing to re-export after an edit. Edit the deck in PowerPoint only: every text box that contains an
  equation also stores a fallback picture, which other programs show instead, so they may show old text.
  The simplex demo `.pptx` is a copy of Week 02's: if you change one, copy it to the other week.
- **Hidden slide.** Slide 3 of the `.pptx` is a hidden blank slide; the README and the notebooks give `.pptx`
  slide numbers, which count it (the handbook's teaching guide uses the same numbers).
- **Question numbers.** Demos 2–4 follow the slides' numbering (*Tutorial Question 5a–c*, and "Q4" for the
  manufacturing problem); on this year's Week 2 sheet these are **Q6** and **Q5**. Demo titles give both.
- **Corrections made to the course files** (the deck, sheet and answers differ from the originals on these
  points):
  - slide 6: "we call linprog with the negated objective, c = [-5, -7]" (it said "using -f");
  - slide 10: vitamin B constraint $14x_5$ (it said $12x_5$); vitamin C constraint $10x_9$ (it said $10x_{10}$);
    the "(Vitamin C Constraint)" label lines up with the others;
  - slide 14: title "Tutorial Question 5b";
  - slide 19: $P^* = 262.22$ (it said 262.62; $11.5 \cdot 80/9 + 160 = 262.22$);
  - slide 20: "if you round", "round down,", "you get a profit of £262", "Ten pounds might not…";
  - slide 22: the non-optimal points (1, 2) and (2, 2) are labelled $P = 9$, $P = 11$ (not $P^*$);
  - slide 27: links to the course site and the `2 Lecture Demos` folder (it linked to a Colab notebook that
    needs a sign-in);
  - tutorial and answers Q2: the selection must weigh "at least" 320 g, with fat "at most" 45% and "at most"
    2850 calories (it said "more than" / "less than"; the model uses ≥ / ≤ and the Q2c answer uses exactly
    2850 calories). Answers only: Q2a no longer adds "Is this a good selection?" (Q2d asks it), Q2b's heading
    has the sheet's `**`, a note says any selection costing 268 is correct, and Q2c names the candies as the
    tables do ("Lime sherbet", "Grape bunch").
- **Text inside pictures, which cannot be edited:** the code on slides 7, 24 and 26 says GLPK (the notebooks
  use HiGHS); slide 16's code comment says "minimize total cost" for a maximisation; slide 6's comment says
  "to minimise we need the negatives"; slide 12's code shows a stray text cursor on line 14.
- **Q1 answers were rewritten for the current tutorial.** The old Q1 scripts solve a different problem
  (maximise 5x + 17y with 2x + 3y ≤ 60, x + 2y ≤ 25) from an earlier version of the sheet. They are kept in
  `5 Source Files/Python/Old Q1 (previous tutorial version)`; the MATLAB Q1 files are the same old version.
- **Several optimal solutions.** Q2b has more than one cheapest selection: HiGHS gives 9 Caramel softie,
  8 Rose-water posy and 4 Grape bunch; the answer sheet (GLPK) shows 9, 10 and 3. Both cost 268.
- **Scripts.** The notebooks use HiGHS (`SolverFactory('appsi_highs')`) so they run in the browser; the
  scripts in `5 Source Files/Python` still use GLPK for desktop use. `Week2_question_5b_pyomo.py` solves with
  `load_solutions=False` and prints the termination condition, because HiGHS stops with an error when asked to
  load a solution from an unbounded model. To change a demo, edit the notebook directly; to rebuild one from
  its script, run `python tools/convert_to_notebooks.py "<path to the .py>"` and move the new notebook into
  place.
- **Running in the browser.** All nine notebooks run top to bottom in Pyodide 314.0.0 (the version the site
  loads) and print the same results as desktop Python and as the original GLPK scripts. In the browser `tee`
  has no effect: the first code cell switches off Pyomo's capture of solver output (browsers have no threads),
  so HiGHS always prints its log.
- **Saved outputs.** The notebooks store no outputs; students see the results when they run them.

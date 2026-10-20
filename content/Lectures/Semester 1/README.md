# Semester 1 – Operational Research: Lectures

This is the starting page for Semester 1. It is written for a student working **completely alone**,
with no one to ask. Read it once from top to bottom, then go to
[Week 01](Week%2001%20-%20Introduction%20to%20Operational%20Research/README.md) and work through the
weeks in order.

Every week has its own README that tells you exactly what to open, in what order, what result you
should get and how to check your answers. This page tells you:

- what the semester covers and what you will be able to do at the end;
- what you need, and the instructions that are the same in every week;
- how the weeks fit together;
- how to check that you have really finished.

---

## Contents

1. [What you will be able to do](#1-what-you-will-be-able-to-do)
2. [The weeks at a glance](#2-the-weeks-at-a-glance)
3. [Your plan for the semester](#3-your-plan-for-the-semester)
4. [How the weeks build on each other](#4-how-the-weeks-build-on-each-other)
5. [What you need](#5-what-you-need)
6. [How every week folder is organised](#6-how-every-week-folder-is-organised)
7. [Where the answers are](#7-where-the-answers-are)
8. [How to use the course site (same every week)](#8-how-to-use-the-course-site-same-every-week)
9. [How to work through a week](#9-how-to-work-through-a-week)
10. [The key ideas of the semester on one page](#10-the-key-ideas-of-the-semester-on-one-page)
11. [Reading results and checking your answers](#11-reading-results-and-checking-your-answers)
12. [If something goes wrong](#12-if-something-goes-wrong)
13. [Test yourself](#13-test-yourself)
14. [Key words](#14-key-words)
15. [Checklist: have you finished the semester?](#15-checklist-have-you-finished-the-semester)
16. [Assumptions made in this README](#16-assumptions-made-in-this-readme)

---

## 1. What you will be able to do

Operational Research (OR) uses mathematical models to make better decisions. Over eleven weeks you
learn to turn a problem written in words into a model, solve it on a computer, and judge whether the
answer makes sense.

By the end of the semester you should be able to:

- **use the maths behind the models:** solve systems of linear equations, work with matrices, and draw
  the feasible region of a set of inequalities (Week 01);
- **write a linear programme (LP)** from a word problem and solve it by drawing, in matrix form, with
  SciPy's `linprog`, with Excel Solver and with **Pyomo** (Weeks 02–03);
- **model well:** use summation notation, extend a model, combine two objectives, and read slack and
  binding constraints (Weeks 03–04);
- **use integer and binary variables:** knapsack, set covering, purchasing with logical rules, vertex
  and edge cover, matching and assignment, and explain why rounding an LP answer is not enough
  (Weeks 03, 05–06);
- **schedule jobs:** draw Gantt charts, compute the makespan, apply Johnson's rule and the Campbell,
  Dudek and Smith heuristic by hand, and model a job shop as a big-M MILP (Week 07);
- **solve network problems by hand:**
  - find shortest paths with Dijkstra's algorithm, and explain why it fails with negative weights;
  - build minimum spanning trees with Prim's and Kruskal's algorithms (Week 08);
- **model routing problems:** the Travelling Salesman Problem with the Miller–Tucker–Zemlin (MTZ)
  constraints, and the Vehicle Routing Problem with capacity, minimising either the total distance or
  the longest route (Weeks 09–10);
- **pack rectangles** without overlap, with rotation, and with different objectives (Week 11);
- **explain why some problems are hard** (NP-hard), and what a heuristic gives you and what it does not
  (Weeks 07, 09–11).

Python runs **inside your web browser** on the course site, so there is nothing to install.

---

## 2. The weeks at a glance

Click a week to open its README.
- **Work** says how most of the week is done.
- **Tutorial** says where its exercises are.
- [Section 7](#7-where-the-answers-are) says where the answers are.

| Week | What it is about | Work | Tutorial |
| --- | --- | --- | --- |
| [01 – Introduction to Operational Research](Week%2001%20-%20Introduction%20to%20Operational%20Research/README.md) | What OR is; revision of linear equations, matrices, determinants, inequalities and feasible regions, done in NumPy, Matplotlib and Desmos | Pen and paper, Python (NumPy) | Notebook, Exercises 1–8 |
| [02 – Linear Programming 1](Week%2002%20-%20Linear%20Programming%201/README.md) | Writing a word problem as an LP; solving it by drawing, in matrix form, with `linprog` and with Excel Solver; the idea of the simplex method | Pen and paper, Python (`linprog`), Excel | Word sheet, Q1–Q6 |
| [03 – Linear Programming 2](Week%2003%20-%20Linear%20Programming%202/README.md) | LPs in Pyomo with summation notation; unbounded LPs; integer (ILP) and mixed-integer (MILP) programmes, and why rounding is not enough | Python (Pyomo), some pen and paper | Word sheet, Q1–Q2 |
| [04 – Mathematical Programming: Modelling](Week%2004%20-%20Mathematical%20Programming%20-%20Modelling/README.md) | Extending a model, combining two objectives, slack variables and binding constraints, one model for a whole system. Two decks: the main slides and `Slack Variables.pptx` | Python (Pyomo) | Word sheet, Q1–Q2 |
| [05 – Mixed Integer Programming](Week%2005%20-%20Mixed%20Integer%20Programming/README.md) | Binary variables; the knapsack, set covering and purchasing problems; linking an amount to a yes/no decision; logical rules | Python (Pyomo) | Word sheet, Q1–Q3 |
| [06 – Integer Linear Programming: Further Problems](Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/README.md) | Costed set cover written three ways; graph problems (edge cover, vertex cover, matching); the assignment problem | Python (Pyomo); tasks 3–4 read examples on gurobi.com | Last slide of the lecture (slide 28), tasks 1–5 |
| [07 – Flow Shop and Job Shop Scheduling](Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/README.md) | Single machine; makespan and Gantt charts; Johnson's rule and the Campbell, Dudek and Smith heuristic; job shop as a big-M MILP; a first look at constraint programming. The job shop half is taught from a notes notebook, not slides | Pen and paper, Excel, Python (Pyomo), Google Colab | Word sheet (flow shop, Q1–Q4) and notebook (job shop, Q1–Q5) |
| [08 – Networks: Shortest Paths and MST](Week%2008%20-%20Networks%20-%20Shortest%20Paths%20and%20MST/README.md) | Dijkstra's algorithm, and why it fails with negative weights; minimum spanning trees with Prim and Kruskal | Pen and paper only (one optional checking notebook) | Word sheet, Q1–Q2 |
| [09 – Travelling Salesman Problem](Week%2009%20-%20Travelling%20Salesman%20Problem/README.md) | Counting tours; P, NP and NP-hard; the TSP as a MILP; subtours and the MTZ constraints; a genetic algorithm | Python (Pyomo), a little pen and paper | Slide 22, done in the demo notebook |
| [10 – Vehicle Routing Problem](Week%2010%20-%20Vehicle%20Routing%20Problem/README.md) | From the TSP to several vehicles: demand, capacity and flow; minimising total distance or the longest route; the nearest-neighbour heuristic | Python (Pyomo), pen and paper | No sheet: notebook questions and exercises in the README |
| [11 – Floor Planning](Week%2011%20-%20Floor%20Planning/README.md) | Packing rectangles without overlap: big-M with binary variables, rotation, the smallest square, fitting the most items or the most area, keeping connected items close | Python (Pyomo), a little pen and paper | No sheet: notebook questions and questions in the README |

> **If a link above does not open on the course site:** the links work when this page is viewed on
> GitHub. On the course site, open the week's folder in the file browser instead and open its
> `README.md` as described in [section 8](#8-how-to-use-the-course-site-same-every-week).

---

## 3. Your plan for the semester

Do the weeks **in order** and tick each one when you finish it. A week is finished when every box on
its own checklist is ticked:
- Week 11 keeps its tick boxes in its plan (section 4 of its README);
- Week 04 keeps them in its section 2;
- every other week has a final "Checklist" section.

- [ ] **Before Week 01:** read this page, open the course site and run `00_START_HERE.ipynb`
  ([section 8](#8-how-to-use-the-course-site-same-every-week)).
- [ ] **Week 01** – maths refresher. Do the tasks on slides 10 and 13, the NumPy notebook and
  Exercises 1–8.
- [ ] **Week 02** – LP 1. Do the 8-step plan and tutorial Q1–Q6. Q6 is hard on purpose: you are not
  expected to finish it yet, and Week 03 starts by discussing it.
- [ ] **Week 03** – LP 2 in Pyomo, ILP and MILP. Run demos 1–6 and do tutorial Q1–Q2.
- [ ] **Week 04** – modelling. Go through both decks, the demo and tutorial Q1–Q2.
- [ ] **Week 05** – binary variables. Run demos 1–7 (demo 8 is optional) and do tutorial Q1–Q3.
- [ ] **Week 06** – further integer problems. Run demos 1–7 and do slide 28, tasks 1–5.
- [ ] **Week 07** – scheduling. Part A is flow shop (slides, Excel, tutorial Q1–Q3). Part B is job shop
  (notes notebook, flow shop Q4, job shop Q1–Q5). Q4–Q5 run in Google Colab.
- [ ] **Week 08** – networks, all by hand. Do the slides, the negative-weight deck and tutorial
  Q1–Q2.
- [ ] **Week 09** – TSP. Go through the slides, the demo notebook and the slide 22 tutorial. Its README
  suggests about 4 hours in total.
- [ ] **Week 10** – VRP. Do steps 1–10 with checkpoints, the demo notebook, exercises 1–4 and the
  self-test.
- [ ] **Week 11** – floor planning. Do steps 1–9, the four notebooks and the "Check yourself"
  questions.
- [ ] **At the end:** answer [Test yourself](#13-test-yourself) and tick
  [the semester checklist](#15-checklist-have-you-finished-the-semester).

Only Week 09 gives study times, and only as suggestions. Plan your own time
([assumption 1](#16-assumptions-made-in-this-readme)).

---

## 4. How the weeks build on each other

Each week assumes the earlier ones. The table lists what each weekly README says you need first.

| Week | Says you need first |
| --- | --- |
| 01 | Nothing: it is the starting point |
| 02 | Week 01: vectors and matrices (matrix × vector) |
| 03 | Week 02: feasible regions, matrix form, `linprog`; Week 02 tutorial Q5 and Q6 come back in the lecture |
| 04 | Weeks 02 and 03: the diet problem and the Icki-Toffee model (your own, or the Week 03 answer notebook) |
| 05 | Week 03 (Pyomo, Icki-Toffee) and Week 04 (turning a word problem into a model) |
| 06 | Week 05 (binary variables, the fire-station set cover; demo 8 is a preview); Weeks 03–04 (building a Pyomo model) |
| 07 | Weeks 03–04 (Pyomo) and Week 05 (binary variables) |
| 08 | The README lists no earlier weeks: the algorithms are done by hand |
| 09 | Weeks 05–06 (binary variables, MILP), earlier weeks for Pyomo, Week 08 (networks) |
| 10 | Week 09 (TSP tours and the variable $x_{ij}$); its slides 3–5 recap it |
| 11 | Week 05 (binary variables), Week 07 (big-M either/or constraints) and basic Pyomo |

Some examples **come back** in later weeks. When you meet one again, look back at where it started:

| Example | Where it appears |
| --- | --- |
| Chairs and tables LP (maximise $5x + 7y$) | Week 02 lecture and demos → Week 03 demo 1 (in Pyomo) |
| Simplex LP (maximise $5x + 4y$, optimum C = (4, 1.5), P = 26) | `Simplex Method 2 Variable Graphical Demo.pptx` in Weeks 02 and 03 (the same file) → Week 04 `Slack Variables.pptx` (same LP, different deck) |
| Diet problem (10 foods) | Week 02 tutorial Q6 → Week 03 demos 2–4 → Week 04 slides 8–10 |
| Icki-Toffee candy selection | Week 03 tutorial Q2 → Week 04 tutorial Q1 → Week 05 tutorial Q3 |
| Integer LP, maximise $2x + 3.5y$ | Week 03 demos 5–6 → Week 05 demo 1 → Week 11 recap (slides 2–4) |
| Fire stations (set covering) | Week 05 demo 3 and tutorial Q2 → Week 06 demos 1–3 (with costs, and different data) |
| Minimum vertex cover | Week 05 demo 8 (optional preview) → Week 06 demo 4 (a different graph: security cameras) |
| A large number (big-M) that a binary variable uses to switch a constraint on or off | Week 07 (job shop) → Week 09 (MTZ) → Week 10 (VRP) → Week 11 (non-overlap) |
| TSP with MTZ constraints | Week 09 → start of Week 10's notebook |

---

## 5. What you need

| You need | Used in | Notes |
| --- | --- | --- |
| A recent **Chrome, Edge or Firefox** | Every week | Runs the course site and its Python notebooks. Nothing to install. Week 02 says Safari works but is slow. |
| An internet connection | Every week | The first run of a notebook downloads Python and its packages into the browser tab. Week 06 tasks 3–4 also read example notebooks on gurobi.com. |
| **PowerPoint** | Every week | The lecture slides are `.pptx` files. Week 08's tutorial answers are also `.pptx`. |
| **Word** | Weeks 02, 03, 04, 05, 07, 08 | Tutorial sheets and written answers are `.docx` files. |
| **Desktop Excel** | Week 02 (with the **Solver** add-in); Week 07 (formula tables and Gantt charts, no Solver) | Week 02's README shows how to switch Solver on. Excel for the web is not covered. |
| A PDF reader | Weeks 04, 06, 07, 08, 10 | Optional: further reading, annotated (older) slides and previous versions. |
| Pen, paper (a ruler or graph paper helps) | Weeks 01, 02, 07, 08, 10, and parts of 03, 09 and 11 | Week 08 is done entirely by hand. Modelling on paper first helps in every week. |
| **Desmos** (free online graphing calculator) | Weeks 01 and 02; optional in Week 03 | <https://www.desmos.com/calculator> |
| A **Google account** for **Google Colab** | Week 07, job shop tutorial Q4–Q5 | Google OR-Tools does not run on the course site. |
| MATLAB | Never required | Some `5 Source Files` folders contain MATLAB versions. You do not need them. |

---

## 6. How every week folder is organised

The sub-folders are numbered the same way in every week. Not every week has all of them.

| Folder | What is in it | Do you need it? |
| --- | --- | --- |
| `1 Lecture` | The slides (`.pptx`). See the note below for the weeks that have more. | **Yes** |
| `2 Lecture Demos` | Notebooks (and in Weeks 02 and 07 Excel files) that run the lecture's examples | **Yes**. Week 08 has none. |
| `3 Tutorial` | The tutorial sheet or notebook | **Yes**. Weeks 06, 09, 10 and 11 have no tutorial folder (see [section 2](#2-the-weeks-at-a-glance)). |
| `4 Tutorial Answers` | Worked answers: Word files, notebooks, answer slides | **Yes**, but only **after** you have tried the questions. Weeks 10 and 11 have no answers folder ([section 7](#7-where-the-answers-are)). |
| `5 Source Files` | The original scripts the notebooks were made from, older versions, staff notes | **No.** Every week that has this folder says you can ignore it. |
| `6 Further Reading` | Papers and extra slides | Optional |

**Weeks with more than one lecture file:**

| Week | Extra files in `1 Lecture` |
| --- | --- |
| 02 and 03 | The simplex method demonstration deck |
| 04 | `Slack Variables.pptx`, needed for tutorial Q2a |
| 06 | An annotated PDF of an older version of the slides (optional) |
| 07 | The job shop lecture notes (notebooks); these are the lecture for the second half of the week |
| 08 | Two short extra decks (Dijkstra, the negative-weight example) and an annotated PDF. The PDF is an older version: follow the `.pptx` when they differ. |
| 10 | Written lecture notes (`.md`) |

Week 07's `5 Source Files/Previous Versions` holds an out-of-date answers PDF. Use the `.docx` answers
in `4 Tutorial Answers` instead.

**Slide numbers** in the weekly READMEs are the numbers PowerPoint shows in its slide list on the
left. Some decks have a hidden blank slide (slide 3 in Weeks 03, 04 and 05; slide 2 in Week 06). It is
skipped in a slide show but still counts in the numbering.

**Star marks** on the Word tutorial sheets of Weeks 02–05: one star (\*) is a medium question, two
stars (\*\*) a hard one.

---

## 7. Where the answers are

The answers are already in the folders. It is up to you to try each question first. A few questions
have **no worked answer**; their weekly README tells you how to check yourself.

| Week | Answers | Questions without a worked answer |
| --- | --- | --- |
| 01 | `4 Tutorial Answers/Week 1 Tutorial - Answers.ipynb` | – |
| 02 | `4 Tutorial Answers`: Word answers, notebooks for Q3, Q5a–c and Q6, Excel file for Q4 | – |
| 03 | `4 Tutorial Answers`: Word answers, notebooks for Q1, Q2b and Q2c | Q2d (no official answer) |
| 04 | `4 Tutorial Answers`: Word answers, notebooks for Q1b (three versions), Q2a (factories A and B) and Q2b | – |
| 05 | `4 Tutorial Answers`: Word answers, notebooks for Q1a–c, Q2 and Q3 | – |
| 06 | `4 Tutorial Answers/Q5 …ipynb` for task 5; task 2 is checked against demo 2 | Tasks 3 and 4 |
| 07 | Flow shop: `Week 7 - Flow Shop Scheduling - Tutorial - Answers.docx`, `Flow Shop Q4 MILP answers.ipynb`, and the answer sheets in `2 Lecture Demos/2 Johnsons rule in Excel.xlsx`. Job shop: `Job Shop Q1-Q3 answers.ipynb` | Job shop Q4–Q5 |
| 08 | `4 Tutorial Answers`: Q1 and Q2 answer decks (`.pptx`), and an optional checking notebook | – |
| 09 | `4 Tutorial Answers/Tutorial answers (slide 22).ipynb` | – |
| 10 | No answers folder: hidden answers in the notebook and in the README (exercises and self-test) | – |
| 11 | No answers folder: hidden answers in the four notebooks and in the README (sections 7–8) | – |

Hidden answers in notebooks and READMEs sit under a line marked **Answer**: click it to open it.

---

## 8. How to use the course site (same every week)

### Open the site

1. Go to **<https://ctsallis.github.io/operational_research/>** in Chrome, Edge or Firefox
   ([assumption 4](#16-assumptions-made-in-this-readme)).
2. **At the start of a session**, open `00_START_HERE.ipynb` (at the top of the file list) and choose
   **Run → Run All Cells**. If every cell prints `OK`, the course notebooks will run in your browser.
3. In the file browser on the left, double-click `Lectures` → `Semester 1` → the week's folder.

### Open each kind of file

| File | How to open it |
| --- | --- |
| Notebook (`.ipynb`) | Double-click it. It opens and runs in the browser. If asked to choose a kernel, choose **Python (Pyodide)**. |
| README (`.md`) | Right-click → **Open With** → **Markdown Preview**. A plain double-click shows the raw text. |
| Slides, Word, Excel (`.pptx`, `.docx`, `.xlsx`) | The site cannot show them. Right-click → **Download**, then open the file in PowerPoint, Word or Excel. On GitHub, open the file and use the download button. |
| PDF | Double-click to view in the browser, or download it. |

If Office opens a downloaded file in **Protected View**, click **Enable Editing**. Excel needs this
before Solver will run.

### Run a notebook

- **Run the first code cell first.** What it does depends on the week:

  | Weeks | What the first code cell does |
  | --- | --- |
  | 01 | The tutorial notebook installs `ipywidgets` (`%pip install ipywidgets`). Run it again every time you reopen or restart the notebook. |
  | 02 | Nothing: there is no install cell. `linprog` is part of SciPy, which is already on the site. |
  | 03 onwards | In notebooks that use Pyomo, it installs **Pyomo** and the **HiGHS** solver into the open browser tab. The first time this takes about a minute. |

  An install lasts only for that tab: after reloading the page, or in a new tab, run it again.
- Then choose **Run → Run All Cells**, or click a cell and press **Shift + Enter** to run it and move
  to the next one.
- **Always run cells from top to bottom.** Later cells use things made in earlier ones.
- While a cell runs it shows `[*]`; when it finishes the star becomes a number.
- Most notebooks are saved **without results**: you only see output after you run them.
- To start again cleanly: **Kernel → Restart Kernel and Run All Cells…**

### Save your work (important)

Anything you change on the site is stored **only in that browser on that computer**. Clearing browser
data, using a private window or moving to another computer loses it.

- **Before you change a notebook**, right-click it → **Duplicate**, and work in the copy.
- **Before you leave**, right-click each notebook you changed → **Download**.
- To write your own notebook: **File → New → Notebook** (kernel **Python (Pyodide)**), or duplicate
  the closest demo notebook. If it uses Pyomo, keep (or copy in) the demo's first code cell.

### Working outside the site

Notebooks also run in **Google Colab** or **Anaconda Jupyter**: download the `.ipynb` and open it
there. In the Pyomo notebooks the first cell installs what is needed.

---

## 9. How to work through a week

Every weekly README starts with what the week covers and how to open its files, and gives a
step-by-step plan. Most also have:
- the key ideas explained;
- a guide to the slides;
- the tutorial with hints;
- answers to check against;
- common problems;
- self-test questions;
- a checklist;
- a list of assumptions.

Week 01 and Week 04 have no assumptions section, and Week 01 has no self-test.

In general:

1. **Read the weekly README's plan** and its "key ideas" section.
2. **Go through the slides.** Run each demo notebook when the README tells you to, and compare your
   output with the expected result it gives.
3. **Answer each demo's "What do you notice?" or "Try it" question before you open its hidden answer.**
4. **Do the tutorial.** For modelling questions:
   - write the model on paper first: decision variables, objective, constraints, real or integer;
   - then code it, usually in a copy of the closest demo notebook.
5. **Check with the answers** ([section 7](#7-where-the-answers-are)).
6. **Answer the self-test questions** and **tick the week's checklist**. You have finished the week
   when every box is ticked.
7. **Download** any notebook you changed.

---

## 10. The key ideas of the semester on one page

| Idea | What it means | Where |
| --- | --- | --- |
| **Model = variables + objective + constraints** | Decide what you choose (decision variables), what you want to make as large or small as possible (objective), and what limits you (constraints). Write it on paper before coding. | Weeks 02–04, used every week after |
| **Feasible region and vertices** | The points that satisfy every constraint. For an LP the best answer is at a corner (vertex) of this region; the simplex method moves from corner to corner. | Weeks 01–02 |
| **Infeasible / unbounded** | No point satisfies every constraint / the objective can improve for ever (a limit is missing). | Weeks 02–03 |
| **Binding constraint, slack** | A constraint is binding when it holds with equality at the optimum; its slack is the unused amount. | Weeks 02–04 |
| **Integer and binary variables** | Whole numbers, or 0/1 for yes/no decisions. Rounding an LP answer can be infeasible or far from the best integer answer. | Weeks 03, 05–06 |
| **Big-M** | Adding $M$ times a binary variable (or $M(1 - \text{binary})$) to a constraint switches it off for one value of the binary and on for the other. This gives either/or and if-then rules. | Weeks 07, 09–11 |
| **Exact algorithms you do by hand** | Johnson's rule (two-machine flow shop), Dijkstra (shortest path, no negative weights), Prim and Kruskal (minimum spanning tree). | Weeks 07–08 |
| **Subtours and MTZ** | A TSP model with "one arc in, one arc out" per city can split into several small loops; the MTZ constraints remove them. | Weeks 09–10 |
| **Two kinds of "best" route** | Minimise the total distance, or the longest single route (a minimax objective). | Week 10 (and minimax in Week 11) |
| **NP-hard and heuristics** | No method is known that solves every large case quickly. A heuristic finds a good answer fast but does not prove it is the best. | Weeks 07, 09, 10, 11 |

---

## 11. Reading results and checking your answers

These points come up in almost every week:

- **Python counts from 0.** In most notebooks item 1 is `x[0]`, item 2 is `x[1]`, and so on. Some
  weeks number things differently in the slides and the code; the weekly README gives a table when
  this matters (for example Weeks 06 and 07).
- **`linprog` only minimises** (Weeks 02–03). To maximise, give it minus the objective and change the
  sign of the answer back. Pyomo can maximise directly with `sense=maximize`; without it, Pyomo
  minimises.
- **Pyomo's output.**
  - `model.pprint()` prints the model with the data filled in. Compare it with your paper model to
    find typing mistakes.
  - `model.display()` gives the results. Under *Variables*, the `Value` column is the solution. Under
    *Constraints*, if `Body` equals a bound, that constraint is **binding**.
- **The HiGHS log.** Several weekly READMEs (Weeks 03 and 05–07) say that in the browser HiGHS prints
  a long progress log. If you see one, skip to its end: `Status Optimal` means the solver proved it
  found the best answer. Notebooks that print their own summary show this as `optimal` (for example
  `Status: optimal` in Week 11).
- **Tiny rounding errors.** Values like `-0.0`, `1e-10`, `0.9999999` or `49.99999999999984` are the
  computer's rounding: read them as 0, 0, 1 and 50.
- **Different but equal answers.** Many problems have several optimal solutions. If your **objective
  value** matches the expected one but the chosen items, order or picture differ, check that your
  answer satisfies every constraint. If it does, it is also correct.
- **Slides that show GLPK.** Some slides and the scripts in `5 Source Files` use
  `SolverFactory('glpk')`. GLPK does not run in the browser. The notebooks use
  `SolverFactory('appsi_highs')` instead; the models and answers are the same.

---

## 12. If something goes wrong

Each weekly README has its own table of problems. These are the ones that recur across the weeks:

| What you see | What to do |
| --- | --- |
| The notebook says "busy" or the first cell runs for a long time | The first run downloads Python and the packages. Wait about a minute. If nothing happens, reload the page and run the first cell again. |
| `ModuleNotFoundError` (for example `No module named 'pyomo'`) | Run **this** notebook's first code cell again. Each notebook has its own Python, so an install in another notebook (or before a page reload) does not count. Week 02's notebooks need no install. |
| `NameError: name '…' is not defined` | A cell was run before the cell above it. Choose **Run → Run All Cells**, or **Kernel → Restart Kernel and Run All Cells…** |
| `ApplicationError: No executable found for solver 'glpk'` | Use `SolverFactory('appsi_highs')`. GLPK and CBC do not run in the browser. |
| The kernel dies, or "table index is out of bounds" | You used SciPy's `linprog` and Pyomo in the same notebook. Keep them in separate notebooks. |
| The solver says `infeasible`, `unbounded`, or `RuntimeError: A feasible solution was not found…` | Sometimes this is the expected answer (the weekly README says so, for example in Week 10). Otherwise check each constraint's direction (`<=`, `>=`, `==`) and right-hand side; for unbounded, look for a missing limit. |
| A cell shows `[*]` for minutes | Some solves are slow on purpose. The weekly README warns you: for example, Week 11 notebook 2 takes 2–4 minutes. In Week 09, do not try 40 or more cities, and use **Kernel → Restart** rather than Interrupt if a run takes too long. |
| A `.pptx`, `.docx` or `.xlsx` does not open on the site | Expected. Download it and open it in PowerPoint, Word or Excel. |
| No **Solver** button in Excel | Switch on the Solver add-in (Week 02 README, section 4), and click **Enable Editing**. |
| `ModuleNotFoundError: No module named 'ortools'` or `'gurobipy'` | These do not run on the course site. Week 07 uses Google Colab for OR-Tools; Week 06 translates Gurobi examples into Pyomo. |
| Week 01's tutorial widgets do not appear | Run the notebook's first cell (`%pip install ipywidgets`) again after every reopen or restart. |
| Your changes have disappeared | Work is stored only in the browser you used. Download notebooks before you leave next time. |
| The site does not work at all | Use a recent Chrome, Edge or Firefox. Or download the notebook and run it in Google Colab or Anaconda Jupyter. |

---

## 13. Test yourself

These questions connect the weeks. Answer each one on paper first, then open the answer.

**Q1.** `linprog` can only minimise. How do you use it to maximise $P = 5x + 7y$?
<details><summary>Answer</summary>

Minimise $-P = -5x - 7y$ instead, then change the sign of the optimal value back. The optimal $x$ and
$y$ are the same (Weeks 02–03).
</details>

**Q2.** The LP "maximise $2x + 3.5y$" has its optimum at $(1.9, 2.9)$. Why not just round it to get the
best integer answer?
<details><summary>Answer</summary>

The integer points next to $(1.9, 2.9)$ are either infeasible or poor ($P = 9$ or $11$). The best
integer point, $(3, 2)$ with $P = 13$, is somewhere else (Week 03, slides 22–23). You have to solve the
integer problem itself. This example comes back in Week 05 demo 1 and the Week 11 recap.
</details>

**Q3.** In `model.display()`, how do you see that a constraint is binding? What does that tell you?
<details><summary>Answer</summary>

Its `Body` equals its bound. The resource is used up: it has no slack, and it limits the optimum
(Weeks 03–04).
</details>

**Q4.** Big-M appears in Weeks 07, 09, 10 and 11. What does it do in all of them?
<details><summary>Answer</summary>

A term such as $M \times (\text{binary})$ is added to a constraint. For one value of the binary the term
is 0 and the constraint holds as written. For the other value it adds a very large number, so the
constraint is always satisfied, that is, switched off. The solver chooses the binary, and so chooses
which constraint applies. Examples:
- which of two operations on the same machine goes first (Week 07);
- the MTZ ordering constraint, which applies only when the tour goes straight from city $i$ to city $j$
  (Weeks 09–10);
- which side two rectangles are on (Week 11).

$M$ must be large enough to switch a constraint off. A needlessly huge $M$ can cause rounding trouble.
</details>

**Q5.** Why can Dijkstra's algorithm give a wrong answer when a weight is negative?
<details><summary>Answer</summary>

Dijkstra makes a vertex *permanent* as soon as it has the smallest label, assuming no later path can
get cheaper. With a negative weight a longer start can become cheaper later. In Week 08's example
Dijkstra gives 1–2 with length 1, but 1–3–4–2 has length $3 + (-5) + 1 = -1$.
</details>

**Q6.** A TSP model says "every city has exactly one arc in and one arc out". Why is that not enough?
<details><summary>Answer</summary>

The arcs can form several small loops (**subtours**), for example 1 → 2 → 1 and 3 → 4 → 5 → 3. Every
city is entered and left once, but there is no single tour. Subtours are often shorter, so the solver
picks them. The MTZ constraints remove them (Week 09); Week 10 builds on the same model.
</details>

**Q7.** In Week 10, two vehicle-routing models give different "best" routes. Why?
<details><summary>Answer</summary>

They have different objectives:
- one minimises the **total distance** of all routes;
- the other minimises the **longest single route** (a minimax objective), so all deliveries finish as
  early as possible.

"Optimal" depends on the objective you choose. Week 11 makes the same point with four objectives for
packing.
</details>

**Q8.** What does "NP-hard" mean for you in practice, and what does a heuristic give you?
<details><summary>Answer</summary>

For NP-hard problems (the TSP, and packing in Week 11) no method is known that solves every large case
quickly; solve times can grow very fast with the size. A **heuristic**, such as:
- the Campbell, Dudek and Smith method for more than two machines (Week 07);
- a genetic algorithm (Week 09);
- nearest neighbour (Week 10);

finds a good answer quickly but **does not prove** it is the best. Compare Johnson's rule, which does
give the smallest possible makespan, but only for a two-machine flow shop. A MILP solver that reports
`optimal` has also proved it.
</details>

**Q9.** Your Pyomo answer has the expected objective value, but different variable values from the
answer file. Is it wrong?
<details><summary>Answer</summary>

Not necessarily. Many problems have several optimal solutions. Check that your solution satisfies
every constraint and gives the same objective value. If it does, it is also correct.
</details>

---

## 14. Key words

Each weekly README defines its own words in more detail. These are the ones used across several weeks.

| Word | Meaning |
| --- | --- |
| **Operational Research (OR)** | Using mathematical models to make better decisions |
| **Decision variable** | A quantity you choose (how many, which one, yes or no) |
| **Objective** | What you maximise or minimise |
| **Constraint** | A rule the solution must satisfy, written as an equation or inequality |
| **Feasible region** | All points that satisfy every constraint |
| **LP / ILP / MILP** | Linear programme / integer LP (all variables whole numbers) / mixed-integer LP (some variables whole numbers) |
| **Binary variable** | A variable that can only be 0 or 1, used for yes/no decisions |
| **Binding constraint, slack** | A constraint that holds with equality at the optimum / the unused amount of a constraint |
| **Infeasible / unbounded** | No solution satisfies every constraint / the objective can improve without limit |
| **Big-M** | A large constant that a binary variable uses to switch a constraint on or off |
| **Minimax** | Minimising the largest of several values (the longest route, the furthest edge) |
| **Makespan** | The time at which the last job finishes (Week 07) |
| **Network / graph** | Vertices (points) joined by edges or arcs, often with weights (Weeks 06, 08–10) |
| **Subtour** | A closed loop that visits only some of the cities (Weeks 09–10) |
| **NP-hard** | At least as hard as every problem in NP; no method is known that is fast for every large case |
| **Heuristic** | A method that finds a good answer quickly but does not prove it is the best |
| **Pyomo** | The Python modelling language used from Week 03 |
| **HiGHS** | The solver the notebooks use, `SolverFactory('appsi_highs')` |
| **GLPK** | The solver some slides and source scripts use; it does not run in the browser |
| **Notebook, cell, kernel** | A file of code and text / one block of it / the Python that runs it |

---

## 15. Checklist: have you finished the semester?

- [ ] I ticked every box on the checklist of each week, 01 to 11.
- [ ] I tried every tutorial question before looking at its answer, and checked it against
      [section 7](#7-where-the-answers-are).
- [ ] I can answer every question in [Test yourself](#13-test-yourself) without opening the answers.
- [ ] I can turn a word problem into decision variables, an objective and constraints on paper, and
      say which variables are real, integer or binary.
- [ ] I can write and solve that model in Pyomo with HiGHS, and read `model.display()`.
- [ ] I can carry out Johnson's rule, Dijkstra, Prim and Kruskal by hand.
- [ ] I can explain big-M, subtours and MTZ, and the difference between an exact method and a
      heuristic.
- [ ] I downloaded every notebook I changed.

---

## 16. Assumptions made in this README

This page was written only from the eleven weekly READMEs and the files in this folder. These points
are missing from them or do not agree between them. Check them with your lecturer or the module
handbook.

1. **Timetable, time per week, deadlines and marks.** No weekly README gives dates, deadlines or
   marks. Only Week 09 gives study times (about 4 hours in total, as suggestions). Week 02 says the
   course files mention no hand-in.
2. **Assessment.** Week 08 says minimum spanning trees are part of the in-class test revision, in
   `Assignments/03-in-class-test/revision/` (outside this folder). Week 09 says it does not know
   whether the TSP is assessed. No other week mentions assessment.
3. **Module handbook.** Week 01 points to `Handbook/Module Handbook Operational Research (5CM522)
   2526.pdf` (two folders up from this page). Week 08 notes that the handbook calls Week 8 *"Network
   Models: Transportation and Transhipment Problem"*, but the Week 08 folder teaches shortest paths and
   minimum spanning trees. Week 08 says transhipment examples are in Semester 2.
4. **Course site address.** The repository's main `README.md` gives the address
   <https://ctsallis.github.io/operational_research/>. Weeks 02, 08, 10 and 11 also list it among their
   assumptions; Week 10 takes it from the link on its last slide. Weeks 02 and 07 also use longer forms that start
   with the same address (`…/lab/index.html`). If your course gives you a different link, use that one.
5. **`00_START_HERE.ipynb`.** Weeks 02–07 and 11 tell you to run it. Weeks 02–04 and 07 say once per
   session; Weeks 05, 06 and 11 say in your first session. Weeks 01, 08, 09 and 10 do not mention it.
   This page says "at the start of a session" to cover both.
6. **When answers become available.** Several answer notebooks (Weeks 03, 04 and 05) say "Release after
   the practical", but the answers are already in the folders. The weekly READMEs assume a student
   working alone tries each question first.
7. **The HiGHS log.** Weeks 03 and 05–07 say HiGHS prints a long log in the browser, while Week 11's
   notebooks 2–4 say `tee=False` hides it (Week 11's notebook 1 asks for the log with `tee=True`).
   Either way, the result lines at the end are what matter.
8. **After Week 11.** The Week 11 README does not say what comes next. Week 08 refers to a Semester 2
   folder, but no Semester 1 README describes it.
9. **Software versions.** The menu names (Run, Kernel, Open With, Duplicate) and the Office steps are
    those described when the weekly READMEs were written; they may change slightly.

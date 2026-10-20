# Semester 1 – Operational Research: Lectures

This is the starting page for Semester 1. Read it once from top to bottom, then go to
[Week 01](Week%2001%20-%20Introduction%20to%20Operational%20Research/README.md) and work through the
weeks in order. Every week has its own README that tells you exactly what to open, in what order, what
result you should get and how to check your answers. This page tells you what the semester covers,
what you need, and the instructions that are the same in every week, so the weekly pages make sense.

---

## Contents

1. [What the semester covers](#1-what-the-semester-covers)
2. [The weeks at a glance](#2-the-weeks-at-a-glance)
3. [How the weeks build on each other](#3-how-the-weeks-build-on-each-other)
4. [What you need](#4-what-you-need)
5. [How every week folder is organised](#5-how-every-week-folder-is-organised)
6. [How to use the course site (same every week)](#6-how-to-use-the-course-site-same-every-week)
7. [How to work through a week](#7-how-to-work-through-a-week)
8. [Reading results and checking your answers](#8-reading-results-and-checking-your-answers)
9. [If something goes wrong](#9-if-something-goes-wrong)
10. [Things this page could not confirm](#10-things-this-page-could-not-confirm)

---

## 1. What the semester covers

Operational Research (OR) uses mathematical models to make better decisions. Over eleven weeks you
learn to turn a problem written in words into a model, solve it on a computer, and judge whether the
answer makes sense.

- **Weeks 01–04: linear programming.** The maths you need (equations, matrices, inequalities,
  feasible regions), then linear programmes (LPs): solving them by drawing, in matrix form, in Python
  with SciPy's `linprog`, with Excel Solver, and then with **Pyomo**, a Python modelling language.
  Week 04 is about good modelling: combining objectives, slack variables and planning a whole system.
- **Weeks 05–06: integer programming.** Variables that must be whole numbers or 0/1 (binary), and
  classic models: knapsack, set covering, vertex cover, matching and assignment.
- **Weeks 07–11: applications.** Scheduling (flow shop and job shop), networks (shortest paths and
  minimum spanning trees), the Travelling Salesman Problem, the Vehicle Routing Problem, and floor
  planning (packing rectangles). These use the integer-programming tricks from Weeks 05–06, together
  with algorithms and heuristics that you carry out by hand or in Python.

Python runs **inside your web browser** on the course site, so there is nothing to install.

---

## 2. The weeks at a glance

Click a week to open its README. "Work" says how most of the week is done; "Tutorial" says where its
exercises are.

| Week | What it is about | Work | Tutorial |
| --- | --- | --- | --- |
| [01 – Introduction to Operational Research](Week%2001%20-%20Introduction%20to%20Operational%20Research/README.md) | What OR is; revision of linear equations, matrices, determinants, inequalities and feasible regions, done in NumPy and Desmos | Pen and paper, Python (NumPy) | Notebook, Exercises 1–8 |
| [02 – Linear Programming 1](Week%2002%20-%20Linear%20Programming%201/README.md) | Writing a word problem as an LP; solving it by drawing, in matrix form, with `linprog` and with Excel Solver; the idea of the simplex method | Pen and paper, Python (`linprog`), Excel | Word sheet, Q1–Q6 |
| [03 – Linear Programming 2](Week%2003%20-%20Linear%20Programming%202/README.md) | LPs in Pyomo with summation notation; unbounded LPs; integer (ILP) and mixed-integer (MILP) programmes, and why rounding is not enough | Python (Pyomo) | Word sheet, Q1–Q2 |
| [04 – Mathematical Programming: Modelling](Week%2004%20-%20Mathematical%20Programming%20-%20Modelling/README.md) | Extending a model, combining two objectives, slack variables and binding constraints, one model for a whole system | Python (Pyomo) | Word sheet, Q1–Q2 |
| [05 – Mixed Integer Programming](Week%2005%20-%20Mixed%20Integer%20Programming/README.md) | Binary variables; the knapsack, set covering and purchasing problems; linking an amount to a yes/no decision; logical rules | Python (Pyomo) | Word sheet, Q1–Q3 |
| [06 – Integer Linear Programming: Further Problems](Week%2006%20-%20Integer%20Linear%20Programming%20-%20Further%20Problems/README.md) | Costed set cover written three ways; graph problems (edge cover, vertex cover, matching); the assignment problem | Python (Pyomo) | Last slide of the lecture (slide 28), tasks 1–5 |
| [07 – Flow Shop and Job Shop Scheduling](Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/README.md) | Makespan and Gantt charts; Johnson's rule and the Campbell, Dudek and Smith heuristic; job shop as a big-M MILP; a first look at constraint programming | Pen and paper, Excel, Python (Pyomo), Google Colab | Word sheet (flow shop) and notebook (job shop) |
| [08 – Networks: Shortest Paths and MST](Week%2008%20-%20Networks%20-%20Shortest%20Paths%20and%20MST/README.md) | Dijkstra's algorithm, and why it fails with negative weights; minimum spanning trees with Prim and Kruskal | Pen and paper only (one optional checking notebook) | Word sheet, Q1–Q2 |
| [09 – Travelling Salesman Problem](Week%2009%20-%20Travelling%20Salesman%20Problem/README.md) | Counting tours; P, NP and NP-hard; the TSP as a MILP; subtours and the Miller–Tucker–Zemlin (MTZ) constraints; a genetic algorithm | Python (Pyomo) | Slide 22, done in the demo notebook |
| [10 – Vehicle Routing Problem](Week%2010%20-%20Vehicle%20Routing%20Problem/README.md) | From the TSP to several vehicles: demand, capacity and flow; minimising total distance or the longest route; the nearest-neighbour heuristic | Python (Pyomo), pen and paper | No sheet: notebook questions and exercises in the README |
| [11 – Floor Planning](Week%2011%20-%20Floor%20Planning/README.md) | Packing rectangles without overlap: big-M with binary variables, rotation, fitting the most items, keeping connected items close | Python (Pyomo) | No sheet: notebook questions and questions in the README |

> **If a link above does not open on the course site:** the links work when this page is viewed on
> GitHub. On the course site, open the week's folder in the file browser instead and open its
> `README.md` as described in [section 6](#6-how-to-use-the-course-site-same-every-week).

---

## 3. How the weeks build on each other

Do the weeks **in order**. Each one assumes the earlier ones. The table lists what each weekly README
says you need first.

| Week | Says you need first |
| --- | --- |
| 02 | Week 01: vectors and matrices (matrix × vector) |
| 03 | Week 02: feasible regions, matrix form, `linprog`; Week 02 tutorial Q5 and Q6 come back in the lecture |
| 04 | Weeks 02 and 03: the diet problem and the Icki-Toffee model (your own, or the Week 03 answer notebook) |
| 05 | Week 03 (Pyomo, Icki-Toffee) and Week 04 (turning a word problem into a model) |
| 06 | Week 05 (binary variables, the fire-station set cover); Weeks 03–04 (building a Pyomo model) |
| 07 | Weeks 03–04 (Pyomo) and Week 05 (binary variables) |
| 09 | Weeks 05–06 (binary variables, MILP), earlier weeks for Pyomo, Week 08 (networks) |
| 10 | Week 09 (TSP tours and the variable $x_{ij}$); its slides 3–5 recap it |
| 11 | Week 05 (binary variables, big-M) and Week 07 (either/or constraints) |

The Week 08 README does not list earlier weeks; its algorithms are done by hand.

Some examples **come back** in later weeks. When you meet one again, look back at where it started:

| Example | Where it appears |
| --- | --- |
| Chairs and tables LP (maximise $5x + 7y$) | Week 02 lecture and demos → Week 03 demo 1 (in Pyomo) |
| Simplex method demonstration deck (optimum C = (4, 1.5), P = 26) | Week 02 and Week 03 (the same file is in both folders) |
| Diet problem (10 foods) | Week 02 tutorial Q6 → Week 03 demos 2–4 → Week 04 slides 8–10 |
| Icki-Toffee candy selection | Week 03 tutorial Q2 → Week 04 tutorial Q1 → Week 05 tutorial Q3 |
| Integer LP, maximise $2x + 3.5y$ | Week 03 demos 5–6 → Week 05 demo 1 → Week 11 recap (slides 1–4) |
| Fire stations (set covering) | Week 05 demo 3 and tutorial Q2 → Week 06 demos 1–3 (with costs) |
| Minimum vertex cover | Week 05 demo 8 (optional preview) → Week 06 demo 4 |
| A large number (big-M) that a binary variable uses to switch a constraint on or off | Week 07 (job shop) → Week 09 (MTZ) → Week 10 (VRP) → Week 11 (non-overlap) |
| TSP with MTZ constraints | Week 09 → start of Week 10's notebook |

---

## 4. What you need

| You need | Used in | Notes |
| --- | --- | --- |
| A recent **Chrome, Edge or Firefox** | Every week | Runs the course site and its Python notebooks. Nothing to install. Week 02 says Safari works but is slow. |
| An internet connection | Every week | The first run of a notebook downloads Python and its packages into the browser tab. |
| **PowerPoint** | Every week | The lecture slides are `.pptx` files. |
| **Word** | Weeks 02, 03, 04, 05, 07, 08 | Tutorial sheets and written answers are `.docx` files. |
| **Desktop Excel with the Solver add-in** | Week 02 (Solver); Week 07 (Excel workings and tutorial) | Week 02's README shows how to switch Solver on. Excel for the web is not covered. |
| A PDF reader | Weeks 06, 07, 08, 10 | Optional annotated slides and further reading. |
| Pen, paper (a ruler or graph paper helps) | Weeks 01, 02, 07, 08, and modelling on paper in most weeks | Week 08 is done entirely by hand. |
| **Desmos** (free online graphing calculator) | Weeks 01 and 02; optional in Week 03 | <https://www.desmos.com/calculator> |
| A **Google account** for **Google Colab** | Week 07, job shop tutorial Q4–Q5 | Google OR-Tools does not run on the course site. |
| MATLAB | Never required | Some `5 Source Files` folders contain MATLAB versions. You do not need them. |

---

## 5. How every week folder is organised

The sub-folders are numbered the same way in every week. Not every week has all of them.

| Folder | What is in it | Do you need it? |
| --- | --- | --- |
| `1 Lecture` | The slides (`.pptx`). In Week 07 also job shop lecture notes (a notebook); in Week 10 also written lecture notes (`.md`) | **Yes** |
| `2 Lecture Demos` | Notebooks (and in Weeks 02 and 07 Excel files) that run the lecture's examples | **Yes**. Week 08 has none. |
| `3 Tutorial` | The tutorial sheet or notebook | **Yes**. Weeks 06, 09, 10 and 11 have no tutorial folder (see [section 2](#2-the-weeks-at-a-glance)). |
| `4 Tutorial Answers` | Worked answers: Word files, notebooks, answer slides | **Yes**, but only **after** you have tried the questions |
| `5 Source Files` | The original scripts the notebooks were made from, older versions, staff notes | **No.** Every week that has this folder says you can ignore it. |
| `6 Further Reading` | Papers and extra slides | Optional |

**Slide numbers** in the weekly READMEs are the numbers PowerPoint shows in its slide list on the
left. Some decks have a hidden blank slide (slide 3 in Weeks 03, 04 and 05; slide 2 in Week 06). It is
skipped in a slide show but still counts in the numbering.

**Star marks** on tutorial sheets: one star (\*) is a medium question, two stars (\*\*) a hard one.

---

## 6. How to use the course site (same every week)

### Open the site

1. Go to **<https://ctsallis.github.io/operational_research/>** in Chrome, Edge or Firefox.
2. **Once per session**, open `00_START_HERE.ipynb` (at the top of the file list) and choose
   **Run → Run All Cells**. If every cell prints `OK`, the course notebooks will run in your browser.
3. In the file browser on the left, double-click `Lectures` → `Semester 1` → the week's folder.

### Open each kind of file

| File | How to open it |
| --- | --- |
| Notebook (`.ipynb`) | Double-click it. It opens and runs in the browser. If asked to choose a kernel, choose **Python (Pyodide)**. |
| README (`.md`) | Right-click → **Open With** → **Markdown Preview**. A plain double-click shows the raw text. |
| Slides, Word, Excel (`.pptx`, `.docx`, `.xlsx`) | The site cannot show them. Right-click → **Download**, then open the file in PowerPoint, Word or Excel. On GitHub, open the file and use the download button. |
| PDF | Double-click to view in the browser, or download it. |

If Office opens a downloaded file in **Protected View**, click **Enable Editing** (Excel needs this
before Solver will run).

### Run a notebook

- **Run the first code cell first.** In notebooks that use Pyomo (Week 03 onwards), it installs
  **Pyomo** and the **HiGHS** solver into the open browser tab. The first time this takes about a minute. The install lasts only
  for that tab: after reloading the page, or in a new tab, run it again.
- Then choose **Run → Run All Cells**, or click a cell and press **Shift + Enter** to run it and move
  to the next one.
- **Always run cells from top to bottom.** Later cells use things made in earlier ones.
- While a cell runs it shows `[*]`; when it finishes the star becomes a number.
- Some notebooks are saved **without results**: you only see output after you run them.
- To start again cleanly: **Kernel → Restart Kernel and Run All Cells…**

### Save your work (important)

Anything you change on the site is stored **only in that browser on that computer**. Clearing browser
data, using a private window or moving to another computer loses it.

- **Before you change a notebook**, right-click it → **Duplicate**, and work in the copy.
- **Before you leave**, right-click each notebook you changed → **Download**.
- To write your own notebook: **File → New → Notebook** (kernel **Python (Pyodide)**), or duplicate
  the closest demo notebook. If it uses Pyomo, keep (or copy in) the demo's first code cell.

### Working outside the site

Every notebook also runs in **Google Colab** or **Anaconda Jupyter**: download the `.ipynb` and open it
there. The first cell installs what is needed.

---

## 7. How to work through a week

Each weekly README has a study plan. Most also have the same parts: a guide to the slides, the key
ideas explained, the tutorial with hints, answers to check against, common problems, self-test
questions, a checklist and a list of assumptions. In general:

1. **Read the weekly README's plan** and the "key ideas" section.
2. **Go through the slides.** Run each demo notebook when the README tells you to, and compare your
   output with the expected result it gives.
3. **Answer each demo's "What do you notice?" or "Try it" question before you open its hidden answer**
   (click the **Answer** line to reveal it).
4. **Do the tutorial.** For modelling questions, write the model on paper first (decision variables,
   objective, constraints, real or integer), then code it, usually in a copy of the closest demo
   notebook.
5. **Check with the answers** in `4 Tutorial Answers` and in the README. The answers are already in
   the folders: it is up to you to try each question first.
6. **Answer the self-test questions** and **tick the checklist** at the end of the README. You have
   finished the week when every box is ticked.
7. **Download** any notebook you changed.

---

## 8. Reading results and checking your answers

These points come up in almost every week:

- **Python counts from 0.** In most notebooks item 1 is `x[0]`, item 2 is `x[1]`, and so on. Some
  weeks number things differently in the slides and the code; the weekly README gives a table when
  this matters (for example Weeks 06 and 07).
- **`linprog` only minimises** (Weeks 02–03). To maximise, give it minus the objective and change the
  sign of the answer back. Pyomo can maximise directly with `sense=maximize`; without it, Pyomo
  minimises.
- **Pyomo's output.** `model.pprint()` prints the model with the data filled in: compare it with your
  paper model to find typing mistakes. `model.display()` gives the results: under *Variables* the
  `Value` column is the solution; under *Constraints*, if `Body` equals a bound, that constraint is
  **binding**.
- **The HiGHS log.** In the browser HiGHS prints a long progress log even when the code does not ask
  for it. Skip to the end: `Status Optimal` means the solver proved it found the best answer.
- **Tiny rounding errors.** Values like `-0.0`, `1e-10`, `0.9999999` or `49.99999999999984` are the
  computer's rounding: read them as 0, 0, 1 and 50.
- **Different but equal answers.** Many problems have several optimal solutions. If your **objective
  value** matches the expected one but the chosen items, order or picture differ, check that your
  answer satisfies every constraint. If it does, it is also correct.
- **Slides that show GLPK.** Some slides and the scripts in `5 Source Files` use
  `SolverFactory('glpk')`. GLPK does not run in the browser. The notebooks use
  `SolverFactory('appsi_highs')` instead; the models and answers are the same.

---

## 9. If something goes wrong

Each weekly README has its own table of problems. These are the ones that recur across the weeks:

| What you see | What to do |
| --- | --- |
| The notebook says "busy" or the first cell runs for a long time | The first run downloads Python and the packages. Wait about a minute. If nothing happens, reload the page and run the first cell again. |
| `ModuleNotFoundError` (for example `No module named 'pyomo'`) | Run the notebook's first code cell again (or `00_START_HERE.ipynb` in Week 02). Installs last only for the open tab. |
| `NameError: name '…' is not defined` | A cell was run before the cell above it. Choose **Run → Run All Cells**, or **Kernel → Restart Kernel and Run All Cells…** |
| `No executable found for solver 'glpk'`, or `SolverFactory('glpk')` fails | Use `SolverFactory('appsi_highs')`. GLPK and CBC do not run in the browser. |
| The kernel dies, or "table index is out of bounds" | You used SciPy's `linprog` and Pyomo in the same notebook. Keep them in separate notebooks. |
| The solver says `infeasible`, `unbounded`, or `RuntimeError: A feasible solution was not found…` | Sometimes this is the expected answer (the weekly README says so). Otherwise check each constraint's direction (`<=`, `>=`, `==`) and right-hand side; for unbounded, look for a missing limit. |
| A `.pptx`, `.docx` or `.xlsx` does not open on the site | Expected. Download it and open it in PowerPoint, Word or Excel. |
| No **Solver** button in Excel | Switch on the Solver add-in (Week 02 README, section 4), and click **Enable Editing**. |
| `ModuleNotFoundError: No module named 'ortools'` or `'gurobipy'` | These do not run on the course site. Week 07 uses Google Colab for OR-Tools; Week 06 translates Gurobi examples into Pyomo. |
| Your changes have disappeared | Work is stored only in the browser you used. Download notebooks before you leave next time. |
| The site does not work at all | Use a recent Chrome, Edge or Firefox. Or download the notebook and run it in Google Colab or Anaconda Jupyter. |

---

## 10. Things this page could not confirm

This page was written only from the eleven weekly READMEs. These points are missing from them or do
not agree between them. Check them with your lecturer or the module handbook.

1. **Timetable, time per week, deadlines and marks.** No weekly README gives dates, deadlines or marks,
   and only Week 09 gives rough study times (as suggestions). Week 02 says no hand-in is mentioned in
   the course files.
2. **Assessment.** Week 08 says minimum spanning trees are part of the in-class test revision, in
   `Assignments/03-in-class-test/revision/` (outside this folder). Week 09 says it does not know
   whether the TSP is assessed. No other week mentions assessment.
3. **Module handbook.** Week 01 points to `Handbook/Module Handbook Operational Research (5CM522)
   2526.pdf` (two folders up from this page). Week 08 notes that the handbook calls Week 8 *"Network
   Models: Transportation and Transhipment Problem"*, but the Week 08 folder teaches shortest paths and
   minimum spanning trees. Week 08 says transhipment examples are in Semester 2.
4. **Course site address.** Weeks 02 and 11 say the address
   <https://ctsallis.github.io/operational_research/> is assumed (the repository's GitHub Pages site)
   rather than confirmed. Week 02 gives the longer form `…/operational_research/lab/index.html`. If your
   course gives you a different link, use that one.
5. **`00_START_HERE.ipynb`.** Weeks 02–07 and 11 tell you to run it once per session; Weeks 01, 08, 09
   and 10 do not mention it.
6. **When answers become available.** Several answer notebooks say "Release after the practical", but
   the answers are already in the folders. The weekly READMEs assume a student working alone tries
   each question first.
7. **Pyomo start week.** Week 09 says Pyomo was used in "Weeks 02–06", but Week 02 uses only `linprog`
   and Excel; Pyomo starts in Week 03.
8. **After Week 11.** The Week 11 README does not say what comes next. Week 08 refers to a Semester 2
   folder, but no Semester 1 README describes it.
9. **Software versions.** The menu names (Run, Kernel, Open With, Duplicate) and the Office steps are
   those described at the time the weekly READMEs were written; they may change slightly.

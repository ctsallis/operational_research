# Week 7: Flow Shop and Job Shop Scheduling

This README is your guide to Week 7 if you are studying on your own. It tells you what to open, in which
order, what each file is for, and what result you should get at every step. It also explains the key
ideas, so you can go through the week with nothing but this page, the slides, the notes and the notebooks.

**What you will learn this week**

- **Scheduling** words: job, machine (stage), processing time, **makespan**, completion time, **idle time**,
  **Gantt chart**.
- **One machine:** why the order of the jobs does not change the makespan, and why **shortest processing
  time first** (SPT) gives the smallest total completion time.
- **Flow shop, two machines:** every job visits machine A and then machine B. **Johnson's rule** finds the
  order with the smallest makespan.
- **Flow shop, more than two machines:** Johnson's rule becomes a **heuristic** (a good answer, not always the
  best). This is the **Campbell, Dudek and Smith** method.
- **How to compute a makespan by hand** with a small table (the *network* method).
- **Job shop:** every job has its **own** order of machines. You will write it as a mixed-integer linear
  program (MILP) with **big-M** constraints and solve it with **Pyomo** and the **HiGHS** solver.
- A first look at **constraint programming** and Google **OR-Tools**.

**What you need from earlier weeks**

- Weeks 3–4: building a Pyomo model (variables, objective, constraints) and solving it.
- Week 5: binary (0/1) variables. If they are new to you, look at
  [Week 5 demo 5, *Purchasing - binary variables*](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2005%20-%20Mixed%20Integer%20Programming/2%20Lecture%20Demos/5%20Purchasing%20-%20binary%20variables.ipynb)
  first. The job shop and flow shop models this week use them.

The first half of the week (flow shop, Johnson's rule) needs no programming at all: pencil, paper and the
slides are enough.

---

## Contents

1. [How to open the files](#1-how-to-open-the-files)
2. [What is in this folder](#2-what-is-in-this-folder)
3. [Your plan for the week](#3-your-plan-for-the-week)
4. [The key ideas, explained](#4-the-key-ideas-explained)
5. [Lecture guide: slides, notes and demos](#5-lecture-guide-slides-notes-and-demos)
6. [Tutorials: tasks, hints and how to check your answers](#6-tutorials-tasks-hints-and-how-to-check-your-answers)
7. [How to read the output](#7-how-to-read-the-output)
8. [If something goes wrong](#8-if-something-goes-wrong)
9. [Check your understanding](#9-check-your-understanding)
10. [Checklist: have you finished the week?](#10-checklist-have-you-finished-the-week)
11. [Assumptions](#11-assumptions)

---

## 1. How to open the files

This week has **notebooks** (`.ipynb`), which run on the course website, and **PowerPoint**, **Word**, **Excel**
and **PDF** files, which you download and open on your computer.

### Notebooks (`.ipynb`): run them in your browser

The course website runs Python **inside your web browser**. You install nothing, and you need no account.

1. Open the course site: <https://ctsallis.github.io/operational_research/>
   Use a recent **Chrome, Edge or Firefox**.
2. In the file list on the left, double-click your way to
   `Lectures` → `Semester 1` → `Week 07 - Flow Shop and Job Shop Scheduling`.
3. Open a sub-folder (for example `2 Lecture Demos`) and double-click a notebook to open it.
4. **Run the first code cell first** if the notebook uses Pyomo (all of them except the Johnson's rule demo and
   the tutorial sheet). It installs Pyomo and HiGHS into the open browser tab. The first time, this takes
   about a minute.
5. Then choose *Run → Run All Cells* from the menu, or run the cells one by one with **Shift + Enter** while
   you read.

The notebooks are saved **without results**: you only see numbers and charts after you run them.

You can also open each notebook directly with the links in [section 5](#5-lecture-guide-slides-notes-and-demos)
and [section 6](#6-tutorials-tasks-hints-and-how-to-check-your-answers).

If this is your first session on the site, open `00_START_HERE.ipynb` (at the top of the file list) and run all
its cells. If every cell prints `OK`, all the course examples will run in your browser.

> **Save your work.** Changes you make to a notebook on the site are kept **only in this browser**. Clearing
> browser data, using a private window or switching computer loses them. Before you leave, right-click the
> notebook in the file list → **Download**.

### PowerPoint, Word, Excel and PDF files: download and open them

The website cannot display these files. Download them and open them in **PowerPoint**, **Word** or
**Excel** (the PDFs in any PDF reader). The slides and the tutorial sheets contain equations and pictures, so open them in those programs
to see everything correctly. If Office opens a file in *Protected View*, click **Enable Editing**.

- **Lecture slides (start here):** [download `Week 7 - Flow Shop Scheduling.pptx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/1%20Lecture/Week%207%20-%20Flow%20Shop%20Scheduling.pptx)
- **Excel workings for the slides:** [download `2 Johnsons rule in Excel.xlsx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/2%20Lecture%20Demos/2%20Johnsons%20rule%20in%20Excel.xlsx)
  (its `Tutorial` and `Gantt 5 machines` sheets contain tutorial **answers**, see section 2)
- **Flow shop tutorial sheet:** [download `Week 7 - Flow Shop Scheduling - Tutorial.docx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/3%20Tutorial/Week%207%20-%20Flow%20Shop%20Scheduling%20-%20Tutorial.docx)
- **Flow shop tutorial answers (after you have tried it):** [download `Week 7 - Flow Shop Scheduling - Tutorial - Answers.docx`](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/4%20Tutorial%20Answers/Week%207%20-%20Flow%20Shop%20Scheduling%20-%20Tutorial%20-%20Answers.docx)
- **Further reading, optional:**
  [download *Integer vs Constraint Programming*](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/6%20Further%20Reading/Integer%20vs%20Constraint%20Programming%20%28Bockmayr%20and%20Reinert%29.pdf)
  and [download *Introduction to Constraint Programming*](https://github.com/ctsallis/operational_research/raw/main/content/Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/6%20Further%20Reading/Introduction%20to%20Constraint%20Programming%20%28Rodriguez-Carbonell%2C%20UPC%29.pdf)

Another way to get them: on the course site, right-click the file in the file list → **Download**.

**Slide numbers** in this README are the numbers PowerPoint shows in the slide list on the left. The deck has
25 slides and none is hidden.

**There are no slides for the job shop half of the week.** Its lecture material is the notebook
*Job Shop Scheduling Notes* in `1 Lecture/Notes` ([section 5](#5-lecture-guide-slides-notes-and-demos), part B).

---

## 2. What is in this folder

| Folder | File | What it is | When to use it |
| --- | --- | --- | --- |
| `1 Lecture` | `Week 7 - Flow Shop Scheduling.pptx` | The flow shop lecture (25 slides) | Read first (part A) |
| `1 Lecture/Notes` | `Job Shop Scheduling Notes.ipynb` | The job shop lecture notes: constraint programming, a puzzle, job shop scheduling, its MILP and the Pyomo code | Part B; **use this one** |
| | `Job Shop Scheduling Notes (Short).ipynb` | The same notes **without** the constraint programming and puzzle sections | Only if you want the job shop part alone |
| | `Job Shop Scheduling Notes.md`, `… (Short).md` | The text of the two notebooks, for reading only (no runnable code cell) | Not needed |
| | `assets/` | Two pictures used by the notes | Opened by the notes |
| `2 Lecture Demos` | `1 Johnsons rule.ipynb` | Johnson's rule in Python, on the two examples from the slides | With slides 13–20 |
| | `2 Johnsons rule in Excel.xlsx` | The lecturer's Excel workings: every example on the slides, step by step, with makespans and Gantt charts | With slides 15–23 |
| `3 Tutorial` | `Week 7 - Flow Shop Scheduling - Tutorial.docx` | Flow shop tutorial, questions 1–4 | After part A |
| | `Job Shop Scheduling Tutorial.ipynb` | Job shop tutorial, questions 1–5 (text only, nothing to run) | After part B |
| `4 Tutorial Answers` | `Week 7 - Flow Shop Scheduling - Tutorial - Answers.docx` | Worked answers to the flow shop tutorial, Q1–Q4 | After you have tried them |
| | `Flow Shop Q4 MILP answers.ipynb` | Flow shop tutorial Q4: a MILP that finds the best order for Q1–Q3 | After you have tried Q4 |
| | `Job Shop Q1-Q3 answers.ipynb` | Job shop tutorial Q1–Q3 solved with Pyomo, with Gantt charts | After you have tried Q1–Q3 |
| `5 Source Files` | `Python/johnsons_rule.py`, `Python/jss_tutorial_answers_pyomo.py` | The scripts two notebooks were made from | Not needed |
| | `MATLAB/johnsons_rule_demo.m` | Johnson's rule in MATLAB, with other data | Not needed |
| | `Notes (Markdown)/Job Shop Scheduling Tutorial.md` | The text of the job shop tutorial notebook | Not needed |
| | `HTML Exports/` (3 files) | Web-page copies of the notes and the job shop tutorial, for printing | Not needed |
| | `Previous Versions/` | Older material (see below) | Optional |
| `6 Further Reading` | `Integer vs Constraint Programming (Bockmayr and Reinert).pdf` | 7 pages of lecture notes (Bockmayr and Reinert, 2011) comparing integer programming and constraint programming | Optional, after part B |
| | `Introduction to Constraint Programming (Rodriguez-Carbonell, UPC).pdf` | 39 slides on constraint programming (Enric Rodríguez-Carbonell, 2023) | Optional, after part B |

**About the Excel workbook.** Its sheets follow the slides:

| Sheet | What it shows | Slides |
| --- | --- | --- |
| `Example 1` | Johnson's rule one job at a time, for the 5-job example | 15–18 |
| `Makespan 1`, `Gantt 1` | Makespan tables for the order R S T Q P (30) and the original order P Q R S T (40), and Gantt charts | 15, 18 |
| `Example 2`, `Makespan 2`, `Makespan 2 pres`, `Gantt 2` | The same for the 3-job example: the makespan table for P R Q (18), and Gantt charts for P Q R (19) and P R Q (18) | 19–20 |
| `More than 2 stages`, `Gantt more than 2` | The 4-machine example: P Q R S (52), R Q S P (46), Q R S P (46), Q R P S (48), one more order R S P Q (47), and the combined-machine tables | 21–23 |
| `Tutorial`, `Gantt 5 machines` | **The answers to flow shop tutorial Q1–Q3.** Open these only after you have tried the tutorial. | – |

**About `Previous Versions`.** You do not need these files. They are older versions of this week's material:

- `Flow Shop Scheduling (2023-24 slides).pptx`: last year's deck (28 slides). Its slides 23–24, *Determining
  Makespan via Network* and *Easily Converted to Excel*, explain the table method of
  [section 4.5](#45-computing-a-makespan-by-hand-the-network-method), which this year's deck no longer has.
- `Flow Shop Scheduling (2020-21 slides, annotated).pdf`: an older deck with the lecturer's handwriting.
- `Flow Shop Scheduling Tutorial Answers (older export).pdf`: an **out-of-date** copy of the answers. On its
  page 5 the network for "A+B and D+E" is for the wrong order (R T S Q P, 72). **Use the `.docx` in
  `4 Tutorial Answers` instead.**

**About `5 Source Files`.** Every Python script has a notebook version, and the first cell of that notebook names the
script it came from. The notebooks that solve a model use the HiGHS solver, which runs in the browser.

---

## 3. Your plan for the week

Work in this order. Try each tutorial question **before** you open its answer: the answers are in the folder,
so it is up to you.

**Part A: flow shop (slides)**

1. Run `00_START_HERE.ipynb` once if you have not used the site before (section 1).
2. Read slides 1–12 with [sections 4.1–4.3](#41-words-you-need-this-week) of this README.
3. Read slides 13–20 (Johnson's rule) and [section 4.4](#44-johnsons-rule-two-machines-slides-1320). Work the
   two examples on paper first, then run demo 1 and look at the Excel sheets `Example 1` and `Example 2`.
4. Learn the table method for the makespan ([section 4.5](#45-computing-a-makespan-by-hand-the-network-method)).
5. Read slides 21–24 (more than two machines) with [section 4.6](#46-more-than-two-machines-campbell-dudek-and-smith-slides-2124).
6. Do the **flow shop tutorial** Q1–Q3 on paper or in Excel ([section 6.1](#61-flow-shop-tutorial-word-file)),
   then check them with the answers `.docx`.

**Part B: job shop (notes)**

7. Open *Job Shop Scheduling Notes* and read sections 1–2 (constraint programming, the puzzle) with
   [section 4.9](#49-constraint-programming-notes-sections-12).
8. Read section 3 (job shop scheduling) with [sections 4.7–4.8](#47-job-shop-scheduling-notes-section-3), run
   the Pyomo cell, and do the *Try it* at the end.
9. Do flow shop tutorial **Q4** (a MILP for the flow shop, [section 4.8](#48-big-m-scheduling-as-a-mixed-integer-linear-program)),
   then check it with `Flow Shop Q4 MILP answers.ipynb`.
10. Do the **job shop tutorial** Q1–Q3 in the browser ([section 6.2](#62-job-shop-tutorial-notebook)), then check
    them with `Job Shop Q1-Q3 answers.ipynb`.
11. Do job shop tutorial Q4–Q5 (OR-Tools examples) in Google Colab.
12. Answer the questions in [section 9](#9-check-your-understanding) and tick the checklist in
    [section 10](#10-checklist-have-you-finished-the-week).

---

## 4. The key ideas, explained

### 4.1 Words you need this week

| Word | Meaning |
| --- | --- |
| **Job** | Something to be processed, for example a product or a customer. Jobs are named P, Q, R, … on the slides. |
| **Machine** (or **stage**) | Something that processes one job at a time. Named A, B, C, … on the slides and $M_0, M_1, …$ in the notes. |
| **Processing time** $p$ | How long a job needs on a machine. |
| **Operation** | One job on one machine. A job made of 3 steps has 3 operations. |
| **Schedule** | When each operation starts on its machine. In a flow shop, it is enough to give the **order** of the jobs. |
| **Completion time** $C_j$ | The time at which job $j$ is finished. |
| **Makespan** $C_{\max}$ | The time at which the **last** job is finished: the total time to complete all jobs. This week we minimise it. |
| **Idle time** | Time during which a machine does nothing, between time 0 and the makespan. |
| **Gantt chart** | A picture of a schedule: one row per machine, time from left to right, one coloured block per operation. |
| **Flow shop** | Every job visits the machines in the **same** order (A, then B, then C, …). |
| **Job shop** | Every job has **its own** order of machines. |
| **Heuristic** | A quick method that gives a good answer, but not always the best one. |
| **NP-hard** | A class of problems for which no fast method is known that always finds the best answer. In practice, the time needed grows explosively with the problem size. |

### 4.2 One machine: shortest processing time first (slides 2–7)

With **one** machine (a supermarket queue at one checkout), the jobs are processed one after another, so the
**makespan is the same in every order**: it is the sum of all processing times.

The **completion times** do depend on the order. With jobs of length $p_1, p_2, …, p_n$ done in that order,
job 1 finishes at $p_1$, job 2 at $p_1 + p_2$, and so on. The sum of all completion times is

$$\sum_j C_j = n\,p_1 + (n-1)\,p_2 + \dots + 2\,p_{n-1} + p_n .$$

The first job is counted $n$ times, so it should be the shortest. **Shortest processing time first (SPT)** puts
the jobs in increasing order of length, $p_1 \le p_2 \le \dots \le p_n$, and gives the smallest total completion
time. Slides 4–7 prove this: a small lemma about scalar products (slides 4–6), then the theorem (slide 7).

*Example:* jobs of length 4, 1 and 3. In that order they finish at 4, 5 and 8 (sum 17). In SPT order 1, 3, 4 they
finish at 1, 4 and 8 (sum 13). The makespan is 8 both times.

### 4.3 Flow shop, makespan and idle time (slides 8–12)

In a **flow shop** every job goes first to machine A, then to machine B (and so on). A machine does one job at
a time, and a job can only start on B once it has finished on A. Both machines process the jobs in the same
order, so a schedule is just an **order** of the jobs.

*Slides' Example 2:* three jobs with these times.

| Job | P | Q | R |
| --- | --- | --- | --- |
| Machine A | 2 | 4 | 6 |
| Machine B | 3 | 3 | 7 |

- In the order **P Q R**, machine A works from 0 to 12 and R finishes on B at **19** (slide 10).
- In the order **P R Q**, everything is finished at **18** (slides 10–11).

**Idle time** of a machine = makespan − total processing time on that machine. For P R Q: machine A works
2 + 6 + 4 = 12 units, so it is idle 18 − 12 = **6**; machine B works 3 + 7 + 3 = 13, so it is idle
18 − 13 = **5** (0–2 while it waits for P, and 5–8 while it waits for R). This is slide 11.

**Why not try every order?** With $n$ jobs there are $n! = n \times (n-1) \times \dots \times 1$ orders
(slide 12): 6 for 3 jobs, 120 for 5 jobs and 3 628 800 for 10 jobs. For two machines there is a much faster
way: Johnson's rule.

### 4.4 Johnson's rule: two machines (slides 13–20)

Johnson's rule gives an order with the **smallest possible makespan** for a two-machine flow shop (slide 13).
The idea: a job that is quick on A should go **early**, so that B can start soon; a job that is quick on B
should go **late**, so that B finishes soon after A.

**The rule (slide 14)**

1. List the jobs and draw an empty schedule with one box per job.
2. Find the **smallest time** left in the table (break ties arbitrarily).
   - If it is on the **first** machine (A), put that job in the **first** empty box (as early as possible).
   - If it is on the **second** machine (B), put that job in the **last** empty box (as late as possible).
3. Cross the job out of the table (both of its times).
4. Repeat steps 2 and 3 until every job is scheduled.

**Worked example (slides 15–18)**

| Job | P | Q | R | S | T |
| --- | --- | --- | --- | --- | --- |
| Machine A | 5 | 8 | 1 | 4 | 6 |
| Machine B | 2 | 3 | 11 | 6 | 7 |

| Step | Smallest time left | Where it goes | Schedule |
| --- | --- | --- | --- |
| 1 | 1 (R on A) | first empty box | R _ _ _ _ |
| 2 | 2 (P on B) | last empty box | R _ _ _ P |
| 3 | 3 (Q on B) | last empty box | R _ _ Q P |
| 4 | 4 (S on A) | first empty box | R S _ Q P |
| 5 | only T is left | the remaining box | **R S T Q P** |

The order R S T Q P has makespan **30**, with idle time 6 on A and 1 on B (total 7). The original order
P Q R S T has makespan 40, with idle times 16 and 11 (total 27). Slide 18 shows both. Section 4.5 shows how to
compute these numbers.

**Ties.** When two times are equal, you may take either one first. This includes a job with the same time on
both machines, which you may put first or last. Every choice gives the smallest makespan, but the order (and
the Gantt chart) can differ. Flow shop tutorial Q2 has such a tie (job P: 8 and 8).

**Demo 1** does the same in Python. It numbers the jobs from 0 (0 = P, 1 = Q, 2 = R, 3 = S, 4 = T), so the order
R S T Q P is printed as `[2, 3, 4, 1, 0]`. When there is a tie, it always picks machine A first.

### 4.5 Computing a makespan by hand: the network method

Draw a small table: one column per job **in the order you are testing**, and one row per machine. In each cell
write the time at which that operation **finishes**:

$$\text{finish} = \max(\text{finish of the cell to the left},\ \text{finish of the cell above}) + \text{own processing time}$$

- *The cell to the left* is the previous job on the same machine: the machine must be free.
- *The cell above* is the same job on the previous machine: the job must have arrived.
- In the first row there is nothing above, and in the first column nothing to the left (use 0).

The number in the **bottom-right cell is the makespan**. You can draw the same thing as a network: one node per
cell, arrows to the right and downwards, and the makespan is the longest path through it. That is why the
tutorial calls it a *network representation*. The first page of the answers `.docx` (*Determining Makespan via
Network*) draws this network for P R Q, and the Excel sheets `Makespan 1` and `Makespan 2` do the same with
formulas.

*Example: order R S T Q P from section 4.4*

| | R | S | T | Q | P |
| --- | --- | --- | --- | --- | --- |
| A (times 1, 4, 6, 8, 5) | 1 | 1 + 4 = 5 | 5 + 6 = 11 | 11 + 8 = 19 | 19 + 5 = 24 |
| B (times 11, 6, 7, 3, 2) | max(0, 1) + 11 = 12 | max(12, 5) + 6 = 18 | max(18, 11) + 7 = 25 | max(25, 19) + 3 = 28 | max(28, 24) + 2 = **30** |

Machine A works 24 units, so it is idle 30 − 24 = 6; machine B works 29 units, so it is idle 30 − 29 = 1. With
more machines, add more rows: the rule is the same.

### 4.6 More than two machines: Campbell, Dudek and Smith (slides 21–24)

With three or more machines, Johnson's rule no longer guarantees the best order, and the problem is NP-hard
in general. You can still use the rule as a **heuristic**: turn the problem into a two-machine problem, apply
Johnson's rule, and compute the real makespan of the order you get (section 4.5).

*Slides' example: 4 machines (A–D), 4 jobs (P–S).* The original order P Q R S has makespan 52 (slide 21).

| Two "machines" used | Johnson's order | Makespan with all 4 machines | Slide |
| --- | --- | --- | --- |
| A and D (first and last machine only) | R Q S P | 46 | 22 |
| A+B and C+D (times added) | Q R S P | 46 | 23 |
| A+B+C and B+C+D | Q R P S | 48 | 23 |

With $m$ machines there are $m - 1$ such pairs (slide 24): pair $k$ adds the times of the first $k$ machines and
of the last $k$ machines. Compute the makespan of each order and **keep the best one**: here 46. This method is
known as the **Campbell, Dudek and Smith** heuristic. It is quick, but not always optimal: in flow shop tutorial
Q3 the best order it finds has makespan 66, while the true optimum is 64.

### 4.7 Job shop scheduling (notes, section 3)

In a **job shop**, each job is a list of operations, each on a given machine for a given time, and **each job
has its own order of machines**. The notes' example has 3 jobs and 3 machines:

| Job | Machines in order | Times |
| --- | --- | --- |
| $J_0$ | $M_0, M_1, M_2$ | 3, 2, 2 |
| $J_1$ | $M_0, M_2, M_1$ | 2, 1, 4 |
| $J_2$ | $M_1, M_2$ | 4, 3 |

In the code each job is written as a list of `(machine, time)` pairs, for example `Job 1 = [(0, 2), (2, 1), (1, 4)]`.

A schedule is now more than an order of jobs: each machine can process its operations in a different order.
Johnson's rule does not apply. Instead we write the problem as a MILP and let a solver search. The optimal
makespan of the notes' example is **11**.

### 4.8 Big-M: scheduling as a mixed-integer linear program

**Variables**

- $S_{ij} \ge 0$: start time of operation $j$ of job $i$ (processing time $p_{ij}$);
- $C_{\max} \ge 0$: the makespan;
- $y \in \lbrace 0, 1 \rbrace$: one binary variable for **each pair of operations that use the same machine**.
  $y = 1$ means the first operation of the pair goes first.

**Objective:** minimise $C_{\max}$.

**Constraints**

1. *Precedence:* an operation starts after the previous operation of the same job has finished:
   $S_{ij} + p_{ij} \le S_{i,j+1}$.
2. *No overlap:* two operations $(i,j)$ and $(k,l)$ on the same machine must not overlap. One of them must
   finish before the other starts. An "either … or" cannot be written as one linear constraint, so we write
   two constraints with the binary $y$ and a large number $H$ (the **big-M**):

   $$S_{ij} + p_{ij} \le S_{kl} + H\,(1 - y), \qquad S_{kl} + p_{kl} \le S_{ij} + H\,y .$$

   - If $y = 1$, the first constraint becomes $S_{ij} + p_{ij} \le S_{kl}$: $(i,j)$ goes first. The second has
     $+H$ on the right, which makes it always true, so it does nothing.
   - If $y = 0$, it is the other way round: $(k,l)$ goes first.
3. *Makespan:* $C_{\max} \ge S_{ij} + p_{ij}$ for every operation.

**How big must $H$ be?** Larger than any schedule worth considering. The notes use the **sum of all processing
times** (21 in the example), because no sensible schedule is longer than doing everything one after another.
If $H$ were too small, it would also forbid some good schedules.

**The flow shop as a MILP (flow shop tutorial Q4).** The same model works for a flow shop. The answer notebook
uses **one $y$ per pair of jobs**, shared by all machines, so every machine processes the jobs in the same order.
If you give each machine its own $y$, the model becomes a job shop model and may find a shorter schedule in which
the machines use different orders. For tutorial Q3 that gives 63 instead of 64, but such schedules are not a
flow shop in the sense of the lecture.

### 4.9 Constraint programming (notes, sections 1–2)

A **constraint satisfaction problem** (CSP) has variables, a **domain** of allowed values for each variable,
and **constraints** that say which combinations are allowed. A solution is a value for every variable that
satisfies all constraints. **An objective is optional**: a sudoku is a CSP with no objective.

The notes' puzzle `OR + IS + FUN = TRUE` is a CSP. It has 9 variables (one per letter: O, R, I, S, F, U, N, T and
E), each with domain 0–9. The constraints are the sum, "all letters different", and "O, I, F and T are not 0".
It has 96 solutions, for example 20 + 75 + 948 = 1043.

Constraint programming solvers such as **Google OR-Tools CP-SAT** search these problems directly. OR-Tools does
not run on the course site, so job shop tutorial Q4–Q5 use Google Colab ([section 6.2](#62-job-shop-tutorial-notebook)).
In this course you solve the job shop with Pyomo and HiGHS instead.

### 4.10 Letters, 0 and 1: how things are numbered

The material numbers things in several ways. When a result looks wrong, check the numbering first.

| Where | Jobs | Machines | Operations |
| --- | --- | --- | --- |
| Slides, flow shop tutorial | P, Q, R, … | A, B, C, … | – |
| Demo 1 (Johnson's rule) | 0 = P, 1 = Q, … | row 0 = A, row 1 = B | – |
| Flow shop Q4 notebook | P, Q, R, … | 0 = A, 1 = B, … | – |
| Job shop notes (tables) | $J_0, J_1, J_2$ | $M_0, M_1, M_2$ | $O_{01}, O_{02}, …$ (from 1) |
| Job shop notes (code) | 0, 1, 2 | 0, 1, 2 | `op (i, j)`, with `j` from 1 |
| Job shop tutorial Q2 | $J_1$–$J_4$ | A–D | from 1 |
| Job shop tutorial Q3 | $J_A, J_B, J_C$ | $M_1$–$M_5$ | from 1 |
| `Job Shop Q1-Q3 answers.ipynb` | Job 0, 1, … (first row of the table = Job 0) | 0, 1, … (Q2: A = 0, …, D = 3; Q3: $M_1$ = 0, …, $M_5$ = 4) | `task k` = operation k + 1 |

The picture `schedule1.png` in the notes (from Google OR-Tools) numbers operations from 0: `job(1, 0)` is the
first operation of job $J_1$.

---

## 5. Lecture guide: slides, notes and demos

**Part A: flow shop.** Slides from `1 Lecture/Week 7 - Flow Shop Scheduling.pptx`.

| Slides | Topic | What to do | What you should get |
| --- | --- | --- | --- |
| 1–7 | One machine; shortest processing time first, with a proof | Read with section 4.2 | SPT minimises the sum of completion times |
| 8–11 | Flow shop; makespan; idle time | Read with section 4.3; redo slide 11 on paper | P R Q: makespan 18, idle A 6, idle B 5 |
| 12 | Why trying every order is hopeless | Read | $n!$ orders; 10 jobs give 3 628 800 |
| 13–14 | Johnson's rule | Read with section 4.4 | – |
| 15–18 | Example 1 (5 jobs) | Work it on paper first; then the Excel sheets `Example 1`, `Makespan 1`, `Gantt 1` | R S T Q P, makespan 30 (original order 40) |
| 19–20 | Example 2 (3 jobs) | Work it on paper; then the Excel sheets `Example 2`, `Makespan 2`, `Gantt 2` | P R Q, makespan 18 (original order 19) |
| 13–20 | Demo: [`1 Johnsons rule.ipynb`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/2%20Lecture%20Demos/1%20Johnsons%20rule.ipynb) | *Run → Run All Cells* (nothing to install); then do its *Try it* | `[0, 2, 1]` twice, then `[2, 3, 4, 1, 0]` twice; *Try it*: `[2, 3, 0, 1, 4]` |
| 21–24 | More than two machines; Campbell, Dudek and Smith | Read with section 4.6; then the Excel sheets `More than 2 stages`, `Gantt more than 2` | Original 52; best heuristic order 46 |
| 25 | Trivia | – | – |

**Part B: job shop.** No slides: use the notes notebook
[`Job Shop Scheduling Notes.ipynb`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/1%20Lecture/Notes/Job%20Shop%20Scheduling%20Notes.ipynb).
Run its first code cell (the installer) when you reach it.

| Notes section | Topic | What to do | What you should get |
| --- | --- | --- | --- |
| 1 | Constraint satisfaction; CP vs mathematical programming | Read with section 4.9 | The integer program in the notes has optimum 35 at $x = 7$, $y = 3$, $z = 5$ |
| 2 | Cryptarithmetic: `OR + IS + FUN = TRUE` | Read; check the two given solutions by adding them up | 20 + 75 + 948 = 1043; 60 + 37 + 928 = 1025 |
| 3 | Job shop: example, history, formal definition, MILP | Read with sections 4.7–4.8 | – |
| 3, Pyomo code | The MILP in Pyomo | Run the cell | `Optimal makespan Cmax = 11.00`, then the schedule per machine |
| *Try it* | Job shop tutorial Q1 with the same code | Replace the data as shown, run again | $C_{\max} = 12$ |

The short version,
[`Job Shop Scheduling Notes (Short).ipynb`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/1%20Lecture/Notes/Job%20Shop%20Scheduling%20Notes%20%28Short%29.ipynb),
is the same notes without sections 1–2. There, the Pyomo code is in section 4. You do not need to read both.

The notes print the solver's schedule **and** show a saved schedule from an earlier run. They may list different
start times: several schedules reach 11 (section 7).

---

## 6. Tutorials: tasks, hints and how to check your answers

### 6.1 Flow shop tutorial (Word file)

Open `3 Tutorial/Week 7 - Flow Shop Scheduling - Tutorial.docx`. Its first page repeats Johnson's rule and the
slides' Example 2. Work on paper or in your own Excel sheet. The answers are in
`4 Tutorial Answers/Week 7 - Flow Shop Scheduling - Tutorial - Answers.docx`.

**Q1. Johnson's rule, Gantt chart, makespan, idle times.** Two machines, jobs P–T, with times A: 5, 7, 2, 4, 7
and B: 7, 5, 3, 8, 4.

- (a) Apply the rule (section 4.4) and draw a Gantt chart: two rows (A and B), a time axis, one block per job.
- (b) Compute the makespan with the table method (section 4.5).
- (c) Idle time of each machine = makespan − its total processing time.

<details><summary>Check your answer</summary>

Order **R S P Q T**, makespan **30**. Idle time on A: 5 (after 25). Idle time on B: 3 (0–2 and 5–6). Total 8.
The table has two ties (4: S on A and T on B; 5: P on A and Q on B), but they do not change the order.
</details>

**Q2. Johnson's rule; makespan via a network.** Jobs P–T, with times A: 8, 12, 12, 16, 7 and B: 8, 15, 13, 19, 8.
Use the table/network method of section 4.5.

<details><summary>Hint</summary>

Job P has the same time, 8, on both machines. Put it first (after T) or last; both are allowed. Q and R also
tie on A (12): either order.
</details>

<details><summary>Check your answer</summary>

T first. Then either **T Q R S P** (P last) or **T P Q R S** (P early). Both have makespan **74**, and so do the
orders with Q and R swapped. The answers `.docx` works through both.
</details>

**Q3. More than two machines.** Five machines A–E. Compute the makespan of the original order P Q R S T, then
use Campbell, Dudek and Smith (section 4.6) to find a better order. The tutorial suggests Excel, because there
are many sums: one table row per machine, and each cell = `MAX(left, above) + time`.

<details><summary>Check your answer</summary>

- Original order P Q R S T: **75**.
- A and E only: Johnson gives **R Q P T S**, makespan **66**: the best heuristic order.
- A+B and D+E: **R T Q S P**, 68. A+B+C and C+D+E: also **R T Q S P**, 68.
- The fourth pair, A+B+C+D and B+C+D+E, is not on the answer sheet. It gives R P Q S T (73) or R Q P S T (75), so
  66 stays the best.
- The true optimum (from Q4) is **64**, with **R P T Q S**: the heuristic is good but not optimal.
</details>

**Q4. Can you write a (mixed-integer) linear program?** Use section 4.8: start times $s_{jk}$ for job $j$ on
machine $k$, a makespan $C_{\max}$, and one binary $y_{ab}$ for each pair of jobs ($y_{ab} = 1$ if $a$ goes
before $b$ on every machine). Try to write the constraints on paper first, then compare with
[`Flow Shop Q4 MILP answers.ipynb`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/4%20Tutorial%20Answers/Flow%20Shop%20Q4%20MILP%20answers.ipynb).

<details><summary>Check your answer</summary>

Run the answer notebook (first cell first). It prints `Q1  optimal makespan = 30`, `Q2  optimal makespan = 74`
and `Q3  optimal makespan = 64`, each with an optimal order. For Q1 and Q2 the solver may print a different order
from Johnson's: several orders reach 30 (Q1) and 74 (Q2). For Q3, R P T Q S is the only optimal order.
</details>

### 6.2 Job shop tutorial (notebook)

Open [`3 Tutorial/Job Shop Scheduling Tutorial.ipynb`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/3%20Tutorial/Job%20Shop%20Scheduling%20Tutorial.ipynb).
It only contains the questions; there is nothing to run in it. The sheet says to use Google Colab and OR-Tools,
but **Q1–Q3 can be done on the course site** by adapting the Pyomo cell in *Job Shop Scheduling Notes*.

**How to adapt the notes' Pyomo cell to a new problem.** Copy the notebook first (right-click → *Duplicate*) so you
keep the original. Then change **four** things at the top of the Pyomo cell, and nothing else:

1. `model.JOBS`: one number per job, from 0;
2. `model.MACHINES`: one number per machine, from 0;
3. `n_ops`: the number of operations of each job;
4. `ops_data`: for each job, its list of `(machine, time)` pairs in operation order.

Sketch the schedule on paper (a Gantt chart) and check that it is **feasible**: each job's operations are in
order, and no machine does two things at once.

**Q1.** 3 jobs, machines $M_0$–$M_2$. The *Try it* at the end of the notes gives the data.

<details><summary>Check your answer</summary>

$C_{\max} = 12$. Your start times may differ from the answer notebook's: several schedules reach 12.
</details>

**Q2.** 4 jobs, machines A–D. Number the jobs $J_1$–$J_4$ as 0–3 and the machines A–D as 0–3.

<details><summary>Check your data</summary>

```python
model.JOBS = Set(initialize=[0, 1, 2, 3])
model.MACHINES = Set(initialize=[0, 1, 2, 3])
n_ops = {0: 4, 1: 3, 2: 4, 3: 3}
ops_data = {
    0: [(0, 3), (1, 2), (2, 4), (3, 3)],
    1: [(1, 5), (0, 3), (3, 2)],
    2: [(2, 2), (3, 1), (0, 4), (1, 4)],
    3: [(3, 4), (2, 3), (1, 5)],
}
```
</details>

<details><summary>Check your answer</summary>

$C_{\max} = 16$.
</details>

**Q3.** 3 jobs, machines $M_1$–$M_5$. Number $J_A$, $J_B$, $J_C$ as 0, 1, 2 and $M_1$–$M_5$ as 0–4.

<details><summary>Check your data</summary>

```python
model.JOBS = Set(initialize=[0, 1, 2])
model.MACHINES = Set(initialize=[0, 1, 2, 3, 4])
n_ops = {0: 5, 1: 4, 2: 4}
ops_data = {
    0: [(0, 4), (1, 2), (2, 3), (3, 5), (4, 2)],
    1: [(2, 2), (3, 1), (1, 3), (4, 4)],
    2: [(0, 3), (1, 4), (2, 2), (3, 3)],
}
```
</details>

<details><summary>Check your answer</summary>

$C_{\max} = 18$.
</details>

Then open
[`Job Shop Q1-Q3 answers.ipynb`](https://ctsallis.github.io/operational_research/lab/index.html?path=Lectures/Semester%201/Week%2007%20-%20Flow%20Shop%20and%20Job%20Shop%20Scheduling/4%20Tutorial%20Answers/Job%20Shop%20Q1-Q3%20answers.ipynb)
and run it (first cell first). It solves all three with one function and draws a Gantt chart for each. Its
"What do you notice?" question explains why Q1 cannot be done in less than 12.

**Q4. N-queens** and **Q5. Employee scheduling** are reading exercises on the Google OR-Tools website (the
links are in the tutorial notebook). OR-Tools does not run on the course site, so use **Google Colab**:

1. Go to <https://colab.research.google.com> and sign in with a Google account.
2. Create a new notebook (*File → New notebook*).
3. In the first cell type `!pip install ortools` and run it.
4. Copy the Python code from the OR-Tools page into the next cells, run it, and read it line by line.

Make sure you understand what each variable and constraint means and how it translates into the Python code.
There are no answer files for Q4–Q5. As a check for Q4: the standard 8 × 8 board has **92** solutions.

---

## 7. How to read the output

**Demo 1 (Johnson's rule)** prints each order as a list of job numbers (0 = P, 1 = Q, …). Each example is solved
twice, with a recursive and an iterative version of the rule, and the two lines must agree.

**The job shop notes** print `Optimal makespan Cmax = 11.00`, then for each machine its operations in order of
start time, for example `op (1, 1)  start= 0.00  finish= 2.00`. That is job 1, operation 1: the first operation
of $J_1$.

**`Job Shop Q1-Q3 answers.ipynb`** prints lines such as `Machine 0: Job 1 task 0  start 3  end 7` and draws a Gantt
chart. Each row of the chart is a machine and each colour a job, with labels J0, J1, ….

**`Flow Shop Q4 MILP answers.ipynb`** prints one line per question, for example
`Q1  optimal makespan = 30   order: R S P Q T`. The order is read from the first machine.

**The HiGHS log.** In the browser, HiGHS prints a long progress log before each result, even though the code
does not ask for it. You can skip it. Look for **`Status  Optimal`** in its *Solving report*: it means the
solver proved that it found the best answer.

**Different but equal answers.** Many scheduling problems have **several optimal schedules**. If your makespan
matches the expected one but the start times or the order differ, check that your schedule is feasible. If it
is, it is also optimal. The makespan is what must match.

**Small number effects.** A value such as `10.999999` or `1e-13` is the solver's rounding: read it as 11 or 0.

---

## 8. If something goes wrong

| Problem | What to do |
| --- | --- |
| A notebook shows no results | The notebooks are saved without outputs. Run them: *Run → Run All Cells*. |
| `ModuleNotFoundError: No module named 'pyomo'` | Run the **first code cell** of the notebook again. The install lasts only for the open tab. |
| Nothing happens for a long time when you first run a cell | The first run downloads Python and the packages. Wait about a minute. If nothing has changed after that, reload the page and run the first cell again. |
| `NameError: name 'model' is not defined` (or similar) | You skipped a cell. Use *Run → Run All Cells*. |
| `KeyError: 3` (or another number) after you changed the job shop data | A machine in `ops_data` is missing from `model.MACHINES`, or a job in `model.JOBS` is missing from `n_ops` or `ops_data`. Update all four items in section 6.2. |
| `KeyError: (0, 4)` (a pair of numbers) | `n_ops` says a job has more operations than its list in `ops_data`. |
| A makespan smaller than expected | Part of the problem is missing. Check that `model.JOBS` lists every job and that `n_ops` matches the length of each list: missing jobs or operations are silently left out. Then check every `(machine, time)` pair against the table, and the numbering (section 4.10). |
| The makespan matches but the schedule differs | That is fine: see "Different but equal answers" (section 7). |
| `ModuleNotFoundError: No module named 'ortools'` on the course site | OR-Tools does not run in the browser. Use Google Colab for job shop tutorial Q4–Q5 (section 6.2). |
| `ApplicationError: No executable found for solver 'glpk'` | Use `SolverFactory('appsi_highs')`. GLPK and CBC do not run in the browser. |
| Your Johnson order differs from the answer | Look for ties (section 4.4). With a tie, both choices can be correct; compare the makespans. |
| The `.pptx`, `.docx` or `.xlsx` does not open on the site | Download it and open it in PowerPoint, Word or Excel (section 1). |
| Excel shows *Protected View* and you cannot type | Click **Enable Editing** at the top. |
| Your edits disappeared | Edits are kept only in the browser you used. Next time, download the notebook before you leave (section 1). |
| The site will not load at all | Try another browser (Chrome, Edge or Firefox). The notebooks also run in Google Colab or Anaconda Jupyter: the first cell installs the packages there too. |

---

## 9. Check your understanding

Try to answer each question in a sentence or two before you open the answer.

<details><summary>1. With one machine, why does the order of the jobs not change the makespan? What does it change?</summary>

The machine is busy without a break until every job is done, so the makespan is the sum of all processing times
in every order. The order changes the **completion times**, and so the total (or average) waiting time.
</details>

<details><summary>2. Three jobs take 4, 1 and 3 minutes on one machine. In which order should they go to minimise the sum of completion times, and what is that sum?</summary>

Shortest first: 1, 3, 4. They finish at 1, 4 and 8, sum **13**. In the order 4, 1, 3 the sum is 4 + 5 + 8 = 17.
</details>

<details><summary>3. Apply Johnson's rule to three jobs X, Y, Z with times A: 3, 5, 1 and B: 6, 2, 2. What is the makespan?</summary>

Smallest time 1 (Z on A): Z first. Next 2: Y on B (Z's 2 on B is already crossed out): Y last. X goes in the
middle: **Z X Y**. Table: A finishes 1, 4, 9; B finishes 1 + 2 = 3, max(3, 4) + 6 = 10, max(10, 9) + 2 = **12**.
Trying all 6 orders confirms that 12 is the smallest.
</details>

<details><summary>4. In a two-machine flow shop, why is machine B always idle at the start?</summary>

B cannot start until the first job has finished on A. That is one more reason why Johnson's rule puts a job that is
short on A first. In slides' Example 1, R takes 1 on A, so B is idle only 1 unit in total.
</details>

<details><summary>5. Why is Johnson's rule only a heuristic when there are three or more machines?</summary>

Adding up machine times (or keeping only the first and last machine) throws information away. The two-machine
problem you solve is not the real one, so its best order need not be best for the real problem. Tutorial Q3
shows it: the heuristic gives 66, the optimum is 64.
</details>

<details><summary>6. In job shop tutorial Q2, why can no schedule finish before time 16?</summary>

Machine B has operations of 2, 5, 4 and 5 units: 16 units of work, and it can do only one at a time. So
$C_{\max} \ge 16$. The solver finds 16, so it is optimal, and machine B is never idle.
</details>

<details><summary>7. What does the binary variable y do in the job shop MILP, and why must H not be too small?</summary>

$y$ decides which of two operations on the same machine goes first. $H$ switches off the constraint for the other
order. If $H$ is too small, the "switched off" constraint still bites and forbids some valid schedules. The
answer could then be worse than the true optimum, or the model could even become infeasible.
</details>

<details><summary>8. What is the difference between the flow shop MILP (tutorial Q4) and the job shop MILP?</summary>

The flow shop model has one $y$ per **pair of jobs**, the same on every machine, so all machines use the same
order. The job shop model has one $y$ per **pair of operations on the same machine**, so each machine can use
its own order.
</details>

<details><summary>9. How many orders would you have to try for 5 jobs? For 10?</summary>

$5! = 120$ and $10! = 3\,628\,800$. That is why we use Johnson's rule, heuristics or a MILP solver instead of
trying everything.
</details>

<details><summary>10. Why does a constraint satisfaction problem not need an objective?</summary>

The aim is just to find values that satisfy every constraint, for example a filled sudoku or a solution of
`OR + IS + FUN = TRUE`. If you also want the best such solution, you add an objective, and it becomes an
optimisation problem.
</details>

---

## 10. Checklist: have you finished the week?

- [ ] I ran `00_START_HERE.ipynb` and every cell printed `OK`.
- [ ] I read slides 1–25 and can explain makespan, completion time, idle time and a Gantt chart.
- [ ] I can apply Johnson's rule by hand, and I got R S T Q P (30) and P R Q (18) for the slides' examples.
- [ ] I can compute a makespan with the table/network method.
- [ ] I ran demo 1 and did its *Try it*.
- [ ] Flow shop tutorial: Q1 (30), Q2 (74), Q3 (original 75, heuristic 66, optimum 64) and Q4 (the MILP).
- [ ] I read *Job Shop Scheduling Notes*, ran its Pyomo cell (11) and did its *Try it* (12).
- [ ] Job shop tutorial: Q1 (12), Q2 (16) and Q3 (18) with Pyomo; Q4–Q5 read and run in Google Colab.
- [ ] I answered the questions in section 9.
- [ ] I downloaded any notebooks I changed and want to keep.

**Next week (Week 8)** is *Networks – Shortest Paths and MST*.

---

## 11. Assumptions

These points are not stated in the course material for this week. This README assumes them:

1. **Order of work:** the slides come before the flow shop tutorial, and the job shop notes before the job shop
   tutorial. The tutorials come before their answers. The answers are already in this folder, so a student
   working alone is trusted to attempt each question first.
2. **The job shop notes are the lecture** for the second half of the week, because they are in `1 Lecture` and
   there are no job shop slides. The README recommends the full notes over the short version. The material
   does not say which one is required.
3. **The table/network method** (section 4.5) is not on this year's slides. Tutorial Q2 asks for it, so the
   README explains it, following the first page of the answers `.docx`, the Excel `Makespan` sheets and last
   year's slides 23–24.
4. **The fourth Campbell, Dudek and Smith pair** for tutorial Q3 (A+B+C+D and B+C+D+E: 73 or 75) is the
   README's own calculation. The answer sheet shows only the first three pairs.
5. **Job shop tutorial Q2 and Q3 data** in section 6.2 are typed from the tutorial tables into the format of the
   notes' code. The answers notebook uses the same numbering.
6. **Job shop tutorial Q4–Q5 have no answers** in this folder, and the material does not say how they are
   checked. The figure of 92 solutions for 8 queens is a standard result, not from the course material.
7. **Google Colab** needs a Google account. The tutorial sheet itself asks students to use Colab.
8. **The practice examples** in section 9 (questions 2 and 3) and section 4.2 are made up for this README.
   Their answers were checked by trying every order.
9. **Office:** students can open `.pptx`, `.docx` and `.xlsx` files in PowerPoint, Word and Excel.
10. **No time estimates or deadlines** are given, because the course material does not state them.
11. **`Previous Versions`, `5 Source Files` and `6 Further Reading` are optional.** Nothing in the week depends on
    them. The years in their file names are taken as given.
12. **Next week's topic** (end of section 10) is taken from the Week 8 folder name, not from a timetable.
13. **The links** point to the course site and to the files on the repository's `main` branch, as they were when
    this README was written.

# Coursework Part A: linear and integer programming (25%, Semester 1)

**What it is about.** Three modelling questions: a two-variable linear programme solved graphically and in
Python (binding constraints, matrix form); a risk-minimising investment model, then reduced to two
variables; and an integer programme (knapsack-style item selection) compared with its LP relaxation.

**What a student hands in.** One Word or PDF document with every answer (models with defined notation,
solutions, interpretation; equations typed or neatly handwritten and scanned), **plus** the Python code used
for each model as separate files labelled with the question number (`.py` or a downloaded `.ipynb`).
Screenshots of the code output are encouraged. Marks: 85% answers, 15% presentation (rubric in the brief's
Appendix A). A 10–15 minute viva may follow. Submission point and deadline: see the brief.

## Students: what to do, in order

| Step | Open | Do |
|---|---|---|
| 1 | `brief/assessment-brief-part-a.pdf` | Read the questions, the submission rules and the presentation rubric |
| 2 | `starter/pyomo_starter_template.ipynb` (or `.py`) | Run it: the smallest complete Pyomo + HiGHS model. Copy it for each model you need to solve |
| 3 | your own notebook or scripts | Formulate and solve each model; take screenshots of the output |
| 4 | your report | Write it up and submit the report plus the code files |

Run the template on the [course website](https://ctsallis.github.io/operational_research/lab/index.html?path=Assignments/01-coursework-part-a/starter/pyomo_starter_template.ipynb)
(first cell, then *Run All*) or on your computer (`python starter/pyomo_starter_template.py`); see
[Running the code](../README.md#running-the-code).

## Staff

| Step | Open | Use |
|---|---|---|
| 1 | `solutions/part-a-model-solutions.docx` | Model answers to Questions 1–3 (graphs, formulations, solver output) |
| 2 | `solutions/part_a_solutions.ipynb` (or `.py`) | Worked Python answers to every part of the 2025/26 questions, with explanations (new, see below) |
| 3 | `staff/part-a-marking-rubric-template.xlsx` | Blank marking sheet. Make a copy **outside this repository**; duplicate the `Rubric` sheet once per student |

Marking with the sheet: for each sub-question (rows Q1a–Q3d) enter a score out of 10 in the column of the
grade band awarded (F … A+); the `Mark` column scales it to the marks available. Do the same for the three
presentation rows. The sheet totals automatically: answers scaled to 85% + presentation scaled to 15% =
final mark (cell K35). Enter final marks in the university's gradebook; never save completed sheets here.

The Word model answers were produced with MATLAB and Desmos (screenshots in the Word file) for an earlier
version of the questions: they do not cover the basic-solution table, the binding constraints or the Python
parts of the 2025/26 brief. `solutions/part_a_solutions.ipynb` (and the same code as `part_a_solutions.py`),
added in the October 2026 review and not part of the original module material, answers every part in Python
with Pyomo + HiGHS; it runs on the
[course website](https://ctsallis.github.io/operational_research/lab/index.html?path=Assignments/01-coursework-part-a/solutions/part_a_solutions.ipynb)
or with `python solutions/part_a_solutions.py`. Results: Q1 x = 5, y = 7.5, maximum 27.5; Q2 £5,333.33 /
£2,666.67 / £2,000, return £706.67; Q3 items 1, 3, 4, 5, 10, value £27 (LP relaxation £28.44).

## Files

| File | What it is |
|---|---|
| `brief/assessment-brief-part-a.pdf` | The brief (`.docx` next to it is the editable source) |
| `starter/pyomo_starter_template.ipynb` | Minimal Pyomo + HiGHS model, notebook version (runs in the browser) |
| `starter/pyomo_starter_template.py` | The same model as a script |
| `solutions/part-a-model-solutions.docx` | Model answers (staff) |
| `solutions/part_a_solutions.ipynb` | Worked Python answers to every question, notebook version (runs in the browser; new in the October 2026 review) |
| `solutions/part_a_solutions.py` | The same answers as a script |
| `staff/part-a-marking-rubric-template.xlsx` | Blank rubric marking sheet (staff) |

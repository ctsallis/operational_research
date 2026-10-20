# Week 04 – Mathematical Programming: Modelling and Some Issues

This page takes you through the whole of Week 4 on your own: what to read, what to run, what to solve,
and how to check your answers. Work through the sections in order and tick the boxes as you go.

**By the end of the week you should be able to:**

- explain why constraints use $\le$ and $\ge$, never $<$ or $>$;
- write a sum $\sum_i a_i x_i$ as a vector product $a^T x$, and type it into Pyomo with `sum(...)`;
- extend a model with a new constraint (a weight cap) and see what it changes;
- combine two objectives (cost and popularity) in three ways: a ratio, a weighted sum and a
  normalised weighted sum, and explain what the weight $\alpha$ does;
- add slack variables to $\le$ constraints, read their values, and say which constraints are
  **binding**;
- build one model for a whole system instead of separate models for its parts, and explain why the
  combined plan can be better.

---

## 0. Before you start

**You need Weeks 2 and 3 first.** This week reuses them:

| From | What you need | Where |
| --- | --- | --- |
| Week 2 | The diet problem (tutorial Q6a) | `Week 02 - Linear Programming 1` folder |
| Week 3 | Pyomo basics, and the **Icki-Toffee** chocolate-box model (tutorial Q2): minimise cost, then maximise popularity | `Week 03 - Linear Programming 2` folder, especially `4 Tutorial Answers/Q2b Icki-Toffee - minimise cost.ipynb` and `Q2c Icki-Toffee - maximise popularity.ipynb` |

Tutorial Q1 this week starts from **your Week 3 Icki-Toffee model**. If you don't have one, use the
Week 3 answer notebook `Q2b Icki-Toffee - minimise cost.ipynb` as your starting point.

**Set up the course site (once per session):**

1. Open the course site: <https://ctsallis.github.io/operational_research/>. Use a recent Chrome, Edge
   or Firefox.
2. Open `00_START_HERE.ipynb` and choose *Run → Run All Cells*. If every cell prints `OK`, everything
   this week will run. The first time takes about a minute while Python and the packages download.
3. In the file browser on the left, go to `Lectures` → `Semester 1` →
   `Week 04 - Mathematical Programming - Modelling`.

**How to get the files:**

- **Notebooks (`.ipynb`)** open and run in the browser: double-click them.
- **Slides (`.pptx`) and Word files (`.docx`)** don't open in the browser. Right-click the file →
  **Download**, then open it in PowerPoint or Word.
- **This README:** right-click `README.md` → *Open With* → *Markdown Preview*.

**Saving your work.** Anything you change on the site is stored **only in this browser**. Clearing
browser data, using a private window or switching computer loses it. Before you stop, right-click each
notebook you changed → **Download**.

---

## 1. What is in this folder

| Folder | File | What it is | Do you need it? |
| --- | --- | --- | --- |
| `1 Lecture` | [`Week 4 - Mathematical Programming - Modelling.pptx`](1%20Lecture/Week%204%20-%20Mathematical%20Programming%20-%20Modelling.pptx) | Main lecture slides | **Yes** |
| `1 Lecture` | [`Slack Variables.pptx`](1%20Lecture/Slack%20Variables.pptx) | Short deck (10 slides): slack variables, binding and non-binding constraints, slack vs surplus | **Yes**; needed for tutorial Q2a ii |
| `2 Lecture Demos` | [`1 Pyomo expressions and constraints.ipynb`](2%20Lecture%20Demos/1%20Pyomo%20expressions%20and%20constraints.ipynb) | Runs the Pyomo code on slides 6–7 | **Yes** |
| `3 Tutorial` | [`Week 4 - Mathematical Programming - Modelling - Tutorial.docx`](3%20Tutorial/Week%204%20-%20Mathematical%20Programming%20-%20Modelling%20-%20Tutorial.docx) | The tutorial sheet: Q1 (Icki-Toffee) and Q2 (two factories) | **Yes** |
| `4 Tutorial Answers` | [`Week 4 - Mathematical Programming - Modelling - Tutorial - Answers.docx`](4%20Tutorial%20Answers/Week%204%20-%20Mathematical%20Programming%20-%20Modelling%20-%20Tutorial%20-%20Answers.docx) | Worked answers to the whole sheet | After you have tried the tutorial |
| `4 Tutorial Answers` | [`Q1b Icki-Toffee - popularity per cost ratio.ipynb`](4%20Tutorial%20Answers/Q1b%20Icki-Toffee%20-%20popularity%20per%20cost%20ratio.ipynb) | Q1b with a ratio objective | After you have tried Q1b |
| `4 Tutorial Answers` | [`Q1b Icki-Toffee - weighted objective.ipynb`](4%20Tutorial%20Answers/Q1b%20Icki-Toffee%20-%20weighted%20objective.ipynb) | Q1b with a weighted objective | After you have tried Q1b |
| `4 Tutorial Answers` | [`Q1b Icki-Toffee - normalised weighted objective.ipynb`](4%20Tutorial%20Answers/Q1b%20Icki-Toffee%20-%20normalised%20weighted%20objective.ipynb) | Q1b with a normalised weighted objective | After you have tried Q1b |
| `4 Tutorial Answers` | [`Q2a Factory A.ipynb`](4%20Tutorial%20Answers/Q2a%20Factory%20A.ipynb), [`Q2a Factory B.ipynb`](4%20Tutorial%20Answers/Q2a%20Factory%20B.ipynb) | Q2a, one model per factory | After you have tried Q2a |
| `4 Tutorial Answers` | [`Q2b Factories combined.ipynb`](4%20Tutorial%20Answers/Q2b%20Factories%20combined.ipynb) | Q2b, one model for the whole company | After you have tried Q2b |
| `5 Source Files` | `Python/*.py`, `MATLAB/*.m` | The original scripts the notebooks were made from | No (see section 8) |
| `6 Further Reading` | Two papers by R. E. D. Woolsey (*A Candle to Saint Jude…*, *A Novena to St. Jude…*) | Case studies of integer and mathematical programming in practice, recommended on the last slide | Optional |

**Slide numbers** in this README are the numbers PowerPoint shows in its slide list. The main deck has 27
slides. Slide 3 is hidden and blank, so the slide show skips it, but it still counts in the numbering.

---

## 2. Your checklist for the week

- [ ] Section 0: Week 3 done, `00_START_HERE.ipynb` prints `OK`
- [ ] Section 3: main slides 1–27, with the demo notebook at slides 6–7
- [ ] Section 4: `Slack Variables.pptx`
- [ ] Section 5: tutorial Q1a, Q1b, Q2a, Q2b, written up in your own notebook
- [ ] Section 6: answers checked against the answer notebooks and the answer sheet
- [ ] Section 7: self-test questions answered
- [ ] Your notebooks downloaded to your own computer

---

## 3. Lecture: the main slides

Download and open `1 Lecture/Week 4 - Mathematical Programming - Modelling.pptx`. Read it in this
order. The notes below say what each part is about and what you should take from it.

### Slides 1–5: two building blocks

- **Slide 4: always use $\le$ or $\ge$.** With a strict inequality the feasible set is not *closed*: it
  leaves out its own boundary. Try the slide's example: maximise $x$ subject to $x < 1$. Whatever $x$
  you pick ($0.9$, $0.99$, $0.999$…) there is a bigger one that still satisfies $x < 1$, so there is
  **no maximum**. With $x \le 1$ the maximum is $x = 1$. Solvers only accept $\le$, $\ge$ and $=$.
- **Slide 5: sums as vector products.** If $a = (a_1, \dots, a_n)^T$ and $x = (x_1, \dots, x_n)^T$,
  then $a^T x = \sum_{i=1}^{n} a_i x_i$. A list of coefficients times a list of variables is how you
  type long constraints quickly.

### Slides 6–7: the same thing in Pyomo (run the demo now)

Slide 6 writes $10x_1 + 6x_2 + 8x_3 + 16x_4$ by hand and with `sum(...)`. Slide 7 turns it into the
constraint $10x_1 + 6x_2 + 8x_3 + 16x_4 \ge 120$.

Open `2 Lecture Demos/1 Pyomo expressions and constraints.ipynb`, run the first cell, then
*Run → Run All Cells*, and read each cell's explanation as you go. What to notice:

- Python counts from 0, so the slides' $x_1, \dots, x_4$ are `x[0]` … `x[3]`.
- Writing the sum by hand and with `sum(cost[i] * model.x[i] for i in model.x)` gives **exactly the
  same expression**.
- Pyomo prints every constraint as *Lower ≤ Body ≤ Upper*, with `-Inf` or `+Inf` for a missing side.
- A yellow **WARNING: Implicitly replacing the Component attribute constraint1** is **expected**. The
  notebook redefines a constraint on purpose to show what happens.
- `deactivate()` switches a constraint off without deleting it (`Active` becomes `False`).

Do the notebook's *Try it* cell at the end.

### Slides 8–10: recap of the diet problem

This is Week 2 tutorial Q6a, written first in full (slide 8), then with symbols and sums (slide 9),
then in Pyomo (slide 10). The point is the notation: one symbol per data column ($v_i^A$ = vitamin A
in food $i$, $c_i$ = cost of food $i$, and so on), which makes the model short and easy to check.
To run it, use Week 3's `2 Lecture Demos/2 Diet problem 6a - minimise cost.ipynb`.

> The code on slide 10 uses `SolverFactory('glpk')`. GLPK does not work on the course site; use
> `SolverFactory('appsi_highs')`, as every course notebook does.

### Slides 11–17: the chocolate box, and why interpretation matters

- **Slides 11–12** repeat Week 3's Icki-Toffee model and its two answers: minimise cost (cost **268**)
  and maximise popularity (popularity **365**). Ask yourself the slide's question: *what do we think of
  these selections?* The popular box weighs **635 g**, almost twice the 320 g minimum, and neither box
  has much variety.
- **Slides 13–15:** a model is only as good as your reading of the problem, and its answers often show
  what you left out. Your opinions and preferences shape the model (for example, how much cost
  matters), so be aware of bias. Modelling is **iterative**: build, look at the answer, improve.
- **Slides 16–17: extending the model.** Add a weight cap of 1.5 times the minimum:
  $\sum_i W_i x_i \le 1.5 \times 320 = 480$ (this is tutorial **Q1a**). With the cap, the
  maximum-popularity box changes (popularity **305**). The minimum-cost box doesn't change, because it
  already weighed less than 480 g.

### Slides 18–24: combining two objectives (tutorial Q1b)

We want a box that is both popular **and** cheap, but a model has only one objective. Slide 18 lists
the two ideas used here.

| Slides | Method | Objective | What to watch out for |
| --- | --- | --- | --- |
| 19–20 | **Ratio** | maximise $\sum_i \dfrac{P_i}{C_i} x_i$ | Each candy scores its own popularity per unit cost. This rewards many cheap candies; it is **not** the same as total popularity ÷ total cost (that ratio is not linear) |
| 21 | **Weighted** | maximise $(1-\alpha)\sum_i P_i x_i - \alpha \sum_i C_i x_i$ | $\alpha$ (between 0 and 1) is how much cost matters: $\alpha = 0$ is popularity only, $\alpha = 1$ is cost only. Costs (10–20) are bigger numbers than popularities (3–10), so cost wins unless $\alpha$ is small |
| 22–24 | **Normalised weighted** | maximise $(1-\alpha)\sum_i \dfrac{P_i x_i}{\max_i P_i} - \alpha \sum_i \dfrac{C_i x_i}{\max_i C_i}$ | Dividing by the largest value ($\max P_i = 10$, $\max C_i = 20$) puts both on a 0–1 scale, so $\alpha$ really means "how much I care about cost" |

Why minimise cost becomes "minus cost" (slide 21): minimising $\sum_i C_i x_i$ gives the same choice
of $x$ as maximising $-\sum_i C_i x_i$, so both aims fit in one *maximise*.

Slide 24 compares all the capped models. With the normalised objective, $\alpha \gtrsim 0.59$ gives the
minimum-cost box and $\alpha < 1/6 \approx 0.167$ gives the maximum-popularity box. Values in between
give a real compromise, such as $\alpha = 0.5$ on slide 23.

### Slides 25–27: practical modelling advice

- **Slide 25: solve the LP first.** Drop the "whole numbers" condition and solve the faster linear
  programme. If its answer already happens to be whole numbers, you are done.
- **Slide 26: a recipe for any model.** Write down what you know; identify the variables, the objective
  and the constraints; check they are linear; choose clear notation; decide whether the variables are
  real or integer; then write the model. Use this recipe for the tutorial.
- **Slide 27: tips.** Test on a small version first; compare with known data; watch for *under*-modelling
  (missing constraints) and *over*-modelling (too restrictive, redundant or conflicting constraints,
  which can make the model infeasible). The Woolsey papers in `6 Further Reading` are recommended here.

---

## 4. Lecture: `Slack Variables.pptx`

Download and open `1 Lecture/Slack Variables.pptx`. It uses one small problem:

$$\text{maximise } P = 5x + 4y \quad \text{subject to} \quad 2x + 3y \le 15,\; 3x + 2y \le 15,\; 2x + 2y \le 11,\; x, y \ge 0.$$

- **Slack variable:** the unused amount in a $\le$ constraint. Adding $s_1 \ge 0$ turns
  $2x + 3y \le 15$ into $2x + 3y + s_1 = 15$. A model written only with equalities and non-negative
  variables is in **standard form** (slide 3).
- **Slides 4–9** visit the corners A–E of the feasible region and fill in a table of $x, y, s_1, s_2,
  s_3, P$. At each corner, work out the slacks yourself **before** you move to the next slide.
- The optimum is C, $(x, y) = (4, 1.5)$ with $P = 26$. There $s_1 = 2.5$, $s_2 = 0$, $s_3 = 0$.
- **Binding constraint:** slack $= 0$, the constraint is "used up" and is holding the solution back.
  **Non-binding:** slack $> 0$, so there is spare capacity.
- **Slide 10, surplus variable:** for a $\ge$ constraint, the amount *above* the minimum. Subtracting
  $e_1 \ge 0$ turns $2x + 3y \ge 15$ into $2x + 3y - e_1 = 15$.

You need this for tutorial Q2a ii ("unused hours" = slack).

---

## 5. Tutorial

Download `3 Tutorial/Week 4 - Mathematical Programming - Modelling - Tutorial.docx`. One star (\*)
marks a medium question and two stars (\*\*) a hard one. Do the questions in order: **Q1a, Q1b, Q2a,
Q2b**.

### Where to write your code

Make your own copy of a course notebook so you keep its first cell (it installs Pyomo and HiGHS and
makes Pyomo's printing work in the browser):

1. In the file browser, right-click a course notebook (for Q1, Week 3's
   `Q2b Icki-Toffee - minimise cost.ipynb`; for Q2, this week's `1 Pyomo expressions and constraints.ipynb`)
   → **Duplicate**.
2. Right-click the copy → **Rename**, e.g. `My Week 4 Q1.ipynb`.
3. Keep the first cell and replace the rest with your own model. Solve with
   `SolverFactory('appsi_highs')`.

For each question, first write the model on paper using the recipe on slide 26 (variables, objective,
constraints, real or integer). Then code it.

### Q1: Icki-Toffee

- **Q1a.** Add the weight cap $\sum_i W_i x_i \le 1.5 \times 320$ to your Week 3 model. Solve it twice,
  once minimising cost and once maximising popularity, and compare with the uncapped answers (268 and
  365).
- **Q1b\*.** Combine cost and popularity into **one** objective, keeping the weight cap. Pick one of
  the methods on slides 19–23 (ratio, weighted, normalised weighted), choose $\alpha$ if your method has
  one, and write two or three sentences saying **why**: do you think cost and popularity matter equally?
  There is no single right answer; the justification is the point.

Hints:

- The data are in Tables 1 and 2 of the sheet. A "-" in the fat column means 0.
- "Fat at most 45% of the weight" is $\sum_i F_i x_i \le 0.45 \sum_i W_i x_i$: the right-hand side
  contains the variables too, which is allowed because it is still linear.
- The variables are numbers of candies, so make them whole numbers (`NonNegativeIntegers`).

### Q2: two factories

- **Q2a.** Build a **separate** model for factory A and for factory B, each maximising its own profit.
  Use the raw material each factory is given (75 kg for A, 45 kg for B).
  - i. How many standard and deluxe units should each factory make? What is each profit, and the total?
  - ii. How many grinding and polishing hours are left unused at each factory?
- **Q2b.** Now let the model share out the 120 kg itself: build **one** model for the whole company.
  - i. What is the total profit? Is it better or worse than Q2a's total?
  - ii. How much raw material does each factory use? What does this say about planning the factories
    separately?

Hints:

- Q2a: two variables per factory, $s$ (standard) and $d$ (deluxe). One constraint per limited
  resource: grinding hours, polishing hours, raw material (4 kg per unit of either product).
- Q2a ii: unused hours = capacity − hours used at your solution. This is the **slack** from section 4.
- Q2b: four variables $s_1, d_1$ (factory A) and $s_2, d_2$ (factory B). Each factory's machines only
  work on its own products, so A's grinding constraint contains only $s_1$ and $d_1$. The raw material
  is shared: $4(s_1 + d_1 + s_2 + d_2) \le 120$.
- The answer sheet uses whole units; the sheet says real values are also acceptable.

---

## 6. Check your answers

Only open this once you have your own answers. The answer notebooks in `4 Tutorial Answers` show the
full code with an explanation above each step; each one starts with an *Expected result* and ends with
a *Try it* or *What do you notice?* question. The Word answer sheet has the written working.

<details>
<summary><b>Show the final numbers</b></summary>

| Question | Answer |
| --- | --- |
| Q1a | Constraint $\sum_i W_i x_i \le 480$. Minimum cost stays **268**, e.g. 9 Caramel softie, 10 Rose-water posy, 3 Grape bunch (323 g). Maximum popularity drops from 365 to **305**, e.g. 30 Coconut Ice, 5 Rose-water posy, 5 Grape bunch (475 g) |
| Q1b, ratio | 8 Coconut Ice, 32 Lime sherbet, 8 Rose-water posy: weight 480 g, cost 616, popularity 288, objective 21.97 |
| Q1b, weighted, $\alpha = 0$ | Popularity **305** (cost ignored). Any $\alpha$ from about 0.42 gives the minimum-cost box; only $\alpha$ below about 0.09 gives the maximum-popularity box |
| Q1b, normalised, $\alpha = 0.5$ | 24 Coconut Ice, 11 Rose-water posy: 376 g, 2795 calories, 168 g fat, cost 470, popularity 249 |
| Q1b, normalised, $\alpha = 0.59$ | The minimum-cost box (cost 268), objective −2.494 |
| Q2a, factory A | 10 standard, 8 deluxe, profit **£220**. Unused: grinding 24 h, polishing 0 h (binding); 3 kg raw material left |
| Q2a, factory B | 0 standard, 11 deluxe, profit **£165**. Unused: grinding 27 h, polishing 9 h; 1 kg raw material left |
| Q2a, total | £220 + £165 = **£385** |
| Q2b | $s_1 = 10$, $d_1 = 8$, $s_2 = 0$, $d_2 = 12$: profit **£400**, better than £385. A uses 72 kg and B 48 kg (instead of 75 and 45). A could not use its last 3 kg, while B had spare hours for one more deluxe unit |

</details>

**If your answer is different:**

- **Same objective value, different selection?** That's fine. Some of these problems have several
  optimal answers (for example popularity 305 in Q1a). Any selection that meets every constraint and
  reaches the same objective value is correct.
- **Different objective value?** Print your model with `model.pprint()` and compare each constraint
  with the formulation in the answer notebook, line by line. Common slips: a wrong number copied from a
  table, $\le$ instead of $\ge$, forgetting the weight cap, or a "-" not entered as 0.
- **Q1b:** your answer depends on the method and $\alpha$ you chose, so compare your **reasoning** with
  slides 19–24 and with the notebooks' *Try it* answers, not just the numbers.

---

## 7. Self-test

Answer these without looking, then open the answers.

1. Why can't a solver handle "maximise $x$ subject to $x < 1$"?
2. Write $3x_1 + 5x_2 + 2x_3$ as $a^T x$. What is $a$?
3. In the Slack Variables example, what are $s_1, s_2, s_3$ at corner B $(5, 0)$? Which constraints are
   binding there?
4. Why does the plain weighted objective with $\alpha = 0.5$ give the minimum-cost box, even though
   0.5 sounds like "equal preference"?
5. In Q2b, why does the company earn more when one model plans both factories?

<details>
<summary><b>Show the answers</b></summary>

1. The feasible set $x < 1$ has no largest point: for any $x < 1$ there is a bigger one. With $x \le 1$
   the maximum $x = 1$ exists (slide 4).
2. $a = (3, 5, 2)^T$ and $x = (x_1, x_2, x_3)^T$, so $a^T x = 3x_1 + 5x_2 + 2x_3$.
3. $s_1 = 15 - 10 = 5$, $s_2 = 15 - 15 = 0$, $s_3 = 11 - 10 = 1$. Of the three constraints, only the second
   ($3x + 2y \le 15$) is binding (slide 5).
4. Costs (10 to 20) are bigger numbers than popularities (3 to 10), so the cost term dominates unless
   $\alpha$ is small. Normalising (slide 22) fixes this.
5. With fixed shares, factory A cannot use its last 3 kg (its polishing is binding), while factory B has
   spare machine hours but no material. One model moves the material to where it earns most.

</details>

---

## 8. Extras (optional)

- **Further reading.** Two short papers by R. E. D. Woolsey in `6 Further Reading` (right-click →
  **Download**). They are case studies of integer and mathematical programming in practice; slide 27
  calls them "insightful and amusing".
- **Source files.** `5 Source Files` holds the original scripts the notebooks were made from. You do
  not need them. The Python scripts use the GLPK solver, which you would have to install on your own
  computer; the MATLAB scripts need MATLAB with the Optimization Toolbox. The notebooks give the same
  answers.
- **Running on your own computer.** Every notebook also runs in Google Colab or Anaconda Jupyter.

---

## 9. If something goes wrong

| Problem | What to do |
| --- | --- |
| `ModuleNotFoundError: No module named 'pyomo'` | Run the notebook's **first cell** again. Installs last only while the browser tab is open |
| The notebook seems stuck the first time | The first run downloads Python and the packages. Wait about a minute; if nothing happens, reload the page and run the first cell again |
| A yellow `WARNING: Implicitly replacing the Component attribute…` | Expected in the demo notebook (see section 3). In your own model it means you used the same name twice |
| Your selection differs from the slides or the answers | See section 6: several selections can be optimal |
| A `.pptx` or `.docx` won't open in the browser | Right-click → **Download**, then open it in PowerPoint or Word |
| Your changes have disappeared | They are kept only in the browser you used. Download your notebooks before you finish (section 0) |
| `SolverFactory('glpk')` fails | GLPK does not run in the browser. Use `SolverFactory('appsi_highs')` |
| Anything else | Run `00_START_HERE.ipynb` (it lists more fixes at its end), or open the notebook in Google Colab |

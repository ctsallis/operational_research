# Semester 1 · Week 10 – Vehicle Routing Problem

From the travelling salesman problem (TSP) to vehicle routing: several tours that all start and end at a depot,
customers with a demand, vehicles with a capacity, and two objectives, the total distance and the longest route.
The models are mixed-integer linear programs (MILPs) solved in Pyomo. Work through the folders in number order.

| Folder | What is in it | When |
| --- | --- | --- |
| `1 Lecture` | Slides (PDF) and the lecture notes (`Notes/`, with a PDF copy) | The lecture |
| `2 Lecture Demos` | `1 TSP and VRP with Pyomo.ipynb`: the three models of the lecture on one 8-node example | Run in the lecture; its *Try it* questions are this week's practice |
| `5 Source Files` | Editable slides (.pptx), HTML exports of the notes, an earlier draft of the notes, staff notes for slides 27 and 33 | Staff only; edit here, then republish the PDFs |
| `6 Further Reading` | The two original papers: Miller, Tucker and Zemlin (1960) and Christofides (1976) | Optional |

## Before you start

- **Week 09:** the TSP as a MILP and the Miller–Tucker–Zemlin (MTZ) constraints
  $u_i - u_j + 1 \le (n-1)(1 - x_{ij})$. This week starts from that model.
- **Week 05:** binary variables and big-M constraints (a constraint switched on or off by a binary variable).
- **Week 08:** networks: nodes, arcs and arc costs.
- **Python:** a Pyomo model as in Weeks 03–05 (`Var`, `Constraint` with a rule, `Objective`,
  `SolverFactory('appsi_highs')`).

## Work through this week in order

Slide numbers are those of the `.pptx`. Slide 2 is hidden, so in the PDF the page number is the slide number minus 1.

| Step | File | What it is for |
| --- | --- | --- |
| 1 | Slides 3–5 | The TSP reminder: one arc in and one arc out of every city still allows *subtours* |
| 2 | Slides 6–13 | The MTZ constraints: why they force one tour, why city 1 is left out, why $M = n - 1$, the compact model |
| 3 | `1 Lecture/Notes/Routing Problems - Lecture Notes.md`, sections *Travelling Salesman Problem* and *Explaining the MTZ Subtour Constraint* | The same argument in more detail, with Pyomo code |
| 4 | Slides 14–17 | Several tours from city 1: relax city 1's constraints and fix the number of arcs leaving it |
| 5 | Slides 18–24 | The vehicle routing problem (VRP): what "optimal" means, demand and capacity, minimise the total distance |
| 6 | Slides 25–28 | The flow model with capacity, and why its flow constraints already rule out subtours |
| 7 | `2 Lecture Demos/1 TSP and VRP with Pyomo.ipynb`, sections 1–2 | TSP without MTZ: **233.4** (subtours), with MTZ: **281.4** (one tour); VRP, total distance: **327.6** with two full vehicles |
| 8 | Slides 29–33 | Deliver as quickly as possible: one copy of the network per vehicle, minimise the longest route $C_{Max}$ |
| 9 | Notebook section 3, *What do you notice?* and *Try it* | Longest route **137.4** with three vehicles (total 362.5). Questions on capacity, fleet size, an extra customer and the cost of balancing; answers are hidden in the notebook |
| 10 | Slides 34–35; notes sections *Limitations of the Model* and *NP-Hard Problems and Heuristic Solutions* | Routing on a subgraph, extensions (time windows, mixed fleets), heuristics such as nearest neighbour |
| 11 | *Optional:* `6 Further Reading` | The original MTZ paper (1960) and Christofides' survey of the VRP (1976) |

The notes are Markdown: right-click → *Open With* → *Markdown Preview*. `1 Lecture/Lecture Notes - Routing Problems.pdf`
is a PDF copy of the same notes.

## By the end of this week you can

- explain why the MTZ constraints remove subtours, why city 1 is left out of them and why $M = n - 1$ is enough;
- turn the TSP into a model with $m$ tours from a depot;
- write the capacitated VRP with flow variables $f_{ij}$, and explain why flow conservation with positive demands
  rules out subtours;
- write the minimax VRP with per-vehicle variables $x_{ijk}$, $f_{ijk}$ and $C_{Max}$, and explain why each vehicle
  must leave every location it enters;
- solve both models in Pyomo and compare them: the total distance against the length of the longest route.

**Next:** Week 11 (Floor Planning): binary variables again, this time to stop rectangles from overlapping.

## Practice answers

The week has no tutorial sheet; the practice questions are at the end of the demo notebook, with hidden answers.

| Question | Answer |
| --- | --- |
| Why does model 2 use only two vehicles? | Every route drives out of the depot and back, so fewer routes are shorter in total: two full vehicles (15 + 15 = 30) give 327.6 |
| `capacity = 12` | Two vehicles carry only 24 < 30, so model 2 uses three routes, total 362.5; models 1 and 3 do not change |
| `num_vehicles = 2`, `capacity = 14` | 2 × 14 = 28 < 30: infeasible. The model-2 cell stops with "A feasible solution was not found" |
| Customer 9 at (60, 70), demand 2 | TSP 288.8; model 2 total 363.8 (three routes); model 3 longest route still 137.4 |
| Model 2 vs model 3 | Balancing adds 34.9 to the total (+10.7 %) and cuts the longest route by 35.4 (−20.5 %) |

A route may be printed in the opposite direction; its length is the same.

## Notes for staff

- `2 Lecture Demos/1 TSP and VRP with Pyomo.ipynb` is a companion notebook written for this repository. Slide 36 used
  to link to a separate Google Colab notebook (https://colab.research.google.com/drive/1BLPImK2TcdCrTaTN2-N6b2z3QNdUXpMe),
  which is not in the repository; it now links to this notebook on the course site (Oct 2026).
- **Notebook text (Oct 2026).** The title cell gives the problem, how to run it and the expected results; a cell
  before the data explains the data and helper functions; models 1 and 2 have a comment for each constraint; a
  *What do you notice?* question and answers to the four *Try it* questions were added. The code is unchanged. The
  expected results were checked in Pyodide 314.0.0 (HiGHS 1.13.1) and on a desktop (HiGHS 1.15.1).
- **In the browser** the test run printed HiGHS's full solver log after every solve (the first cell switches off
  Pyomo's output capture); a desktop prints nothing. The course site was checked by hand after the October 2026 merge.
- **Lecture slides (Oct 2026).** The `.pptx` was corrected and the PDF re-exported from PowerPoint (17 October 2026):
  6 $r_k$ is the city visited $k$-th (it said "the order in which city $j$ is visited"), and $u_i$ "need not equal the
  position". 7 $u_j > u_i$ (it said $u_j > u_j$). 8, 11, 12 the MTZ constraint is $u_i - u_j + 1 \le M(1 - x_{ij})$:
  the slides had $u_j - u_i$, which gives $u_i > u_j$, the opposite of what slides 6–7 ask for. 9 "an increasing
  sequence". 10 $k = r_n$ (it said $k = 1$). 12 no "1 < … < 1"; $M \ge u_{r_n} - u_{r_2} + 1 \ge n - 1$.
  16 several chains, each joined to location 1 (the slide said the chain *must* start and end at 1, then "Instead").
  20 "Royal Mail", "There is no capacity", the parcel sentence reworded. 21, 31 the depot is location 1 (it said 0).
  21 $m$ vehicles (it said $K$). 22 it is the depot constraint that is relaxed. 23 with the triangle inequality one
  vehicle is always among the best. 24 "deliver". 25, 32 $V$ includes the depot; 25 $x_{ij}$ has no $k$.
  27 subtours are impossible if every $q_i > 0$ (zero demands allow them too). 28 says which model the example uses.
  31 $q_i$ (it said $d_i$). 36 links to the notebook on the course site. As in Week 09, the boxes with equations keep a
  stored picture of the old text, which only LibreOffice and old viewers show; export from PowerPoint.
- **Slides 27 and 33: corrected pictures (Oct 2026).** The picture on slide 33 (*Full Model*) and the upper picture on
  slide 27 were replaced with corrected versions typeset in LaTeX, in the same place and scaled to fit the old frame.
  Slide 33: the labels of the first two constraints were swapped ($\sum_j x_{ijk}$ counts the arcs *leaving* $i$);
  "less than $Q_{max}$" is now "at most $C_{Max}$"; "Length of a route is less than vehicle capacity" is now "The load on
  an arc is at most the vehicle capacity"; and the constraint "if vehicle $k$ enters location $i$ then it must leave
  location $i$" moved from "Optional" into the model (without it the route lengths, and so $C_{Max}$, mean nothing; the
  notebook's `mm.cont` and the notes include it). Slide 27: "Flow conservation for $r_j$, $r_k$, $r_i$" (it said $j$,
  $k$, $i$). `5 Source Files/Staff Notes/Week 10 - notes for slides 27 and 33.docx` explains these changes and has
  speaker notes for both slides; its Word equations paste into PowerPoint as editable equations. Its "Replace the
  picture" step is already done. The slides PDF in `1 Lecture` shows the new pictures since the 19 October 2026
  re-export.
- **Second review (19 Oct 2026).** Slides (`.pptx`): 6 "Let $u_i \in \mathbb{R}$ represent" (it said "and
  represent"); 11, 12 "… sufficiently large?"; 17 the two chains are $u_7 < u_3$ and $u_5 < \dots < u_{10}$, each joined
  to location 1 at both ends (it said "$1 < u_7 < u_3 < 1$", the notation removed from slides 12 and 16); 28 a shorter
  sentence (the longer one ran under the pictures, so its end was hidden); 31 "at most $m$ subtours (i.e. at most $m$
  vehicles used)" (it said $K$, which slide 32 uses for the set of vehicles); 32 a new bullet "$m$ – number of vehicles
  that may leave the depot" (slide 33 uses $m$). Slide 26's label "Route capacity less than $Q$" was part of
  a picture (the picture was replaced later the same day, see below). Notes (`.md` and, edited by hand, its HTML
  export): "visited *just* before city $j$"; Model 1 item 5 "The load on an arc is at most the vehicle capacity $Q$";
  without constraint 3 a single tour is
  one of the best solutions *if the distances obey the triangle inequality*. Notebook (text and comments only, code
  unchanged): the title cell no longer mentions Colab; section 3 says that slide 33 includes `mm.cont`, how the model
  differs from the slide (each vehicle leaves the depot at most once; the flow is kept per vehicle) and that only the
  longest route is unique; comments on `mm.x`, `mm.f`, `mm.Cmax` and `mm.cap`; the customer-9 answer gives both routes
  HiGHS prints (Pyodide 314.0.0: 1 → 4 → 5 → 9 → 1, 127.0; desktop HiGHS 1.15.1: 1 → 9 → 4 → 5 → 1, 115.5; the longest
  route is 137.4 in both). Both PDFs were re-made afterwards (see *PDF status* below).
- **PDF status (19 Oct 2026).** `1 Lecture/Vehicle Routing Problem.pdf` was re-exported from PowerPoint on 19 October
  2026 and checked against the `.pptx`: all the slide changes above are in it (including the new pictures on slides 27
  and 33), and slide 36 links to the notebook on `ctsallis.github.io`. `1 Lecture/Lecture Notes - Routing Problems.pdf`
  was rebuilt on 19 October 2026 from the HTML export (which matches the `.md`): 11 A4 pages, printed with headless
  Chromium (margins 16 mm top and bottom, 14 mm left and right, background graphics on, long code lines wrapped), the
  same layout as the 18 October copy.
- **Slides 26 and 28 (19 Oct 2026, after the PDF re-export).** Slide 26: the picture of the model (a screenshot of the
  notes' Model 1) was replaced with the same section of the corrected notes, rendered from the HTML export with KaTeX;
  item 5 now reads "The load on an arc is at most the vehicle capacity $Q$" (it said "Route capacity less than $Q$").
  The new picture sits in the old frame, scaled to its height and centred. Slide 28: the two pictures moved 0.4 cm down,
  because their white background covered the bottom of the letter p and the brackets in the second line of text.
  The slides PDF in `1 Lecture` was re-exported from PowerPoint afterwards (19 October 2026, 15:04) and shows both
  changes.
- **Third review (19 Oct 2026).** Slides (`.pptx`, text only): 6 "city 3 is visited second" (the raised "nd" of "2nd"
  touched $u_{r_n}$ on the line above); 18, 19 "a fleet of $m$ vehicles", "If $m = 1$" and 34 "Route m vehicles" (they
  said $K$, which slide 32 uses for the *set* of vehicles); 23 a full stop at the end. Notes (`.md` and its HTML
  export, formulas rendered with KaTeX like the rest of the file): the compact TSP model has $u_i$ only for
  $i \in V \setminus \{1\}$; the sub-tour argument of Model 1 says "Flow conservation for $r_j$, $r_k$, $r_i$" (as slide
  27); the notation of Model 2 defines $m$, the number of vehicles that may leave the depot (as slide 32). Slides 12
  and 22 have very small text (12 pt, or shrunk to fit): enlarge it or split the slides if it is hard to read when
  projected. Both PDFs in `1 Lecture` were re-made the same evening (19 October 2026): the slides PDF re-exported from
  PowerPoint (checked: slides 6, 18, 19, 23 and 34 show the changes) and the notes PDF printed from the HTML export
  (11 A4 pages; checked: the compact TSP model, the sub-tour argument and the Model 2 notation show the changes).
- **Lecture notes (Oct 2026).** `Routing Problems - Lecture Notes.md` was corrected: the minimax model (the same four
  points as slide 33), "$u_i$ orders the cities", the $r_k$ definition, $r_2$ / $r_n$, the $M \ge n-1$ chain, $m$ tours,
  $q_i \le 0$, "$Q$ is the largest number of locations one vehicle can visit", minimum-cost flow (it said
  "multi-commodity flow"), typos and British spelling. Its Pyomo code now runs: the TSP printout used an undefined
  `cities`, model 1 overwrote the node set with the vehicles and had no `u`, model 2 used undefined `Qmax` and `c`, and
  both called GLPK; they now use HiGHS and reproduce the notebook's 327.6 and 137.4. The two "PLACEHOLDER IMAGE"
  lines, the author's "currently working on these notes" note and a dead MathJax `<script>` were removed.
- **Notes PDF and HTML exports (Oct 2026).** `1 Lecture/Lecture Notes - Routing Problems.pdf` and
  `5 Source Files/HTML Exports/Routing Problems - Lecture Notes.html` were rebuilt from the corrected `.md` (on
  18 October 2026, after the notes gained "page 29 of the PDF" next to "slide 30"; the notes PDF again on 19 October,
  after the second review). The HTML export of the short notes
  was rebuilt from the earlier draft; its content is unchanged. The HTML exports' images point to
  `1 Lecture/Notes/assets`. They were made the way the VS Code extension *Markdown All in One* does it: Markdown with
  formulas rendered by KaTeX, then printed to an A4 PDF without headers and footers; long code lines wrap. To export
  again yourself: in VS Code with *Markdown All in One*, set `markdown.extension.print.absoluteImgPath` to `false`, open
  the `.md` and run *Markdown All in One: Print current document to HTML*; open the HTML in Edge and print it to PDF
  (A4, default margins, headers and footers off, background graphics on). **Print style (19 Oct 2026).** The exports
  load VS Code's `markdown.css` from the CDN without a version, and newer copies of it give code blocks no grey
  background and stop them from breaking across pages (printing then gave 14 pages with large gaps, one of them blank).
  Both HTML exports now end their `<head>` with a short `<style>` block that restores the original look, so printing
  them gives the 11-page layout again. A fresh export from VS Code does not have this block: copy it across from the
  current file before printing. The 19 October notes PDF was printed from the HTML export with headless Chromium
  (A4, margins 16 mm top and bottom, 14 mm left and right, background graphics on).
- `5 Source Files/Previous Versions/Routing - Short Notes for the Lecture (earlier draft).md` was in `1 Lecture/Notes`
  until October 2026. It is a shorter, earlier draft of the full notes, and its minimax model is wrong: the objective
  is $Q_{Max}$ and the route length adds up the flows $f_{ijk}$ instead of the distances $c_{ij}x_{ijk}$.
- Removed in Oct 2026: `5 Source Files/Images/Routing.jpeg`, a full-page image of the old notes (it still showed
  "dsad"); and earlier, an older export of the slides (March 2025) and an older HTML export of the notes.

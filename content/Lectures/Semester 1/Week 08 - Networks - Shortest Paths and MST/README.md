# Week 8: Networks – Shortest Paths and Minimum Spanning Trees

This week is about **networks**: dots (vertices) joined by lines (edges), where each line has a number
(a weight) such as a distance, a time or a cost. You will learn three algorithms that you can carry out
by hand with a table:

| Algorithm | Question it answers | Works on |
| --- | --- | --- |
| **Dijkstra** | What is the shortest route from one vertex to another? | Directed networks (one-way arrows) with weights that are **not negative** |
| **Prim** | What is the cheapest set of edges that connects every vertex? | Undirected networks (two-way lines) |
| **Kruskal** | Same question as Prim, answered in a different way | Undirected networks |

The minimum spanning tree (Prim and Kruskal) is part of the in-class test revision (see
[section 10](#10-checklist-have-you-finished-the-week)).

There is **no programming this week**: everything is done with pen and paper. One optional notebook
(Python, runs in your browser) repeats every calculation so that you can check your own tables.

> **Note on the module handbook.** The handbook's week list calls Week 8 *"Network Models:
> Transportation and Transhipment Problem"*. This folder teaches shortest paths and minimum spanning
> trees. Course examples of transhipment (minimum-cost flow) are in Semester 2:
> `Lectures/Semester 2/Week 01 - Introduction to Simulation/2 Lecture Demos/6 Production-distribution (minimum-cost flow).ipynb`
> and `Lectures/Semester 2/Week 10 - Revision/4 Tutorial Answers/F.B. Knight - transhipment (Pyomo).ipynb`.

## Contents

1. [How to open the files](#1-how-to-open-the-files)
2. [What is in this folder](#2-what-is-in-this-folder)
3. [Your plan for the week](#3-your-plan-for-the-week)
4. [The key ideas, explained](#4-the-key-ideas-explained)
5. [Lecture guide: slide by slide](#5-lecture-guide-slide-by-slide)
6. [Tutorial: tasks, hints and how to check your answers](#6-tutorial-tasks-hints-and-how-to-check-your-answers)
7. [How to read the answers notebook](#7-how-to-read-the-answers-notebook)
8. [If something goes wrong](#8-if-something-goes-wrong)
9. [Check your understanding](#9-check-your-understanding)
10. [Checklist: have you finished the week?](#10-checklist-have-you-finished-the-week)
11. [Assumptions](#11-assumptions)

---

## 1. How to open the files

The course site is **https://ctsallis.github.io/operational_research/**. It shows the course folders
in a file browser on the left. This week's folder is
`Lectures/Semester 1/Week 08 - Networks - Shortest Paths and MST`.

### PowerPoint, Word and PDF files: download them

The browser site cannot display `.pptx` or `.docx` files. To open one:

1. In the file browser, **right-click** the file → **Download**.
2. Open the downloaded file on your computer: `.pptx` in **PowerPoint**, `.docx` in **Word**, `.pdf` in
   any PDF reader.

Open the slides as a **slide show** (PowerPoint: *Slide Show → From Beginning*) or click through them one
by one: the worked examples change a little on every slide, and the change is the lesson.

### The notebook (`.ipynb`): run it in your browser

1. In the file browser, open the folder `4 Tutorial Answers` and **double-click**
   `Q1-Q2 answers in Python.ipynb`.
2. Choose the menu **Run → Run All Cells**.
3. Wait until every code cell shows a number in square brackets on its left, e.g. `[9]`. The printed
   results appear under the cells.

The notebook uses plain Python only: nothing needs to be installed and it runs in a second or two.
If you change it, your changes are kept **only in this browser**. To keep a copy: right-click the
notebook → **Download**.

### This README

On the course site: right-click `README.md` → **Open With → Markdown Preview**.

---

## 2. What is in this folder

| Folder | File | What it is | Do you need it? |
| --- | --- | --- | --- |
| `1 Lecture` | `Week 8 - Networks - Shortest Paths and MST.pptx` | The lecture: 70 slides (networks, Dijkstra, Prim, Kruskal) | **Yes** |
| `1 Lecture` | `Negative weight example (Dijkstra fails).pptx` | 6 slides: an example where Dijkstra gives the wrong answer because one weight is negative | **Yes** (short) |
| `1 Lecture` | `Dijkstra Algorithm.pptx` | 29 slides from another university's course (Brian C. Dean, *Lecture 20. Shortest Paths*, CpSc 212, Clemson University, 2012): the same Dijkstra example in a different style, plus breadth-first search and the Bellman-Ford algorithm | Optional |
| `1 Lecture` | `Week 8 - Networks - Shortest Paths and MST (annotated).pdf` | An older (2020-21) copy of the lecture with the lecturer's handwritten notes | Optional |
| `3 Tutorial` | `Week 8 - Tutorial - Networks - Shortest Paths and MST.docx` | The tutorial sheet: a summary of the three algorithms, then the exercises Q1, Q2a and Q2b | **Yes** |
| `4 Tutorial Answers` | `Week 8 - Tutorial - Networks - Q1 Answers.pptx` | 20 slides: Q1 solved step by step, with Prim and with Kruskal | **Yes**, after you try Q1 |
| `4 Tutorial Answers` | `Week 8 - Tutorial - Networks - Q2 Answers.pptx` | 15 slides: Q2a and Q2b solved step by step with Dijkstra | **Yes**, after you try Q2 |
| `4 Tutorial Answers` | `Q1-Q2 answers in Python.ipynb` | Runs Dijkstra, Prim and Kruskal on the lecture examples, Q1, Q2a, Q2b and the negative weight example, printing every step | Optional, for checking |
| `5 Source Files/Staff Notes` | `Do flow shop scheduling problem live.txt` | An empty file whose name is a note for the lecturer | No |
| `6 Further Reading` | `MIT 6.006 Lecture 16 - Dijkstra.pdf` | 7 pages of MIT lecture notes: relaxation, shortest paths in acyclic networks, Dijkstra, why it is correct, running time | Optional, harder |

There is no `2 Lecture Demos` folder this week, because there are no lecture notebooks.

**About the annotated PDF.** It has the same 70 slides in the same order as the `.pptx`, so slide
numbers match. Some wording has been corrected since 2020-21. For example, the old slides 24–27 say "work
backwards from the *source*"; the correct version (in the `.pptx`) says "from the *destination t*". When
the two disagree, **the `.pptx` is right**.

---

## 3. Your plan for the week

Work in this order. Have paper and a pencil ready: you will copy tables and fill them in.

1. **Networks and the shortest path problem:** lecture slides 1–6 ([section 4.1](#41-words-you-need-this-week)
   and [4.2](#42-describing-a-network-slides-24)).
2. **Dijkstra's algorithm:** slides 7–31 ([section 4.3](#43-dijkstras-algorithm-shortest-paths-slides-731)).
   Before you look at each new slide of the example (slides 10–28), predict what changes. Then check.
3. **When Dijkstra fails:** the 6-slide deck `Negative weight example (Dijkstra fails).pptx`
   ([section 4.4](#44-when-dijkstra-fails-negative-weights)).
4. Slides 32–35 are a short break activity (find Wally). Nothing to learn there.
5. **Minimum spanning trees and Prim's algorithm:** slides 36–55
   ([sections 4.5](#45-minimum-spanning-trees-slides-3637) and [4.6](#46-prims-algorithm-slides-3855)).
6. **Kruskal's algorithm:** slides 56–69 ([section 4.7](#47-kruskals-algorithm-slides-5669)).
   Slide 70 lists the textbooks.
7. **Tutorial:** do Q1, Q2a and Q2b by hand **before** you open any answers
   ([section 6](#6-tutorial-tasks-hints-and-how-to-check-your-answers)).
8. **Check:** compare every table you made with the answer decks. Optionally run the answers notebook
   ([section 7](#7-how-to-read-the-answers-notebook)).
9. **Optional depth:** `Dijkstra Algorithm.pptx` and the MIT notes.
10. Answer the questions in [section 9](#9-check-your-understanding), then go through the checklist in
   [section 10](#10-checklist-have-you-finished-the-week).

---

## 4. The key ideas, explained

### 4.1 Words you need this week

| Word | Meaning |
| --- | --- |
| **Network** (or graph) | A set of **vertices** (also called nodes: the dots) and **edges** (the lines between them). |
| **Directed** edge | A one-way edge, drawn as an arrow. Edge (u, v) goes **from** u **to** v; you may not travel it backwards. |
| **Undirected** edge | A two-way edge, drawn as a plain line. It can be used in both directions. |
| **Weight** w(u, v) | The number on an edge: distance, time or cost. |
| **Path** | A route along edges, e.g. 1–3–4. Its **length** is the sum of its weights. |
| **Source** and **destination** | Where a path starts and where it ends. In the lecture example they are called s and t. |
| **Cycle** | A path that comes back to where it started without reusing an edge. |
| **Tree** | A connected set of edges with no cycle. |
| **Spanning tree** | A tree that reaches **every** vertex. With n vertices it always has exactly **n − 1 edges**. |
| \|V\|, \|E\| | The number of vertices and the number of edges. |
| **Label** | The numbers written next to a vertex during an algorithm: a distance d and a predecessor π. |
| **Predecessor** π (pi) | The vertex you came from on the best route found so far. "−" means none. |
| **Temporary (T)** / **Permanent (P)** | Dijkstra's two kinds of vertex. A temporary label may still improve; a permanent label is final. On the slides, blue vertices are temporary and yellow ones are permanent. |
| ∞ (infinity) | "No route found yet". |

### 4.2 Describing a network (slides 2–4)

A network can be written as a list of edges with their weights. Slide 2 shows the network
V = {1, 2, 3, 4, 5}, E = {(1,2), (1,3), (2,3), (3,4), (3,5), (4,2), (4,5)}, with, for example,
w(1, 2) = 100. An undirected network can be turned into a directed one by replacing each line with two
arrows, one in each direction (slide 2, right).

**Slide 3, one edge per direction.** Two edges from u to v with different weights are not allowed,
because then w(u, v) would have two values. Two edges in **opposite** directions are fine: in the lecture
example d → e has weight 8 and e → d has weight 1.

**Slide 4, the adjacency matrix.** Put the weight of edge i → j in row i, column j. The diagonal is 0
(going nowhere costs nothing). Where there is no edge, write "–" or ∞ (the slide shows both versions).
For example, row 1 of the first network is `0 100 30 – –`: from vertex 1 you can reach vertex 2 (100)
and vertex 3 (30). The slide says you won't need the matrix this week; it is shown because it is a
standard way to store a network.

### 4.3 Dijkstra's algorithm: shortest paths (slides 7–31)

**The problem (slide 5).** Find the path from a source to a destination with the smallest total weight.
This is what route planners such as Google Maps solve.

**The four steps (slide 7, also in the tutorial sheet).**

1. **Initialise.** The source gets distance 0. Every other vertex gets distance ∞. All vertices are
   temporary (T).
2. **Choose.** Make permanent (P) the **temporary** vertex with the **smallest** distance. Call it u.
3. **Update.** For every edge u → v where v is still **temporary**: if d(u) + w(u, v) is **smaller**
   than d(v), replace d(v) by d(u) + w(u, v) and set π(v) = u.
4. **Repeat** steps 2 and 3 until every vertex is permanent.

**The table.** Keep one row per vertex with four columns: `v | Label (T or P) | d_v | π_v`. When a value
changes, cross out the old value and write the new one next to it, as the slides do (e.g. ~~9~~ 6).

**Reading off the path (slides 24–28).** Start at the **destination** and follow the predecessors
backwards until you reach the source, then reverse the list.

**Why it works (slides 9 and 29–30).** Shortest distances satisfy the *triangle inequality*:
d_i + c_ij ≥ d_j for every edge (i, j). If it fails for some edge, going through i would be shorter, so
d_j can be improved. That is exactly the check in step 3. When a vertex becomes permanent, no
path through the remaining temporary vertices can beat it, as long as no weight is negative. As a
bonus, at the end you know the shortest path from the source to **every** vertex, not only the
destination (slides 29–30).

**The lecture example, step by step.** Edges: s→b 9, s→d 2, b→c 11, b→e 3, d→b 4, d→e 8, e→d 1, e→t 6,
c→e 5, c→t 12.

| Slides | Made permanent | Updates in step 3 |
| --- | --- | --- |
| 8, 10 | — (initialise) | s = 0, all others ∞ |
| 11–12 | s (0) | b: 0 + 9 = 9 via s; d: 0 + 2 = 2 via s |
| 13–14 | d (2) | b: 2 + 4 = 6 < 9, so 6 via d; e: 2 + 8 = 10 via d |
| 15–16 | b (6) | c: 6 + 11 = 17 via b; e: 6 + 3 = 9 < 10, so 9 via b |
| 17–18 | e (9) | t: 9 + 6 = 15 via e (d is already permanent, so e → d is skipped) |
| 19–20 | t (15) | none (no edge leaves t) |
| 21–22 | c (17) | none: e is permanent, and 17 + 12 = 29 is not smaller than 15 |
| 23–28 | Done | Backwards from t: t ← e ← b ← d ← s. **Shortest path s–d–b–e–t, length 15** |

Final labels: s 0 (−), b 6 (d), c 17 (b), d 2 (s), e 9 (b), t 15 (e).

**Slide 6** shows the same network with the vertices numbered 0–5 (s = 0, b = 1, c = 2, d = 3, e = 4,
t = 5). Its answer, 0–3–1–4–5 of length 15, is the same path.

**Running time (slide 31), for interest.** Finding the smallest temporary label by scanning every vertex
takes about |V|² operations in total. A priority queue (binary heap) brings this down to about
(|E| + |V|) log |V|. You won't need to compute these.

### 4.4 When Dijkstra fails: negative weights

Dijkstra needs every weight to be **zero or positive** (slide 7). The deck
`Negative weight example (Dijkstra fails).pptx` shows why. The network has edges 1→2 1, 1→4 2, 1→3 3,
3→4 **−5**, 4→2 1.

| Deck slide | What happens |
| --- | --- |
| 2 | Initialise: vertex 1 = 0, the others ∞ |
| 3 | 1 becomes permanent: 2 = 1, 4 = 2, 3 = 3 (all via 1) |
| 4 | 2 becomes permanent with distance 1 (the smallest), **and is never changed again** |
| 5 | 4 becomes permanent with distance 2 |
| 6 | 3 becomes permanent. The edge 3 → 4 would give 3 + (−5) = −2, but 4 is already permanent, so its label stays 2 |

Dijkstra says the shortest path from 1 to 2 is 1–2 with length 1. But 1–3–4–2 has length
3 + (−5) + 1 = **−1**, which is shorter. The algorithm made vertex 2 permanent too early, because it
assumed that a longer start (3) could never become cheaper later. With a negative weight, it can.

For networks with negative weights there is the **Bellman-Ford algorithm** (lecture slide 7; optional
deck `Dijkstra Algorithm.pptx`, slide 11). You don't need to learn it this week.

### 4.5 Minimum spanning trees (slides 36–37)

A **minimum spanning tree (MST)** is a set of edges of a connected, weighted, undirected network that
reaches every vertex, contains no cycle and has the **smallest possible total weight** (slide 36).

**Application (slide 37).** A fibre-optic company must connect a set of areas with cable. Laying cable
between some pairs of areas is possible at a known cost. The cheapest way to connect every area is an
MST. On slide 38 the existing cable reaches area A.

**MST and shortest path are different questions.** A shortest path connects **two** vertices as
cheaply as possible. An MST connects **all** vertices as cheaply as possible, and the route between two
particular vertices inside the tree may be long.

### 4.6 Prim's algorithm (slides 38–55)

**The steps (slide 38, also in the tutorial sheet).**

1. Initialise every distance to ∞ and every predecessor to −.
2. Pick **any** vertex and mark it **selected**. It gets distance 0.
3. **Update:** for every **unselected** vertex v joined by an edge to the vertex just selected, u: if
   w(u, v) is smaller than d(v), set d(v) = w(u, v) and π(v) = u.
4. **Select** the unselected vertex with the smallest distance. The edge from it to its predecessor
   joins the tree.
5. Repeat 3 and 4 until every vertex is selected.

> **Most common mistake.** In Prim, d(v) is the weight of **one edge**: the cheapest edge from v to the
> tree. It is **not** a distance from the start vertex. Do **not** add d(u) as you would in Dijkstra.
> Compare slide 43: E's label becomes 7, the weight of edge G–E, not 2 + 7.

The total weight of the tree is the sum of the final d values (slide 55: Σ d_v = 21).

**The lecture example** (slides 39–55, start at D). Edges: A–F 10, A–B 8, A–H 4, F–C 3, F–B 7, F–D 18,
F–E 2, C–D 3, C–B 4, B–E 10, B–H 9, D–G 2, D–E 25, G–H 3, G–E 7.

| Slides | Selected | Updates |
| --- | --- | --- |
| 40–41 | D (0) | C 3, E 25, F 18, G 2 (all via D) |
| 42–43 | G (2) | E: 7 < 25, via G; H 3 via G |
| 44–45 | C (3) | B 4 via C; F: 3 < 18, via C |
| 46–47 | F (3) | A 10 via F; E: 2 < 7, via F |
| 48–49 | E (2) | none (B–E 10 is not smaller than 4) |
| 50–51 | H (3) | A: 4 < 10, via H |
| 52–53 | A (4) | none (A–B 8 is not smaller than 4) |
| 54–55 | B (4) | All selected. **Tree: D–G, D–C, C–F, F–E, G–H, H–A, C–B; total 21** |

There are ties on slides 44, 46 and 52: C and H both have 3, then F and H both have 3, then A and B
both have 4. The slides take C, then F, then A. The other choices give the same total.

**Why start at D when the cable starts at A?** Any start vertex gives the same total weight (slide 40).

### 4.7 Kruskal's algorithm (slides 56–69)

**The steps (slide 56, also in the tutorial sheet).**

1. List the edges from **lightest to heaviest**.
2. Go down the list. Take the next edge **unless it would form a cycle** with the edges already taken.
   Mark it T (taken) or F (rejected).
3. Stop when you have taken **|V| − 1** edges.

**How to spot a cycle.** An edge u–v forms a cycle if you can **already** travel from u to v using the
edges taken so far. Picture the taken edges as separate groups of connected vertices. An edge
inside one group forms a cycle; an edge between two groups joins them.

> **Watch out.** Kruskal's example (slides 56–69) uses the **same letters A–H as Prim's example but
> different weights**. Use the table on slide 57, not the network from slides 39–55. Both trees happen
> to weigh 21.

**The lecture example** (8 vertices, so stop after 7 edges):

| Slide | Edge (weight) | Taken? | Why |
| --- | --- | --- | --- |
| 58 | D–E (1) | T | |
| 59 | D–G (2) | T | |
| 60 | E–G (3) | F | E and G are already connected through D |
| 61 | C–D (3) | T | |
| 62 | G–H (3) | T | |
| 63 | C–F (3) | T | |
| 64 | B–C (4) | T | |
| 65 | B–E (4) | F | B–C–D–E already connects them |
| 66 | B–F (4) | F | B–C–F |
| 67 | B–H (4) | F | B–C–D–G–H |
| 68 | A–H (5) | T | That is the 7th edge: stop |
| 69 | — | | Total 1 + 2 + 3 + 3 + 3 + 4 + 5 = **21**. The remaining edges D–F, A–B, A–F are not needed |

**Ties.** Edges with equal weight may be taken in any order. You may end with a different tree, but its
total weight is always the same minimum.

### 4.8 The three algorithms side by side

| | Dijkstra | Prim | Kruskal |
| --- | --- | --- | --- |
| Result | Shortest paths from one source | A minimum spanning tree | A minimum spanning tree |
| Edges | Directed (follow the arrows) | Undirected | Undirected |
| Grows from | The source | Any one start vertex: always a single connected tree | The cheapest edges anywhere: several pieces that join up |
| Label of a vertex | **Total** length of the best path from the source | Weight of the **single** cheapest edge to the tree | (no vertex labels; one T/F per edge) |
| Update rule | d(u) + w(u, v) < d(v)? | w(u, v) < d(v)? | Does the edge form a cycle? |
| Stops when | All vertices are permanent | All vertices are selected | \|V\| − 1 edges are taken |
| Negative weights | **Not allowed** | Allowed | Allowed |

---

## 5. Lecture guide: slide by slide

**Main deck: `Week 8 - Networks - Shortest Paths and MST.pptx`**

| Slides | Topic | What to take away |
| --- | --- | --- |
| 1 | Title | |
| 2–3 | Network definitions | Vertices, edges, weights; directed vs undirected; one edge per direction ([4.2](#42-describing-a-network-slides-24)) |
| 4 | Adjacency matrix | How to read one; not used later |
| 5 | Shortest path problem | The definition |
| 6 | "Blue Peter" example | The answer you should get: 0–3–1–4–5, length 15 |
| 7 | Dijkstra's algorithm | The four steps. Weights must not be negative |
| 8 | Set up | The table and the label boxes (dashed box = predecessor, solid box = distance) |
| 9 | Improving cost labels | Triangle inequality: the idea behind step 3 |
| 10–23 | Dijkstra example | One step per slide; red values are the ones that just changed ([4.3](#43-dijkstras-algorithm-shortest-paths-slides-731)) |
| 24–28 | Reading the path | Follow the predecessors back from t. Answer s–d–b–e–t, 15 |
| 29–30 | Correctness | Every vertex's final label is its shortest distance |
| 31 | Proof and time complexity | Running time; proofs in the textbook and the MIT notes |
| 32–35 | Break activity | Find Wally |
| 36 | Minimum spanning tree | The definition |
| 37 | Example application | The fibre-optic cable problem |
| 38 | Prim's algorithm | The five steps |
| 39–55 | Prim example | Start at D; total 21 ([4.6](#46-prims-algorithm-slides-3855)) |
| 56 | Kruskal's algorithm | The three steps, and what a cycle looks like |
| 57–69 | Kruskal example | Sorted edge table; total 21 ([4.7](#47-kruskals-algorithm-slides-5669)) |
| 70 | References | Cormen et al., *Introduction to Algorithms*; Taha, *Operations Research: An Introduction* |

**`Negative weight example (Dijkstra fails).pptx`:** see [section 4.4](#44-when-dijkstra-fails-negative-weights).
Its table headings use i, d_i and π_i instead of v, d_v and π_v; they mean the same thing.

**`Dijkstra Algorithm.pptx` (optional).** The worked example on slides 9 and 13–19 is the **same
network** as the lecture example, renamed s, 1, 2, 3, 4, 5 (1 = b, 2 = c, 3 = d, 4 = e, 5 = t). It writes
c[j] for the distance label and pred[j] for the predecessor, and calls step 3 "tighten" (or "relax").
Its results, c[1] = 6, c[2] = 17, c[3] = 2, c[4] = 9, c[5] = 15, match the lecture. Other slides:
types of shortest path problems (2–4); breadth-first search (5–6); negative-cost cycles (7);
Bellman-Ford (11); Dijkstra in pseudocode (12), why it is correct (20) and its running time (21); centrality (22–23);
problems that can be rewritten as shortest path problems (24–29). Slide 22 says "Recall": it refers to
an earlier lecture of that course, not of this one.

---

## 6. Tutorial: tasks, hints and how to check your answers

Open `3 Tutorial/Week 8 - Tutorial - Networks - Shortest Paths and MST.docx`. The first part repeats the
three algorithms, with pictures of the tables to copy. The **Exercises** come at the end.

Before you start, write down the edge list from the picture and compare it with the lists below. Most
wrong answers come from misreading a weight or an arrow.

### Q1: minimum spanning tree with Prim **and** with Kruskal

Undirected network, 7 vertices A–G. Edges: A–B 7, A–D 5, B–C 8, B–D 9, B–E 7, C–E 5, D–E 15, D–F 6,
E–F 8, E–G 9, F–G 11.

**Hints**
- **Prim:** the answer slides start at **A**. Start there too, so you can compare every step. Use the
  table `v | Selected | d_v | π_v`. Remember that d is one edge's weight
  ([4.6](#46-prims-algorithm-slides-3855)).
- **Kruskal:** first write all 11 edges in order of weight. Use the table `Edge | w_e | Selected`.
  With 7 vertices you stop after **6** edges.
- Both methods must give the **same total**.

**Check:** `4 Tutorial Answers/Week 8 - Tutorial - Networks - Q1 Answers.pptx`. Prim is on slides 1–9:
slides 2–8 select A, D, F, B, E, C, G in that order, and slide 9 shows the result. Kruskal is on slides
10–20, one edge per slide from slide 11 on.

<details>
<summary>Q1 final answer (open after you finish)</summary>

- **Prim from A:** selects D (5, from A), F (6, from D), B (7, from A), E (7, from B), C (5, from E),
  G (9, from E). Final labels: A 0 (−), B 7 (A), C 5 (E), D 5 (A), E 7 (B), F 6 (D), G 9 (E).
- **Kruskal:** A–D 5 T, C–E 5 T, D–F 6 T, A–B 7 T, B–E 7 T, B–C 8 F, E–F 8 F, B–D 9 F, E–G 9 T (6th
  edge: stop).
- **Tree:** A–D, C–E, D–F, A–B, B–E, E–G. **Total weight 39.**
</details>

### Q2a: shortest path from node 1 to node 4

Directed network. Edges: 1→2 2, 1→3 3, 2→3 1, 2→4 4, 3→4 2.

**Hints**
- Follow the arrows: 2→3 can be used, 3→2 cannot.
- When vertex 2 becomes permanent, look closely at vertex 3: 2 + 1 = 3, which **equals** its current
  label 3. Step 3 changes a label only if the new value is **strictly smaller**, so leave it.

**Check:** `Week 8 - Tutorial - Networks - Q2 Answers.pptx`, slides 1–7. Slide 2 initialises, slides 3–6
make 1, 2, 3, 4 permanent in turn, and slide 7 gives the answer. The table headings i, d_i, π_i mean
the same as v, d_v, π_v.

<details>
<summary>Q2a final answer</summary>

Final labels: 1 0 (−), 2 2 (1), 3 3 (1), 4 5 (3). Backwards from 4: 4 ← 3 ← 1.
**Shortest path 1–3–4, length 5.** The path 1–2–3–4 also has length 2 + 1 + 2 = 5. Both are shortest
paths, and either one is a correct answer (slide 7 says so).
</details>

### Q2b: shortest path from node 1 to node 2

Directed network. Edges: 1→2 100, 1→3 30, 2→3 20, 3→4 10, 3→5 60, 4→2 15, 4→5 50.

**Hints**
- The direct edge 1→2 (100) is **not** the answer. Keep going until 2 is permanent.
- The edge between 2 and 4 points **from 4 to 2**, and the one between 2 and 3 points **from 2 to 3**.
- This is the same network as lecture slide 2 (left).

**Check:** Q2 answers deck, slides 8–15. Slide 9 initialises and slide 10 shows the network again
without the label boxes. Slides 11–15 make 1, 3, 4, 2, 5 permanent; slide 15 also gives the answer.

<details>
<summary>Q2b final answer</summary>

Order made permanent: 1 (0), 3 (30), 4 (40), 2 (55), 5 (90). Vertex 2 goes from 100 (via 1) to 55 (via
4) when 4 becomes permanent. Final labels: 1 0 (−), 2 55 (4), 3 30 (1), 4 40 (3), 5 90 (3).
Backwards from 2: 2 ← 4 ← 3 ← 1. **Shortest path 1–3–4–2, length 55.**
(Vertex 5 can be reached by 1–3–5 or 1–3–4–5, both 90. That tie does not affect the answer.)
</details>

### How to mark your own work

- **The final answer is right but some steps differ.** Look for ties (two equal smallest values). Any
  choice in a tie is allowed: the distances and totals stay the same, but the order or the path may
  differ.
- **Your total in Q1 is more than 39.** You probably took an edge that closed a cycle (Kruskal) or added
  distances as in Dijkstra (Prim).
- **Your Q2 distance is too small.** Check that you followed every arrow in its direction.
- **Your Q2 distance is too large.** Check that you updated labels after **every** new permanent
  vertex, not only after the first.

---

## 7. How to read the answers notebook

`4 Tutorial Answers/Q1-Q2 answers in Python.ipynb` (optional). How to run it: [section 1](#the-notebook-ipynb-run-it-in-your-browser).

| Section | What it does | What you should see |
| --- | --- | --- |
| 1. Dijkstra | The lecture example, Q2a, Q2b | `shortest path s -> t: s-d-b-e-t length 15`; `Q2a: path 1-3-4 length 5`; `Q2b: path 1-3-4-2 length 55` |
| 2. Prim | The lecture example, from D | 7 `select …` lines, then `total weight 21` |
| 3. Kruskal | The lecture example and Q1 (with Prim and Kruskal) | `total weight 21`; then for Q1 `total weight 39` twice |
| 4. When Dijkstra fails | The negative weight example | `Dijkstra says 1 -> 2: 1-2 length 1` and `but 1-3-4-2 has length -1` |
| What do you notice? / Try it | Two short questions | Click **Answer** to reveal each answer |

How to read the printed lines:

- Dijkstra prints one line per step:
  `permanent d (d = 2); updated: b: 6 via d, e: 10 via d`. This means vertex d became permanent with
  distance 2, and then the labels of b and e changed. It is one row of the step table in
  [section 4.3](#43-dijkstras-algorithm-shortest-paths-slides-731). The table printed after it has the
  columns `v`, `d_v`, `pi_v` (pi = π).
- Prim prints `select G via edge (G,D) of weight 2`: vertex G joins the tree through edge G–D.
- Kruskal prints `(B,E) 4: F (forms a cycle)` or `(A,H) 5: T`. These are the T/F column of the slides.
- When values are equal, the notebook breaks ties by taking the vertex or edge listed first. A different
  but equally valid choice of yours is still correct.

---

## 8. If something goes wrong

| Problem | What to do |
| --- | --- |
| A `.pptx` or `.docx` shows an error or strange characters on the site | The site cannot display these files. Right-click → **Download** and open the file in PowerPoint or Word |
| The slides show the whole example at once, or I can't see what changed | Go through the slides one at a time. Red numbers and coloured edges show what changed on that slide |
| The notebook shows no output | Choose **Run → Run All Cells** and wait until every cell has a number in `[ ]` |
| The notebook shows an error after I edited it | Choose **Kernel → Restart Kernel and Run All Cells**. If that doesn't help, download a fresh copy: right-click → **Download** before you change anything next time |
| My notebook changes have disappeared | Changes are stored only in the browser you used. Clearing browser data, a private window or another computer loses them. Download your copy before you leave |
| My answer differs from the answer slides | Read [How to mark your own work](#how-to-mark-your-own-work): usually it is a tie, a misread weight or an arrow followed the wrong way |
| The annotated PDF says something different from the `.pptx` | Follow the `.pptx`; the PDF is the 2020-21 version |

---

## 9. Check your understanding

Try each question first, then open the answer.

1. Why does every vertex start with distance ∞ in Dijkstra, except the source?
   <details><summary>Answer</summary>No route to it has been found yet. Any real route will be shorter
   than ∞, so the first route found will replace it. The source is 0 away from itself.</details>

2. In the lecture example, what is the shortest distance from s to c, and which path gives it?
   <details><summary>Answer</summary>17, by s–d–b–c (2 + 4 + 11). You can read it from the final table:
   c 17 (b), b 6 (d), d 2 (s).</details>

3. Why can't Dijkstra handle a negative weight?
   <details><summary>Answer</summary>Once a vertex is permanent, Dijkstra never changes it. It assumes
   that a path which is already longer cannot become shorter by adding more edges. With a negative edge
   it can, as in the negative weight example (1–3–4–2 = −1 beats 1–2 = 1).</details>

4. In Prim's algorithm, vertex E has label 7 via G. Then F is selected and the edge F–E weighs 2. What is
   E's new label: 2, or d(F) + 2?
   <details><summary>Answer</summary>2. In Prim the label is the weight of the single cheapest edge to
   the tree; distances are never added (slides 46–47).</details>

5. A connected network has 12 vertices. How many edges does its minimum spanning tree have?
   <details><summary>Answer</summary>11 (always |V| − 1).</details>

6. In Kruskal's algorithm, how do you know that an edge would form a cycle?
   <details><summary>Answer</summary>Its two ends are already connected by edges you have taken. For
   example, on slide 60, E–G is rejected because D–E and D–G are already taken.</details>

7. If you start Prim from G instead of A in Q1, do you get a different total weight?
   <details><summary>Answer</summary>No. The order of selection changes, but the total is still 39,
   and the tree is the same: Q1 has only one minimum spanning tree.</details>

8. Write the adjacency matrix of the Q2a network (rows and columns 1–4, "–" for no edge).
   <details><summary>Answer</summary>

   ```
   0  2  3  –
   –  0  1  4
   –  –  0  2
   –  –  –  0
   ```
   </details>

9. You need the cheapest way to connect 10 towns with roads. Do you use Dijkstra or an MST algorithm?
   And to find the fastest drive between two of the towns?
   <details><summary>Answer</summary>Connecting all towns: an MST (Prim or Kruskal). The fastest drive
   between two towns: Dijkstra (shortest path).</details>

10. Dijkstra is run from the source. At the end, what do you know besides the shortest path to the
    destination?
    <details><summary>Answer</summary>The shortest distance (and, through the predecessors, the shortest
    path) from the source to **every** vertex (slides 29–30).</details>

---

## 10. Checklist: have you finished the week?

- [ ] I have gone through lecture slides 1–31 and can explain the four steps of Dijkstra.
- [ ] I can redo the lecture's Dijkstra example on paper and get s–d–b–e–t = 15.
- [ ] I have gone through the negative weight deck and can explain why Dijkstra fails there.
- [ ] I have gone through slides 36–69 and know the difference between Prim and Kruskal.
- [ ] I know that Prim's label is one edge's weight, not a total distance.
- [ ] I solved tutorial Q1 with both Prim (from A) and Kruskal: total 39.
- [ ] I solved Q2a (1–3–4 or 1–2–3–4, length 5) and Q2b (1–3–4–2, length 55).
- [ ] I compared every step with the answer decks and understand any difference (ties).
- [ ] *(Optional)* I ran the answers notebook and read its output.
- [ ] *(Optional)* I looked at `Dijkstra Algorithm.pptx` and the MIT notes.
- [ ] I answered the questions in section 9.

**For the in-class test.** The revision material in `Assignments/03-in-class-test/revision/` includes
minimum spanning tree questions. The full revision booklet asks you to explain what an MST is, to find
one with Prim's or Kruskal's algorithm showing the main steps, and to state the selected links and their
total cost. Practise writing out each step in a table, as in Q1.

---

## 11. Assumptions

These points were not stated in the course material, so this README assumes them:

- Students reach the files through the course site https://ctsallis.github.io/operational_research/
  (the address in the repository's start-here notebook) and have PowerPoint and Word to open the
  downloaded `.pptx` and `.docx` files.
- The tutorial answers in `4 Tutorial Answers` are available to you now. This README asks you to try
  each question before opening them. It does not say when the answers are released in the taught
  course.
- No time estimates are given, because the material does not state how long each part should take.
- The handbook's Week 8 title ("Transportation and Transhipment Problem") differs from this folder's
  content. This README covers what the folder contains: shortest paths and minimum spanning trees.
- The annotated PDF and the `.pptx` were matched slide by slide by their titles. Small differences in
  wording are expected, because the PDF is an older version.
- The empty staff note in `5 Source Files/Staff Notes` is for the lecturer only. It is assumed to need
  no action from students.

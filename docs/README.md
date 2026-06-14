# cOde(n) — Algorithm Reference

Welcome to the cOde(n) algorithm reference. This is the in-app
companion to the 263 challenges you can solve inside the
desktop app — every algorithm has a write-up here that explains
the problem, the approach, the pseudocode, a worked example,
the complexity, real-world applications, and links to related
algorithms you can practice next.

## How to read this

- **Inside the app:** pick a challenge from the left rail,
  then click the new **Reference** tab. The doc for that
  algorithm renders inline (powered by the same markdown engine
  this README uses).
- **On disk:** every per-algorithm doc is a plain `.md` file
  under `docs/algorithms/{category}/{id}_{slug}.md`. You can
  read them in any editor, search them with `grep`, or open
  them in a browser.
- **Editing:** copy `docs/_template.md` into the right
  category folder, fill in the sections, and the new doc
  will appear in the app on the next launch.

## What the ratings mean

Each algorithm has two scores (both 1-10):

- **Difficulty** — how hard the algorithm is to implement
  correctly on a whiteboard. 1 = trivial (one loop, no logic),
  10 = research-level (Strassen, push-relabel, FPTAS).
- **Interview relevance** — how often the algorithm is asked
  in coding interviews at FAANG-tier and adjacent companies.
  1 = never (esoteric), 10 = must-know (binary search, DP
  basics, hash maps).

A high-relevance + low-difficulty algorithm is "free win"
material. A low-relevance + high-difficulty one is "stretch
goal" territory.

## Quick stats

- **263** algorithms across **27** categories
- **102** automated tests (83 engine + 19 server), all green
- **89.6 MB** Windows installer (`cOde(n)-Setup-{version}.exe`)
  with in-app auto-update via GitHub Releases
- 11 algorithms written up in detail so far; the rest will
  follow the same template (`docs/_template.md`)

## Per-category summary

The columns are: number of challenges in the category (`#`),
the engine's existing `difficulty` (avg), my `difficulty` (avg),
and my `relevance` (avg). Higher relevance = interview priority.

| Category | # | existing d | my d | **my r** |
|---|---:|---:|---:|---:|
| **hashing** | 6 | 4.0 | 4.0 | **9.0** |
| **dynamic** | 30 | 5.0 | 5.1 | **8.9** |
| **searching** | 12 | 3.6 | 3.0 | **8.0** |
| **graphs** | 21 | 5.2 | 5.0 | **8.0** |
| **sorting** | 14 | 4.6 | 4.0 | **8.0** |
| **trees** | 23 | 3.4 | 4.0 | **8.0** |
| **bit_manipulation** | 12 | 3.0 | 2.7 | **7.0** |
| **linked_list** | 5 | 3.0 | 3.0 | **7.0** |
| **recursion** | 4 | 2.8 | 3.0 | **7.0** |
| **stack** | 8 | 3.9 | 4.0 | **7.0** |
| **strings** | 14 | 4.6 | 4.0 | **7.0** |
| **greedy** | 13 | 4.1 | 4.0 | **6.7** |
| **backtracking** | 6 | 4.8 | 5.0 | **6.0** |
| **heap** | 6 | 5.0 | 5.0 | **6.0** |
| **divide_conquer** | 19 | 4.7 | 5.2 | **5.9** |
| **trie** | 4 | 3.0 | 3.0 | **5.0** |
| **math** | 10 | 3.7 | 4.3 | **4.7** |
| **queue** | 5 | 3.6 | 2.4 | **4.0** |
| **fenwick** | 7 | 4.1 | 4.0 | **3.9** |
| **segment_tree** | 6 | 4.5 | 5.0 | **3.0** |
| **branch_and_bound** | 6 | 5.8 | 6.0 | **2.7** |
| **randomized** | 7 | 4.3 | 5.3 | **2.1** |
| **geometric** | 7 | 4.4 | 4.7 | **2.0** |
| **flow** | 6 | 6.0 | 6.2 | **1.8** |
| **suffix_array** | 5 | 4.2 | 5.0 | **1.8** |
| **approximation** | 7 | 5.0 | 5.6 | **1.1** |
| **intro** | 1 | 1.0 | 1.0 | **1.0** |

The top 6 categories by relevance (hashing, dynamic, searching,
graphs, sorting, trees) cover **~75 % of real coding interview
questions.** The bottom 7 (randomized, geometric, flow,
suffix_array, approximation, intro, …) are mostly research
material — interesting to know, rarely asked.

## Recommended interview-prep path

The path below is ordered by **interview priority first, then
difficulty ramp**. Aim to write each algorithm from scratch
(in the cOde(n) editor or on a whiteboard) before moving on;
being able to recite the approach from memory is the goal.

### Phase 1 — Foundations (≈ 1 week)

These are the "if you don't know these, stop here" topics.
All are difficulty ≤ 3.

| # | ID | Name | d | r |
|---|---|---|---:|---:|
| 1 | `intro_01` | Hello Grid | 1 | 1 |
| 2 | `bit_02` | Power of Two Check | 1 | 7 |
| 3 | `recursion_01` | Power Sum | 2 | 7 |
| 4 | `linked_list_01` | Reverse Linked List | 2 | 7 |
| 5 | `sort_01` | Bubble Sort | 2 | 8 |
| 6 | `search_01` | Linear Search | 1 | 8 |
| 7 | `search_02` | Binary Search | 3 | 8 |
| 8 | `hash_01` | Two Sum | 4 | 9 |
| 9 | `stack_01` | Balanced Parentheses | 2 | 7 |
| 10 | `tree_01` | Preorder Traversal | 3 | 8 |

**Checkpoint:** you should be able to write binary search, a
hash-map-backed two-sum, and a recursive linked-list reversal
from memory in under 10 minutes.

### Phase 2 — Core interview topics (≈ 3-4 weeks)

The 80 %-of-interviews topics. Difficulty 3-5, relevance 7-9.

| # | ID | Name | d | r |
|---|---|---|---:|---:|
| 11 | `graph_02` | Breadth-First Search | 5 | 8 |
| 12 | `graph_03` | Depth-First Search | 5 | 8 |
| 13 | `graph_09` | Union-Find (DSU) | 5 | 8 |
| 14 | `sort_04` | Merge Sort | 5 | 8 |
| 15 | `sort_05` | Quick Sort | 5 | 8 |
| 16 | `sort_06` | Heap Sort | 6 | 8 |
| 17 | `heap_02` | Kth Largest Element | 5 | 6 |
| 18 | `heap_05` | Sliding Window Maximum | 5 | 6 |
| 19 | `linked_list_02` | Detect Cycle | 3 | 7 |
| 20 | `linked_list_03` | Merge Two Sorted Lists | 3 | 7 |
| 21 | `stack_02` | Next Greater Element | 4 | 7 |
| 22 | `stack_04` | Largest Rectangle in Histogram | 6 | 7 |
| 23 | `string_01` | Anagram Check | 1 | 7 |
| 24 | `string_03` | Longest Substring Without Repeating | 4 | 7 |
| 25 | `greedy_01` | Activity Selection | 4 | 6 |
| 26 | `greedy_06` | Gas Station | 4 | 6 |
| 27 | `dp_01` | Fibonacci | 5 | 9 |
| 28 | `dp_02` | Climbing Stairs | 5 | 9 |
| 29 | `dp_11` | House Robber | 5 | 9 |
| 30 | `dp_03` | 0/1 Knapsack | 5 | 9 |
| 31 | `dp_05` | Coin Change | 5 | 9 |
| 32 | `dp_04` | Longest Common Subsequence | 5 | 9 |
| 33 | `dp_08` | Edit Distance | 5 | 9 |
| 34 | `dp_07` | Longest Increasing Subsequence | 5 | 9 |

**Checkpoint:** 8-10 standard DP problems in 30-45 min each.
You should be able to look at a fresh DP problem and identify
the state, the recurrence, and the base cases in under 5 min.

### Phase 3 — Advanced (≈ 3-4 weeks)

For staff / senior candidates and the harder rounds at
FAANG. Difficulty 5-6, relevance 7-8.

| # | ID | Name | d | r |
|---|---|---|---:|---:|
| 35 | `graph_04` | Dijkstra | 5 | 8 |
| 36 | `graph_07` | Topological Sort | 5 | 8 |
| 37 | `graph_05` | Bellman-Ford | 5 | 8 |
| 38 | `graph_06` | Floyd-Warshall | 5 | 8 |
| 39 | `graph_08` | Kruskal's MST | 6 | 8 |
| 40 | `graph_10` | Prim's MST | 6 | 8 |
| 41 | `graph_18` | A* Search | 6 | 8 |
| 42 | `graph_15` | Tarjan's SCC | 6 | 8 |
| 43 | `dp_13` | Matrix Chain Multiplication | 6 | 9 |
| 44 | `dp_21` | Boolean Parenthesization | 6 | 9 |
| 45 | `dp_26` | Optimal Binary Search Tree | 6 | 9 |
| 46 | `tree_22` | AVL Insert (Simplified) | 5 | 8 |
| 47 | `segtree_02` | Range Sum Query (Segtree) | 4 | 3 |
| 48 | `heap_04` | Median in a Stream | 6 | 6 |
| 49 | `string_03` | KMP String Matching | 4 | 7 |
| 50 | `string_06` | Rabin-Karp | 4 | 7 |
| 51 | `string_07` | Z-Algorithm | 4 | 7 |
| 52 | `trie_01` | Trie Insert and Search | 3 | 5 |
| 53 | `trie_02` | Word Count with Prefix | 3 | 5 |

**Checkpoint:** implement Dijkstra from a blank file, then
re-implement it the next day without looking.

### Phase 4 — Stretch (optional, for the truly ambitious)

Specialist material. Difficulty 7+. Asked at Meta Staff,
Google L7, hedge funds, quant shops. Most candidates stop
after Phase 3.

| ID | Name | d | r |
|---|---|---:|---:|
| `approx_04` | Christofides TSP | 7 | 1 |
| `approx_07` | 0/1 Knapsack FPTAS | 7 | 1 |
| `flow_06` | Push-Relabel Max Flow | 7 | 1 |
| `dc_06` | Strassen Matrix Multiplication | 7 | 1 |
| `graph_20` | Held-Karp TSP | 6 | 8 |
| `dp_16` | Egg Dropping | 5 | 5 |
| `segtree_05` | Range Update w/ Lazy Propagation | 6 | 3 |
| `randomized_05` | Karger's Min-Cut | 6 | 1 |
| `suffix_03` | LCP Array (Kasai) | 5 | 1 |
| `bb_06` | TSP via Reduced Matrix (B&B) | 7 | 1 |

## Where to start

If you have **2 hours**, do Phase 1.
If you have **1 week**, do Phase 1 + the first 10 of Phase 2.
If you have **1 month**, do all of Phases 1-3.
If you have **2 months** and want a real edge, add the DP
classics from Phase 2 (items 27-34) and the graph algorithms
from Phase 3 (items 35-42).

For each algorithm, the recommended practice loop is:

1. **Read** the doc in the Reference tab.
2. **Implement** the algorithm in the cOde(n) editor without
   looking at the solution. Run it on the test inputs until
   it passes.
3. **Re-implement** the next day from memory. If you get
   stuck, read just the approach section — not the pseudocode.
4. **Explain it** out loud (rubber-duck or a friend). If you
   can't, you don't yet know it.

## About the docs themselves

- Each per-algorithm doc is **original content** written for
  cOde(n), modeled on the canonical structure used by
  competitive-programming reference sites (problem statement,
  approach, pseudocode, walk-through, complexity, variants,
  applications). It is NOT copied from any other source.
- The **Wikipedia link at the top of every doc** is the
  canonical encyclopedia entry — read that if you want the
  mathematically rigorous treatment.
- Docs that aren't yet written render in the app as a
  friendly empty state with a "Contribute" link that opens
  a pre-filled GitHub issue. See
  [`docs/_template.md`](file:///C:/dawei7/code_n/docs/_template.md)
  for the markdown skeleton to fill in.
- The heuristic that generates the difficulty + relevance
  scores lives in [`rate_algos.py`](file:///C:/dawei7/code_n/rate_algos.py)
  and is re-runnable. The output is
  [`algo_ratings.md`](file:///C:/dawei7/code_n/algo_ratings.md).

Happy learning — and may your complexity be O(n log n).

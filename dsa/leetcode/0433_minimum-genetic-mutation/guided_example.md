# Guided Example: Minimum Genetic Mutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"startGene": "AACCGGTT", "endGene": "AACCGGTA", "bank": ["AACCGGTA"]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A gene string can be represented by an 8-character long string, with choices from `'A'`, `'C'`, `'G'`, and `'T'`.

The objective is to compute `1` from `{"startGene": "AACCGGTT", "endGene": "AACCGGTA", "bank": ["AACCGGTA"]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Model valid genes as an unweighted graph

Treat each gene string as a vertex. Two genes have an edge when they differ in exactly one character, because one mutation changes precisely one position. The starting gene is a valid initial vertex even if absent from `bank`; every later vertex must come from the bank.

Every edge represents one mutation and has equal cost. The requested minimum number of mutations is therefore an unweighted shortest-path distance from `startGene` to `endGene`. Breadth-first search is the appropriate traversal because it visits vertices in nondecreasing distance from the start.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"startGene": "AACCGGTT", "endGene": "AACCGGTA", "bank": ["AACCGGTA"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Queue each gene with its distance

The queue begins with `(startGene, 0)`, and `vis` initially contains `startGene`. The integer `depth` is the exact number of edges in the discovered path to `gene`.

When a pair is removed with `popleft()`, the code first checks `gene == endGene`. If true, it returns `depth`. This correctly handles `startGene == endGene` with answer zero, even if the target is not listed in the bank.

Because the queue is first-in, first-out, all states at depth $d$ are removed before states first discovered at depth $d+1$. The first target removal therefore has the smallest possible depth.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Discover neighbors by comparing against the bank

For the current gene, the solution loops through every string `nxt` in `bank`. It computes

`diff = sum(a != b for a, b in zip(gene, nxt))`.

The paired positions have equal fixed length, so each unequal character contributes `true`, which Python sums as one. `diff` is exactly the Hamming distance between the two gene strings.

When `diff == 1`, one legal mutation transforms `gene` into `nxt`. If `nxt` has not been visited, it is appended with `depth + 1` and marked immediately.

Marking at enqueue time is important. If marking waited until dequeue, several current-level genes could enqueue the same neighbor, wasting work and potentially expanding it multiple times. Immediate marking keeps one queue entry per gene string.

The loop does not generate arbitrary strings. Every discovered next state comes directly from `bank`, automatically enforcing mutation validity. The starting gene is the sole allowed exception.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"startGene": "AACCGGTT", "endGene": "AACCGGTA", "bank": ["AACCGGTA"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate all one-character mutations:** For each of $L$ positions, try the other three bases and test membership in a bank set. This reaches $O(BL)$ expected time after set construction and matches the manifest bound.
- **Wildcard-pattern buckets:** Map patterns such as `AACCGGT*` to genes, then retrieve neighbors through shared patterns. This is useful for larger banks but adds preprocessing machinery.
- **Depth-first search:** It can determine reachability but does not naturally guarantee the first found path is shortest; it would need exhaustive distance tracking.
- **Bidirectional BFS:** Search simultaneously from start and target to reduce explored layers in larger graphs. The bank limit is tiny, so ordinary BFS is simpler.
- **Target equals start:** The dequeue check returns zero immediately, independent of bank membership.
- **Target absent from bank:** Unless it equals the start, it can never be enqueued because every mutation destination is selected from `bank`, so the result is `-1`.
- **Empty bank:** Only the start is processed; a distinct target is unreachable.
- **Duplicate bank strings:** `vis` prevents duplicate string states from being enqueued more than once.
- **Difference zero:** A gene is not a one-mutation neighbor of itself and is not enqueued by `diff == 1`.
- **Difference greater than one:** It cannot be traversed in a single step, though intermediate bank genes may eventually connect it.
- **Mark on enqueue:** This prevents multiple shortest-path parents from creating duplicate queue entries while preserving the first, minimal depth.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B^2L)$. Let $B$ be `len(bank)` and $L$ the gene length. At most $B$ bank strings, plus the start, are dequeued. For every dequeued state, the exact implementation scans all $B$ bank entries, and each `zip`/sum comparison costs $O(L)$. Its generalized worst-case time is therefore
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

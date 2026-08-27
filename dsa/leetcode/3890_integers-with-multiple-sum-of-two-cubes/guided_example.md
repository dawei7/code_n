# Guided Example: Integers With Multiple Sum of Two Cubes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4104}`
- **Required output:** `[1729, 4104]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `[1729, 4104]` from `{"n": 4104}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why canonical pairs prevent false duplicates

Addition is symmetric:

$$
a^3+b^3=b^3+a^3.
$$

If both ordered pairs $(a,b)$ and $(b,a)$ were counted, almost every sum with $a\ne b$ would incorrectly appear to have two representations. The requirement $a\le b$ provides one canonical orientation. The nested loops enforce it by starting `b` at `a`.

Pairs with $a=b$ are allowed and are visited once. They count as one representation, not two. A sum enters the answer only when the count of distinct canonical pairs is greater than one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4104}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why bases through 1000 cover the fixed limit

Both bases are positive. If either base were at least 1000, then even the smallest possible other cube would make

$$
1000^3+1^3=1{,}000{,}000{,}001>10^9.
$$

Therefore no valid sum at most `LIMIT` needs a base greater than 999. The source builds



for indices 0 through 1000. Including 1000 is harmless and lets the loop discover the boundary by its ordinary stopping condition.

For every `a` from 1 through 1000, `b` increases from `a` through 1000. The value

$$
x=a^3+b^3
$$

strictly increases as `b` increases. As soon as `x > LIMIT`, every later `b` for the same `a` would also be too large, so `break` safely ends that inner loop. Every legal canonical pair is visited exactly once before a break, and no illegal over-limit value is inserted into the counter.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Both bases are positive.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the counter represents

The global dictionary `cnt` maps a cube sum to the number of canonical pairs that produce it. Each visited pair performs `cnt[x] += 1`.

After enumeration, the comprehension keeps precisely those keys whose count is greater than one:

$$
\texttt{GOOD}
=
\operatorname{sorted}\{x:\texttt{cnt}[x]>1\}.
$$

The “greater than one” test matches “at least two distinct pairs.” It also naturally handles numbers with three or more representations: they appear once in `GOOD`, because `GOOD` contains sum values rather than representation pairs.

Sorting is performed once. The resulting global list is strictly increasing because dictionary keys are unique.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1729, 4104]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4104}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1729, 4104]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Per-query enumeration:** Enumerating only pair:** - **Per-query enumeration:** Enumerating only pairs whose sums are at most the supplied `n` can do less work for a small one-off input, but it repeats the expensive stage across calls and differs from the fixed global strategy in the source.
- **Store only repeated sums:** A set-based transition from “seen once” to “seen multiple times” can reduce stored counts, although all first occurrences still need tracking to detect the second representation.
- **Pair-sum sorting:** Generating every cube sum into a list, sorting it, and detecting adjacent duplicates also works, but stores duplicate sum entries and pays to sort the full pair list.
- **Positive bases only:** Zero is not a legal base. The loops correctly begin at 1, so representations such as $0^3+b^3$ never count.
- **Equal bases:** A pair $(a,a)$ is legal and is enumerated once. It cannot alone make a number good; another distinct canonical pair is still required.
- **Boundary value inclusion:** `bisect_right` is necessary because the answer includes values equal to `n`. A left-biased search would wrongly exclude a good value exactly at the query boundary.
- **Small upper bounds:** When no precomputed good value is at most `n`, `idx` is zero and slicing returns `[]`.
- **Values with more than two representations:** The counter may exceed two, but `GOOD` still contains the integer only once.
- **Fixed constraint ceiling:** The precomputation is valid because the contract caps `n` at $10^9$. Raising that ceiling without also raising `LIMIT` and the base range would silently omit answers.
- **Module-level work:** Importing the file performs the full enumeration before `findGoodIntegers` is called. This can be advantageous for repeated queries but should not be mistaken for a constant-cost method call in a fresh process.
- **Required library names:** Standalone execution needs `defaultdict` and `bisect_right` supplied from the Python standard library; the checked-in file assumes the harness exposes them.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B^2)$. The source has two phases, so their costs should be stated separately.
- **Auxiliary Space Complexity:** $O(B^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

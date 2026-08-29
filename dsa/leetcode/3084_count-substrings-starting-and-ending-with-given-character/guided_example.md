# Guided Example: Count Substrings Starting and Ending with Given Character

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abada", "c": "a"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and a character `c`. Return *the total number of substrings of *`s`* that start and end with *`c`*.*

The objective is to compute `6` from `{"s": "abada", "c": "a"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**A valid substring is determined by endpoint occurrences.** Let character $c$ appear $q$ times in `s`. A substring starting and ending with $c$ can use:

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abada", "c": "a"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

- the same occurrence as both endpoints, producing a length-one substring;
- two distinct occurrences, with the earlier one as start and later one as end.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Every choice of endpoints determines exactly one substring, including all characters between them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abada", "c": "a"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Store every occurrence index:** It also yields $q$, but wastes $O(q)$ space because exact positions are unnecessary.
- **Enumerate all substrings:** There are $O(N^2)$ and checking endpoints repeats work.
- **Streaming count:** As each $c$ appears, add the number of occurrences seen so far; this also derives the triangular total in $O(N)$ time and $O(1)$ space.
- **No occurrence of $c$:** $q=0$ and the formula returns zero.
- **One occurrence:** Only its length-one substring counts, returning one.
- **Every character equals $c$:** Every substring qualifies and the formula returns total substring count.
- **Interior copies of $c$:** They create additional endpoint choices but do not invalidate larger ranges.
- **Identical substring text at different positions:** Both occurrences count through distinct endpoints.
- **Integer division:** $q(q-1)$ is always even, so `//2` is exact.
- **Character length:** The contract supplies one lowercase character `c`; longer strings would change the meaning of `s.count`.
- **Endpoint order is automatic:** For two selected occurrences, the smaller index must be the start and larger index the end, so each unordered pair yields exactly one substring rather than two.
- **Length-one ranges use one occurrence:** They are not included in $\binom q2$, which is why the separate $q$ term is necessary.
- **Closed-form alternative:** The expression can simplify to `cnt * (cnt + 1) // 2`. The source's form mirrors the two endpoint cases more explicitly.
- **Overlapping substrings:** They are independent endpoint choices and all count; no disjointness requirement exists.
- **Whole string:** It qualifies whenever both the first and final characters equal `c`, corresponding to that endpoint pair.
- **Middle characters unrestricted:** They may include any number of additional `c` occurrences, and the larger substring still counts once for its chosen outer endpoints.
- **Counting built-in:** `str.count` with a one-character argument counts every occurrence, including adjacent ones.
- **Maximum result:** With $q=N=10^5$, the answer is $5{,}000{,}050{,}000$, demonstrating why a 64-bit or arbitrary-precision result is needed.
- **No answer reconstruction:** Only the total is requested, so storing endpoint positions would be unnecessary.
- **Combinatorial partition is exhaustive:** Every valid range has either equal endpoint indices or distinct endpoint indices; the $q$ and combination terms cover these disjoint cases.
- **No double counting between cases:** Length-one substrings cannot arise from choosing two occurrences, while every longer valid substring has two distinct endpoint occurrences.
- **Linear lower bound:** Any solution must at least inspect the string to know how many target characters occur, so the $O(N)$ scan is asymptotically optimal.
- **Character not present:** The arithmetic remains well-defined because both terms vanish when `cnt=0`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. `s.count(c)` scans the length-$N$ string once, taking $O(N)$ time. The arithmetic afterward is constant work. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

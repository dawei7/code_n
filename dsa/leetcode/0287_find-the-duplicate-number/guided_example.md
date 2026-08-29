# Guided Example: Find the Duplicate Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 4, 2, 2]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `nums` containing $n + 1$ integers where each integer is in the range `[1, n]` inclusive.

The objective is to compute `2` from `{"nums": [1, 3, 4, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search the value range without rearranging the array

The array has length $n+1$, but every value lies from 1 through $n$. The extra array position guarantees a duplicate by the pigeonhole principle: placing $n+1$ entries into only $n$ possible value categories forces at least one category to contain multiple entries.

The exact protected solution does not use the cycle-detection method described by the manifest. It binary-searches the possible duplicate value using a counting predicate. This respects the requirements because it only reads `nums` and keeps no set, copied array, or other size-dependent structure.

For a candidate value $x$, define

$$
C(x)=\#\{v\in\texttt{nums}:v\le x\}.
$$

The helper `f(x)` returns whether `C(x) > x`. The solution finds the smallest $x$ for which this predicate is true.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 4, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why compare the count with `x`

There are exactly $x$ possible values in the range `[1, x]`. If more than $x$ array entries fall into that range, at least one of those values must repeat. This is another direct pigeonhole argument: more than $x$ entries are occupying only $x$ value categories.

The special contract that only one distinct number repeats makes the first overloaded prefix identify that repeated value exactly. Before the duplicate value enters the prefix, no value in the prefix can occur more than once. Once the duplicate enters, the prefix contains too many entries for its number of possible values.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Prove the predicate is false before the duplicate

Let the one repeated value be $d$. For any $x<d$, the prefix `[1, x]` excludes every occurrence of $d$. Every value it does include occurs at most once, because no other distinct value repeats.

There are only $x$ possible values in that prefix, so at most $x$ array entries can be at most $x$:

$$
C(x)\le x.
$$

Therefore, `f(x)` is false for every $x<d$.

Some values in `[1, x]` may be missing from the array, making the count strictly smaller than $x$; that only strengthens the false result.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 4, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Floyd cycle detection:** Interpret each value as the next array index, find a cycle intersection, then find its entrance. It achieves the manifest's $O(n)$ time and $O(1)$ space without mutation, but it is not the exact source.
- **Hash set:** Return the first value seen twice. Expected time is $O(n)$, but the set needs $O(n)$ additional space.
- **Sort then scan:** Adjacent equal values reveal the duplicate in $O(n\log n)$ time, but in-place sorting violates the non-modification requirement and sorting a copy uses $O(n)$ space.
- **Negative marking or cyclic placement:** These can use constant auxiliary space but mutate `nums`, which is explicitly forbidden.
- **Duplicate appears twice:** No allowed value needs to be missing. At $d$, the prefix gains exactly one extra occurrence and becomes overloaded.
- **Duplicate appears many times:** Exactly $r-2$ allowed values are absent when the duplicate occurs $r$ times. The extra occurrences still exceed all possible missing-prefix deficits by one.
- **Duplicate is 1:** `f(0)` is false and `f(1)` is true, so the boundary search returns 1.
- **Duplicate is `n`:** Every smaller candidate is false and the guaranteed true endpoint `n` is returned.
- **Absent candidate values:** Binary search searches the numeric domain, not just values occurring in `nums`. The prefix-count predicate remains meaningful at absent candidates.
- **Only one distinct repeated value:** The proof relies on this guarantee. With several different duplicate values, the first overloaded prefix could identify the smallest repeated region but would not satisfy the stated single-answer contract.
- **Array values outside `[1, n]`:** Zero or larger values would invalidate the sentinel and pigeonhole arguments. The implementation intentionally trusts the range constraint.
- **Read-only behavior:** Repeated full scans may be slower than Floyd's method, but they preserve every input byte and need no auxiliary collection.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Binary search evaluates `f` $O(\log n)$ times. Each evaluation scans all $n+1$ entries to compute `C(x)`, taking $O(n)$ time. The exact total is therefore
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

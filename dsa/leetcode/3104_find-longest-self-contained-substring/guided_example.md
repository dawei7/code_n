# Guided Example: Find Longest Self-Contained Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abba"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, your task is to find the length of the **longest self-contained** substring of `s`.

The objective is to compute `2` from `{"s": "abba"}` while avoiding redundant calculations and unnecessary overhead.

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

**What self-contained really requires.** A substring `s[i:j + 1]` is self-contained when every occurrence in the complete string of every character appearing inside the substring also lies between `i` and `j`. It must also be a proper substring, so its length must be smaller than `len(s)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

This can be expressed with global first and last occurrences. If a character `c` appears inside a candidate, then:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | This can be expressed with global first and last occurrences... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
\texttt{first[c]}\ge i
\quad\text{and}\quad
\texttt{last[c]}\le j.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Partition-label intervals:** Build closed inte:** - **Partition-label intervals:** Build closed intervals from first and last occurrences and merge dependencies. It can express the same closure idea but needs care to consider the longest proper union.
- **Try every substring:** Checking outside occurrences for all $O(n^2)$ candidates is far slower.
- **Prefix frequency counts:** They can test one candidate quickly but still leave too many candidate boundaries without the first-occurrence reduction.
- **Whole string only:** It is explicitly forbidden, so the length check must reject it even though it is always occurrence-closed.
- **No proper candidate:** `ans` stays -1.
- **One unique character at an interior position:** Its one-character substring is self-contained and can be recorded.
- **Character seen before the start:** `a < i` makes the entire start impossible, so breaking is stronger and safer than merely skipping one endpoint.
- **Character whose last occurrence is later:** `mx` extends the required boundary to include it.
- **Nested dependencies:** Newly included characters can extend `mx` repeatedly; scanning until closure resolves the chain.
- **Multiple closures for one start:** The scan continues because a later closure can be longer.
- **Repeated start character:** Initial `mx = last[c]` guarantees every copy is included.
- **Lowercase alphabet:** The constant 26 is what turns the outer-times-inner work into $O(n)$.
- **Dictionary iteration order:** It follows first insertion order in Python, but answer correctness does not depend on candidate order.
- **Length at least two for input:** The full-string exclusion can therefore still leave meaningful proper candidates.
- **No input mutation:** The source only records positions and scans `s`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(26n)$. The first/last map construction takes $O(n)$ time. The outer loop has at most 26 iterations, and each inner loop scans at most $n$ positions. Total time is $O(26n)=O(n)$ under the fixed lowercase alphabet.
- **Auxiliary Space Complexity:** $O(26)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

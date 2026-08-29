# Guided Example: Find Unique Binary String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": ["01", "10"]}`
- **Required output:** `"11"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of strings `nums` containing `n` **unique** binary strings each of length `n`, return *a binary string of length *`n`* that **does not appear** in *`nums`*. If there are multiple answers, you may return **any** of them*.

The objective is to compute `"11"` from `{"nums": ["01", "10"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Classify strings by how many ones they contain

A binary string of length $N$ can contain zero, one, two, and so on through $N$ ones. That gives $N+1$ possible one-count classes.

The input contains only $N$ strings. Even if every input string belongs to a different class, at most $N$ of the $N+1$ classes can be present. By the pigeonhole principle, at least one count $i$ from zero through $N$ is missing.

If the method constructs any length-$N$ string containing exactly $i$ ones, that string cannot equal an input string. Equal binary strings necessarily have equal numbers of ones, while no input has that chosen count.

This is the central idea of the exact source. It differs from the familiar diagonal-bit construction, although both guarantee a missing string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": ["01", "10"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store present counts in a bit mask

`mask` is an integer used as a compact set. Bit $k$ is one exactly when an input string with $k$ ones has been observed.

For each string `x`, `x.count("1")` scans its characters and returns its number of ones. The expression `1 << count` creates an integer whose only set bit is at that position. Bitwise OR,

`mask |= 1 << x.count("1")`,

records the class without disturbing any class recorded earlier. Several strings with the same one count simply set the same bit again.

For example, if the input one counts are one and two, bits one and two become set. Bit zero is clear, so a string with no ones is guaranteed absent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the first missing class

`count(0)` supplies the infinite sequence 0, 1, 2, and so forth. For each candidate `i`, the expression `mask >> i & 1` extracts bit $i$.

The source then XORs that bit with one. For a bit value of zero, `0 ^ 1` is one and the condition succeeds. For a set bit, `1 ^ 1` is zero and the search continues. In plain language, the condition asks whether class $i$ has not appeared.

Although the iterator is unbounded syntactically, the proof guarantees a missing class among 0 through $N$. The loop therefore returns after at most $N+1$ checks and never reaches an impossible one-count larger than the string length.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"11"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": ["01", "10"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"11"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Cantor diagonal construction:** Flip `nums[i][i]` for every $i$. It gives $O(N)$ time and an immediate per-row difference proof.
- **Hash set plus enumeration:** Generate candidates until one is absent, but candidate construction and membership storage are unnecessary here.
- **Integer-set search:** Convert inputs to integers and test $0$ through $N$; conversion still reads $O(N^2)$ input characters.
- **Missing class zero:** Return the all-zero string.
- **Missing class $N$:** Return the all-one string; the zero suffix has length zero.
- **Several missing counts:** Returning the smallest is valid because any missing class works.
- **Many strings share a one count:** One mask bit represents them all, leaving even more classes absent.
- **Input order:** It has no effect because bitwise OR records only presence.
- **One input string:** There are two weight classes, so the loop finds the other one.
- **No direct membership test:** The missing-weight proof makes one unnecessary.
- **Infinite-looking iterator:** `count(0)` terminates through the guaranteed return by index $N$ at the latest.
- **Output format:** Repeating strings produces exactly $N$ characters containing only zero and one.
- **Input preservation:** Counting characters does not modify the strings or list.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2)$. Let $N=\texttt{len(nums)}$, which is also every string's length. Counting ones in all strings takes $O(N^2)$ time. Testing at most $N+1$ mask bits and building the $N$-character result take $O(N)$ additional time. Total exact time is $O(N^2)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

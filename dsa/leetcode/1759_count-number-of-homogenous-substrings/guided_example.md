# Guided Example: Count Number of Homogenous Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abbcccaa"}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the number of **homogenous** substrings of *`s`*.* Since the answer may be too large, return it **modulo** $10^{9} + 7$.

The objective is to compute `13` from `{"s": "abbcccaa"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Split the string into maximal equal-character runs

A homogenous substring cannot cross a position where the character changes. Therefore every valid substring lies entirely inside one maximal consecutive run of a single character.

The exact solution scans these runs with two indices. `i` is the first index of the current run. `j` starts at `i` and advances while `j < n` and `s[j] == s[i]`. When that inner loop ends, the half-open interval `[i, j)` is the complete maximal run beginning at `i`.

The run length is `cnt = j - i`. After counting its substrings, assigning `i = j` moves directly to the first unprocessed character, which begins the next run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abbcccaa"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count substrings inside one run

For a run of length $c$, any choice of a start and an end within the run creates a homogenous substring because every character is equal.

Count by substring length:

- There are $c$ substrings of length one.
- There are $c-1$ substrings of length two.
- This continues down to one substring of length $c$.

The total is:

$$
c+(c-1)+\cdots+1
=
\frac{c(c+1)}{2}.
$$

The source computes exactly this triangular number as:

`(1 + cnt) * cnt // 2`.

The product is always even because one of two consecutive integers `cnt` and `cnt + 1` is even, so integer division loses no fractional part.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a run of length $c$, any choice of a start and an end wi... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why runs can be counted independently

Every homogenous substring belongs to exactly one maximal run. It cannot include characters from two different runs because crossing their boundary would include at least two distinct characters.

Within a run, every contiguous substring is homogenous. Therefore summing the triangular count of each run includes every valid substring once and includes no invalid substring.

Even when two separate runs contain the same letter, they remain independent. For example, the two `a` runs in `"abbcccaa"` are separated by other characters, so no contiguous all-`a` substring can combine them.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abbcccaa"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Ending-streak counting:** Maintain the current:** - **Ending-streak counting:** Maintain the current equal-character streak and add its length at every position. It is also $O(n)$ time and $O(1)$ space.
- **Run-length array:** First store all run lengths, then sum their triangular values. It is correct but uses up to $O(n)$ extra space.
- **Enumerate substrings:** Checking all $O(n^2)$ intervals is far too slow for $n=100000$.
- **Count only distinct texts:** This is incorrect because identical substring text at different positions counts multiple times.
- **Single character:** One run of length one contributes one.
- **All characters equal:** One triangular number gives $n(n+1)/2$.
- **All adjacent characters different:** Every run has length one, so the answer is $n$.
- **Repeated letter in separated runs:** Runs cannot be merged across different intervening characters.
- **Maximum run ending at n:** The condition `j < n` prevents out-of-range access and still records the final run.
- **Half-open interval:** `j - i` is the exact run length because `j` is the first excluded index.
- **Integer division:** The product of consecutive integers is even, so `// 2` is exact.
- **Modulo placement:** Reducing after each run preserves the final modular sum.
- **No substring allocation:** Counting by lengths avoids slicing, copying, or comparing candidate strings.
- **Lowercase alphabet:** Only equality matters; the method would work for any character set.
- **Empty string:** The official constraint excludes it, so no special return branch is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. Although an inner loop appears inside an outer loop, `j` advances across each character only as part of its one run, and `i` jumps to `j` afterward. Across the whole method, every character is examined a constant number of times. Time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

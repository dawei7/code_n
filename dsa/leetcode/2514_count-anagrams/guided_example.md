# Guided Example: Count Anagrams

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "too hot"}`
- **Required output:** `18`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` containing one or more words. Every consecutive pair of words is separated by a single space `' '`.

The objective is to compute `18` from `{"s": "too hot"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count permutations independently inside each word

Words cannot exchange positions, and letters cannot move from one word to another. Only the letters inside each word are permuted.

For a word of length $L$ with character frequencies $f_1,f_2,\ldots$, the number of distinct permutations is the multinomial count

$$
\frac{L!}{\prod_c f_c!}.
$$

$L!$ counts arrangements if every occurrence were distinguishable. Dividing by $f_c!$ removes the overcount from permuting identical copies of character $c$.

Choices for different words are independent, so the total number of full-string anagrams is the product of these per-word counts.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "too hot"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Accumulate all numerator factorials

`ans` starts at one. For each word, `enumerate(w,1)` produces positions `i=1,2,...,L`.

The update

`ans = ans*i % mod`

multiplies by

$$
1\cdot2\cdots L=L!.
$$

Because this repeats independently for every word, `ans` eventually contains the product of all word-length factorials modulo `mod`.

The name `ans` is temporary at this stage: it contains only the numerator until modular division is applied at the end.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build denominator factorials without tables

A new `Counter` is created for each word because equal letters in different word positions do not belong to one shared permutation group.

When character `c` is seen for the $r$-th time, `cnt[c]` becomes $r$, and the code multiplies `mul` by $r$.

If a letter occurs $f$ times in one word, its successive contributions are

$$
1\cdot2\cdots f=f!.
$$

Doing this for every distinct letter and every word makes `mul` equal to the complete product of frequency factorials.

This incremental technique avoids precomputing factorial and inverse-factorial arrays, despite the manifest summary describing such tables.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `18` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "too hot"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `18` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Factorial tables:** Precompute factorials and inverse factorials through $N$; it also gives $O(N)$ time and space but is not the exact implementation.
- **One-letter word:** It contributes exactly one permutation.
- **All identical letters:** Numerator and denominator factorial cancel, producing one.
- **All distinct letters:** The word contributes its full length factorial.
- **Repeated letters across different words:** Their frequencies must remain separate because words are permuted independently.
- **Word order:** It never changes.
- **Single-space input:** `split` produces no empty tokens.
- **Modular inverse:** It exists because all factors are smaller than the prime modulus.
- **Large answer:** Reducing after each multiplication keeps values controlled.
- **Manifest mismatch:** The source accumulates factorial products incrementally instead of building shared tables.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert s\rvert$. Splitting and scanning every character takes $O(N)$ time. Counter operations are expected $O(1)$, and modular multiplications occur once per non-space character. Computing the modular inverse costs $O(\log \texttt{mod})$, effectively constant relative to input size. Total expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

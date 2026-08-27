# Guided Example: Find the Occurrence of First Almost Equal Substring

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcdefg", "pattern": "bcdffg"}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `s` and `pattern`.

The objective is to compute `1` from `{"s": "abcdefg", "pattern": "bcdffg"}` while avoiding redundant calculations and unnecessary overhead.

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

**A candidate is valid when all but at most one position match.** For every length-$m$ substring of `s`, where $m=\lvert\texttt{pattern}\rvert$, a direct comparison would find the first mismatch and then check the rest. Doing this independently at every start can repeat almost the same character comparisons and cost $O(nm)$. The source instead precomputes, for every start, how much matches from the left and how much matches from the right.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcdefg", "pattern": "bcdffg"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

If a candidate differs from `pattern` at one position $q$, then its first $q$ characters match and its final $m-q-1$ characters match. Their lengths sum to $m-1$. If it matches exactly, the prefix and suffix information is even larger. With two or more mismatch positions, the characters between the earliest and latest mismatch leave a gap of at least two positions, so the matching prefix and suffix sum to at most $m-2$. This creates the test used by the source:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If a candidate differs from `pattern` at one position $q$, t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

$$
\text{matchingPrefix}+\text{matchingSuffix}\ge m-1.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcdefg", "pattern": "bcdffg"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Compare every candidate directly:** It uses $O:** - **Compare every candidate directly:** It uses $O(1)$ auxiliary space but can cost $O(nm)$ on repetitive strings where comparisons run nearly to the end at many starts.
- **Rolling hash plus longest-common-prefix searches:** Hashes can locate the first mismatch and verify the suffix in roughly $O(n\log m)$ time, but ordinary modular hashing introduces collision risk.
- **Extended KMP or prefix-function methods:** Other linear string-matching preprocessors can derive comparable left/right match lengths. The Z representation is especially direct for prefix-length queries.
- **More than one mismatch:** The earliest and latest mismatches force the prefix/suffix sum below $m-1$, so the candidate is rejected.
- **Exactly one mismatch at the first character:** Prefix length is zero and suffix length is $m-1$, which passes.
- **Exactly one mismatch at the last character:** Prefix length is $m-1$ and suffix length is zero, which also passes.
- **Exact match:** “At most one” includes zero changes, so it must pass even though prefix and suffix matches may overlap.
- **Pattern length one:** Every source character can be changed into it, and the smallest valid index is zero.
- **Pattern nearly as long as source:** The loop simply has few candidate starts; index mapping into the reversed string remains valid.
- **Separator choice:** `#` is safe only because inputs contain lowercase English letters. A general alphabet would require choosing a sentinel absent from both strings or representing symbols structurally.
- **Z-array first entry:** `values[0]` remains zero by convention. The algorithm never needs it for a candidate because all queried positions lie after the separator.
- **Follow-up with $k$ consecutive changes:** The one-gap prefix/suffix condition would become a bound on the unmatched middle block's length; additional care is needed because the changes must be consecutive.
- **First occurrence requirement:** Candidate starts are inspected in increasing order and the method returns immediately, which is what turns validity testing into the minimum-index answer.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n=\lvert s\rvert$ and $m=\lvert\texttt{pattern}\rvert$. Each concatenated text has length $n+m+1$, and each Z computation is linear in that length. Reversing strings, constructing concatenations, and scanning the $n-m+1$ candidate starts are also linear. Total time is $O(n+m)$.
- **Auxiliary Space Complexity:** $O(n+m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

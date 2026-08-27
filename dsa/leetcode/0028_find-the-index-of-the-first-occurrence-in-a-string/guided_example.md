# Guided Example: Find the Index of the First Occurrence in a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"haystack": "sadbutsad", "needle": "sad"}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

The objective is to compute `0` from `{"haystack": "sadbutsad", "needle": "sad"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the search into a sequence of candidate starting positions

Let $n$ be the length of `haystack` and $m$ the length of `needle`. If a match begins at index `i`, it occupies the half-open interval from `i` through `i + m`: the included character indices are `i, i + 1, ..., i + m - 1`.

For all $m$ pattern characters to fit, the final included index must satisfy

$$
i+m-1<n.
$$

Rearranging gives $i\le n-m$. Therefore the only possible starts are

$$
0,1,\ldots,n-m,
$$

which is exactly `n - m + 1` candidates when $m\le n$.

The selected source tests those candidates directly from left to right. It is a straightforward sliding-window comparison implemented with Python string slicing, not the KMP algorithm described later in the local editorial.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"haystack": "sadbutsad", "needle": "sad"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the range includes the final legal start

Python's `range(stop)` excludes `stop`. The loop uses



so its final value is `n - m`. Omitting the `+ 1` would fail to examine the window ending exactly at the end of `haystack`. For example, searching for `"sad"` inside `"butsad"` requires start `3 = 6 - 3`; `range(3)` would stop at two, while `range(4)` correctly includes three.

If `needle` is longer than `haystack`, then `n - m + 1` is zero or negative. Python produces an empty range, so the loop performs no slice and the method returns `-1`. The exact implementation therefore handles this case without a separate length check.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Python's `range(stop)` excludes `stop`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Extract one window of exactly the pattern length

For each candidate `i`, the expression



creates the substring beginning at `i` and ending just before `i + m`. Because the loop considers only legal starts, this slice always contains exactly $m$ characters. It is then compared with `needle` using ordinary string equality.

Equality is true only when the two strings have the same length and every corresponding character is equal. Their lengths are already both $m$, so this comparison precisely asks whether `needle[j] == haystack[i + j]` for every $0\le j<m$.

There is no hash and therefore no collision risk. A true comparison is an exact character match.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"haystack": "sadbutsad", "needle": "sad"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **KMP prefix table:** Preprocess `needle` so a m:** - **KMP prefix table:** Preprocess `needle` so a mismatch reuses the longest matching border instead of restarting. It guarantees $O(n+m)$ time and uses $O(m)$ extra space.
- **Character-by-character naive windows:** Compare without creating slices. It still has $O(nm)$ worst-case time but uses $O(1)$ auxiliary space and can stop a candidate at its first mismatch.
- **Rabin–Karp rolling hash:** Update a window hash in constant time and verify hash matches. It can be linear on average, but modular hashes require collision handling for deterministic correctness.
- **Built-in `haystack.find(needle)`:** In production Python it is concise and highly optimized, but it hides the algorithm and is not the selected source being explained.
- **Needle longer than haystack:** The computed range is empty, so `-1` is returned safely.
- **Equal strings:** There is one candidate at index zero, and it matches.
- **One-character needle:** Every slice has length one; the first equal character index is returned.
- **Match at the last legal start:** The `+ 1` in the range includes index `n - m`.
- **Overlapping matches:** Increasing start order and immediate return still select the earliest one.
- **Repeated prefixes:** They can trigger the quadratic-style worst case because this method does not reuse earlier comparison work.
- **Lowercase restriction:** The algorithm itself works for any Python string characters; the contract's lowercase alphabet needs no special handling.
- **Strings are not mutated:** Slicing creates temporary strings, while both `haystack` and `needle` remain unchanged.
- **Non-empty needle:** Guaranteed locally. For an out-of-contract empty pattern, the exact implementation returns zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O((n-m+1)$. Let $n=\lvert\texttt{haystack}\rvert$ and $m=\lvert\texttt{needle}\rvert$.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

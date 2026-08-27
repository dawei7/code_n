# Guided Example: H-Index

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"citations": [3, 0, 6, 1, 5]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of integers `citations` where $\text{citations}[i]$ is the number of citations a researcher received for their $$i^{\text{th}}$$ paper, return *the researcher's h-index*.

The objective is to compute `3` from `{"citations": [3, 0, 6, 1, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the definition into a rank test

The h-index is the largest integer $h$ for which at least $h$ papers have at least $h$ citations each. The two occurrences of $h$ play different roles: one is a number of qualifying papers, and the other is the citation threshold each of those papers must meet.

If citations are sorted in descending order, the first value is the most-cited paper, the second is the next most cited, and so on. For a candidate $h$, the value at zero-based index `h - 1` is the $h$-th largest citation count. Therefore,

$$
\text{at least }h\text{ papers have at least }h\text{ citations}
\quad\Longleftrightarrow\quad
\texttt{citations}[h-1]\ge h.
$$

This single comparison works because sorting supplies an order guarantee. If the $h$-th largest value is at least $h$, every earlier value is at least as large, so the first $h$ papers all qualify. If the $h$-th largest value is below $h$, only the first $h-1$ positions could possibly meet the threshold, so there cannot be $h$ qualifying papers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"citations": [3, 0, 6, 1, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort from most cited to least cited

The exact protected solution calls `citations.sort(reverse=true)`. This modifies the input list in place and arranges citation counts from largest to smallest.

The manifest summary describes a linear-time bucket-counting method, but that is not the algorithm in this source. The protected implementation is the comparison-sort rank method, so its reasoning and true complexity are based on sorting.

Sorting is useful here because it converts the global question “how many entries are at least $h$?” into one indexed comparison. There is no need to count qualifying papers separately for every candidate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact protected solution calls `citations.sort(reverse=t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Test candidates from the largest possible value downward

A researcher with $n$ papers cannot have h-index greater than $n$, regardless of how large any individual citation count is. The source therefore tests `h = n, n - 1, ..., 1`.

For each candidate, it checks `citations[h - 1] >= h`. The first successful candidate is returned immediately. Because candidates are examined in strictly descending order, every larger candidate has already failed. The returned value is therefore not just feasible; it is the maximum feasible value required by the definition.

If no positive candidate succeeds, the method returns zero. This occurs, for example, when every paper has zero citations.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"citations": [3, 0, 6, 1, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Citation buckets capped at `n`:** Count each v:** - **Citation buckets capped at `n`:** Count each value in bucket `min(citation, n)`, accumulate qualifying-paper counts from `n` downward, and return the first threshold with enough papers. This achieves the manifest's $O(n)$ time and $O(n)$ space and avoids comparison sorting, but it is not the exact source.
- **Ascending sort:** Sort normally and test the corresponding ranked positions from the end. It has the same $O(n\log n)$ time; descending order makes the `h - 1` index direct.
- **Binary search after sorting:** Feasibility across ranks is monotone, so binary search can reduce the post-sort scan to $O(\log n)$. The initial $O(n\log n)$ sort still dominates, making the simpler linear scan reasonable.
- **Recount for every candidate:** For each $h$, scanning all citations to count values at least $h$ costs $O(n^2)$ in the worst case. Sorting once avoids repeated counting.
- **All zeros:** Every positive candidate fails and the final `0` is the only valid h-index.
- **Every paper highly cited:** If all $n$ values are at least $n$, the very first test succeeds and the answer is $n$.
- **One paper:** A positive citation count gives h-index 1; a zero count gives h-index 0.
- **Repeated citation counts:** Sorting and the rank test handle duplicates naturally. Papers are counted by position, not by distinct citation value.
- **Citations greater than `n`:** They remain large after sorting, but the candidate loop never exceeds $n$, so they cannot incorrectly produce an impossible index.
- **More than `h` qualifying papers:** This is allowed. The definition requires at least `h`, so no condition on exactly how many remaining papers fall above or below the threshold is needed.
- **Input mutation:** `sort(reverse=true)` changes the caller's list. If preserving input order were required, use `sorted(citations, reverse=true)` and account for the copied list.
- **Non-negative guarantee:** Negative citation counts are outside the contract. The proof assumes ordinary non-negative counts, though the rank comparisons would simply treat negative values as unable to qualify.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of papers. Python's comparison sort takes $O(n\log n)$ time in the worst case. The descending candidate loop performs at most $n$ constant-time comparisons, adding $O(n)$. Sorting dominates, so the exact source runs in $O(n\log n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

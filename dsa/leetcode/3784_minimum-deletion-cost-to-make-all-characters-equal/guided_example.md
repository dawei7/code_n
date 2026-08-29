# Guided Example: Minimum Deletion Cost to Make All Characters Equal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabaac", "cost": [1, 2, 3, 4, 1, 10]}`
- **Required output:** `11`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` of length `n` and an integer array `cost` of the same length, where $\text{cost}[i]$ is the cost to **delete** the $i^{\text{th}}$ character of `s`.

The objective is to compute `11` from `{"s": "aabaac", "cost": [1, 2, 3, 4, 1, 10]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose which character survives

The final string must be nonempty and contain one distinct character. Therefore every valid result can be described by choosing a lowercase letter `c` to keep and deleting every occurrence of every other letter.

Because all deletion costs are positive, once `c` is chosen there is no benefit in deleting an occurrence of `c`. Keeping it costs nothing, preserves the all-equal condition, and makes the result no worse. The cheapest result for chosen `c` keeps all its occurrences.

The optimization is consequently not over arbitrary subsets. It is over the distinct characters already present in `s`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabaac", "cost": [1, 2, 3, 4, 1, 10]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Accumulate total and per-character costs together

The source scans `s` and `cost` in parallel with `zip`. For each character `c` and deletion cost `v`:

- `tot += v` adds the position to the cost of deleting everything;
- `g[c] += v` adds the position to the cost that can be saved if character `c` is retained.

`g` is a `defaultdict(int)`, so a character's first update starts from zero without a separate existence check.

After the scan,

$$
\texttt{tot}=\sum_{i=0}^{N-1}\texttt{cost}[i],
$$

and `g[c]` is the sum of costs at exactly those positions whose character equals `c`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Convert retained value into deletion cost

If `c` is kept, all positions contributing to `g[c]` remain and every other position is deleted. Its cost is

$$
\texttt{tot}-\texttt{g}[c].
$$

The source evaluates this expression for every character present and returns the minimum:

`min(tot - x for x in g.values())`.

This is equivalent to subtracting the largest per-character saved cost from `tot`. The generator form directly lists each feasible final-character choice.

Because `tot` is the same constant for every candidate, comparing `tot-g[c]` values reverses the comparison between retained totals: a larger saved amount always produces a smaller deletion bill. This is why no other property of the chosen letter—such as its frequency or alphabetic position—enters the optimization.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `11` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabaac", "cost": [1, 2, 3, 4, 1, 10]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `11` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Count character frequency only:** Frequency ignores unequal deletion costs and may retain the wrong letter.
- **Try deleting positions independently with dynamic programming:** Once the final character is chosen, every decision is forced; subset DP is unnecessary.
- **Keep only the most expensive single occurrence:** All same-character occurrences can remain for free and should have their costs saved together.
- **Delete some copies of the retained letter:** Positive costs make this strictly worse while preserving the same final character.
- **All characters already equal:** The single retained total equals `tot`, so the answer is zero.
- **One-character string:** Keeping its character gives zero deletion cost.
- **All characters distinct:** Choosing a final character means keeping one position; the best choice is the position with greatest deletion cost.
- **Most frequent versus most expensive group:** The algorithm correctly maximizes summed retained cost, not count.
- **Equal candidate costs:** Any tied character may remain; only the minimum numeric cost is returned.
- **Large costs:** The running total may exceed 32-bit range.
- **Nonempty requirement:** Iterating only present dictionary keys guarantees at least one survivor.
- **Input preservation:** The string and cost list are only read.
- **Fixed alphabet:** At most 26 dictionary totals justify the manifest's $O(1)$ space.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+26)$. The paired scan visits $N$ positions once, and the final minimum visits at most 26 lowercase character totals. Time is $O(N+26)=O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

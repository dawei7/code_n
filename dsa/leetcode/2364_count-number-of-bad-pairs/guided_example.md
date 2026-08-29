# Guided Example: Count Number of Bad Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 1, 3, 3]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`. A pair of indices `(i, j)` is a **bad pair** if `i < j` and $j - i \neq \text{nums}[j] - \text{nums}[i]$.

The objective is to compute `5` from `{"nums": [4, 1, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count each pair when its right endpoint arrives

For a fixed index `i`, there are exactly `i` earlier indices: `0` through `i - 1`. Therefore, there are `i` pairs whose right endpoint is `i`. If we can quickly determine how many of those pairs are good, the number of newly completed bad pairs is:

$$
i-\text{number of good earlier partners}.
$$

Summing that contribution while scanning left to right counts every pair exactly once. A pair is counted on the iteration of its larger index, never before and never again.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 1, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Transform the good-pair equation into equal keys

The definition says a pair with earlier index $j$ and later index $i$ is good when:

$$
i-j=\texttt{nums}[i]-\texttt{nums}[j].
$$

Rearrange terms belonging to the same index:

$$
i-\texttt{nums}[i]=j-\texttt{nums}[j].
$$

This shows that each index can be assigned the key `index - value`. Two indices form a good pair exactly when their keys are equal. The original comparison of two differences has become a frequency lookup.

The sign could be reversed for every key—`value - index` would group the same indices—but the exact implementation uses `i - x`, where `x` is `nums[i]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Maintain frequencies of earlier keys

`cnt` is a `Counter` mapping each key to the number of previously processed indices with that key. A Counter returns zero for a missing key, which handles the first occurrence without a special branch.

At the start of index `i`'s iteration, `cnt` contains only indices smaller than `i` because the current key is added after its contribution is calculated. Thus:



is exactly the number of earlier indices that form good pairs with `i`.

The line



adds all `i` possible earlier pairs minus those good pairs. It then performs `cnt[i - x] += 1` so this index becomes available as a possible partner for later indices.

The order of lookup and increment matters. Incrementing first would count the current index as its own matching predecessor, even though a valid pair requires two different indices with the earlier one strictly smaller.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 1, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Total pairs minus good pairs:** Count each key frequency and use $\binom{f}{2}$ for good pairs, then subtract from $\binom{n}{2}$. This is correct but requires a second aggregation step or final frequency loop.
- **Brute-force pair enumeration:** Testing every `(i, j)` directly is simple but takes $O(n^2)$ time and is too slow for $10^5$ elements.
- **Use `nums[i] - i` as the key:** Reversing every key's sign preserves equality, so it is equally correct. The exact code uses `i - nums[i]`.
- **One element:** There are no index pairs. The only contribution is zero, and the result is `0`.
- **All keys equal:** Every pair is good; at index `i` the matching frequency equals `i`, so no bad pairs are added.
- **All keys distinct:** No pair is good; the contributions are `0, 1, ..., n - 1` and the answer is all $\binom{n}{2}$ pairs.
- **Large values:** A key may be a large negative integer, but Counter keys support it directly.
- **Update order:** The frequency must be read before the current index is inserted, or the current index would be incorrectly treated as an earlier partner.
- **Duplicate array values:** Equal values at different indices do not automatically make a pair good; equality depends on `i - nums[i]`, which changes with the index.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. The loop visits every element once. Computing the integer key, reading and updating a Counter entry, and updating `ans` take expected $O(1)$ time each. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

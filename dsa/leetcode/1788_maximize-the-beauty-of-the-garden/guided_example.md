# Guided Example: Maximize the Beauty of the Garden

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"flowers": [1, 2, 3, 1, 2]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a garden of `n` flowers, and each flower has an integer beauty value. The flowers are arranged in a line. You are given an integer array `flowers` of size `n` and each $\text{flowers}[i]$ represents the beauty of the $$i^{\text{th}}$$ flower.

The objective is to compute `8` from `{"flowers": [1, 2, 3, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose the two flowers that must remain

Removing flowers preserves the relative order of every flower that remains. Therefore, any valid resulting garden can be described by two original indices $l<r$ that become its first and last positions. Validity requires `flowers[l] == flowers[r]`. Every retained flower between those endpoints is optional.

Once the endpoints are fixed, the best interior choice is immediate:

- keep every interior flower with positive beauty, because it increases the sum;
- remove every interior flower with negative beauty, because it decreases the sum;
- keeping or removing a zero makes no difference.

The two endpoints are different. They are mandatory even when their shared beauty is negative, because without both of them the selected garden would not have two equal boundary flowers.

If their common value is $v$, the best beauty for endpoints $l$ and $r$ is

$$
2v+
\sum_{l<j<r}\max(\texttt{flowers}[j],0).
$$

The problem has now become finding the equal-valued endpoint pair that maximizes this expression.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"flowers": [1, 2, 3, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Prefix sums answer each interior query

The solution builds an array `s` where `s[i]` is the sum of positive contributions among indices strictly before $i$. It starts with zero, and after processing value `v = flowers[i]` it sets

`s[i + 1] = s[i] + max(v, 0)`.

For endpoints $l$ and $i$, the positive sum strictly between them is `s[i] - s[l + 1]`. The first term includes positive values through index $i-1$. The second includes positive values through index $l$, so subtracting it removes everything before or at the left endpoint. The current right endpoint is not yet in `s[i]` and is therefore also excluded, exactly as required.

Adding `v * 2` then supplies the actual endpoint values. This is important when $v$ is negative: prefix sums deliberately ignore negative interior values, but the two required negative endpoints must still count.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution builds an array `s` where `s[i]` is the sum of ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the first occurrence of each value is stored

Dictionary `d` maps a flower value to its first index. When value `v` appears for the first time, the solution stores its index. On every later occurrence at index $i$, that first position becomes the proposed left endpoint and $i$ becomes the right endpoint.

Keeping only the first occurrence is sufficient because every prefix contribution is nonnegative. Suppose the same value occurs at two possible left endpoints $l_1<l_2<i$. Extending the interval from $l_2$ leftward to $l_1$ can only add optional positive flowers or add nothing. It never forces any extra interior negative flower to remain. Both choices still use the same two endpoint values $v$, so

$$
\texttt{s}[i]-\texttt{s}[l_1+1]+2v
\geq
\texttt{s}[i]-\texttt{s}[l_2+1]+2v.
$$

Thus the earliest occurrence is always at least as good as any later occurrence for a fixed right endpoint. There is no need to keep a list of positions or search among earlier copies.

The solution still evaluates every later occurrence as a possible right endpoint. It updates `ans` with the largest candidate seen. `ans` starts at negative infinity because a valid garden can have negative maximum beauty; initializing it to zero would be wrong for inputs such as the third example.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"flowers": [1, 2, 3, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every equal pair:** Enumerating all endpoi:** - **Try every equal pair:** Enumerating all endpoint pairs and summing their interiors can take $O(n^3)$ time without prefix sums or $O(n^2)$ with them, both slower than the one-pass first-occurrence argument.
- **Keep every interior flower:** This fails when an interior beauty is negative, because removal is optional and can improve the total.
- **Kadane's algorithm:** Maximum-subarray logic forces a contiguous retained range, while this problem allows arbitrary interior removals and requires equal endpoints.
- **Store every occurrence:** Lists of positions are unnecessary because the earliest occurrence always dominates later left endpoints for the same value.
- **Running positive prefix scalar:** Store, for each first occurrence, the positive-prefix total immediately after it. This retains the same formula with $O(U)$ rather than $O(n+U)$ space.
- **Negative endpoints:** They must be counted twice even though negative interior values are removed.
- **Adjacent equal values:** The interior sum is zero, so the candidate is exactly twice the shared value.
- **Zero endpoints:** They can form a valid garden; positive interior flowers can still make its beauty positive.
- **All values negative:** The answer may be negative, so zero is not a safe initial maximum.
- **More than two equal flowers:** The first is best as the left endpoint, while every later occurrence is considered as a right endpoint.
- **Repeated negative value inside the interval:** An intermediate copy may be removed; equality is required only for the retained first and last flowers.
- **Guaranteed feasible input:** At least one value repeats, so some candidate replaces negative infinity before the loop ends.
- **Input preservation:** The algorithm records summaries and never changes the `flowers` array.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of flowers and $U$ the number of distinct beauty values. The loop visits every flower once. Prefix updates, dictionary membership, dictionary insertion, and candidate evaluation are expected $O(1)$ operations, so total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n+U)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

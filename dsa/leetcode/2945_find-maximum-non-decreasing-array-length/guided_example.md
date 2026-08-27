# Guided Example: Find Maximum Non-decreasing Array Length

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 2, 2]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`.

The objective is to compute `1` from `{"nums": [5, 2, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: DP and predecessor meaning

`f[i]` is the maximum number of non-decreasing segments covering the first $i$ elements.

`pre[i]` identifies the chosen start $p$ of the final segment in the dominant state for prefix $i$. That final segment has sum

$$
\texttt{s}[i]-\texttt{s}[p].
$$

The update `pre[i] = max(pre[i], pre[i - 1])` propagates predecessor candidates that became feasible at an earlier endpoint. A candidate cut remains feasible for later endpoints because positive prefix sums only increase segment sums.

Among feasible predecessors, a later $p$ dominates an earlier one: `f[p]` is non-decreasing with prefix length, and a later start makes the current final-segment sum smaller, which can only make future extension easier. Hence taking the maximum predecessor index is safe.

The best partition at $i$ appends one segment after that predecessor:

`f[i] = f[pre[i]] + 1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 2, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Schedule when cut $i$ becomes a feasible predecessor

Suppose the last segment in the chosen partition of prefix $i$ starts at $p=\texttt{pre}[i]$. Its sum is `s[i] - s[p]`.

For a future segment from $i$ through $j-1$ to be non-decreasing, it must satisfy

$$
\texttt{s}[j]-\texttt{s}[i]
\ge
\texttt{s}[i]-\texttt{s}[p].
$$

Rearranging:

$$
\texttt{s}[j]\ge2\texttt{s}[i]-\texttt{s}[p].
$$

Since `s` is sorted, `bisect_left` finds the smallest such $j$. The assignment `pre[j] = i` records that, beginning at endpoint $j$, cut $i$ is a feasible predecessor. Propagation at subsequent iterations carries it to every later endpoint.

`pre` has length $n+2$ because `bisect_left` may return $n+1$ when the required next sum exceeds the total prefix-sum range. Recording there is safe and simply never affects `f[1..n]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the last segment in the chosen partition of prefix $... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the final state is optimal

Every update from cut $i$ represents appending a future segment whose sum is at least the previous segment. Thus all constructed partitions are valid.

Conversely, consider an optimal partition ending at some prefix. Its penultimate cut becomes feasible no later than that endpoint according to the same prefix-sum inequality. The propagation mechanism makes it available. Selecting the latest dominant feasible predecessor retains at least as many segments and no larger final segment sum, so it cannot be worse for the current or any future prefix.

Inductively, `f[i]` is the maximum length for every prefix, and `f[n]` is the requested maximum final array length.

For an already non-decreasing positive array, each single-element segment can remain separate; the successive feasibility thresholds allow `f[n]=n`. For `[5,2,2]`, no two-segment partition has non-decreasing sums, and the DP eventually returns one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 2, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Quadratic partition DP:** Try every preceding :** - **Quadratic partition DP:** Try every preceding cut for each endpoint in $O(N^2)$ time.
- **Monotonic deque optimization:** It can maintain feasible predecessor thresholds in linear time, matching the manifest but not this source.
- **Keep the original array:** When it is already non-decreasing, choosing no merge gives the maximum possible length $N$.
- **Merge everything:** Always produces a valid length-one array, so an answer exists.
- **Positive-number requirement:** It makes prefix sums strictly increasing. Zeros or negatives would invalidate the simple binary-search and dominance reasoning.
- **Threshold beyond total sum:** `bisect_left` returns $n+1$, and the oversized `pre` array safely absorbs the unused update.
- **Equal segment sums:** Allowed because the target array is non-decreasing, not strictly increasing.
- **Latest predecessor:** It dominates by preserving at least as many segments while reducing the most recent segment sum.
- **Manifest mismatch:** Complexity and data structure descriptions must follow the exact prefix-DP plus binary-search implementation.
- **Why prefix $f$ is non-decreasing:** Any partition of the first $i-1$ positive elements can extend its last segment with `nums[i-1]`, preserving segment count and non-decreasing order. Thus a later predecessor never offers fewer achievable segments.
- **No array values are actually merged:** Prefix differences represent segment sums mathematically, so the method avoids repeated list replacement and index shifting.
- **One-based prefix endpoints:** Segment after cut $p$ through endpoint $i$ corresponds to original indices $p$ through $i-1$, preventing an off-by-one interpretation of `s[i]-s[p]`.
- **Dominance has two parts:** A later feasible cut has at least as large `f` and a no-larger last-segment sum. Both current objective and future extensibility are therefore no worse.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Prefix sums take $O(N)$ time. Each of $N$ iterations performs one `bisect_left` on a length-$N$ sorted list, costing $O(\log N)$. Total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Rearrange Array Elements by Sign

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 1, -2, -5, 2, -4]}`
- **Required output:** `[3, -2, 1, -5, 2, -4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums` of **even** length consisting of an **equal** number of positive and negative integers.

The objective is to compute `[3, -2, 1, -5, 2, -4]` from `{"nums": [3, 1, -2, -5, 2, -4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prepare the fixed output layout

The exact solution allocates `ans = [0] * len(nums)`. These zeros are placeholders only; zero never appears in the input because every legal value has absolute value at least one.

Two cursors identify the next open slot for each sign:

- `i = 0` is the next even index for a positive;
- `j = 1` is the next odd index for a negative.

Each cursor advances by two after a placement, so it remains on indexes of its assigned parity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 1, -2, -5, 2, -4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the source in original order

The loop `for x in nums` visits elements from left to right. When `x > 0`, the code writes `ans[i] = x` and then performs `i += 2`. Otherwise, the constraints imply `x < 0`, so it writes `ans[j] = x` and advances `j` by two.

Processing in source order is what preserves relative order within each sign. Suppose positive value $p_1$ appears before positive value $p_2$ in `nums`. The loop encounters $p_1$ first and gives it the earlier unused even slot. The cursor then advances, so $p_2$ receives a later even slot. The same reasoning applies independently to negatives and odd slots.

No later placement can overwrite an earlier one because each cursor always moves forward to an unused index.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why alternation is automatic

After all placements, every even slot holds a positive and every odd slot holds a negative. Index zero is even, so the result begins positive. Any consecutive indexes have opposite parity, hence their values have opposite signs. All three requirements follow from the fixed layout.

For `[3,1,-2,-5,2,-4]`, positive encounters fill indexes zero, two, and four with `3,1,2`. Negative encounters fill indexes one, three, and five with `-2,-5,-4`. The result is `[3,-2,1,-5,2,-4]`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, -2, 1, -5, 2, -4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 1, -2, -5, 2, -4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, -2, 1, -5, 2, -4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Separate positive and negative lists:** Filter both signs, then alternate values from the two lists. This is also $O(n)$ time but uses two extra collections in addition to the result.
- **In-place stable rearrangement:** Rotating misplaced elements can preserve order but may degrade to $O(n^2)$ time. More advanced stable partitioning is unnecessarily complex here.
- **Sort by sign:** Sorting can place signs into blocks rather than alternating them and generally destroys relative order.
- **Use one output append cursor:** Maintain queues of signs and append alternately. This works but needs extra sign collections; direct parity cursors fill positions in one source pass.
- **Two-element input:** The single positive goes to index zero and the single negative to index one, regardless of source order.
- **Input already valid:** The method reconstructs the same ordering because each sign subsequence is already stable.
- **Input grouped by sign:** Even if all negatives precede all positives, independent cursors still place each group into the correct alternating slots.
- **No zero values:** The `else` branch safely means negative because the constraints exclude zero.
- **Equal sign counts:** This guarantee prevents an out-of-range cursor and ensures every placeholder is replaced.
- **Stable positives:** Their encounter order is exactly their increasing sequence of even output indexes.
- **Stable negatives:** Their encounter order is exactly their increasing sequence of odd output indexes.
- **Maximum length:** The single pass remains linear for $2\cdot10^5$ values.
- **Placeholder zeros:** They are never observable in the returned legal result because every slot receives one input value.
- **Input preservation:** Returning a new list honors the statement that modification in place is unnecessary and leaves `nums` unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `nums`. Allocating `ans` initializes $n$ positions. The loop reads each input value once and performs one constant-time assignment and cursor update. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Maximize Expression of Three Elements

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 4, 2, 5]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `8` from `{"nums": [1, 4, 2, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose extremes according to each coefficient

The expression is

$$
a+b-c.
$$

The coefficients of `a` and `b` are positive, so those roles should receive the two largest array occurrences. The coefficient of `c` is negative, so `c` should receive the smallest occurrence.

If the sorted values are

$$
x_1\le x_2\le\cdots\le x_n,
$$

the optimal value is

$$
x_n+x_{n-1}-x_1.
$$

Distinct indices are respected: the two maxima are two occurrences, not merely one maximum value reused twice, and the array has at least three positions. Even when extreme values tie, sorted positions remain distinct.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 4, 2, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track the two largest occurrences

`a` is the largest value seen so far and `b` is the second-largest occurrence. Both start at negative infinity.

When a new `x>=a` arrives, it becomes the new largest, while the old `a` shifts into `b`:

`a,b=x,a`.

Using `>=` rather than `>` matters for duplicates. If two equal maximum values occur, the second copy must occupy the other positive role.

If `x<a` but `x>b`, it becomes the second largest. Otherwise it cannot improve either maximum state.

After the scan, `a` and `b` are the greatest two values counting positions.

As a short state trace for `[3,1,3]`, the first three sets `a=3` and leaves `b` at negative infinity. One then becomes `b=1`. The final three satisfies `x>=a`, so it moves the old three into `b` and becomes the new `a`. The two equal maxima are retained as separate occurrences.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track the smallest occurrence independently

`c` begins at positive infinity and is replaced whenever `x<c`. At the end it is the global minimum.

Although the source stores values rather than indices, the extreme formula remains realizable with distinct positions. In sorted positional order, `x_1`, `x_{n-1}`, and `x_n` refer to three positions. If all values are equal, any three distinct indices supply the same three stored values.

If `n=3`, those sorted positions are exactly all array indices. If `n>3`, the minimum position and final two positions are still distinct unless values tie; ties change only values, not the existence of three separate positions. Thus value-only tracking cannot accidentally reuse one physical element.

For `[1,4,2,5]`, the states finish as `a=5`, `b=4`, and `c=1`, returning eight.

For `[-2,0,5,-2,4]`, the two largest occurrences are five and four, and the smallest is negative two. Subtracting a negative adds two, giving eleven.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 4, 2, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate ordered triples:** There are $O(n^3)$ choices. Coefficient signs identify the optimal extremes directly.
- **Sort the array:** Reading the smallest and two largest positions after sorting costs $O(n\log n)$ and may mutate input. One-pass extrema are sufficient.
- **Use the maximum twice:** The roles require distinct indices. `a` and `b` track two occurrences, including duplicates when available.
- **Track only one maximum:** The second positive term needs the second-largest occurrence.
- **Choose the largest `c`:** Because it is subtracted, that would reduce rather than increase the expression.
- **All values negative:** “Largest” means least negative, while subtracting the most negative value provides a large gain.
- **All values equal:** Any three indices give one copy plus one copy minus one copy, equal to the common value.
- **Duplicate maximum:** The `x>=a` branch preserves both occurrences as `a` and `b`.
- **Duplicate minimum:** Any minimum occurrence distinct from the top positions can serve as `c`; values alone are sufficient for the score.
- **Exactly three elements:** All positions must be used, and the formula assigns their roles optimally.
- **Input order:** Roles have no positional ordering requirement, so scan order does not constrain the chosen triple.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the array length. The method makes one pass and performs constant work per element, so time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Minimum Common Value

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2, 3], "nums2": [2, 4]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, return *the **minimum integer common** to both arrays*. If there is no common integer amongst `nums1` and `nums2`, return `-1`.

The objective is to compute `2` from `{"nums1": [1, 2, 3], "nums2": [2, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use one pointer for each sorted array

Pointer `i` identifies the smallest not-yet-discarded value in `nums1`, and `j` does the same for `nums2`.

At each step, compare `nums1[i]` and `nums2[j]`:

- if equal, that value is common and is returned;
- if the first is smaller, increment `i`;
- otherwise, increment `j`.

The sorted order proves that the smaller current value can be discarded permanently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2, 3], "nums2": [2, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a smaller value cannot match later

Suppose `nums1[i]<nums2[j]`. Every element from `nums2[j]` onward is at least `nums2[j]` because `nums2` is nondecreasing. Therefore, none of those unexamined elements can equal the smaller `nums1[i]`.

Any earlier element of `nums2` has already been passed by `j`. If it had matched `nums1[i]` at the relevant comparison, the method would already have returned.

Thus advancing `i` cannot skip a possible future common occurrence. The argument is symmetric when `nums2[j]` is smaller.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the first equality is the minimum common value

Pointers move only from left to right, so all discarded values are no larger than current pointer values. Before the first equality, each discarded value was proven unable to match anything still relevant in the other array.

When equality `v` is found, no smaller common value could remain:

- smaller positions have already been examined or safely discarded;
- future positions contain values at least `v`.

The first match is therefore the minimum common integer, not just any common integer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2, 3], "nums2": [2, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hash set:** Expected $O(m+n)$ time but $O(m)$ or $O(n)$ extra space.
- **Binary search each value:** Search the longer array for each element of the shorter, costing $O(\min(m,n)\log\max(m,n))$.
- **First elements match:** Return immediately.
- **Last elements provide the only match:** Both pointers may scan almost everything.
- **Duplicate runs:** Advancing through smaller duplicates remains safe.
- **No overlap in ranges:** One pointer reaches the end and `-1` is returned.
- **One-element arrays:** The single comparison decides the result.
- **Nondecreasing order:** It is the property that justifies discarding the smaller value.
- **Minimum requirement:** Returning at the first equality is essential.
- **Input preservation:** Neither sorted array is changed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+n)$. Let $m=\lvert\texttt{nums1}\rvert$ and $n=\lvert\texttt{nums2}\rvert$. Every loop iteration advances at least one pointer, and neither pointer moves backward.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

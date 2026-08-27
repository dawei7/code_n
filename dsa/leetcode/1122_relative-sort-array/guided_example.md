# Guided Example: Relative Sort Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr1": [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], "arr2": [2, 1, 4, 3, 9, 6]}`
- **Required output:** `[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two arrays `arr1` and `arr2`, the elements of `arr2` are distinct, and all elements in `arr2` are also in `arr1`.

The objective is to compute `[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]` from `{"arr1": [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], "arr2": [2, 1, 4, 3, 9, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the desired order into a numeric key

Every value appearing in `arr2` must come first, ordered by its position in `arr2`. All other values must follow in ascending numeric order.

The dictionary comprehension `pos = {x: i for i, x in enumerate(arr2)}` maps each listed value to its required priority index. Distinctness of `arr2` makes every mapping unique.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr1": [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], "arr2": [2, 1, 4, 3, 9, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Key listed values by their required position

For a value `x` found in `pos`, the sorting key is `pos[x]`. These keys range from zero through `len(arr2) - 1`.

All copies of one listed value receive the same key and therefore form one block. Blocks themselves appear in the exact order given by `arr2`.

Python’s sort is stable, but stability is not essential among equal numeric copies because they are indistinguishable in the returned integer array.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a value `x` found in `pos`, the sorting key is `pos[x]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Place unlisted values after every listed value

For a value absent from `pos`, the key is `1000 + x`. Input values are between zero and one thousand, so these keys begin at one thousand.

`arr2` has at most one thousand distinct values, so its largest position key is at most 999. Therefore, every unlisted key is strictly greater than every listed key, placing all unlisted elements at the end.

Among two unlisted values $a$ and $b$, their keys are `1000 + a` and `1000 + b`. Adding the same constant preserves order, so smaller numeric values sort first. This supplies the required ascending tail.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr1": [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], "arr2": [2, 1, 4, 3, 9, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Counting sort:** Count every value from zero t:** - **Counting sort:** Count every value from zero through one thousand, emit `arr2` values by priority, then emit remaining values in numeric order. This achieves the manifest’s $O(n+m+V)$ time and $O(V)$ space.
- **Tuple key:** Use listed key `(0, pos[x])` and unlisted key `(1, x)`. It avoids numeric-sentinel assumptions and is easier to generalize.
- **Custom comparator:** It can express the same cases but is more verbose and often slower in Python than key extraction.
- **Repeated listed value:** Every copy receives the same priority and appears in one block.
- **Repeated unlisted value:** Copies remain together in the ascending tail.
- **All values listed:** No tail exists; blocks follow `arr2` exactly.
- **No unlisted duplicates:** Ascending order still follows numeric keys.
- **Value zero unlisted:** Its key is exactly 1000, still above every possible listed position.
- **Position 999 listed:** Its key is 999, still below the smallest unlisted key.
- **Distinct `arr2`:** Required so one value does not receive conflicting priorities.
- **Every `arr2` value occurs in `arr1`:** No requested priority block is empty under the contract.
- **Input preservation:** `sorted` returns a new list rather than mutating `arr1`.
- **Manifest mismatch:** The approach must distinguish the exact comparison sort from the theoretically optimal bounded counting method.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + m + V)$. Let $n$ be the length of `arr1` and $m$ the length of `arr2`. Building `pos` costs $O(m)$ expected time and space. Python comparison sorting costs $O(n\log n)$ time, with constant-time key computation per element.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

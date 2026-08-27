# Guided Example: Maximum Size of a Set After Removals

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums1": [1, 2, 1, 2], "nums2": [1, 1, 1, 1]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** integer arrays `nums1` and `nums2` of even length `n`.

The objective is to compute `2` from `{"nums1": [1, 2, 1, 2], "nums2": [1, 1, 1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only distinct values matter after removal

Each array keeps exactly $n/2$ elements, but the final container is a set. Keeping duplicate copies of a value contributes only one to its size. The goal is therefore to preserve as many distinct values as the two per-array capacities allow.

The code builds `s1 = set(nums1)` and `s2 = set(nums2)`. Their values fall into three disjoint categories:

- exclusive to `nums1`: `s1 - s2`;
- exclusive to `nums2`: `s2 - s1`;
- common to both: `s1 & s2`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums1": [1, 2, 1, 2], "nums2": [1, 1, 1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Prioritize exclusive values

An exclusive-to-first value can be contributed only by the $n/2$ elements retained from `nums1`. Keeping one copy adds a unique final-set value that the second array can never supply. The most such values that can survive is:

`a = min(len(s1 - s2), n // 2)`.

The symmetric count for second-only values is:

`b = min(len(s2 - s1), n // 2)`.

There is no benefit in giving an array slot to a duplicate while an unkept exclusive distinct value is available. Thus an optimal construction can always preserve `a` and `b` exclusives first.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An exclusive-to-first value can be contributed only by the $... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use common values to fill remaining distinct capacity

There are `len(s1 & s2)` possible common values. Each needs to be retained in only one array to appear in the union. Since it exists on both sides, its copy can be assigned to whichever retained half has room.

Ignoring the total element count momentarily, the available distinct categories suggest:

`a + b + len(s1 & s2)`.

However, the two remaining arrays contain only $n/2+n/2=n$ elements total. A set formed from $n$ retained elements can never have more than $n$ distinct values. The final expression is therefore:

`min(a + b + len(s1 & s2), n)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums1": [1, 2, 1, 2], "nums2": [1, 1, 1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Greedy over raw occurrences:** Duplicate copie:** - **Greedy over raw occurrences:** Duplicate copies obscure the real objective; classify distinct values first.
- **Take half the distinct count from each set:** This can double-count common values and miss the value of exclusives.
- **Prioritize common values:** Exclusives are less flexible because only one array can provide them; preserving them first is never worse.
- **Disjoint sets:** Every retained distinct value is exclusive, and the answer can reach $n$ when each side has at least $n/2$ distinct values.
- **Identical sets:** There are no exclusives; the answer is limited by the shared distinct count and $n$.
- **All values identical:** The final set size is one despite retaining $n$ elements.
- **More exclusives than capacity:** `min` caps that array’s contribution at $n/2$.
- **Duplicate padding:** Exact retention counts remain achievable even after all useful distinct choices are made.
- **Expected hashing:** Python set operations have expected linear behavior under the standard hash-table model.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the common array length. Creating both sets takes expected $O(N)$ time. Difference and intersection operations are linear in the set sizes, also expected $O(N)$ total at this scale. The remaining arithmetic is constant, giving expected $O(N)$ time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

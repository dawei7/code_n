# Guided Example: Contains Duplicate

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 1]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return `true` if any value appears **at least twice** in the array, and return `false` if every element is distinct.

The objective is to compute `true` from `{"nums": [1, 2, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sorting turns a global duplicate question into adjacent comparisons

In the original unsorted array, two equal values can be arbitrarily far apart.
Checking every pair would eventually find a duplicate, but an array of length
$n$ has $n(n-1)/2$ index pairs, which is quadratic work.

The exact solution first evaluates `sorted(nums)`. Sorting groups values in
non-decreasing order. If a value occurs at least twice, all copies of that value
form one consecutive block in the sorted list. Therefore some adjacent pair in
that block must be equal. Conversely, equal adjacent entries clearly came from
two different array positions with the same value and prove that a duplicate
exists.

This equivalence means the method no longer needs to compare arbitrary pairs.
It needs only one comparison between each neighboring pair after sorting.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `pairwise` produces

For a sequence `[x0, x1, x2, x3]`, `pairwise` yields
`(x0, x1)`, `(x1, x2)`, and `(x2, x3)`. There are $n-1$ such pairs for a
length-$n$ sequence. Each interior element participates once as a right member
and once as a left member, ensuring that every adjacency boundary is examined.

The generator expression `a == b for a, b in pairwise(sorted(nums))` converts
each adjacent pair into a boolean. It produces `true` exactly at a boundary
where the two sorted values are equal.

`pairwise` and the generator are lazy: they provide the next pair or boolean
only when requested. They do not allocate a second list containing all pairs
or all comparison results.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a sequence `[x0, x1, x2, x3]`, `pairwise` yields
`(x0, x... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `any` is exactly the requested logical operation

The problem asks whether at least one repeated value exists. Python's `any`
returns `true` if at least one generated condition is truthy and returns
`false` if every generated condition is false. It also short-circuits: as soon
as it receives the first `true`, it stops requesting more adjacent pairs.

For `nums = [1, 2, 3, 1]`, sorting creates `[1, 1, 2, 3]`. The first pair is
`(1, 1)`, its comparison is true, and `any` immediately returns `true`. For
`nums = [1, 2, 3, 4]`, every adjacent comparison is false, the generator is
exhausted, and `any` returns `false`.

The early exit applies only to the adjacency scan. `sorted(nums)` must finish
constructing and sorting the entire list before `pairwise` can yield its first
pair. Thus a duplicate discovered at the first sorted boundary does not avoid
the sorting cost.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Hash set of seen values:** Scan the original l:** - **Hash set of seen values:** Scan the original list and return immediately when a value is already in the set. This matches the manifest, gives expected $O(n)$ time and $O(n)$ space, and may stop before reading the whole array; hash operations have expected rather than unconditional constant time.
- **In-place sorting:** Calling `nums.sort()` avoids the separate top-level copy and then uses the same adjacent check. It changes the caller's order and Python sorting still has implementation-dependent temporary memory.
- **Nested pair comparison:** Compare each position with every earlier position. It uses $O(1)$ extra space and can stop early, but worst-case time is $O(n^2)$ and is unsuitable for $n$ up to $10^5$.
- **Counting array:** Direct frequencies are excellent for a small numeric domain, but values here span from $-10^9$ to $10^9$; allocating that range would be wasteful compared with sorting or hashing.
- **One element:** `pairwise` yields no pairs, and `any` over an empty generator returns `false`, which is correct because no value appears twice.
- **Two equal elements:** Sorting leaves them adjacent, the sole comparison is true, and the method returns `true`.
- **Two different elements:** The sole adjacent comparison is false, so the method returns `false`.
- **Many copies of one value:** The first two copies are adjacent after sorting. `any` stops at the first equal pair; it does not need to count all occurrences.
- **Negative and zero values:** Ordinary integer ordering places them correctly, and equality semantics are unchanged. No numeric offset is needed.
- **Already sorted or reverse-sorted input:** The logic is identical. Sorting still creates a separate list, and the later scan checks adjacent values in non-decreasing order.
- **Input preservation:** Because the code uses `sorted(nums)` rather than `nums.sort()`, callers observe the original list in its original order after the method returns.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. Let $n$ be `len(nums)`. Creating and sorting the copy takes $O(n\log n)$ time
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

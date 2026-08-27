# Guided Example: First Unique Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"], "arguments": [[[2, 3, 5]], [], [5], [], [2], [], [3], []]}`
- **Required output:** `[null, 2, null, 2, null, 3, null, -1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You have a queue of integers, you need to retrieve the first unique integer in the queue.

The objective is to compute `[null, 2, null, 2, null, 3, null, -1]` from `{"operations": ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"], "arguments": [[[2, 3, 5]], [], [5], [], [2], [], [3], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maintain frequency and ordered uniqueness as separate facts

The data structure must answer two questions:

1. Is a value currently unique?
2. Among unique values, which one entered the queue earliest?

A frequency map answers the first. An insertion-ordered mapping containing only currently unique values answers the second.

The implementation stores:

- `cnt`, a Counter of every value's total occurrences.
- `unique`, an OrderedDict whose keys are exactly values with frequency one, in their original insertion order.

The OrderedDict values are all the dummy value 1. Only key presence and key order matter, so it is being used as an ordered set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"], "arguments": [[[2, 3, 5]], [], [5], [], [2], [], [3], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build constructor state in two passes

first counts the complete initial queue. This makes it possible to know immediately which values occur exactly once.

Then:



iterates the original sequence from left to right and includes only frequency-one values. Python dictionaries preserve insertion order, and OrderedDict explicitly maintains it. Thus the first key is the earliest unique number in the initial queue.

A value with frequency greater than one is never inserted, even at its first occurrence, because the Counter already knows the completed initial frequency. A truly unique value appears only once in `nums`, so it creates exactly one key.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | first counts the complete initial queue.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Return the first key without removing it

`showFirstUnique` is:



An empty OrderedDict means no currently unique value exists, so -1 is returned.

Otherwise, iteration over `unique.keys()` follows insertion order, and `next` returns its first key. The method does not pop that key. Showing a value does not remove it from the conceptual queue and does not change its frequency, so later calls may return the same number.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 2, null, 2, null, 3, null, -1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["FirstUnique", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique", "add", "showFirstUnique"], "arguments": [[[2, 3, 5]], [], [5], [], [2], [], [3], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 2, null, 2, null, 3, null, -1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Queue plus status map:** Enqueue first occurre:** - **Queue plus status map:** Enqueue first occurrences and lazily remove stale duplicates from the front during show. Operations are $O(1)$ amortized but one show call may perform several removals.
- **Scan the complete queue on every show:** Count or check each value repeatedly. This can be linear or quadratic per query and wastes prior frequency work.
- **Plain unordered set:** It tracks uniqueness but cannot identify which unique value appeared first.
- **Linked hash set:** In languages that provide one, it directly supports ordered keys with constant-time insertion and removal, analogous to OrderedDict.
- **All initial values duplicated:** `unique` starts empty and show returns -1.
- **One initial value:** It is returned until the same value is added again.
- **Third and later occurrence:** The key is already absent, so only Counter changes.
- **A new value after no uniques remain:** Its count becomes one, it enters the ordered mapping, and it becomes the first unique.
- **Show does not consume:** Repeated show calls without additions return the same first value.
- **Arrival order:** Removing an earlier key does not disturb the relative order of remaining keys.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+q)$. Let $n$ be the initial list length and $q$ the number of later operations. Construction counts and scans the initial values in $O(n)$ expected time. Each `add` performs a constant number of expected $O(1)$ hash and OrderedDict operations. `showFirstUnique` checks emptiness and obtains the first iterator item in $O(1)$ time.
- **Auxiliary Space Complexity:** $O(n+q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: Finding the Users Active Minutes

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"logs": [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], "k": 5}`
- **Required output:** `[0, 2, 0, 0, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given the logs for users' actions on LeetCode, and an integer `k`. The logs are represented by a 2D integer array `logs` where each $\text{logs}[i] = [\text{ID}_{i}, \text{time}_{i}]$ indicates that the user with $\text{ID}_{i}$ performed an action at the minute $\text{time}_{i}$.

The objective is to compute `[0, 2, 0, 0, 0]` from `{"logs": [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], "k": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Deduplicate minutes separately for every user

The same user may perform several actions during one minute, but that minute contributes only once to the user's active-minute count. Different users acting at the same minute must remain separate.

The appropriate representation is therefore a mapping:

`user ID -> set of action minutes`.

The protected solution creates `d = defaultdict(set)`. For every log `[i, t]`, it executes `d[i].add(t)`.

If the user has not appeared before, the default factory creates an empty set. If the exact minute is already present, adding it again changes nothing. This enforces uniqueness locally per user.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"logs": [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], "k": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Convert each user's set size into one histogram bucket

After processing all logs, `len(ts)` is that user's UAM.

The requested answer is described with one-based UAM values but returned as a normal zero-based Python list. Therefore:

- UAM 1 belongs at index 0;
- UAM 2 belongs at index 1;
- in general, UAM $j$ belongs at index $j-1$.

The solution creates `ans = [0] * k` and, for each user's set `ts`, increments

`ans[len(ts) - 1]`.

The constraint guarantees `k` is at least the maximum UAM, so this index is always within the list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following the first example

Logs for user 0 contain minutes 5, 2, and 5. Their set becomes `{2,5}`, so UAM is two.

User 1 has minutes 2 and 3, also giving UAM two.

Both users increment index one. The result `[0,2,0,0,0]` means zero users have UAM one, two users have UAM two, and none have larger UAM values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[0, 2, 0, 0, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"logs": [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], "k": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[0, 2, 0, 0, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort logs by user and minute:** Deduplicate adjacent pairs and count runs in $O(n\log n)$ time without nested sets.
- **Global set of pairs:** `(user, minute)` pairs deduplicate correctly, but another grouping pass is still needed.
- **Count every log:** It overcounts users who perform several actions in one minute.
- **Global minute set:** It incorrectly merges different users' activity.
- **Duplicate identical log:** Set insertion leaves UAM unchanged.
- **Same user, different minutes:** Every distinct minute increases that user's set size.
- **Different users, same minute:** Each user's separate set counts the minute independently.
- **One log:** One user has UAM one and increments the first entry.
- **All logs for one user and minute:** The first answer bucket is one regardless of duplicate count.
- **Maximum UAM equals `k`:** Index `k - 1` is valid and receives the user.
- **Large sparse user IDs:** A dictionary avoids allocating an array up to the largest ID.
- **No zero-UAM bucket:** Only users present in logs are considered.
- **Output indexing:** Human UAM value $j$ maps to Python index $j-1$.
- **Input preservation:** Sets summarize logs without modifying the input rows.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(U)$. Let $n$ be the number of logs and $U$ the number of users. Each expected hash-map lookup and set insertion is $O(1)$, so building `d` takes expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n + k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

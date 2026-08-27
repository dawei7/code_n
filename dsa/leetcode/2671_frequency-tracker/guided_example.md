# Guided Example: Frequency Tracker

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["FrequencyTracker", "add", "add", "hasFrequency"], "arguments": [[], [3], [3], [2]]}`
- **Required output:** `[null, null, null, true]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a data structure that keeps track of the values in it and answers some queries regarding their frequencies.

The objective is to compute `[null, null, null, true]` from `{"operations": ["FrequencyTracker", "add", "add", "hasFrequency"], "arguments": [[], [3], [3], [2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store both directions of the question

The data structure must support two different kinds of information:

- `add(number)` and `deleteOne(number)` need the current occurrence count of one particular number.
- `hasFrequency(frequency)` needs to know whether any number has one particular occurrence count.

A map from numbers to counts answers the first question directly, but it does not answer the second one quickly. If only that map existed, every `hasFrequency` call would have to scan all numbers and compare their counts with the requested frequency.

The solution therefore keeps two maps:

- `cnt[number]` is how many copies of `number` are currently present.
- `freq[f]` is how many distinct numbers currently occur exactly `f` times, for positive `f`.

The second map is a set of frequency buckets. It turns the existential question “does at least one number occur this many times?” into the constant-time test `freq[frequency] > 0`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["FrequencyTracker", "add", "add", "hasFrequency"], "arguments": [[], [3], [3], [2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Think of every update as moving one number between buckets

Suppose `number` currently occurs `old` times. Adding one copy changes its count to `old + 1`. The number must leave its old frequency bucket and enter its new one:

1. decrement `freq[old]`;
2. increment `cnt[number]`;
3. increment `freq[old + 1]`.

The code expresses the new bucket as `freq[cnt[number]]` after incrementing `cnt[number]`. Only this one number changes frequency, so no other bucket needs adjustment.

Deleting one copy is the reverse movement. If the old count is positive:

1. decrement the bucket for the old count;
2. decrement the number's count;
3. increment the bucket for the new count.

This transition bookkeeping is the central idea. Updating both views at the same moment prevents them from disagreeing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose `number` currently occurs `old` times.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why deletion first checks the count

`deleteOne(number)` must do nothing when the structure contains no copy of `number`. The condition `if cnt[number]` tests whether its count is nonzero.

Without this guard, a missing number would move from frequency zero to frequency negative one. Negative occurrence counts have no meaning and would corrupt all later operations on that number.

Because `cnt` is a `defaultdict(int)`, reading a previously unseen key yields zero. The read can create an entry with value zero, but that bookkeeping detail has no observable effect: the number still has no positive count, no positive frequency bucket changes, and every permitted query remains correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, null, true]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["FrequencyTracker", "add", "add", "hasFrequency"], "arguments": [[], [3], [3], [2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, null, true]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Scan the number-count map for every query:** T:** - **Scan the number-count map for every query:** This uses only `cnt` but makes `hasFrequency` take $O(d)$ time.
- **Maintain sets of numbers per frequency:** Moving values between sets also supports expected $O(1)$ operations, but stores more information than the query needs.
- **Use a fixed count array:** This works only when the numeric value domain is small and known; hash maps handle the full allowed range naturally.
- **Add a new number:** It enters positive frequency bucket one even though the unused zero bucket is not a meaningful census.
- **Delete the last copy:** The value leaves bucket one and becomes absent; positive bucket accounting remains correct.
- **Delete a missing number:** The guard makes the operation a no-op.
- **Several numbers in one bucket:** `freq[f]` counts all of them, so removing one does not make the query false while another remains.
- **Move the only number out of a bucket:** The bucket count becomes zero and `hasFrequency` correctly becomes false.
- **Query frequency zero:** The problem restricts queries to positive frequencies; the exact implementation does not maintain a semantic zero-frequency bucket.
- **Repeated add and delete cycles:** Each transition reverses the corresponding prior transition, keeping both maps synchronized.
- **Hash-map complexity:** Constant time is expected rather than deterministic worst-case because it relies on ordinary hash-table behavior.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Let $d$ be the number of distinct values that have been referenced and let $m$ be the number of operations.
- **Auxiliary Space Complexity:** $O(m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

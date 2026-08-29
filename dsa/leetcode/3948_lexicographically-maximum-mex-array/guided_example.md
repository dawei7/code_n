# Guided Example: Lexicographically Maximum MEX Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 0]}`
- **Required output:** `[2, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `[2, 1]` from `{"nums": [0, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The largest possible next value is the MEX of the whole suffix

Let $m$ be the MEX of all currently remaining elements. By definition:

- every value $0,1,\ldots,m-1$ occurs somewhere in the suffix;
- value $m$ does not occur anywhere in the suffix.

No prefix can have MEX greater than $m$, because every prefix also lacks $m$. A prefix has MEX exactly $m$ once it contains at least one copy of every value below $m$.

Therefore $m$ is the greatest achievable next result entry. Since lexicographic maximization prioritizes this entry over the complete future, any optimal strategy must choose a prefix whose MEX is $m$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the shortest qualifying prefix is optimal

Among prefixes with MEX $m$, the source stops at the first one containing every required value $0$ through $m-1$.

Taking a longer prefix cannot improve the already fixed first result value because $m$ is absent from the entire suffix. It only discards extra elements that could help future segments.

Keeping those elements cannot lower the maximum MEX available to the next step: adding elements to a sequence's set of available values can only leave its MEX unchanged or increase it. If the next values tie, preserving a longer suffix similarly leaves at least as much freedom for later choices. This exchange can be repeated, so the earliest qualifying endpoint gives the lexicographically best tail among choices with the optimal first value.

The algorithm can therefore make this greedy choice independently at every suffix.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Track the current suffix with `remaining`

The MEX of an array of length $n$ is at most $n$. The source allocates counts for values zero through $n$ and ignores larger values, because no larger value can affect which integer in that range is first missing.

`remaining[v]` is the number of unconsumed occurrences of $v$. It is initialized from the full input and decremented whenever an element is removed.

The source finds the current suffix MEX by starting at zero and advancing while `remaining[mex] > 0`. This checks precisely which consecutive nonnegative values remain present.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every prefix recursively:** This explores exponentially many partitions. Lexicographic priority determines the next MEX greedily.
- **Choose the whole remaining suffix every time:** It obtains the maximum next MEX but may discard elements that could form valuable later entries. The shortest qualifying prefix gives an equal first value and a better available tail.
- **Stop after seeing each required value without deduplication:** Repeated copies of one value cannot substitute for another required value. The `seen` set makes `unseen` count distinct requirements.
- **Track values greater than `n`:** They cannot affect a MEX bounded by the array length and need no frequency slot.
- **Current MEX zero:** Zero is absent everywhere in the suffix, so consuming one element maximizes the number of tied zero outputs.
- **All values are positive:** The full-array MEX is zero and the answer contains one zero per input element.
- **Input contains every value from zero through `n - 1`:** The first MEX is $n$, the shortest qualifying prefix is the entire array, and the result has one entry.
- **Duplicate required values:** The segment ignores repeats for `unseen` but decrements every occurrence from `remaining`.
- **Last copy of a small value is consumed:** Recomputing from zero makes that value the next suffix MEX.
- **Values equal to `n`:** They are tracked because a length-$n$ array can have MEX $n$.
- **Values larger than `n`:** They are consumed normally but omitted from the count array.
- **Input is not mutated:** The source advances an index and maintains counts rather than deleting prefixes from `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the input length. Initial frequency construction is $O(n)$. Every array element is consumed exactly once by either the zero branch or a segment-building loop.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

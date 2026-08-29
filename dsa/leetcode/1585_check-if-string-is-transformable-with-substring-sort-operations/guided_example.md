# Guided Example: Check If String Is Transformable With Substring Sort Operations

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "84532", "t": "34852"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `t`, transform string `s` into string `t` using the following operation any number of times:

The objective is to compute `true` from `{"s": "84532", "t": "34852"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What an ascending substring sort can and cannot move

Sorting a substring into ascending order can move a smaller digit left across larger digits. For instance, sorting `"53"` changes it to `"35"`, so digit three crosses digit five. In contrast, a larger digit cannot move left across a smaller digit by ascending sorts: if the smaller digit and larger digit occur in the same sorted substring, ascending order keeps the smaller one first.

This creates the central blocking rule. To take an occurrence of digit `x` from the source and make it the next output character, no still-unused digit smaller than `x` may occur before that source occurrence. Such a smaller digit cannot be crossed by `x` and must appear earlier in every reachable output.

Larger preceding digits do not block `x`. The digit `x` can move left across them by sorting suitable substrings, equivalently by a sequence of adjacent swaps of inverted pairs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "84532", "t": "34852"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remembering every occurrence position

The solution builds `pos`, a dictionary from each digit to a deque of its indices in `s`. While scanning `s` from left to right, it converts character `c` to integer `int(c)` and appends index `i`.

Therefore, each deque is in increasing source-index order. Its front is the earliest occurrence of that digit that has not yet been assigned to the target prefix.

Keeping occurrence positions rather than only digit frequencies is necessary. Equal digit counts can show that `s` and `t` are anagrams, but counts alone cannot reveal the blocking order. For example, target order may request a larger digit before a smaller source digit that it is unable to cross.

Using deques makes removing an accepted earliest occurrence efficient: `popleft()` takes constant time, while deleting index zero from a Python list would shift all later positions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Matching the target from left to right

The second loop considers each target character `c` in order and converts it to digit `x`. The next target position must use some unused occurrence of `x` from `s`.

The first failure condition is `not pos[x]`. If the deque is empty, every source occurrence of `x` has already been used, or `s` never contained enough copies. The target therefore cannot be formed.

When occurrences exist, the only sensible candidate is `pos[x][0]`, the earliest unused `x`. Choosing a later equal occurrence cannot help: the earlier equal digit would remain before it, and sorting cannot reverse two equal values into a distinguishable advantage. The earliest occurrence also minimizes the number of possible blockers before the chosen digit.

The second failure test examines all digits `i` in `range(x)`, meaning zero through `x - 1`:

`pos[i] and pos[i][0] < pos[x][0]`.

For each smaller digit, only its earliest unused occurrence matters. If that earliest occurrence is not before the chosen `x`, no later occurrence of the same smaller digit can be before it either. If any smaller deque has a front index below the candidate `x` index, that smaller digit is an unavoidable blocker and the method returns `false`.

If no smaller digit blocks `x`, the target character is feasible. `pos[x].popleft()` consumes that source occurrence, conceptually fixing it at the next target position. The loop then repeats for the following target character.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "84532", "t": "34852"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Simulate arbitrary substring sorts:** Searching operation sequences has an enormous state space and hides the simple invariant about which digits can cross. Position queues decide reachability without constructing the operations.
- **Compare only digit frequencies:** Matching frequencies is necessary but not sufficient. Relative blocking by smaller digits can make two anagram strings non-transformable.
- **Repeatedly find characters with `str.index`:** Searching the source for every target position can become quadratic and still needs careful tracking of consumed occurrences. Deques provide ordered unused indices directly.
- **Balanced trees of positions:** Ordered sets can retrieve and delete earliest occurrences in $O(\log N)$ time, but per-digit deques are enough because occurrences are always consumed from left to right.
- **Missing target digit:** An empty deque immediately proves that `t` requests more copies of a digit than `s` supplies.
- **Duplicate digits:** The earliest unused occurrence is always selected. This preserves equal-digit order and cannot be worse than choosing a later copy.
- **Digit zero:** `range(0)` is empty, so zero can always cross larger preceding digits when an unused zero exists. No smaller digit can block it.
- **Digit nine:** Every digit zero through eight is checked, because any of them before the selected nine would be an unavoidable blocker.
- **Already equal strings:** Each target character consumes the matching earliest source occurrence, and no smaller unused digit lies before it. The method returns true.
- **Single-character strings:** The sole target digit succeeds exactly when the source contains that digit, which equal length reduces to ordinary equality.
- **Larger preceding digits:** They are intentionally allowed because adjacent ascending sorts can swap `yx` to `xy` whenever `y > x`.
- **Smaller preceding digits:** They are intentionally rejected because ascending sorting preserves their order before `x`.
- **Equal-length guarantee:** The source and target have the same number of positions. If lengths were not guaranteed equal, the method should reject unequal lengths before building queues.
- **Only decimal digits:** Converting with `int(c)` and checking `range(x)` relies on the alphabet being digits zero through nine with their natural numeric order.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the common length of `s` and `t`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

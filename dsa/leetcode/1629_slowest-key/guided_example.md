# Guided Example: Slowest Key

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"releaseTimes": [9, 29, 49, 50], "keysPressed": "cbcd"}`
- **Required output:** `"c"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A newly designed keypad was tested, where a tester pressed a sequence of `n` keys, one at a time.

The objective is to compute `"c"` from `{"releaseTimes": [9, 29, 49, 50], "keysPressed": "cbcd"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compute durations from cumulative release times

`releaseTimes[i]` is an absolute time, not the duration of press `i`. The first key starts at time 0, so its duration is simply `releaseTimes[0]`. Every later key starts exactly when the preceding key is released, which makes its duration

$$
\textit{releaseTimes}[i]-\textit{releaseTimes}[i-1].
$$

Because release times are strictly increasing, every duration is positive.

The source initializes `ans` to the first character and `mx` to the first release time. This treats the first press as the best press seen so far before the loop begins. The loop can then start at index 1 and use the same “compare current press with best press” logic for every remaining event.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"releaseTimes": [9, 29, 49, 50], "keysPressed": "cbcd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain both parts of the ranking rule

A press is preferable when it has a longer duration. If durations tie, its key is preferable when that key is lexicographically larger. The source encodes these priorities in one condition:

`d > mx or (d == mx and ord(keysPressed[i]) > ord(ans))`.

The first part handles the primary criterion. A strictly longer press always replaces the current answer, regardless of its letter.

The parenthesized second part is considered only when durations are equal. `ord` converts each lowercase letter to its character code. Lowercase English letters have increasing codes from `a` through `z`, so comparing those codes is equivalent to comparing the one-character strings lexicographically.

When either part is true, both `mx` and `ans` are updated together. Keeping them synchronized is essential: `mx` must always describe the particular best ranking represented by `ans`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | A press is preferable when it has a longer duration.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why repeated keys need no special storage

The same key can appear several times with different durations, but the problem asks for the key belonging to the best individual keypress. It does not ask for the total time per key or even each key's maximum stored separately.

The scan compares every press as it occurs. If a later press of the same key is longer, it can replace the current best; if shorter, it is ignored. If the same letter ties itself, the lexicographic comparison is false, but retaining either occurrence yields the same returned key. A map from keys to durations would therefore store information that is not needed for the final decision.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"c"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"releaseTimes": [9, 29, 49, 50], "keysPressed": "cbcd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"c"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build a duration array first:** Calculate all :** - **Build a duration array first:** Calculate all durations, then find the maximum with the tie rule. This remains $O(n)$ time but uses $O(n)$ extra space and separates two steps that can be combined.
- **Map each key to its longest press:** After one pass, scan the at most 26 keys for the best duration. It is correct but unnecessary because the answer concerns the best individual press and can be maintained directly.
- **Fixed 26-entry duration array:** This gives $O(1)$ bounded storage and can scan letters from `z` downward for ties. The direct scalar solution is still simpler.
- **Use tuple comparison:** Tracking `max((duration, key), ...)` captures the same priority because Python compares tuple components in order. The explicit condition makes the primary duration and secondary letter criteria easier to see.
- **First keypress:** Its start time is zero, so its duration is `releaseTimes[0]`. Subtracting `releaseTimes[-1]` would be incorrect Python wraparound.
- **Equal longest durations:** Choose the lexicographically larger key. The condition must use both equality of durations and a larger character.
- **A lexicographically larger but faster-released key:** It cannot win unless its duration ties the maximum. Letter order never overrides a shorter duration.
- **Repeated presses of one key:** They are separate events. The longest individual occurrence participates normally, and returning the character does not require returning which occurrence won.
- **Strictly increasing release times:** Durations are positive, so the first initialized press is always a valid baseline.
- **Two presses only:** Initialization handles the first and the single loop iteration compares the second, covering both possible winners and a tie.
- **Using release time as duration:** Only index 0 has duration equal to its release time. Later absolute release times must have the previous release subtracted.
- **Character comparison:** `ord` is safe because inputs are lowercase English letters. Direct `keysPressed[i] > ans` would be equivalent for these one-character strings.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of keypresses. Initialization is constant time, and the loop processes indices 1 through $n-1$ once. Each iteration performs one subtraction and a constant number of comparisons and assignments. The total time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

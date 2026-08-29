# Guided Example: Single-Row Keyboard

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"keyboard": "abcdefghijklmnopqrstuvwxyz", "word": "cba"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a special keyboard with **all keys in a single row**.

The objective is to compute `4` from `{"keyboard": "abcdefghijklmnopqrstuvwxyz", "word": "cba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Convert letters into positions once

The keyboard string is a permutation of all 26 lowercase English letters. Its index is the physical position of each key. To type quickly, the algorithm needs to answer “where is this character?” for every character of `word`.

Searching `keyboard` from the beginning for each typed character would repeatedly scan up to 26 positions. Although 26 is fixed, a direct position table is clearer and avoids repeated lookup work.

The dictionary comprehension

`{c: i for i, c in enumerate(keyboard)}`

creates a mapping from each letter `c` to its index `i`. Because every lowercase letter appears exactly once, every key has one unambiguous position and no dictionary entry is overwritten by a duplicate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"keyboard": "abcdefghijklmnopqrstuvwxyz", "word": "cba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track the finger's current position

The assignment `ans = i = 0` initializes both the accumulated time and the current finger position to zero. The starting position is an index, not necessarily the key `a`; whichever character appears at `keyboard[0]` is under the finger initially.

For each target character `c`, `pos[c]` is the destination key index. The movement time is the absolute distance

`abs(pos[c] - i)`.

This value is added to `ans`. Then `i = pos[c]` updates the current position because the finger remains on the key just typed and starts the next movement there.

No separate time is charged for pressing a key. The contract defines cost only as movement distance.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why absolute difference is exact

All keys lie in one row at integer positions zero through 25. Moving from index `i` to index `j` requires crossing exactly `|i - j|` adjacent position gaps.

There is only one dimension and no shorter route around the row, so the absolute difference is both a lower bound and an achievable movement cost. The solution applies precisely the metric provided by the problem.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"keyboard": "abcdefghijklmnopqrstuvwxyz", "word": "cba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Call `keyboard.index(c)` for every character:** This is correct and each scan is bounded by 26, so it is still `O(m)` under the fixed alphabet. The position map avoids repeated scans and makes the data flow explicit.
- **Use a 26-element integer array:** Store positions at `ord(c) - ord("a")`. This has the same bounds and may have lower lookup overhead than a dictionary.
- **Simulate one adjacent step at a time:** It reproduces the distance but performs unnecessary per-position updates. Absolute difference computes the same cost directly.
- **Finger begins at index zero:** It does not begin at the position of `a` unless `a` happens to be the first keyboard character.
- **First word character is already at index zero:** Its first movement contributes zero.
- **Repeated consecutive characters:** Every repeat after the first costs zero movement.
- **Word of length one:** The result is simply the distance from position zero to that key.
- **Arbitrary keyboard permutation:** The dictionary captures the supplied layout; no alphabetical-order assumption is made.
- **Every word key exists:** The permutation and lowercase-word guarantees make dictionary lookup safe.
- **Maximum word length:** The algorithm retains constant state and performs one arithmetic update per character.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m)$. Let `m = len(word)`. Enumerating the keyboard always processes exactly 26 characters, which is `O(1)` under the fixed lowercase alphabet. The typing loop processes each of the `m` word characters once with expected constant-time dictionary lookup and arithmetic. Total time is `O(m)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

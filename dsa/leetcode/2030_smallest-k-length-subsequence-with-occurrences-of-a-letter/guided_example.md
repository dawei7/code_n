# Guided Example: Smallest K-Length Subsequence With Occurrences of a Letter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leet", "k": 3, "letter": "e", "repetition": 1}`
- **Required output:** `"eet"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s`, an integer `k`, a letter `letter`, and an integer `repetition`.

The objective is to compute `"eet"` from `{"s": "leet", "k": 3, "letter": "e", "repetition": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Combine lexicographic greediness with two feasibility constraints

A lexicographically small subsequence wants the earliest possible character at each output position. A monotonic stack supports that goal: when a smaller current character arrives, larger characters at the end of the tentative answer may be removed.

This problem adds two restrictions. The final stack must have exactly `k` characters, and at least `repetition` of them must equal `letter`. Every removal and every skipped character must preserve both possibilities.

The source tracks:

- `stack`: the currently selected subsequence, in original index order;
- `selected_letter`: how many selected characters equal `letter`;
- `remaining_letter`: how many copies of `letter` remain at or after the current scan position.

Initially, `remaining_letter = s.count(letter)`. It is decremented only after the current character has been processed, so during the decisions for one iteration it still includes the current character.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leet", "k": 3, "letter": "e", "repetition": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When a larger stack top may be removed

The `while` loop considers replacing the last selected character with the smaller current `character`. The comparison `character < stack[-1]` is what makes the replacement lexicographically beneficial: the first changed output position becomes smaller.

But a beneficial pop is allowed only when enough source characters remain to refill the output. After popping, there would be `len(stack) - 1` selected characters. The number of characters from the current index through the end is `len(s) - index`. The condition

`len(stack) - 1 + len(s) - index >= k`

guarantees that these together can still produce length `k`. Without it, a late small character could cause the final subsequence to be too short.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Protect the required copies of `letter`

If the stack top is not `letter`, popping it does not reduce `selected_letter` and is harmless to the repetition requirement.

If the top is `letter`, the source requires

`selected_letter - 1 + remaining_letter >= repetition`.

The first term is how many required letters would remain selected after the pop. The second term counts every copy still available from the current position onward. Their sum is the greatest number of `letter` copies the final answer could still contain. A pop is safe only when that maximum remains at least `repetition`.

This check is intentionally made before decrementing `remaining_letter` for the current character. If the current character itself equals `letter`, it is a legitimate replacement for the popped copy and must be counted as available.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"eet"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leet", "k": 3, "letter": "e", "repetition": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"eet"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate subsequences:** There can be exponentially many, so direct comparison is infeasible.
- **Dynamic programming over positions and quota:** It can model feasibility but uses much more time and memory than the monotonic greedy method.
- **Ordinary smallest-subsequence stack:** Ignoring the `letter` quota may pop or skip too many required copies.
- **Exactly `k` source characters:** Nothing can ultimately be omitted; the capacity condition prevents destructive pops.
- **`repetition = k`:** Every output slot is reserved for `letter`, so all non-`letter` characters are skipped.
- **All characters equal `letter`:** The first `k` retained copies form the only value-level answer.
- **More required letters than currently selected:** The non-`letter` append guard reserves enough remaining slots.
- **Popping a required letter:** Allowed only when the current and future suffix can replace it.
- **Extra copies of `letter`:** They are legal because the requirement is at least, not exactly, `repetition`.
- **Equal current and top characters:** No pop occurs because equality cannot create a lexicographic improvement.
- **Late smaller character:** It cannot trigger a pop when too few positions remain to refill length `k`.
- **Duplicate subsequence values:** The task asks for the smallest string, not a unique index selection.
- **Input preservation:** The source reads `s` and builds a separate stack.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert s\rvert$. Counting `letter` takes $O(N)$ time. The main scan takes amortized $O(N)$ time because each character is pushed at most once and popped at most once. Joining at most `k` characters costs $O(k)$, which is within $O(N)$. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

# Guided Example: String Without AAA or BBB

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": 1, "b": 2}`
- **Required output:** `"abb"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers `a` and `b`, return **any** string `s` such that:

The objective is to compute `"abb"` from `{"a": 1, "b": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build safe blocks instead of choosing one character at a time

The output must use exactly `a` copies of `'a'` and exactly `b` copies of `'b'`, while never containing three equal consecutive characters. The protected solution handles both requirements by repeatedly appending a short block whose composition reflects which character is more plentiful.

While both counts are positive, there are three cases:

- if `a > b`, append `"aab"` and consume two `a` characters and one `b` character;
- if `a < b`, append `"bba"` and consume one `a` character and two `b` characters;
- if `a == b`, append `"ab"` and consume one of each.

Each individual block is already safe: no block contains `"aaa"` or `"bbb"`. More importantly, the blocks spend the more abundant character faster. This steadily reduces an imbalance instead of allowing the majority character to accumulate into a dangerous run.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": 1, "b": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the larger count receives two positions

Suppose more `a` characters remain than `b` characters. If the construction alternated one-for-one forever, all `b` characters could be exhausted while too many `a` characters remained. Appending `"aab"` uses the scarce `b` as a separator between groups of at most two `a` characters. The difference `a - b` falls by one:

`(a - 2) - (b - 1) = (a - b) - 1`.

The symmetric `"bba"` case raises `a - b` by one when it is negative, again moving the difference toward zero. When counts are equal, `"ab"` preserves equality.

This is the core greedy idea: use two of the majority character when possible, but immediately follow them with the minority character that prevents a third copy.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The subtractions are always legal

The `while a and b` condition guarantees both counts are at least one. If `a > b` and `b >= 1`, then `a` must be at least two, so subtracting two from `a` is safe. Similarly, `a < b` guarantees `b >= 2`. In the equal case, both are positive and subtracting one from each is safe.

No count can become negative. Every appended block contains exactly the characters reflected by its accompanying subtraction, so the remaining counters always equal the number of unused characters.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abb"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": 1, "b": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abb"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Character-by-character greedy:** Append the more frequent remaining character unless it would match the previous two characters. This is also linear and more directly checks the forbidden pattern, but it performs a decision for every character instead of using safe blocks.
- **Pure alternation:** Alternating `"ab"` works only when counts are close. It can leave too many copies of the majority character at the end.
- **Backtracking over all strings:** It can search for a valid arrangement but explores many equivalent prefixes even though the feasibility guarantee makes a deterministic greedy construction sufficient.
- **Always append two of the majority:** The minority must be inserted as a separator. Appending majority pairs without the trailing opposite character could create a triple where blocks meet.
- **One count initially zero:** The loop is skipped and the only character is repeated. The existence guarantee implies its count is at most two; otherwise no legal string could exist.
- **Both counts zero:** Both final conditions are false, and joining the empty block list correctly returns the empty string of length zero.
- **Equal counts:** Repeated `"ab"` blocks consume both counts together and can never form a triple.
- **Difference of one:** The larger side may first use a three-character block, after which the remainder becomes equal and alternates safely.
- **Maximum counts:** The construction depends only on counts, not on recursion or search, so inputs up to one hundred are handled with the same linear work.
- **Any valid answer accepted:** The method does not try to produce lexicographically smallest output because the contract does not require a unique ordering.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let `L = a + b` denote the requested output length using the original input counts. Every loop iteration consumes at least two and at most three characters, and the final suffix consumes the rest. Across the whole method, exactly `L` characters are created. Constructing the blocks and joining them takes `O(L)` time.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

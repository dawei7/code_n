# Guided Example: Check if Binary String Has at Most One Segment of Ones

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1001"}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary string `s` **without leading zeros**, return `true` *if *`s`* contains **at most one contiguous segment of ones***. Otherwise, return `false`.

The objective is to compute `false` from `{"s": "1001"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn the segment question into one forbidden transition

A segment of ones is a maximal consecutive block of `1` characters. For example, `11100` has one such block, while `110011` has two because the zeros separate the first pair of ones from the last pair.

The constraint that `s[0]` is `1` is unusually useful. It means the string begins inside its first segment of ones. As the scan moves from left to right, only two phases are allowed if there is at most one segment:

1. an initial run of one or more `1` characters; and
2. optionally, a trailing run of `0` characters.

Once the scan has entered the zero phase, another `1` would start a second segment. The exact adjacent boundary that reveals this event is `01`: a zero immediately followed by a one.

This gives a complete criterion:

- if `01` occurs anywhere, the answer is `false`;
- if `01` never occurs, the answer is `true`.

The protected solution expresses that entire scan through Python's substring-membership operation: it asks whether `'01' not in s`. Python searches the string for the two-character pattern and negates the result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1001"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why checking only adjacent characters is sufficient

It may initially seem necessary to remember whether a zero appeared many positions earlier. Adjacency makes that memory unnecessary. Suppose some `1` appears after the initial ones have already ended. There must be one or more zeros between the old segment and the new one. Consider the very first `1` of the new segment. The character immediately before it is the last separating zero, so those two positions form `01`.

Conversely, every occurrence of `01` proves that a new ones segment begins at the second character of that pair. Because the string started with `1`, at least one earlier ones segment already existed before that zero. The occurrence therefore proves that there are at least two segments.

These two directions establish an exact equivalence: the string has at most one contiguous ones segment if and only if it contains no `01`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following representative inputs

For `s = "110"`, the adjacent pairs are `11` and `10`. Neither is `01`, so the membership search finds nothing and the solution returns `true`. Structurally, the string consists of one initial ones block followed by a zero.

For `s = "1001"`, the adjacent pairs are `10`, `00`, and `01`. The final pair shows that a one begins again after the scan entered the zero region. The solution finds that pattern and returns `false`.

For `s = "1111"`, every adjacent pair is `11`. There is one segment covering the entire string, so returning `true` is correct.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1001"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit state flag:** Scan characters while remembering whether a zero has been seen; reject any later one. This is also $O(n)$ time and $O(1)$ space, but the forbidden substring states the same condition more directly.
- **Count `01` transitions:** Counting transitions and checking that the count is zero works, although the scan should return immediately after the first one because additional counting cannot change the answer.
- **Count complete ones segments:** A run-counting solution can detect starts of ones blocks, but it needs more boundary handling than this input's leading-one guarantee requires.
- **Regular expression:** A pattern such as an initial run of ones followed by zeros can validate the shape, but a regex adds machinery without improving complexity or clarity.
- **Length-one input:** The only valid such string is `"1"`. It has no adjacent pair and exactly one ones segment, so the answer is `true`.
- **All ones:** No zero ever ends the initial segment, so `01` cannot occur and the answer is `true`.
- **Trailing zeros:** Strings such as `"1000"` remain valid because zeros after the sole ones segment do not create another segment.
- **Immediate restart:** `"101"` contains `01` at its last two positions and must be rejected.
- **Several separating zeros:** `"100001"` still contains `01` where the final zero meets the new one; the number of separating zeros does not hide the second segment.
- **Early match:** If `01` occurs near the beginning, substring search can finish before examining the remaining suffix.
- **No leading zeros:** The proof relies on `s[0] = '1'`. Reusing this exact test for arbitrary binary strings would require reconsidering inputs that begin with zeros.
- **Binary alphabet:** Since every character is either zero or one, there is no third character that could interrupt a segment or alter the transition argument.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. Searching for the constant-length pattern `01` examines at most a linear number of candidate positions, so the time complexity is $O(n)$. The search may stop early as soon as it finds a match, but the worst case, such as an all-ones string, requires checking through the string.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

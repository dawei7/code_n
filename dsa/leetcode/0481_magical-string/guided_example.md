# Guided Example: Magical String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A magical string `s` consists of only `'1'` and `'2'` and obeys the following rule:

The objective is to compute `3` from `{"n": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

The magical string contains only `1` and `2`, but its defining rule refers to two different views of the same sequence. In the character view, the values form consecutive groups such as `1`, `22`, `11`, and `2`. In the run-length view, the lengths of those groups are `1, 2, 2, 1, ...`. The special property is that this run-length sequence is the magical string itself. The solution uses the already-generated values as instructions for generating the next groups.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Seed the self-describing process.** `s` begins as `[1, 2, 2]`. This is not an arbitrary prefix. Read as values, it is the first three characters of the magical string. Read as group information, `s[0] = 1` describes the initial group containing one `1`, and `s[1] = 2` describes the following group containing two `2`s. Those two groups already produce `[1, 2, 2]`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The next unread run-length instruction is therefore at index `i = 2`. Its value is `2`, meaning that the next group must contain two copies of the next alternating symbol. Keeping `i` separate from `len(s)` is essential: `i` identifies which existing value supplies the next group length, whereas the end of `s` identifies where new characters are appended.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate characters and parse groups afterward:** Building a candidate string without using its prior values as instructions does not solve the self-referential construction. The pointer `i` is what turns the definition into a deterministic process.
- **Recursive generation:** Recursion can mirror the conceptual dependency, but it adds call-stack overhead and makes the distinction between instruction position and write position harder to maintain. The iterative pointer is direct and bounded.
- **Count ones while appending:** This can remove the final full-prefix scan, provided only positions below `n` are counted when the last group overshoots. The present solution favors a simple final slice and count while preserving the same $O(n)$ bounds.
- **Store a textual string:** It is possible, but every run-length instruction must then be converted from `'1'` or `'2'` to an integer. An integer list matches both roles of each element naturally.
- **`n = 1`, `2`, or `3`:** The seed is already long enough. The loop correctly does no work, and slicing selects exactly the requested prefix.
- **Overshooting `n`:** A length-two group can extend one position beyond the requested prefix. `s[:n]` prevents that irrelevant position from changing the count.
- **Toggle correctness:** `3 - pre` relies on `pre` always being exactly `1` or `2`. That guarantee follows from the seed and from appending only values produced by the same toggle.
- **Do not advance `i` by the group length:** `i` indexes run-length instructions, not generated character positions. Exactly one instruction describes each new group, so it advances by one after every append.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The generated list reaches length `n` or at most `n + 1`. Each loop appends either one or two elements, and every run-length instruction is consumed once. The total append work is therefore $O(n)$. The final slice and `count(1)` each inspect at most `n` entries, so they add another $O(n)$ amount rather than changing the overall $O(n)$ time bound.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

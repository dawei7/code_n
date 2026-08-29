# Guided Example: Flip Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"currentState": "++++"}`
- **Required output:** `["--++", "+--+", "++--"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a Flip Game with your friend.

The objective is to compute `["--++", "+--+", "++--"]` from `{"currentState": "++++"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why scanning adjacent pairs covers every move

Two characters are consecutive precisely when their indices have the form $i$ and $i+1$. The iterator `pairwise(s)` produces exactly these pairs:

$$
(s[0],s[1]), (s[1],s[2]), \ldots, (s[n-2],s[n-1]).
$$

`enumerate` supplies the corresponding starting index `i`. Therefore, when the condition `a == b == "+"` succeeds, `i` is the first position of one legal flip. When it fails, that pair is one of `"--"`, `"+-"`, or `"-+"`, none of which the rules permit changing.

No other kind of move exists. Consequently, rejecting every non-`"++"` pair cannot omit a legal result, and accepting every `"++"` pair considers every legal result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"currentState": "++++"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the string becomes a character list

Python strings are immutable: individual positions of `currentState` cannot be changed in place. The source first executes `s = list(currentState)`, producing a mutable list with one character per position. This conversion is useful because each candidate changes exactly two positions. The algorithm can temporarily assign `"-"` to those positions without rebuilding all unchanged characters through several slice expressions.

The list `ans` begins empty and collects the completed next-state strings. It is important that the results placed in `ans` are strings, not references to the mutable list. `"".join(s)` reads the list's current characters and creates a new immutable string, so a result remains unchanged after `s` is restored or edited for a later candidate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The temporary-change-and-restore cycle

For a legal pair beginning at `i`, the source performs three conceptual steps:

1. Set `s[i]` and `s[i + 1]` to `"-"`.
2. Join the complete list and append that snapshot to `ans`.
3. Set the same two positions back to `"+"`.

The restoration is essential. Every answer must represent one move made from the original `currentState`, not a sequence of moves accumulated from earlier iterations. If the first flip were left in place, the next result could contain four changed positions and would describe two turns rather than one.

For example, consider `currentState = "++++"`:

| Pair start `i` | Original pair | Temporary list | Appended state | List after restoration |
| --- | --- | --- | --- | --- |
| 0 | positions 0 and 1 | `--++` | `"--++"` | `++++` |
| 1 | positions 1 and 2 | `+--+` | `"+--+"` | `++++` |
| 2 | positions 2 and 3 | `++--` | `"++--"` | `++++` |

Notice that legal pairs may overlap. The middle plus signs participate in more than one possible move. Restoring after each snapshot ensures that an earlier temporary flip does not hide an overlapping pair. This is why all three moves from `"++++"` are found.

`pairwise(s)` advances one adjacent pair at a time. During an iteration, the current values `a` and `b` have already been obtained. The source restores the list before requesting the next pair, so the iterator continues over the original character values rather than a permanently altered state.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["--++", "+--+", "++--"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"currentState": "++++"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["--++", "+--+", "++--"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Slicing and concatenation:** For every legal index `i`, construct `currentState[:i] + "--" + currentState[i + 2:]`. This is straightforward and has the same $O(n^2)$ worst-case time and output space, but it creates candidate strings through slices rather than reusing a mutable character buffer.
- **Regular-expression matching:** A pattern search can locate occurrences of `"++"`, but overlapping matches require special handling. A normal non-overlapping search would miss moves such as the pair beginning at index 1 in `"+++"`.
- **A set of results:** Duplicate elimination is unnecessary because distinct legal starting indices yield distinct next-state strings. A set would add hashing work and would discard the implementation's natural left-to-right order without improving correctness.
- **Recursive game exploration:** Searching future turns solves a different question, such as whether the current player can force a win. This problem stops after one move, so recursion would add irrelevant states and work.
- **Failure to restore the list:** Leaving a temporary flip in place makes later outputs depend on earlier ones. That generates states containing multiple moves and may also hide overlapping legal pairs.
- **Restoring before joining:** The snapshot must be created while the two positions contain minus signs. Restoring first would append the unchanged input instead of the next state.
- **Joining only the changed pair:** Every answer must be a full state string of length $n$, not merely `"--"` or a move index. Joining the complete list preserves all unaffected positions.
- **Length one:** There is no adjacent pair. `pairwise(s)` yields nothing, the loop body never runs, and the returned answer is correctly empty.
- **No adjacent plus signs:** Strings such as `"----"` or `"+-+-"` contain no legal move, so no result is appended and the method returns `[]`.
- **Exactly one legal pair:** A state such as `"--++-"` produces one result by flipping only those two plus signs, so the method returns a one-element list.
- **Overlapping legal pairs:** `"+++"` has moves starting at indices 0 and 1. They produce `"--+"` and `"+--"`; restoration ensures that both are included.
- **Disjoint legal pairs:** In `"++--++"`, either the left or right pair may be flipped, but one output must never flip both because the contract permits exactly one move.
- **All plus signs:** This maximizes the number of results at $n-1$ and realizes the $O(n^2)$ output size.
- **Allowed output order:** The contract accepts any order. The left-to-right order produced here is deterministic and requires no extra sorting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + mn)$. Let $n$ be the length of `currentState`, and let $m$ be the number of adjacent `"++"` pairs. The pair scan performs $n-1$ constant-time checks. For each of the $m$ legal pairs, `"".join(s)` visits all $n$ characters to materialize an immutable output string. The precise output-sensitive time is therefore
- **Auxiliary Space Complexity:** $O(mn)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

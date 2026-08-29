# Guided Example: Replace All ?'s to Avoid Consecutive Repeating Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "?zs"}`
- **Required output:** `"azs"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` containing only lowercase English letters and the `'?'` character, convert **all **the `'?'` characters into lowercase letters such that the final string does not contain any **consecutive repeating **characters. You **cannot **modify the non `'?'` characters.

The objective is to compute `"azs"` from `{"s": "?zs"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What must be changed

The string contains lowercase English letters and question marks. Every question mark must be replaced by a lowercase letter so that no two adjacent characters are equal. Characters that are already letters must remain unchanged. The implementation constructs one valid result; it does not need to find a lexicographically smallest result or minimize how many distinct letters are used.

Python strings are immutable, so the solution first converts `s` into a list of individual characters. That list allows an assignment such as `s[i] = c` when a replacement is chosen. After all positions have been processed, `"".join(s)` turns the list back into the required string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "?zs"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the decision is local

Whether the character at index `i` is valid depends only on its immediate neighbors:

- if `i > 0`, it must differ from `s[i - 1]`;
- if `i + 1 < n`, it must differ from `s[i + 1]`.

No character farther away can become adjacent to position `i`, because this problem replaces characters without deleting or moving them. Therefore, choosing a replacement does not require dynamic programming, backtracking, or knowledge of the whole prefix beyond its final adjacent character.

The scan moves from left to right. When it reaches a question mark, the position on the left has already been finalized. It is either an original letter or a question mark that an earlier iteration replaced. The position on the right has not necessarily been processed, but its current value still gives all the information needed:

- if the right character is a fixed letter, the current replacement must avoid it;
- if the right character is `?`, it imposes no restriction yet, because that question mark will make its own safe choice when the scan reaches it.

This asymmetry is important. The algorithm never needs to predict what a future question mark will become. The future position will see the current chosen letter as its finalized left neighbor and will avoid it then.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only `a`, `b`, and `c` are tried

For each question mark, the inner loop tries the three candidates in `"abc"`. At most two letters can be forbidden: one by the left neighbor and one by the right neighbor. Even when those neighbors contain two different letters, three candidates guarantee that at least one candidate remains. If both neighbors contain the same letter, only one candidate is forbidden. At an endpoint, there is at most one neighbor, and a one-character string has none.

The source checks a candidate with two short-circuit conditions. The expression `i and s[i - 1] == c` is false at index zero, so it does not access a nonexistent left neighbor. The second condition, `i + 1 < n and s[i + 1] == c`, first verifies that a right neighbor exists. If either existing neighbor equals `c`, `continue` rejects that candidate. Otherwise, the candidate is assigned and `break` stops the three-letter search.

There is no fallback after that loop because the three-candidate argument proves that one candidate must be available. The loop may try one, two, or three letters, but it always assigns the question mark.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"azs"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "?zs"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"azs"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Backtracking over all lowercase letters:** Trying a letter, recursing, and undoing choices can eventually find a valid string, but it solves a much larger search problem than necessary. Adjacency is local, and three candidates always leave a valid choice, so the greedy decision never needs to be reconsidered.
- **Trying all 26 lowercase letters:** This is correct but unnecessary. At most two neighboring letters are forbidden, so `a`, `b`, and `c` already provide the mathematical guarantee the algorithm needs.
- **Copying only the previous character:** A method that avoids the left neighbor but ignores a fixed right neighbor can create an invalid pair. For example, choosing `a` for the middle of `"b?a"` would conflict with the right side. The checked-in implementation tests both existing neighbors.
- **Treating a right-side question mark as a fixed restriction:** A question mark has no chosen letter yet and should not forbid a candidate. It will avoid the current letter when its own turn arrives.
- **Single-character input:** A lone question mark becomes `a`, while a lone fixed letter is returned unchanged. With no adjacent pair, either result automatically satisfies the condition.
- **Question mark at the first or last position:** The short-circuit boundary tests safely consider only the neighbor that exists. There is no negative-index lookup at the first position and no out-of-range lookup at the last.
- **Several consecutive question marks:** Each later replacement sees the finalized replacement immediately to its left. This prevents equal adjacent choices without needing to plan the whole run in advance.
- **Fixed letters outside `a`, `b`, and `c`:** They do not cause difficulty. A fixed `z`, for example, forbids none of the three candidates unless a candidate actually equals it, so `a` is immediately usable.
- **Two different fixed neighbors:** Even if the neighbors forbid two of the three candidates, the third remains. This is the tight reason that a three-letter candidate set is sufficient.
- **Input guarantee about original letters:** The algorithm cannot repair an equal adjacent pair made of two non-question-mark characters because it intentionally never changes fixed letters. Correctness therefore relies on the stated guarantee that such a conflict is absent from the input.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `s`.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

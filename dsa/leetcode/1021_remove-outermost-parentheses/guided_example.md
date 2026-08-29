# Guided Example: Remove Outermost Parentheses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "(()())(())"}`
- **Required output:** `"()()()"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A valid parentheses string is either empty `""`, $"(" + A + ")"$, or $A + B$, where `A` and `B` are valid parentheses strings, and `+` represents string concatenation.

The objective is to compute `"()()()"` from `{"s": "(()())(())"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use nesting depth instead of explicitly splitting primitives

A valid parentheses string can contain several primitive pieces concatenated together. A primitive piece begins when the nesting depth rises from zero to one and ends when the depth falls from one back to zero. Those two characters are exactly its outermost opening and closing parentheses.

This observation means the method does not need to construct the primitive decomposition first. It can scan `s` once, maintain the current nesting depth in `cnt`, and copy every character except a transition between depth zero and depth one.

The list `ans` stores the characters that survive. A list is used rather than repeatedly appending to a Python string because list append is constant time, while repeated immutable-string concatenation can copy the growing prefix again and again. The final `''.join(ans)` creates the result in one pass.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "(()())(())"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What `cnt` means

After the current character has been processed, `cnt` equals the number of unmatched opening parentheses seen so far. It is also the nesting depth immediately after that character.

Because `s` is guaranteed to be valid, `cnt` never becomes negative, and it equals zero after the final character. Each time it becomes zero during the scan, one complete primitive component has ended. The next opening parenthesis, if any, begins the next primitive.

The algorithm treats opening and closing parentheses in slightly different orders because the decision must be based on the depth inside the character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Opening parentheses are tested after incrementing

When `c == '('`, the code first runs `cnt += 1`. If the new depth is one, the character moved from outside every primitive to the outer layer of a new primitive. That is an outermost parenthesis, so it must be omitted.

If the new depth is greater than one, some unmatched opening parenthesis already surrounds this character. The current opening is internal to the primitive and must remain, so `ans.append(c)` runs only when `cnt > 1`.

Another way to state the same rule is that an opening parenthesis is copied exactly when the old depth was at least one. The implementation checks the new depth because it has already incremented it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"()()()"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "(()())(())"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"()()()"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicitly split primitive substrings:** Record a start index whenever depth rises from zero, and when it returns to zero append the slice excluding the two endpoints. This is correct but creates slices and requires more boundary bookkeeping than filtering characters during the scan.
- **Use a stack:** Push opening parentheses and pop for closings, using stack size as depth. Since only the number of unmatched openings matters, a full stack stores redundant identical characters and uses unnecessary `O(N)` auxiliary memory.
- **Track old depth instead:** Append an opening when `cnt > 0` before incrementing, and append a closing when `cnt > 1` before decrementing. That equivalent ordering is correct, but the before and after conventions must not be mixed.
- **Repeated string concatenation:** Updating `result += c` is easy to read but can repeatedly copy the growing immutable string. Accumulating characters in `ans` and joining once is the reliable linear-time pattern.
- **One primitive `"()"`:** Both characters are outermost, so the returned string is empty.
- **Several minimal primitives:** Input such as `"()()()"` returns empty because every character belongs to an outer layer of its own primitive.
- **Deep nesting:** Input `"(((())))"` loses only its first and last characters. All other parentheses occur at internal depths and remain.
- **Internal concatenation:** A primitive may contain valid pieces inside its outer pair, such as `"(()())"`. Depth does not return to zero between those internal pieces, so their parentheses are preserved.
- **Primitive boundary:** A closing that makes `cnt` zero and the following opening that makes it one are both removed, which is exactly right for two adjacent primitive components.
- **Empty output:** `''.join([])` correctly returns `""`, so no special case is needed.
- **Only two character kinds:** The implementation's `else` branch treats every non-opening character as a closing parenthesis. This is safe only because the contract guarantees that `s` contains no other characters.
- **Invalid input:** The method intentionally does not detect negative depth or a nonzero final depth. Such validation would address a different problem because validity is guaranteed here.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = len(s)`. The loop reads each of the `N` characters exactly once. Each iteration performs a comparison, one depth update, and at most one list append, all in constant time. Joining the retained characters takes at most `N` additional work. Total time is `O(N)`, matching the manifest.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

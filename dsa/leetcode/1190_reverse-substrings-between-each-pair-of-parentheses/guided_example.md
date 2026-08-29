# Guided Example: Reverse Substrings Between Each Pair of Parentheses

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "(abcd)"}`
- **Required output:** `"dcba"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` that consists of lower case English letters and brackets.

The objective is to compute `"dcba"` from `{"s": "(abcd)"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What the stack represents before a closing parenthesis

At any scan position, `stk` contains the processed form of the input prefix, plus `"("` markers for regions that have opened but not closed. Any nested region that closed earlier has already been reversed and has had both of its parentheses removed.

Because parentheses are balanced, the marker for the current closing parenthesis exists somewhere below the stack’s top. Because matching is nested, the nearest opening marker on the stack is its matching one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "(abcd)"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Pop the current region in reverse order

When `c == ")"`, the code creates an empty temporary list `t`. It repeatedly pops from `stk` until the new top is `"("`:

`t.append(stk.pop())`.

The stack yields the enclosed processed characters from right to left. Appending them to `t` in that pop order directly creates the reversal. There is no need to reverse `t` again.

Once the loop reaches the opening marker, `stk.pop()` discards that `"("`. The closing parenthesis was never appended, so both parentheses disappear from the eventual result. Finally, `stk.extend(t)` places the reversed characters back above the surrounding content.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why nested reversals occur in the required order

An outer closing parenthesis cannot be encountered until every textual character and every nested closing parenthesis inside it has been scanned. Therefore, when an inner pair closes, its reversal is completed first. Its reversed letters then behave like ordinary processed content inside the outer region.

When the outer pair later closes, popping reverses the entire current interior, including the result of the inner reversal. This exactly simulates “reverse the innermost substring, remove its parentheses, then continue outward.”

Follow `"(u(love)i)"`. The stack first holds the outer marker, `u`, the inner marker, and the letters of `love`. At the inner close, the letters pop as `e`, `v`, `o`, `l` and are extended back in that order, giving processed inner text `evol`. The next letter `i` is appended. At the outer close, the current interior pops in reverse as `i`, `l`, `o`, `v`, `e`, `u`. The final joined text is `"iloveu"`.

Notice that the outer reversal reverses the already reversed sequence `"evol"` again as part of the larger region. That is not redundant from a semantic perspective; nested reversals can cancel direction for some letters, and the stack operations model those effects correctly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"dcba"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "(abcd)"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"dcba"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Paired-parenthesis direction traversal:** First link every matching pair. During a second pass, jump to the mate and reverse direction whenever a parenthesis is reached. This processes each position a constant number of times for $O(n)$ time and $O(n)$ space.
- **Recursive parsing:** A function can parse until a closing parenthesis and return the reversed nested result. It mirrors the grammar clearly but still needs attention to string-copying costs and recursion depth.
- **Repeated string slicing:** Finding an innermost textual pair and replacing slices is intuitive but can cause even more expensive immutable-string copying.
- **No parentheses:** Every letter is appended once, the closing branch never runs, and the original string is returned.
- **Empty parenthesized region:** If allowed by the balanced syntax, the top is immediately `"("` at close; the temporary list stays empty and both markers disappear.
- **Single pair:** All enclosed letters are popped once, producing their simple reversal.
- **Deep nesting:** Semantic processing remains correct, but repeated movement exposes the quadratic worst case.
- **Adjacent pairs:** Each pair is closed and transformed independently, and their resulting letter sequences remain adjacent in input order.
- **Balanced-input guarantee:** The loop safely reads `stk[-1]` because every closing parenthesis has a matching earlier opening marker. Malformed input would require explicit validation.
- **Parentheses removal:** The opening marker is explicitly popped, while the closing marker is never pushed. Joining the stack cannot include brackets.
- **Letters are not deduplicated:** Every pop is followed by exactly one append into `t` and one extension back into `stk`, preserving multiplicity.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let $n$ be the length of `s`. The left-to-right scan itself has $n$ iterations, and ordinary append or marker operations are amortized $O(1)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

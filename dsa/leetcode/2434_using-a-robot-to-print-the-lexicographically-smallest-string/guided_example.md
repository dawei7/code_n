# Guided Example: Using a Robot to Print the Lexicographically Smallest String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "zza"}`
- **Required output:** `"azz"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` and a robot that currently holds an empty string `t`. Apply one of the following operations until `s` and `t` **are both empty**:

The objective is to compute `"azz"` from `{"s": "zza"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model the robot's temporary string as a stack

Characters leave `s` only from its front and are appended to the end of `t`. Characters leave `t` only from its end to reach the paper. Therefore `t` behaves exactly like a last-in, first-out stack. The list `stk` stores that stack, and `ans` stores characters already written on paper.

The important decision after pushing a character is whether to pop the stack now or keep reading from `s` in hope of printing a smaller future character first.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "zza"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Know the smallest unread character

The counter `cnt` initially records how many occurrences of every character remain in all of `s`. The variable `mi` starts at `'a'` and moves only upward. It represents the smallest character still unread after the current input character has been removed.

For each `c`, the code first decrements `cnt[c]` because that occurrence is no longer in unread `s`. It then advances `mi` while the count at the current letter is zero. Counter lookups for absent letters return zero, so `mi` skips every exhausted letter.

The loop stops at the first letter that still occurs, or at `'z'`. When no unread characters remain, `'z'` serves as a harmless upper sentinel: every lowercase stack character is at most `'z'`, so the stack will be completely emptied.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The counter `cnt` initially records how many occurrences of ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When it is safe to print the stack top

After appending `c` to `stk`, the code repeatedly pops while

`stk[-1] <= mi`.

If the top character is no greater than the smallest unread character, continuing to read cannot reveal a character smaller than that top. The top also blocks every older character beneath it, because stack order requires it to be removed first. Printing it now therefore gives the smallest possible next output character among all choices that can become available without first printing that same top.

If the top is greater than `mi`, some unread occurrence of `mi` can eventually be pushed. By waiting, that smaller character can sit above the current top and be printed first. Popping the larger top immediately would make the paper lexicographically worse at the earliest differing position, so the algorithm correctly keeps it in the stack.

The inner loop repeats because removing one safe top may expose another top that is also no greater than the unread minimum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"azz"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "zza"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"azz"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Suffix-minimum array:** Precompute the smalles:** - **Suffix-minimum array:** Precompute the smallest character in every suffix, then pop while the stack top is at most the next suffix minimum. This is equally $O(n)$ but uses another $O(n)$ array instead of a fixed alphabet counter.
- **Priority queue of unread characters:** A heap can reveal the minimum, but deletions of the current streamed occurrence and duplicate handling add overhead. Counts plus a monotone 26-letter pointer are simpler.
- **Explore operation sequences:** Each state can choose a transfer or pop, producing exponentially many possibilities. The greedy comparison eliminates that branching.
- **Already increasing string:** Each pushed character is no greater than the unread minimum and is printed quickly, preserving the string.
- **Strictly decreasing string:** Characters tend to accumulate until smaller ones arrive, then leave in stack order as allowed.
- **All characters equal:** Every top is safe immediately, so the output equals the input.
- **Repeated minimum letters:** `mi` remains at that letter until its last unread occurrence is consumed; stack tops equal to it may be printed safely.
- **No unread characters:** `mi` stops at `'z'`, and every lowercase stack top satisfies the pop condition, ensuring the temporary string empties.
- **Equality in the pop test:** A top equal to the unread minimum is safe to print. Requiring strict inequality would delay equal characters unnecessarily but would not improve the prefix.
- **LIFO restriction:** A smaller character buried below a larger stack top cannot be printed first. The proof always reasons about the accessible top and future characters that can be pushed above it.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. Building `Counter(s)` takes $O(n)$ time. The outer loop performs $n$ iterations. Although the inner loop is nested, every character is pushed once and popped once, so all inner iterations across the entire run total $n$. The pointer `mi` advances at most 25 times through the fixed alphabet. Total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

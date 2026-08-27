# Guided Example: Make The String Great

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leEeetcode"}`
- **Required output:** `"leetcode"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` of lower and upper case English letters.

The objective is to compute `"leetcode"` from `{"s": "leEeetcode"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the processed prefix with a stack

A bad pair consists of the same English letter in opposite cases, adjacent in either order. Removing such a pair can expose a new bad pair across the newly joined boundary.

The list `stk` stores the fully reduced result of the prefix processed so far. For each new character `c`, only the current stack top can become adjacent to it. Everything deeper in the stack remains separated from `c` by that top character.

If the stack is empty, there is no possible partner, so `c` is appended. If the top and `c` are not an opposite-case pair, `c` is also appended. If they are a bad pair, the top is popped and `c` is discarded, exactly simulating removal of those two adjacent characters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leEeetcode"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Recognize opposite case through character codes

For English letters in ASCII-compatible code points, the lowercase and uppercase forms differ by 32. For example, `ord('a') - ord('A')` is 32, while the sign is reversed if their order is reversed.

The source therefore tests:

`abs(ord(stk[-1]) - ord(c)) == 32`.

Absolute value handles both lowercase-uppercase and uppercase-lowercase order.

This test is safe because the input contains only English letters. For arbitrary punctuation, a code-point difference of 32 would not necessarily mean the same letter in opposite cases. A more semantic alternative would compare lowercase forms while also requiring different original characters.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For English letters in ASCII-compatible code points, the low... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the stack top matters

Assume `stk` is already good before reading `c`. It has no internal adjacent bad pair. Appending one character changes only one adjacency: the old top beside `c`.

If that boundary is good, the entire extended stack is good. If it is bad, removing the pair restores the earlier stack prefix, which was already reduced.

The pop can expose a previous character for a future input character, but no immediate repeated loop is needed with the same `c` because `c` was removed as part of the pair. Cascading cancellations happen naturally as later characters arrive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"leetcode"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leEeetcode"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"leetcode"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated deletion with slicing:** It follows t:** - **Repeated deletion with slicing:** It follows the definition directly but can cost $O(N^2)$ time because Python strings are copied.
- **Recursive deletion:** It can also become quadratic and adds recursion depth.
- **Mutable two-pointer buffer:** In a language with mutable strings, the input buffer can simulate the stack with constant extra storage; Python strings are immutable.
- **Empty final result:** Joining an empty stack correctly returns the empty string.
- **Single character:** It has no adjacent partner and is returned unchanged.
- **Same-case neighbors:** `aa` and `AA` are not removable because their code-point difference is zero.
- **Different letters:** Case alone is insufficient; the absolute difference must be exactly 32.
- **Reverse case order:** Absolute value handles both `aA` and `Aa`.
- **Cascading deletion:** Popping reveals an older boundary that can interact with a later input character.
- **Already good string:** Every character is appended and the original string is returned.
- **English-letter restriction:** It is what makes the code-point-difference test valid.
- **Unique answer guarantee:** Any complete legal reduction reaches the same final good string, and the stack performs one such reduction.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be input length. Every character is visited once, appended at most once, and popped at most once. List append and pop at the end are amortized $O(1)$, so total processing time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

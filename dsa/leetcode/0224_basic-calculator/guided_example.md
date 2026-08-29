# Guided Example: Basic Calculator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "1 + 1"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` representing a valid expression, implement a basic calculator to evaluate it, and return *the result of the evaluation*.

The objective is to compute `2` from `{"s": "1 + 1"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Addition and subtraction can be accumulated as signed terms

There is no multiplication or division, so outside parentheses every number or
parenthesized result contributes either positively or negatively to the current
sum. The algorithm does not need an operator-precedence stack. It keeps:

- `ans`, the running value of the expression at the current parenthesis depth;
- `sign`, either 1 or -1, which says how the next number or parenthesized group
  contributes to that running value;
- `stk`, which saves the surrounding result and sign when a new parenthesized
  expression begins.

Rewriting subtraction as addition of a negative term explains the model. For
example, `8 - 3 + 2` is `8 + (-3) + 2`. Once a complete number is read, the
source immediately performs `ans += sign * x`. A following `+` sets `sign = 1`,
and a following `-` sets `sign = -1` for the next term.

The reference permits unary minus. At the beginning of the expression or just
inside an opening parenthesis, `ans` is zero. Encountering `-` sets the sign to
-1, so the next number or group is subtracted from zero. No separate unary
operator implementation is required. Unary plus is excluded by the contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "1 + 1"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parse a whole multi-digit number before adding it

The outer pointer `i` scans the string. When `s[i]` is a digit, a second pointer
`j` advances across the complete contiguous digit run. The number begins at
zero, and each digit updates it with
`x = x * 10 + int(s[j])`. Multiplying by ten shifts the previous decimal digits
left by one place, and adding the new digit fills the units place. Thus the
characters `"123"` become 1, then 12, then 123.

After the run, the source adds `sign * x` to `ans`. It assigns `i = j - 1`
because the common `i += 1` at the bottom of the outer loop will advance to
exactly `j`, the first non-digit character. Without the `-1`, that common
increment would skip the operator or parenthesis immediately after the number.

Although there is a nested digit loop, characters are not repeatedly scanned:
the outer pointer jumps over the digits consumed by `j`. Across the whole
expression, each character participates in constant work.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: An opening parenthesis saves exactly two pieces of outer context

Suppose parsing has reached `outerAns + outerSign * (...)`. The contents inside
the parentheses must be evaluated independently before they can be combined
with the outer expression. On `(`, the exact source pushes `ans` first and
`sign` second:

1. `stk.append(ans)` saves everything already evaluated at the surrounding
   depth.
2. `stk.append(sign)` saves whether the group should be added or subtracted.
3. `ans, sign = 0, 1` starts a fresh inner expression with a neutral sum and a
   positive default sign.

No explicit opening-parenthesis marker is stored. The expression is guaranteed
valid, and each nesting level contributes exactly two stack entries, so the
matching close can recover the latest pair in last-in-first-out order.

Resetting both variables is essential. Carrying the outer running total into
the group would count it again, while carrying an outer negative sign into each
inner term would distribute that sign incorrectly when nested subtraction is
involved. The group must first obtain its own complete value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "1 + 1"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive-descent parser:** Define a function that parses until a matching `)` and returns both the value and new position. It mirrors the grammar naturally but can use $O(d)$ call-stack space and risks Python recursion limits for very deep input.
- **Reverse scan with an operand/operator stack:** Reverse the expression so stack popping preserves subtraction order, then evaluate each closed group. It is correct but processes more stack items and makes multi-digit parsing less intuitive.
- **Global accumulated sign:** Maintain the effective sign contributed by every enclosing parenthesis, using a sign-context stack. This can be compact but requires careful handling of unary minus and context restoration.
- **Leading unary minus:** Initial `ans = 0`; `-` sets `sign = -1`; the following number or parenthesized result is therefore subtracted from zero.
- **Unary minus before parentheses:** In `-(2+3)`, the saved outer context is result 0 and sign -1, so the close produces -5.
- **Multiple digits:** The inner digit loop forms the entire integer before applying its sign, preventing `123` from being treated as three separate terms.
- **Spaces anywhere between tokens:** They trigger no state change and are skipped by the common pointer increment.
- **Deeply nested groups:** Every opening contributes exactly two stack entries and every closing consumes exactly two. Valid balancing prevents underflow, though memory grows with nesting depth.
- **Subtraction after a closed group:** The close leaves the combined value in `ans`; the following `-` overwrites `sign` for the next term, exactly like subtraction after a number.
- **Zero values:** Parsing `0` still completes a number and adds zero with the current sign. It does not interfere with later operators.
- **Integer range:** The reference guarantees every running calculation fits signed 32-bit range. Python integers would remain safe even beyond it.
- **Invalid syntax:** The implementation relies on the validity guarantee. It does not diagnose unmatched parentheses, unsupported characters, unary plus, or malformed operator sequences.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of characters in `s`. The outer loop and the number parser
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

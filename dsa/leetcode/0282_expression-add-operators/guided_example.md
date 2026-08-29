# Guided Example: Expression Add Operators

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "123", "target": 6}`
- **Required output:** `["1+2+3", "1*2*3"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `num` that contains only digits and an integer `target`, return ***all possibilities** to insert the binary operators *`'+'`*, *`'-'`*, and/or *`'*'`* between the digits of *`num`* so that the resultant expression evaluates to the *`target`* value*.

The objective is to compute `["1+2+3", "1*2*3"]` from `{"num": "123", "target": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every expression requires two kinds of choices

The digits must stay in their original order, but the algorithm must decide both where operands end and which operator separates consecutive operands. For `num = "123"`, possible operand partitions include `1 | 2 | 3`, `1 | 23`, `12 | 3`, and `123`. For a partition with more than one operand, every boundary can receive `+`, `-`, or `*`.

No greedy rule can know which boundary or operator will eventually reach `target`, and the problem asks for all valid expressions. The exact solution therefore uses depth-first backtracking to enumerate every legal combination while evaluating each partial expression incrementally.

At a recursive position `u`, the loop chooses every substring `num[u : i + 1]` as the next operand. Moving `i` farther right is the “do not insert an operator at this digit gap” choice; making the recursive call commits the resulting operand and places one operator before the next operand.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "123", "target": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the four recursive state values

The helper `dfs(u, prev, curr, path)` carries exactly the information needed to continue:

- `u` is the index of the next unused digit. Digits before `u` have all been placed in `path`.
- `path` is the expression text built from those consumed digits.
- `curr` is the correctly evaluated value of `path`, respecting multiplication precedence.
- `prev` is the signed value of the final additive term currently included in `curr`.

The first three meanings are direct. The role of `prev` is the important part: it lets a later multiplication revise the most recent term without reparsing the whole expression.

For example, after building `1+2`, `curr = 3` and `prev = 2`. After building `5-2`, `curr = 3` and `prev = -2`; the sign is stored with the term because the expression is effectively `5 + (-2)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose every legal next operand

For each endpoint `i` from `u` through the final digit, the source converts `num[u : i + 1]` to integer `next`. This enumerates all operand lengths beginning at `u`.

If `u == 0`, this is the expression's first operand. A binary operator cannot appear before it, so the solution makes only one recursive call with `prev = next`, `curr = next`, and `path` containing the operand. Handling the first operand separately avoids malformed expressions such as `+1+2` and prevents subtraction from being confused with a unary sign.

For every later operand, the source explores three disjoint branches: addition, subtraction, and multiplication. After each call returns, the loop can extend the operand farther or try another operator, which is the backtracking behavior.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["1+2+3", "1*2*3"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "123", "target": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["1+2+3", "1*2*3"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Build every expression, then evaluate it:** This separates generation from evaluation but reparses every leaf and may rely on forbidden or unsafe `eval`-style functionality. Carrying `curr` and `prev` evaluates each branch incrementally.
- **Mutable expression buffer:** Append operand and operator fragments, recurse, then pop them. This avoids retaining a chain of immutable prefix strings and brings active path storage closer to the manifest's $O(n)$ auxiliary bound.
- **Dynamic programming by index and total:** The same index and current total can have different final multiplicative terms, so memoizing only those two values is incorrect. Including all required arithmetic state still does not naturally preserve every distinct expression string that must be returned.
- **No multiplication:** With only `+` and `-`, `curr` alone would suffice because both operators have equal precedence. `prev` exists specifically to revise the final term for `*`.
- **First operand:** It receives no leading operator. Treating it through the ordinary subtraction branch would generate unary-minus expressions that the insertion contract does not request.
- **Single digit:** The only complete expression is the digit itself. It is returned exactly when its value equals `target`.
- **Operand zero:** A single `0` is valid and participates normally in all three operator branches.
- **Leading-zero run:** When the next digit is zero, only that one digit may form the operand. Longer endpoints are pruned with `break`.
- **Negative intermediate totals:** They are valid. Subtraction can make `curr` negative, and later operations can still reach the target, so they must not be pruned.
- **Large intermediate products:** The target is 32-bit, but intermediate expression values are not promised to stay in that range. Python integers handle them without overflow; fixed-width implementations should use a sufficiently wide integer type.
- **Operator precedence:** The source supports the standard precedence of multiplication over addition and subtraction, with no parentheses. The signed-last-term update is valid precisely for this operator set.
- **All digits must be used:** Reaching the target before `u` reaches the end is not a solution; every digit must appear exactly once and in order.
- **Answer order:** DFS traversal determines the returned ordering. The contract asks for all possibilities and does not require a particular order.
- **No valid expression:** Exhaustive search leaves the result list empty, as in the third example.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(4^n)$. Let $n$ be the number of digits. Each of the $n-1$ gaps has four conceptual choices: join the neighboring digits into one operand, or place `+`, `-`, or `*`. This gives at most $4^{n-1}$ complete expression structures before leading-zero pruning, conventionally written as $O(4^n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.

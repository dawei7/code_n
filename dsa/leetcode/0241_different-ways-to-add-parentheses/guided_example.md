# Guided Example: Different Ways to Add Parentheses

We trace the step-by-step divide-and-conquer operator bifurcation, Cartesian product combination, and sub-expression memoization on representative arithmetic strings:

- **Input:** $\text{expression} = \text{"2-1-1"}$
- **Required output:** $[0, 2]$ (Two parenthesizations: $((2 - 1) - 1) = 0$ and $(2 - (1 - 1)) = 2$)
- **Rich Catalan Instance:** $\text{expression} = \text{"2*3-4*5"} \implies [-34, -14, -10, -10, 10]$ ($C_3 = 5$ distinct evaluation trees)
- **Base Literal Instance:** $\text{expression} = \text{"7"} \implies [7]$ (No operators; single scalar value)

This instance demonstrates recursive divide-and-conquer on binary expression trees, explains why partitioning at each operator splits the problem into independent sub-expressions, details Cartesian cross-product combination ($\text{left\_results} \times \text{right\_results}$), proves Catalan growth ($C_{N-1}$), and prevents exponential recomputations via memoization.

---

## 1. Instance & Teaching Goal

Given an arithmetic expression string with digits and operators (`+`, `-`, `*`):
$$
\text{expression} = \text{"2-1-1"}
$$
Compute all possible numerical outcomes produced by inserting parentheses in all legal ways:
1. Group left first:
   $$
   ((2 - 1) - 1) = 1 - 1 = \mathbf{0}
   $$
2. Group right first:
   $$
   (2 - (1 - 1)) = 2 - 0 = \mathbf{2}
   $$
Output: `[0, 2]`.

### The Binary Expression Tree Duality
Parenthesizing an arithmetic expression is mathematically equivalent to constructing a full binary syntax tree where:
- Each **leaf node** is a number operand.
- Each **internal node** is an operator (`+`, `-`, `*`).
- The root of the tree is the **last operator evaluated**.

By choosing each operator in turn to be the root (the final operation), the problem naturally splits into two independent sub-expressions:
- Everything to the left of the operator.
- Everything to the right of the operator.
Recursively evaluating both halves and applying the operator to all pairs $(l, r) \in \text{Left} \times \text{Right}$ generates all valid outcomes.

---

## 2. Conceptual Foundation & Invariants

### Divide-and-Conquer Recurrence
Define `diffWaysToCompute(expr)`:
1. **Base Case (Pure Integer):**
   If `expr` contains no operators (`+`, `-`, `*`):
   $$
   \text{return } [\text{int}(expr)]
   $$
2. **Recursive Partitioning:**
   Initialize $\text{results} = []$.
   For each index $i$ where $\text{expr}[i] \in \{+, -, *\}$:
   - Solve left sub-expression:
     $$
     \text{left\_vals} = \text{diffWaysToCompute}(\text{expr}[:i])
     $$
   - Solve right sub-expression:
     $$
     \text{right\_vals} = \text{diffWaysToCompute}(\text{expr}[i+1:])
     $$
   - **Cross-Product Evaluation:**
     For every $l \in \text{left\_vals}$ and every $r \in \text{right\_vals}$:
     $$
     \text{val} = \begin{cases}
     l + r, & \text{if } \text{expr}[i] == \text{'+'} \\
     l - r, & \text{if } \text{expr}[i] == \text{'-'} \\
     l \times r, & \text{if } \text{expr}[i] == \text{'*'}
     \end{cases}
     $$
     $\text{results}.\text{append}(\text{val})$.
3. **Memoization:**
   Cache `memo[expr] = results` to avoid resolving duplicate substrings.
   Return `results`.

> **Invariant.** For any sub-expression $S$, `diffWaysToCompute(S)` returns the complete multiset of all values achievable by every valid full parenthesization of $S$.

---

## 3. Step-by-Step Worked Execution

We trace `diffWaysToCompute("2-1-1")`:
The expression has length 5.
Operators are located at index $1$ (`'-'`) and index $3$ (`'-'`).

### Branch A: Partition at Index 1 (Operator `'-'`)
- Expression split: $\text{Left} = \text{"2"}$, $\text{Right} = \text{"1-1"}$.
- **Subproblem 1:** $\text{Left} = \text{"2"}$
  - Contains no operators $\implies$ base case returns $[2]$.
- **Subproblem 2:** $\text{Right} = \text{"1-1"}$
  - Operator at index 1 (`'-'`).
  - Left of subproblem: `"1"` $\implies [1]$.
  - Right of subproblem: `"1"` $\implies [1]$.
  - Combine: for $l \in [1]$ and $r \in [1]$:
    $$
    l - r = 1 - 1 = \mathbf{0}
    $$
  - Subproblem `"1-1"` returns $[0]$.
- **Combine Branch A:**
  Cross-product of $\text{Left} = [2]$ and $\text{Right} = [0]$ under `'-'`:
  $$
  2 - 0 = \mathbf{2}
  $$
  Branch A yields: $[2]$ (corresponding to $2 - (1 - 1)$).

---

### Branch B: Partition at Index 3 (Operator `'-'`)
- Expression split: $\text{Left} = \text{"2-1"}$, $\text{Right} = \text{"1"}$.
- **Subproblem 3:** $\text{Left} = \text{"2-1"}$
  - Operator at index 1 (`'-'`).
  - Left: `"2"` $\implies [2]$.
  - Right: `"1"` $\implies [1]$.
  - Combine:
    $$
    2 - 1 = \mathbf{1}
    $$
  - Subproblem `"2-1"` returns $[1]$.
- **Subproblem 4:** $\text{Right} = \text{"1"}$
  - Contains no operators $\implies$ base case returns $[1]$.
- **Combine Branch B:**
  Cross-product of $\text{Left} = [1]$ and $\text{Right} = [1]$ under `'-'`:
  $$
  1 - 1 = \mathbf{0}
  $$
  Branch B yields: $[0]$ (corresponding to $(2 - 1) - 1$).

---

### Step 5: Merge Results
Union of all branch results:
$$
\text{Total Results} = [2] \cup [0] = \mathbf{[2, 0]} \quad (\text{or } [0, 2])
$$

### The Catalan Instance: All Five Trees of `2*3-4*5`

The two-operator instance has a single value on each side of every split, so its cross-product never multiplies anything. The mixed-operator instance is where the product earns its name: choosing the first operator as the root forces the right side to contribute two values, and choosing the last operator forces the left side to contribute two. Summing the contributions of the three possible roots accounts for exactly $C_3 = 5$ trees.

| Root operator (string index) | Left values | Right values | Cross-product under the root operator | Trees contributed |
|:---|:---:|:---:|:---|:---|
| `'*'` at index 1 | $\{2\}$ | $\{-5, -17\}$ | $2 \times (-5) = -10$ and $2 \times (-17) = -34$ | $(2 \times ((3 - 4) \times 5))$ and $(2 \times (3 - (4 \times 5)))$ |
| `'-'` at index 3 | $\{6\}$ | $\{20\}$ | $6 - 20 = -14$ | $((2 \times 3) - (4 \times 5))$ |
| `'*'` at index 5 | $\{2, -2\}$ | $\{5\}$ | $2 \times 5 = 10$ and $(-2) \times 5 = -10$ | $(((2 \times 3) - 4) \times 5)$ and $((2 \times (3 - 4)) \times 5)$ |

Read down the last column: five trees, five entries, and the value $-10$ arrives twice from trees whose shapes are genuinely different.

---

## 4. Complete Execution Trace

```text
Expression: "2-1-1"

Operator at index 1 ('-'):
  Left: "2" -> [2]
  Right: "1-1" -> Operator at index 1 ('-'):
                   Left: "1" -> [1]
                   Right: "1" -> [1]
                   Result: 1 - 1 = [0]
  Combine: 2 - 0 = [2]  (Grouping: 2 - (1 - 1))

Operator at index 3 ('-'):
  Left: "2-1" -> Operator at index 1 ('-'):
                   Left: "2" -> [2]
                   Right: "1" -> [1]
                   Result: 2 - 1 = [1]
  Right: "1" -> [1]
  Combine: 1 - 1 = [0]  (Grouping: (2 - 1) - 1)

Combined Output: [2, 0] (or [0, 2])
```

| Partition Point | Operator | Left Sub-expression | Right Sub-expression | Left Results | Right Results | Computed Combinations |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Index 1 | `'-'` | `"2"` | `"1-1"` | `[2]` | `[0]` | $2 - 0 = \mathbf{2}$ |
| Index 3 | `'-'` | `"2-1"` | `"1"` | `[1]` | `[1]` | $1 - 1 = \mathbf{0}$ |
| **Output** | - | - | - | - | - | **`[2, 0]`** |

---

## 5. Algorithmic Correctness

**Soundness.** Every valid parenthesization evaluates an operator last. By partitioning at every operator index $i$, we consider every candidate for the final operation. Applying induction, if the recursive calls compute all valid parenthesizations of the left and right sub-expressions, the Cartesian cross-product $L \times R$ under operator $i$ generates all valid outcomes having operator $i$ as the root.

**Completeness.** Since all operators are tested as the root and the base case correctly returns literal numbers, no parenthesization is omitted. Duplicate numerical values (e.g. producing `-10` twice from different bracket structures in `"2*3-4*5"`) are preserved in the result list per problem specifications.

---

## 6. Traps This Instance Exposes

- **Duplicate Numerical Results:** Different parenthesizations can yield the exact same numerical value (e.g. $((2 \times (3 - 4)) \times 5) = -10$ and $(2 \times ((3 - 4) \times 5)) = -10$). The problem requires returning **all** results including duplicates; do not filter with a set!

The length of the returned list is always the Catalan number $C_N$, never the number of distinct values, so multiplicity is part of the contract rather than an accident of the arithmetic.

| Expression | Operators | Trees ($C_N$) | Values returned | Distinct values and their multiplicities | Why the duplicate entry survives |
|:---|:---:|:---:|:---|:---|:---|
| `"11"` | $0$ | $C_0 = 1$ | $[11]$ | $11$ once | A literal has exactly one tree, so there is nothing to merge |
| `"2-1-1"` | $2$ | $C_2 = 2$ | $[0, 2]$ | $0$ once, $2$ once | The two trees differ in which subtraction is evaluated last, and they agree on no value |
| `"1+1+1"` | $2$ | $C_2 = 2$ | $[3, 3]$ | $3$ twice | Both groupings evaluate to $3$, and the list keeps one entry per tree |
| `"2*3-4*5"` | $3$ | $C_3 = 5$ | $[-34, -14, -10, -10, 10]$ | $-34$ once, $-14$ once, $-10$ twice, $10$ once | The trees $(2 \times ((3 - 4) \times 5))$ and $((2 \times (3 - 4)) \times 5)$ collapse to the same number, and both entries remain |
- **Exponential Overlapping Subproblems:** In an expression with $N$ operators, there are Catalan $C_N = \frac{1}{N+1}\binom{2N}{N}$ evaluation trees. Without memoization, substrings like `"1-1"` are recomputed exponentially many times. Using a hash map cache `memo` keeps the number of distinct states to $O(N^2)$.

Counting invocations on `"2*3-4*5"` shows the blow-up before it becomes fatal: the same handful of substrings is requested again and again, while the number of *distinct* states stays at ten. Each state below is a contiguous substring of digits and operators, and each is solved once when the cache is in place.

| Sub-expression | Operators | Invocations without memoization | Invocations with memoization | Values returned by that state |
|:---|:---:|:---:|:---:|:---|
| `"2*3-4*5"` | $3$ | $1$ | $1$ | $\{-34, -14, -10, -10, 10\}$ |
| `"2*3-4"` | $2$ | $1$ | $1$ | $\{-2, 2\}$ |
| `"3-4*5"` | $2$ | $1$ | $1$ | $\{-5, -17\}$ |
| `"2*3"` | $1$ | $2$ | $1$ | $\{6\}$ |
| `"3-4"` | $1$ | $2$ | $1$ | $\{-1\}$ |
| `"4*5"` | $1$ | $2$ | $1$ | $\{20\}$ |
| `"2"` | $0$ | $4$ | $1$ | $\{2\}$ |
| `"3"` | $0$ | $5$ | $1$ | $\{3\}$ |
| `"4"` | $0$ | $5$ | $1$ | $\{4\}$ |
| `"5"` | $0$ | $4$ | $1$ | $\{5\}$ |

The uncached column totals $27$ recursive calls for ten distinct states, and the gap widens with every added operator, because the number of trees grows like $4^N$ while the number of substrings grows like $N^2$.
- **Multi-Digit Numbers:** Numbers can be multiple digits (e.g. `"15-2*10"`). Splitting strictly on non-digit characters (`+`, `-`, `*`) ensures multi-digit integers are not parsed incorrectly.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C_N)$, where $N$ is the number of operators and $C_N = \frac{1}{N+1}\binom{2N}{N} \approx \frac{4^N}{N^{3/2} \sqrt{\pi}}$ is the $N^{\text{th}}$ Catalan number. With memoization, each of the $O(N^2)$ distinct substrings is evaluated once, and combining results is proportional to the total number of valid parenthesizations generated. For LeetCode constraints ($N \le 10$), $C_{10} = 16,796$ operations, executing in $< 20\text{ ms}$.
- **Auxiliary Space Complexity:** $O(C_N)$ auxiliary memory to store all generated numerical outcomes in the recursion trees and memoization table.
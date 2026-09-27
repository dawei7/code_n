# Guided Example: Expression Add Operators

We trace the step-by-step operand partitioning, multiplication precedence rollback via previous term tracking (`prev_term`), leading-zero operand pruning, and target matching on representative digit strings:

- **Input:** $\text{num} = \text{"123"}, \quad \text{target} = 6$
- **Required output:** `["1+2+3", "1*2*3"]` (Both evaluate to $6$; no leading zeros exist)
- **Multiplication Precedence Instance:** $\text{num} = \text{"232"}, \quad \text{target} = 8 \implies \text{["2*3+2", "2+3*2"]}$ ($2 + 3 \times 2 = 2 + 6 = 8$)
- **Leading-Zero Suppression:** $\text{num} = \text{"105"}, \quad \text{target} = 5 \implies \text{["1*0+5", "10-5"]}$ (Expression `"1+05"` is strictly rejected)
- **No Solution Instance:** $\text{num} = \text{"3456237490"}, \quad \text{target} = 9191 \implies []$

This instance demonstrates algebraic operator insertion via backtracking, explains why multiplication requires tracking the previous additive term to reverse lower-precedence addition ($\text{curr} - \text{prev} + \text{prev} \times \text{val}$), details the single-digit limit on leading zeros, and analyzes the $O(4^N)$ combinatorial search space.

---

## 1. Instance & Teaching Goal

Given a digit string $\text{num} = \text{"123"}$ and $\text{target} = 6$:
Insert binary operators `+`, `-`, and `*` between digits such that the resulting expression evaluates to $6$.
Valid expressions:
1. $\text{"1+2+3"} \implies 1 + 2 + 3 = 6$
2. $\text{"1*2*3"} \implies 1 \times 2 \times 3 = 6$
Output: `["1+2+3", "1*2*3"]`.

### The Core Challenge: Multiplication Precedence
Operators `+` and `-` evaluate sequentially from left to right.
However, `*` has higher operator precedence than `+` and `-`:
Consider evaluating `2 + 3 * 2`:
- If evaluated strictly left-to-right: $(2 + 3) \times 2 = 5 \times 2 = 10$ (**Incorrect!**).
- Standard arithmetic: $2 + (3 \times 2) = 2 + 6 = 8$ (**Correct!**).

To maintain $O(1)$ incremental evaluation without reparsing the string or using an expensive expression parser:
The backtracking state must track **the value of the last additive term** ($\text{prev\_term}$).
When encountering `*`:
$$
\text{new\_val} = (\text{curr\_val} - \text{prev\_term}) + (\text{prev\_term} \times \text{val})
$$
The previous term is subtracted out, multiplied by the new factor, and added back!

---

## 2. Conceptual Foundation & Invariants

### Backtracking DFS State `dfs(index, prev_term, curr_val, path)`
- `index`: Next digit index to consume in `num`.
- `prev_term`: Signed value of the most recent term added to `curr_val`.
- `curr_val`: Cumulative arithmetic value of the expression so far.
- `path`: String or list of characters representing the current expression.

### Candidate Operand Generation
From current `index`, slice substrings $\text{num}[\text{index} : j + 1]$ for $j \in [\text{index}, N - 1]$:
Let $\text{val} = \text{int}(\text{num}[\text{index} : j + 1])$.

1. **Leading-Zero Invariant:**
   If $\text{num}[\text{index}] == \text{'0'}$, the only allowable operand is single digit `"0"`.
   Multi-digit operands like `"05"` or `"00"` are invalid.
   We process $j = \text{index}$ (value $0$) and immediately **break** the loop.

2. **First Operand Initialization ($\text{index} == 0$):**
   The first operand has no leading binary operator:
   $$
   \text{dfs}(j + 1, \; \text{val}, \; \text{val}, \; \text{str}(\text{val}))
   $$

3. **Subsequent Operands ($\text{index} > 0$):**
   Branch across all three operators:
   - **Addition (`+`):**
     $$
     \text{dfs}(j + 1, \; +\text{val}, \; \text{curr\_val} + \text{val}, \; \text{path} + \text{"+"} + \text{str}(\text{val}))
     $$
   - **Subtraction (`-`):**
     $$
     \text{dfs}(j + 1, \; -\text{val}, \; \text{curr\_val} - \text{val}, \; \text{path} + \text{"-"} + \text{str}(\text{val}))
     $$
   - **Multiplication (`*`):**
     $$
     \text{dfs}(j + 1, \; \text{prev\_term} \times \text{val}, \; (\text{curr\_val} - \text{prev\_term}) + (\text{prev\_term} \times \text{val}), \; \text{path} + \text{"*"} + \text{str}(\text{val}))
     $$

> **Invariant.** At every recursive step, `curr_val` is the exact mathematical evaluation of `path` according to standard arithmetic precedence, with `prev_term` preserving the trailing multiplicative factor.

---

## 3. Step-by-Step Worked Execution

We trace the backtracking search for $\text{num} = \text{"123"}, \quad \text{target} = 6$:

---

### Step 1: First Operand Choices ($\text{index} = 0$)
- **Choice 1: Operand `"1"` ($j = 0$):**
  Initial call: $\text{dfs}(\text{index} = 1, \; \text{prev} = 1, \; \text{curr} = 1, \; \text{path} = \text{"1"})$.
- **Choice 2: Operand `"12"` ($j = 1$):**
  $\text{dfs}(\text{index} = 2, \; \text{prev} = 12, \; \text{curr} = 12, \; \text{path} = \text{"12"})$.
- **Choice 3: Operand `"123"` ($j = 2$):**
  $\text{val} = 123 \ne 6 \implies$ Fails target check.

---

### Step 2: Exploring Branch `"1"` ($\text{index} = 1$)
Next digit: `"2"` (operand `"2"` at $j = 1$):

#### Sub-branch 1A: Addition (`+ 2`)
- $\text{curr} = 1 + 2 = 3, \quad \text{prev} = 2, \quad \text{path} = \text{"1+2"}$.
- Next digit: `"3"` ($j = 2$):
  - **`+ 3`:** $\text{curr} = 3 + 3 = \mathbf{6}$. Length $3 == N$.
    $\text{curr} == \text{target} \implies$ **Record `"1+2+3"`!**
  - **`- 3`:** $\text{curr} = 3 - 3 = 0 \ne 6$.
  - **`* 3`:**
    $$
    \text{curr} = (3 - 2) + (2 \times 3) = 1 + 6 = 7 \ne 6
    $$

#### Sub-branch 1B: Subtraction (`- 2`)
- $\text{curr} = 1 - 2 = -1, \quad \text{prev} = -2, \quad \text{path} = \text{"1-2"}$.
- Next digit: `"3"` ($j = 2$):
  - `+ 3`: $\text{curr} = -1 + 3 = 2 \ne 6$.
  - `- 3`: $\text{curr} = -1 - 3 = -4 \ne 6$.
  - `* 3`: $\text{curr} = (-1 - (-2)) + (-2 \times 3) = 1 - 6 = -5 \ne 6$.

#### Sub-branch 1C: Multiplication (`* 2`)
- Precedence rollback:
  $$
  \text{curr} = (1 - 1) + (1 \times 2) = \mathbf{2}, \quad \text{prev} = 1 \times 2 = \mathbf{2}, \quad \text{path} = \text{"1*2"}
  $$
- Next digit: `"3"` ($j = 2$):
  - `+ 3`: $\text{curr} = 2 + 3 = 5 \ne 6$.
  - `- 3`: $\text{curr} = 2 - 3 = -1 \ne 6$.
  - **`* 3`:**
    $$
    \text{curr} = (2 - 2) + (2 \times 3) = 0 + 6 = \mathbf{6}
    $$
    Length $3 == N, \quad \text{curr} == \text{target} \implies$ **Record `"1*2*3"`!**

---

### Step 3: Exploring Branch `"12"` ($\text{index} = 2$)
Next digit: `"3"`:
- `+ 3`: $\text{curr} = 12 + 3 = 15 \ne 6$.
- `- 3`: $\text{curr} = 12 - 3 = 9 \ne 6$.
- `* 3`: $\text{curr} = 12 \times 3 = 36 \ne 6$.

Search exhausted.
Collected solutions:
$$
\mathbf{[\text{"1+2+3"}, \text{"1*2*3"}]}
$$

---

## 4. Complete Execution Trace

```text
num = "123", target = 6

Start:
  Pick "1":
    + "2": curr = 3, prev = 2
      + "3": curr = 3 + 3 = 6 == target -> Found "1+2+3"
      - "3": curr = 3 - 3 = 0 != target
      * "3": curr = (3 - 2) + (2 * 3) = 7 != target
    - "2": curr = -1, prev = -2
      + "3": curr = 2 != target
      - "3": curr = -4 != target
      * "3": curr = -5 != target
    * "2": curr = (1 - 1) + (1 * 2) = 2, prev = 2
      + "3": curr = 5 != target
      - "3": curr = -1 != target
      * "3": curr = (2 - 2) + (2 * 3) = 6 == target -> Found "1*2*3"
  Pick "12":
    + "3": 15 != 6;  - "3": 9 != 6;  * "3": 36 != 6
  Pick "123":
    123 != 6

Result: ["1+2+3", "1*2*3"]
```

| Traversal Path | Operand Added | Operator | `prev_term` | Evaluated `curr_val` | Target Reached? |
|:---|:---:|:---:|:---:|:---:|:---:|
| `"1"` | 1 | (First) | 1 | 1 | No |
| `"1+2"` | 2 | `+` | 2 | $1 + 2 = 3$ | No |
| **`"1+2+3"`** | 3 | `+` | 3 | $3 + 3 = \mathbf{6}$ | **Yes (Match!)** |
| `"1+2-3"` | 3 | `-` | -3 | $3 - 3 = 0$ | No |
| `"1+2*3"` | 3 | `*` | $2 \times 3 = 6$ | $(3 - 2) + 6 = 7$ | No |
| `"1*2"` | 2 | `*` | $1 \times 2 = 2$ | $(1 - 1) + 2 = 2$ | No |
| **`"1*2*3"`** | 3 | `*` | $2 \times 3 = 6$ | $(2 - 2) + 6 = \mathbf{6}$ | **Yes (Match!)** |
| `"12"` | 12 | (First) | 12 | 12 | No |
| `"123"` | 123 | (First) | 123 | 123 | No |

---

## 5. Algorithmic Correctness

**Soundness.** Every output string is formed by inserting binary operators between adjacent digits of `num` with no leading-zero operands. The incremental evaluation maintains exact mathematical equivalence at each branch, correctly prioritizing multiplication over addition and subtraction via the `curr - prev + prev * val` term rollback.

**Completeness.** Backtracking exhaustively enumerates all valid partitions of the string into operands, and for each partition boundary, evaluates all three allowable operators (`+`, `-`, `*`). No legal expression can be overlooked.

---

## 6. Traps This Instance Exposes

- **Leading Zeros in Operands:** An operand like `"05"` is invalid in standard mathematical notation. The condition `if j > index and num[index] == '0': break` ensures `"0"` is only evaluated as a single-digit operand.
- **Operator Precedence in Linear Scans:** Evaluating `2 + 3 * 2` as $(2 + 3) \times 2 = 10$ is an arithmetic fallacy. Tracking `prev_term` allows constant-time local rollback without an explicit operand stack.
- **64-Bit Integer Overflow:** Although `target` fits in a 32-bit integer, intermediate products (e.g. $999999999 \times 999999999$) can exceed $2^{31} - 1$. Python handles arbitrary precision automatically; in C++ and Java, 64-bit `long long` / `long` is mandatory.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(4^N)$, where $N$ is the number of digits in `num`. At each of the $N - 1$ gaps between digits, there are 4 choices: insert nothing (extend operand), `+`, `-`, or `*`. There are at most $4^{N-1}$ generated expressions. Slicing and copying strings at each leaf adds an $O(N)$ factor, yielding $O(N \cdot 4^N)$ worst-case time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the recursion call stack and active string buffers.

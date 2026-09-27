# Guided Example: Basic Calculator II

We trace the step-by-step operator precedence decoupling, immediate multiplication/division reduction, and signed-term stack accumulation on representative arithmetic expressions:

- **Input:** $s = \text{"3+2*2"}$
- **Required output:** $7$ (High-precedence multiplication $2 \times 2 = 4$ evaluated before addition $3 + 4 = 7$)
- **Division Truncation Instance:** $s = \text{" 3/2 "} \implies 1$ (Truncation toward zero: $\lfloor 3 / 2 \rfloor = 1$)
- **Mixed Precedence with Spaces:** $s = \text{" 3+5 / 2 "} \implies 5$ (Evaluates $5 / 2 = 2$, then $3 + 2 = 5$)
- **Negative Division Truncation:** $s = \text{"14-3/2"} \implies 13$ ($-3 / 2 = -1$ truncated toward zero; $14 + (-1) = 13$)

This instance demonstrates linear-time multi-precedence arithmetic evaluation without parentheses, proves why delaying addition/subtraction onto a stack while immediately collapsing multiplication/division enforces standard order of operations, clarifies truncation toward zero for signed dividends, and operates in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given an expression string containing non-negative integers, addition, subtraction, multiplication, division, and spaces:
$$
s = \text{"3+2*2"}
$$
Compute its exact numerical value respecting standard operator precedence without using built-in evaluation tools (`eval`).

### The Precedence Hierarchy
In elementary arithmetic:
1. **Multiplication and Division (`*`, `/`)** have **higher precedence**: they must bind directly to their adjacent operands before addition or subtraction can occur.
2. **Addition and Subtraction (`+`, `-`)** have **lower precedence**: they partition the expression into independent additive terms.

In $s = \text{"3+2*2"}$:
- Evaluating left-to-right naively yields $(3 + 2) \times 2 = 5 \times 2 = 10$, which is **incorrect**.
- Proper precedence isolates term $1$ as $3$ and term $2$ as $2 \times 2 = 4$.
- The sum of terms is $3 + 4 = \mathbf{7}$.

By maintaining a **pending operator** (`pre_op`) and delaying addition/subtraction onto a stack while immediately resolving multiplication and division against the top of the stack, the entire expression evaluates in a single forward pass.

---

## 2. Conceptual Foundation & Invariants

### Stack Evaluation Protocol
Maintain:
- `stack = []`: accumulates terms ready to be summed at the end.
- `num = 0`: accumulates decimal digits of the active number.
- `pre_op = '+'`: the operator that immediately preceded the active number (initialized to `'+'` to handle the leading positive number).

Iterate through character $c$ at index $i$ from $0$ to $N - 1$:
1. **Digit Accumulation:**
   If $c$ is a digit:
   $$
   \text{num} \leftarrow \text{num} \cdot 10 + \text{int}(c)
   $$
2. **Operator or Terminal Boundary ($c \in \{+, -, *, /\}$ or $i == N - 1$):**
   *(Skip whitespace unless it is the terminal index)*.
   Apply the **preceding operator** `pre_op` to `num`:
   - **Case `'+'`:** Push positive term:
     $$
     \text{stack}.\text{append}(\text{num})
     $$
   - **Case `'-'`:** Push negative term:
     $$
     \text{stack}.\text{append}(-\text{num})
     $$
   - **Case `'*'`:** Pop top term, multiply, and push result:
     $$
     \text{stack}.\text{append}(\text{stack}.\text{pop}() \cdot \text{num})
     $$
   - **Case `'/'`:** Pop top term, perform integer division truncated toward zero, and push result:
     $$
     \text{stack}.\text{append}(\text{int}(\text{stack}.\text{pop}() / \text{num}))
     $$
   - Reset number: $\text{num} \leftarrow 0$.
   - Update pending operator: $\text{pre\_op} \leftarrow c$.

3. **Final Result:**
   $$
   \text{return } \sum \text{stack}
   $$

> **Invariant.** At any point, every element in `stack` is a fully reduced multiplicative/divisive term ready to be combined by linear addition.

---

## 3. Step-by-Step Worked Execution

We trace the single-pass evaluation on $s = \text{"3+2*2"}$ ($N = 5$):
- Initial state: $\text{stack} = [], \, \text{num} = 0, \, \text{pre\_op} = \text{'+'}$.

---

### Index 0: $c = \text{'3'}$
- Digit detected: $\text{num} = 0 \times 10 + 3 = 3$.
- Not an operator, not terminal index ($0 \ne 4$). Advance.

---

### Index 1: $c = \text{'+'}$ (Boundary Reached)
- Operator detected! Process $\text{num} = 3$ under $\text{pre\_op} = \text{'+'}$:
  $$
  \text{stack}.\text{append}(+3) \implies \text{stack} = [3]
  $$
- Reset $\text{num} = 0$.
- Update pending operator: $\text{pre\_op} \leftarrow \text{'+'}$.

---

### Index 2: $c = \text{'2'}$
- Digit detected: $\text{num} = 0 \times 10 + 2 = 2$.
- Advance.

---

### Index 3: $c = \text{'*'}$ (Boundary Reached)
- Operator detected! Process $\text{num} = 2$ under $\text{pre\_op} = \text{'+'}$:
  $$
  \text{stack}.\text{append}(+2) \implies \text{stack} = [3, 2]
  $$
- Reset $\text{num} = 0$.
- Update pending operator: $\text{pre\_op} \leftarrow \text{'*'}$.

---

### Index 4: $c = \text{'2'}$ (Terminal Index $i = 4 == N - 1$)
- Digit detected: $\text{num} = 0 \times 10 + 2 = 2$.
- Terminal boundary condition $i == N - 1$ triggered!
- Process $\text{num} = 2$ under pending operator $\text{pre\_op} = \text{'*' Tanto high precedence!}$:
  - Pop top of stack: $\text{top} = \text{stack}.\text{pop}() = 2$.
  - Evaluate product: $2 \times 2 = \mathbf{4}$.
  - Push product back:
    $$
    \text{stack}.\text{append}(4) \implies \text{stack} = [3, 4]
    $$
- Reset $\text{num} = 0$.

---

### Step 5: Final Summation
Loop terminates. All multiplications and divisions are resolved.
Sum the stack elements:
$$
\text{Total} = \sum [3, 4] = 3 + 4 = \mathbf{7}
$$

---

## 4. Complete Execution Trace

```text
Expression: "3+2*2"

i = 0: '3' -> num = 3
i = 1: '+' -> pre_op is '+' -> stack.append(3)   -> stack = [3],    pre_op = '+'
i = 2: '2' -> num = 2
i = 3: '*' -> pre_op is '+' -> stack.append(2)   -> stack = [3, 2], pre_op = '*'
i = 4: '2' -> num = 2 (terminal!)
           -> pre_op is '*' -> stack.pop() * 2 = 2 * 2 = 4
           -> stack.append(4)                    -> stack = [3, 4]

sum(stack) = 3 + 4 = 7
```

| Index $i$ | Character $c$ | Current `num` | Pending `pre_op` | Action Taken | Stack State After Step |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | `'3'` | 3 | `'+'` | Accumulate digit | `[]` |
| **1** | **`'+'`** | 0 | **`'+'`** | **`stack.append(3)`** | `[3]` |
| 2 | `'2'` | 2 | `'+'` | Accumulate digit | `[3]` |
| **3** | **`'*'`** | 0 | **`'*'`** | **`stack.append(2)`** | `[3, 2]` |
| **4** | **`'2'`** | 2 | **`'*'`** | **Pop 2, multiply $2 \times 2 = 4$, push 4** | **`[3, 4]` (Terminal)** |
| **End** | - | - | - | $\sum [3, 4] = 3 + 4$ | **$\mathbf{7}$ (Final Answer)** |

---

## 5. Algorithmic Correctness

**Soundness.** Since multiplication and division have higher precedence than addition and subtraction and associate left-to-right, evaluating each `*` and `/` immediately against the preceding operand strictly obeys the algebraic grammar $E \to T \pm T \pm \dots$, where each term $T$ is a chain of factors $F \times F \dots / F$. By storing terms as signed integers in `stack`, the final sum matches the standard mathematical value.

**Completeness.** Every character is processed. The terminal condition $i == N - 1$ ensures that the trailing number is applied to the stack under its governing operator, leaving no uncommitted operands.

---

## 6. Traps This Instance Exposes

- **Integer Division Truncation Toward Zero:** In Python, standard floor division `//` rounds toward $-\infty$ (e.g. `-3 // 2 = -2`), but C/C++ integer division truncates toward zero (e.g. `int(-3 / 2) = -1`). LeetCode 227 requires truncation toward zero, so `int(a / b)` or `math.trunc(a / b)` must be used instead of `a // b`.
- **Operator Processing Lag:** The operator encountered at index $i$ governs the *next* number, not the current one. Applying the current operator immediately causes incorrect evaluations (e.g. interpreting `3 + 2` as `+3`).
- **Whitespace Traps:** Spaces can appear anywhere (e.g. `" 3 / 2 "`). The algorithm must ignore spaces during digit accumulation and only trigger evaluation if a space happens to be at the terminal index $N - 1$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. The string is scanned in a single forward pass, performing $O(1)$ stack operations per token.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for `stack`, storing at most $N/2$ terms in expressions consisting solely of additions/subtractions. (Can be optimized to $O(1)$ auxiliary space using two scalar running variables `last_term` and `total_sum`).

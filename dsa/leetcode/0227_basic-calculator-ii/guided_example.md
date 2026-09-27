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
- Process $\text{num} = 2$ under pending operator $\text{pre\_op} = \text{'*'}$, the higher-precedence operator that governs this second factor:
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

### 4.1 The Same Scan Against a Spaced Expression

The main instance has no whitespace, so it never exercises the skip rule. Running
the identical protocol on $s = \text{" 3+5 / 2 "}$ ($N = 9$) shows what the
spaces do and, more importantly, what they must *not* do: a space is neither a
digit nor an operator, so it neither accumulates into `num` nor commits a term.

| Index $i$ | Character $c$ | `num` after the index | `pre_op` after the index | Term committed at this index | Stack afterwards |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | `' '` | 0 | `'+'` | none; whitespace is inert | `[]` |
| 1 | `'3'` | 3 | `'+'` | none | `[]` |
| 2 | `'+'` | 0 | `'+'` | `+3`, because the governing operator is the initial `'+'` | `[3]` |
| 3 | `'5'` | 5 | `'+'` | none | `[3]` |
| 4 | `' '` | 5 | `'+'` | none; a space must not reset `num` or alter `pre_op` | `[3]` |
| 5 | `'/'` | 0 | `'/'` | `+5`, the factor that the division will consume | `[3, 5]` |
| 6 | `' '` | 0 | `'/'` | none | `[3, 5]` |
| 7 | `'2'` | 2 | `'/'` | none | `[3, 5]` |
| 8 | `' '` (terminal, $i = N - 1$) | 0 | `' '` | pop 5, evaluate $5 / 2 = 2$, push 2 | `[3, 2]` |
| End | - | - | - | $\sum [3, 2] = 3 + 2$ | **$\mathbf{5}$** |

Two details in this trace are worth isolating. First, index 4 proves that a space
between a digit and an operator must leave `num` untouched; clearing `num` on
whitespace would silently discard the 5. Second, the terminal index 8 is a
space, not a digit, yet it still triggers the commit because the trigger is
$i = N - 1$ rather than "the character is an operator". That is why the trailing
space cannot strand the final number: the last uncommitted value is flushed by
position, and `pre_op` at that moment is still `'/'` from index 5.

### 4.2 Why Truncation Toward Zero Is Not Floor Division

The trial input $s = \text{"0-7/2+3*4"}$ expects $9$. Reaching it requires the
division to truncate the negative intermediate toward zero rather than downward,
which in turn depends on the sign of the term already sitting on the stack.

| Index $i$ | Character $c$ | `num` after the index | `pre_op` before the commit | Action on the stack | Stack afterwards |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | `'0'` | 0 | `'+'` | none | `[]` |
| 1 | `'-'` | 0 | `'+'` | push `+0` | `[0]` |
| 2 | `'7'` | 7 | `'-'` | none | `[0]` |
| 3 | `'/'` | 0 | `'-'` | push `-7`; the negative term now sits on top | `[0, -7]` |
| 4 | `'2'` | 2 | `'/'` | none | `[0, -7]` |
| 5 | `'+'` | 0 | `'/'` | pop `-7`, evaluate $-7 / 2$ truncated toward zero $= -3$, push `-3` | `[0, -3]` |
| 6 | `'3'` | 3 | `'+'` | none | `[0, -3]` |
| 7 | `'*'` | 0 | `'+'` | push `+3` | `[0, -3, 3]` |
| 8 | `'4'` (terminal) | 4 | `'*'` | pop 3, evaluate $3 \times 4 = 12$, push `12` | `[0, -3, 12]` |
| End | - | - | - | $\sum [0, -3, 12]$ | **$\mathbf{9}$** |

Had index 5 used floor division, the quotient would have been $-4$ instead of
$-3$, the final sum would have collapsed to $8$, and the submission would be
rejected on exactly this hidden case. Note also that the sign of the term pushed
at index 3 is what makes the quotient negative in the first place: the stack
stores signed terms, so the division sees `-7` and not `7`.

---

## 5. Algorithmic Correctness

**Soundness.** Since multiplication and division have higher precedence than addition and subtraction and associate left-to-right, evaluating each `*` and `/` immediately against the preceding operand strictly obeys the algebraic grammar $E \to T \pm T \pm \dots$, where each term $T$ is a chain of factors $F \times F \dots / F$. By storing terms as signed integers in `stack`, the final sum matches the standard mathematical value.

**Completeness.** Every character is processed. The terminal condition $i == N - 1$ ensures that the trailing number is applied to the stack under its governing operator, leaving no uncommitted operands.

---

## 6. Traps This Instance Exposes

- **Integer Division Truncation Toward Zero:** In Python, standard floor division `//` rounds toward $-\infty$ (e.g. `-3 // 2 = -2`), but C/C++ integer division truncates toward zero (e.g. `int(-3 / 2) = -1`). LeetCode 227 requires truncation toward zero, so `int(a / b)` or `math.trunc(a / b)` must be used instead of `a // b`.
- **Operator Processing Lag:** The operator encountered at index $i$ governs the *next* number, not the current one. Applying the current operator immediately causes incorrect evaluations (e.g. interpreting `3 + 2` as `+3`).
- **Whitespace Traps:** Spaces can appear anywhere (e.g. `" 3 / 2 "`). The algorithm must ignore spaces during digit accumulation and only trigger evaluation if a space happens to be at the terminal index $N - 1$.

### 6.1 The Two Division Roundings Side by Side

The stack holds signed terms, so the dividend passed to a division can be
negative even though every integer literal in the expression is non-negative.
The two candidate roundings agree on non-negative dividends and disagree
everywhere else, which is precisely where the trap bites.

| Dividend $a$ | Divisor $b$ | Truncation toward zero $\text{trunc}(a / b)$ | Floor $\lfloor a / b \rfloor$ | Do the two agree? |
|:---:|:---:|:---:|:---:|:---|
| 3 | 2 | 1 | 1 | Yes; the mandated sample `" 3/2 "` cannot detect the difference |
| 5 | 2 | 2 | 2 | Yes; `" 3+5 / 2 "` also passes under either rounding |
| -7 | 2 | -3 | -4 | No; this is the row exercised by `"0-7/2+3*4"` |
| -6 | 3 | -2 | -2 | Yes; an exact quotient hides the defect |
| -1 | 2 | 0 | -1 | No; the quotient is smaller than 1 in magnitude |
| -9 | 4 | -2 | -3 | No; a second non-exact negative case that a single spot check would miss |

The lesson is that a correct implementation cannot be confirmed with positive
dividends only. Two of the six rows above are non-exact negative divisions, and
an expression whose negative term divides exactly (row four) still passes,
which is why the failure mode survives casual testing and appears only on a
hidden case such as `"0-7/2+3*4"`.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. The string is scanned in a single forward pass, performing $O(1)$ stack operations per token.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for `stack`, storing at most $N/2$ terms in expressions consisting solely of additions/subtractions. (Can be optimized to $O(1)$ auxiliary space using two scalar running variables `last_term` and `total_sum`).

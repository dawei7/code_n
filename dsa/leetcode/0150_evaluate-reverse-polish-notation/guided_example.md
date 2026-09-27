# Guided Example: Evaluate Reverse Polish Notation

We trace the step-by-step operand stack evaluation and toward-zero truncated integer division on representative Reverse Polish Notation (RPN) expressions:

- **Input:** $\text{tokens} = [\text{"2"}, \text{"1"}, \text{"+"}, \text{"3"}, \text{"*"}] \implies ((2 + 1) \times 3) = 9$
- **Compound Division & Negative Truncation Instance:** $\text{tokens} = [\text{"4"}, \text{"13"}, \text{"5"}, \text{"/"}, \text{"+"}] \implies 4 + \lfloor 13 / 5 \rfloor = 4 + 2 = 6$
- **Negative Floor Trap Instance:** $\text{tokens} = [\text{"6"}, \text{"-132"}, \text{"/"}] \implies 0$ ($\text{trunc}(6 / -132) = 0$, distinct from Python floor `//` which yields $-1$)

This instance demonstrates LIFO stack evaluation for postfix arithmetic, enforces strict left-versus-right operand ordering ($a - b$ and $a / b$ where right operand is popped first), explains truncation toward zero for negative quotients, and executes in linear $O(N)$ time and $O(N)$ stack space.

---

## 1. Instance & Teaching Goal

Given an array of strings `tokens` representing an arithmetic expression in **Reverse Polish Notation** (postfix notation):
$$
\text{tokens} = [\text{"2"}, \text{"1"}, \text{"+"}, \text{"3"}, \text{"*"}]
$$
Evaluate the expression and return the resulting integer.

In Reverse Polish Notation:
- Operands precede their operators: no parentheses or operator precedence rules are needed.
- Subexpression `["2", "1", "+"]` evaluates immediately to $2 + 1 = 3$.
- Next subexpression `[3, "3", "*"]` evaluates to $3 \times 3 = 9$.
Output: $9$.

A recursive syntax-tree parser introduces extra overhead.
A single LIFO operand stack provides the optimal execution model:
1. When encountering a number token, convert it to an integer and push it onto the stack.
2. When encountering an operator, pop the **right operand** $b$, pop the **left operand** $a$, apply the operation $a \star b$, and push the result back onto the stack.
3. Division between two integers must strictly **truncate toward zero** (e.g. $6 / (-132) = 0$, not $-1$).

---

## 2. Conceptual Foundation & Invariants

### The LIFO Postfix Evaluation Protocol
Initialize an empty stack `stack = []`.
Define valid operators: $\{ \text{'+'}, \text{'-'}, \text{'*'}, \text{'/'} \}$.

For each `token` in `tokens`:
1. **If `token` is an operator:**
   Pop the right operand first:
   $$
   b = \text{stack.pop()}
   $$
   Pop the left operand second:
   $$
   a = \text{stack.pop()}
   $$
   Apply operation $a \star b$:
   - Addition: $a + b$
   - Subtraction: $a - b$ *(order-sensitive!)*
   - Multiplication: $a \times b$
   - Division: $\text{int}(a / b)$ *(truncation toward zero)*
   Push result back:
   $$
   \text{stack.append}(\text{result})
   $$
2. **If `token` is an operand:**
   Parse signed integer and push:
   $$
   \text{stack.append}(\text{int}(\text{token}))
   $$

At expression end, `stack` contains exactly one value: $\text{stack}[0]$.

> **Invariant.** After processing any token, `stack` stores the exact evaluated scalar values of all completed, unconsumed subexpressions in left-to-right order.

---

## 3. Step-by-Step Worked Execution

We trace $\text{tokens} = [\text{"4"}, \text{"13"}, \text{"5"}, \text{"/"}, \text{"+"}]$:

### Step 1: Token `"4"`
- Operand detected.
- Push: `stack = [4]`.

---

### Step 2: Token `"13"`
- Operand detected.
- Push: `stack = [4, 13]`.

---

### Step 3: Token `"5"`
- Operand detected.
- Push: `stack = [4, 13, 5]`.

---

### Step 4: Operator `"/"`
- Pop right operand: $b = 5$.
- Pop left operand: $a = 13$.
- Compute division truncated toward zero:
  $$
  \text{int}\left(\frac{13}{5}\right) = \text{int}(2.6) = \mathbf{2}
  $$
- Push result: `stack = [4, 2]`.

---

### Step 5: Operator `"+"`
- Pop right operand: $b = 2$.
- Pop left operand: $a = 4$.
- Compute addition:
  $$
  a + b = 4 + 2 = \mathbf{6}
  $$
- Push result: `stack = [6]`.

All tokens consumed.
Return top of stack: $\mathbf{6}$.

---

## 4. Complete Execution Trace

```text
Tokens:      "4"     "13"      "5"         "/"          "+"
Stack:       [4]   [4, 13]  [4, 13, 5]   [4, 2]         [6]
                                      (13 / 5 = 2)   (4 + 2 = 6)
Final Result: 6
```

| Token Index | Token | Token Type | Operands Popped ($a, b$) | Operation Evaluated | Stack After Operation |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | `"4"` | Operand | - | Parse integer $4$ | `[4]` |
| 1 | `"13"` | Operand | - | Parse integer $13$ | `[4, 13]` |
| 2 | `"5"` | Operand | - | Parse integer $5$ | `[4, 13, 5]` |
| **3** | **`"/"`** | **Operator** | **$a=13, \, b=5$** | **$\text{int}(13 / 5) = 2$** | **`[4, 2]`** |
| **4** | **`"+"`** | **Operator** | **$a=4, \, b=2$** | **$4 + 2 = 6$** | **`[6]` (Result)** |

---

## 5. Algorithmic Correctness

**Soundness.** In postfix notation, every operator immediately follows its two operands. The LIFO property of the stack ensures that the two operands available on top of the stack correspond precisely to the left and right inputs of that operator. By replacing them with their evaluated scalar value, the remaining postfix expression is structurally reduced without changing the value of the overall arithmetic expression.

**Completeness.** Since the input expression is guaranteed to be valid, every operator encounters at least two operands on the stack, and exactly one single scalar remains upon exhausting all tokens.

---

## 6. Traps This Instance Exposes

- **Operand Order Asymmetry ($a - b$ vs $b - a$):** Because the stack pops in reverse order, the first popped value is the **right operand** ($b$) and the second popped value is the **left operand** ($a$). Calculating $b - a$ or $b / a$ produces completely incorrect signs and fractions!
- **Python Floor Division Trap (`//` vs `int(a / b)`):** In Python, `-3 // 2 = -2` (floor toward negative infinity). But the problem requires **truncation toward zero**: $\text{trunc}(-1.5) = -1$! Using `int(a / b)` correctly truncates toward zero for both positive and negative results.
- **Negative Integer Tokens:** A token like `"-11"` is a negative number, not the subtraction operator `"-"`! Checking `if token in {"+", "-", "*", "/"}:` prevents misinterpreting negative numerals as operators.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of tokens. Each token is scanned once, performing an $O(1)$ push, pop, or basic arithmetic operation.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the operand stack, which holds at most $\lceil N/2 \rceil$ integers simultaneously.

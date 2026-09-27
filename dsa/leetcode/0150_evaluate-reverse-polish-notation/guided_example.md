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

The package also carries a longer mixed expression whose value is $22$:
$$
\text{tokens} = [\text{"10"}, \text{"6"}, \text{"9"}, \text{"3"}, \text{"+"}, \text{"-11"}, \text{"*"}, \text{"/"}, \text{"*"}, \text{"17"}, \text{"+"}, \text{"5"}, \text{"+"}]
$$
Tracing it token by token shows the same protocol surviving a negative operand, a negative product, and a negative intermediate quotient:

| Token Index | Token | Kind | Operands popped $(a, b)$ | Evaluation | Stack Afterwards |
|:---:|:---:|:---:|:---:|:---|:---|
| 0 | `"10"` | Operand | - | Parse integer $10$ | `[10]` |
| 1 | `"6"` | Operand | - | Parse integer $6$ | `[10, 6]` |
| 2 | `"9"` | Operand | - | Parse integer $9$ | `[10, 6, 9]` |
| 3 | `"3"` | Operand | - | Parse integer $3$ | `[10, 6, 9, 3]` |
| 4 | `"+"` | Operator | $a=9, \, b=3$ | $9 + 3 = 12$ | `[10, 6, 12]` |
| 5 | `"-11"` | Operand | - | Parse integer $-11$, not the subtraction operator | `[10, 6, 12, -11]` |
| 6 | `"*"` | Operator | $a=12, \, b=-11$ | $12 \times (-11) = -132$ | `[10, 6, -132]` |
| 7 | `"/"` | Operator | $a=6, \, b=-132$ | $\text{trunc}(6 / (-132)) = 0$ | `[10, 0]` |
| 8 | `"*"` | Operator | $a=10, \, b=0$ | $10 \times 0 = 0$ | `[0]` |
| 9 | `"17"` | Operand | - | Parse integer $17$ | `[0, 17]` |
| 10 | `"+"` | Operator | $a=0, \, b=17$ | $0 + 17 = 17$ | `[17]` |
| 11 | `"5"` | Operand | - | Parse integer $5$ | `[17, 5]` |
| 12 | `"+"` | Operator | $a=17, \, b=5$ | $17 + 5 = 22$ | `[22]` (Result) |

Index 7 is the decisive row: without truncation toward zero the intermediate value would be $-1$, and the final $*$ and $+$ operations would propagate that error all the way to the wrong answer.

---

## 5. Algorithmic Correctness

**Soundness.** In postfix notation, every operator immediately follows its two operands. The LIFO property of the stack ensures that the two operands available on top of the stack correspond precisely to the left and right inputs of that operator. By replacing them with their evaluated scalar value, the remaining postfix expression is structurally reduced without changing the value of the overall arithmetic expression.

**Completeness.** Since the input expression is guaranteed to be valid, every operator encounters at least two operands on the stack, and exactly one single scalar remains upon exhausting all tokens.

---

## 6. Traps This Instance Exposes

- **Operand Order Asymmetry ($a - b$ vs $b - a$):** Because the stack pops in reverse order, the first popped value is the **right operand** ($b$) and the second popped value is the **left operand** ($a$). Calculating $b - a$ or $b / a$ produces completely incorrect signs and fractions!
- **Python Floor Division Trap (`//` vs `int(a / b)`):** In Python, `-3 // 2 = -2` (floor toward negative infinity). But the problem requires **truncation toward zero**: $\text{trunc}(-1.5) = -1$! Using `int(a / b)` correctly truncates toward zero for both positive and negative results.
- **Negative Integer Tokens:** A token like `"-11"` is a negative number, not the subtraction operator `"-"`! Checking `if token in {"+", "-", "*", "/"}:` prevents misinterpreting negative numerals as operators.

Writing each quotient with its exact rational value separates the required rule from the floor rule that Python's `//` implements:

| Quotient | Exact rational value | Required result, truncated toward zero | Floor result | Where the two rules disagree |
|:---:|:---:|:---:|:---:|:---|
| $13 / 5$ | $2.6$ | $2$ | $2$ | They agree whenever the quotient is non-negative, which is why the trap hides until a negative appears |
| $7 / (-3)$ | $-2.333\ldots$ | $-2$ | $-3$ | On a negative quotient, truncation moves toward $0$ while the floor moves further from it |
| $(-7) / 3$ | $-2.333\ldots$ | $-2$ | $-3$ | Moving the sign to the numerator or the denominator changes nothing: the required rule discards the fractional part of the magnitude |
| $6 / (-132)$ | $-0.045\ldots$ | $0$ | $-1$ | The true quotient lies strictly between $-1$ and $0$, so truncation returns the signed zero $0$ while the floor returns $-1$ |

The second row is the package case `["7", "-3", "/"]`, whose required answer is $-2$, and the fourth is the instance in the header: reading either one through a floor rule yields the wrong value rather than merely a different formatting of the same answer.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of tokens. Each token is scanned once, performing an $O(1)$ push, pop, or basic arithmetic operation.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for the operand stack, which holds at most $\lceil N/2 \rceil$ integers simultaneously.

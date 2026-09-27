# Guided Example: Basic Calculator

We trace the step-by-step operand accumulation, signed term reduction, and stack-driven nested parenthesis unwinding on representative arithmetic expressions:

- **Input:** $s = \text{"(1+(4+5+2)-3)+(6+8)"}$
- **Required output:** $23$
- **Unary Minus Instance:** $s = \text{"- (3 + (4 - 5))"} \implies -2$
- **Whitespace Separation Instance:** $s = \text{" 2-1 + 2 "} \implies 3$
- **Multi-Digit Number Instance:** $s = \text{"2147483647"} \implies 2147483647$

This instance demonstrates linear-time arithmetic expression evaluation without full operator precedence trees, models addition and subtraction as signed scalar accumulations ($\text{ans} \mathrel{+}= \text{sign} \cdot \text{num}$), handles nested parenthetical scope via an $( \text{ans}, \text{sign} )$ call stack, and runs in strictly $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given an arithmetic string with nested parentheses, addition, and subtraction:
$$
s = \text{"(1+(4+5+2)-3)+(6+8)"}
$$
Evaluate the mathematical result without using built-in expression parsers (such as `eval`).

Evaluating the mathematical groupings:
1. Innermost parenthesis: $(4 + 5 + 2) = 11$.
2. Outer first group: $(1 + 11 - 3) = 9$.
3. Second group: $(6 + 8) = 14$.
4. Combine groups: $9 + 14 = \mathbf{23}$.

Because the expression contains only `+` and `-` (operations with equal precedence):
- No operator priority stack (like Dijkstra's Shunting-Yard) is necessary.
- Every term simply carries an effective sign ($+1$ or $-1$).
- When entering an opening parenthesis `(`, the surrounding running sum and sign are pushed onto a stack, resetting the local context.
- When closing a parenthesis `)`, the completed sub-expression is multiplied by the saved sign and added to the saved outer total.

---

## 2. Conceptual Foundation & Invariants

### State Variables
- `ans`: the evaluated result of the current parenthetical scope.
- `sign`: $+1$ for addition, $-1$ for subtraction (applied to the next operand).
- `num`: the integer currently being parsed across consecutive digits.
- `stack`: stores previous $( \text{outer\_ans}, \text{outer\_sign} )$ pairs upon encountering `(`.

### Transition Protocol:
1. **Digit ($'0' \dots '9'$):**
   $$
   \text{num} \leftarrow \text{num} \cdot 10 + \text{int}(c)
   $$
2. **Operator `+`:**
   $$
   \text{ans} \leftarrow \text{ans} + \text{sign} \cdot \text{num}, \quad \text{num} \leftarrow 0, \quad \text{sign} \leftarrow +1
   $$
3. **Operator `-`:**
   $$
   \text{ans} \leftarrow \text{ans} + \text{sign} \cdot \text{num}, \quad \text{num} \leftarrow 0, \quad \text{sign} \leftarrow -1
   $$
4. **Opening Parenthesis `(`:**
   Push outer state, then reset local frame:
   $$
   \text{stack}.\text{append}(\text{ans}), \quad \text{stack}.\text{append}(\text{sign})
   $$
   $$
   \text{ans} \leftarrow 0, \quad \text{sign} \leftarrow +1
   $$
5. **Closing Parenthesis `)`:**
   Complete local sum: $\text{ans} \leftarrow \text{ans} + \text{sign} \cdot \text{num}, \quad \text{num} \leftarrow 0$.
   Pop outer sign and outer answer:
   $$
   \text{prev\_sign} = \text{stack}.\text{pop}()
   $$
   $$
   \text{prev\_ans} = \text{stack}.\text{pop}()
   $$
   Combine:
   $$
   \text{ans} \leftarrow \text{prev\_ans} + \text{prev\_sign} \cdot \text{ans}
   $$

> **Invariant.** At any point inside a parenthetical level, `ans` represents the exact sum of all fully evaluated terms at that level, and `sign` holds the algebraic sign for the pending operand.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"(1+(4+5+2)-3)+(6+8)"}$:
Initial state: $\text{ans} = 0, \, \text{sign} = 1, \, \text{num} = 0, \, \text{stack} = []$.

### Group 1 Evaluation:
- Char `(`: Push $\text{ans} = 0$, push $\text{sign} = 1 \implies \text{stack} = [0, 1]$. Reset $\text{ans} = 0, \text{sign} = 1$.
- Char `'1'`: $\text{num} = 1$.
- Char `+`: $\text{ans} = 0 + 1 \times 1 = 1$. $\text{num} = 0, \text{sign} = 1$.
- Char `(` (Nested):
  - Push $\text{ans} = 1$, push $\text{sign} = 1 \implies \text{stack} = [0, 1, 1, 1]$.
  - Reset $\text{ans} = 0, \text{sign} = 1$.
- Inner Group: `4 + 5 + 2`:
  - `'4'`: $\text{num} = 4$.
  - `+`: $\text{ans} = 4, \text{num} = 0, \text{sign} = 1$.
  - `'5'`: $\text{num} = 5$.
  - `+`: $\text{ans} = 4 + 5 = 9, \text{num} = 0, \text{sign} = 1$.
  - `'2'`: $\text{num} = 2$.
- Char `)` (End of Inner Group):
  - Finish inner sum: $\text{ans} = 9 + 1 \times 2 = \mathbf{11}$. $\text{num} = 0$.
  - Pop $\text{prev\_sign} = 1$, pop $\text{prev\_ans} = 1$.
  - $\text{ans} = 1 + 1 \times 11 = \mathbf{12}$.
  - Stack restored to $[0, 1]$.
- Char `-`: $\text{sign} = -1$.
- Char `'3'`: $\text{num} = 3$.
- Char `)` (End of Group 1):
  - Finish group sum: $\text{ans} = 12 + (-1) \times 3 = \mathbf{9}$. $\text{num} = 0$.
  - Pop $\text{prev\_sign} = 1$, pop $\text{prev\_ans} = 0$.
  - $\text{ans} = 0 + 1 \times 9 = \mathbf{9}$.
  - Stack is now empty: `[]`.

---

### Intermediate Operator:
- Char `+`: $\text{ans} = 9$, $\text{sign} = 1$.

---

### Group 2 Evaluation: `+(6+8)`
- Char `(`: Push $\text{ans} = 9$, push $\text{sign} = 1 \implies \text{stack} = [9, 1]$. Reset $\text{ans} = 0, \text{sign} = 1$.
- Char `'6'`: $\text{num} = 6$.
- Char `+`: $\text{ans} = 6, \text{num} = 0, \text{sign} = 1$.
- Char `'8'`: $\text{num} = 8$.
- Char `)`:
  - Finish sum: $\text{ans} = 6 + 1 \times 8 = \mathbf{14}$. $\text{num} = 0$.
  - Pop $\text{prev\_sign} = 1$, pop $\text{prev\_ans} = 9$.
  - $\text{ans} = 9 + 1 \times 14 = \mathbf{23}$.
  - Stack is empty: `[]`.

Expression ends. Final result: $\mathbf{23}$.

---

## 4. Complete Execution Trace

```text
Expression: (1 + (4 + 5 + 2) - 3) + (6 + 8)

Scope Level 1: (1 + ...)
  Scope Level 2: (4 + 5 + 2) = 11
  Fold Level 2 into Level 1: 1 + 11 = 12
  Level 1 continues: 12 - 3 = 9
Fold Level 1 into Global: 0 + 9 = 9

Scope Level 1: +(6 + 8) = 14
Fold Level 1 into Global: 9 + 14 = 23

Final Answer: 23
```

| Token / Char | Action Taken | Local `ans` | Pending `sign` | Active `num` | Stack Content |
|:---:|:---|:---:|:---:|:---:|:---|
| `(` | Push 0, 1 | 0 | 1 | 0 | `[0, 1]` |
| `1` | Parse digit | 0 | 1 | 1 | `[0, 1]` |
| `+` | Add term: $0 + 1 \times 1$ | 1 | 1 | 0 | `[0, 1]` |
| `(` | Push 1, 1 | 0 | 1 | 0 | `[0, 1, 1, 1]` |
| `4 + 5 + 2` | Evaluate inner terms | 9 | 1 | 2 | `[0, 1, 1, 1]` |
| `)` | Complete inner ($11$), fold: $1 + 1 \times 11$ | 12 | 1 | 0 | `[0, 1]` |
| `-` | Set negative sign | 12 | -1 | 0 | `[0, 1]` |
| `3` | Parse digit | 12 | -1 | 3 | `[0, 1]` |
| `)` | Complete group ($9$), fold: $0 + 1 \times 9$ | 9 | 1 | 0 | `[]` |
| `+` | Set positive sign | 9 | 1 | 0 | `[]` |
| `(` | Push 9, 1 | 0 | 1 | 0 | `[9, 1]` |
| `6 + 8` | Evaluate terms | 6 | 1 | 8 | `[9, 1]` |
| **`)`** | **Complete group ($14$), fold: $9 + 1 \times 14$** | **23** | **1** | **0** | **`[]` (Finished: 23)** |

---

## 5. Algorithmic Correctness

**Soundness.** Since arithmetic addition and subtraction are associative and distributive over parentheses, $A - (B + C) \equiv A + (-1) \cdot B + (-1) \cdot C$. Storing the surrounding sign on the stack and multiplying the entire parenthetical result upon closing correctly distributes negation across all nested subterms.

**Completeness.** Every character in the string is processed exactly once. Balanced parentheses guarantee that every pushed context is popped at the corresponding `)`, leaving the stack empty at termination with the full scalar answer in `ans`.

---

## 6. Traps This Instance Exposes

- **Leading Unary Minus:** For expressions like `"- (3 + 4)"`, `ans` starts at $0$. Encountering `-` sets `sign = -1`. The parenthesized group evaluates to $7$, and the final fold computes $0 + (-1) \times 7 = -7$, naturally supporting unary signs without extra parser rules.
- **Multi-Digit Numbers:** Scanning characters individually requires shifting previous digits (`num * 10 + int(c)`). Forgetting to reset `num = 0` after applying an operator causes digits to bleed into subsequent numbers.
- **Trailing Unapplied Number:** Expressions like `"1 + 2"` have no closing parenthesis at the end. An explicit final accumulation `ans += sign * num` after the loop is required.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. The string is scanned in a single forward pass, with each character triggering $O(1)$ stack operations or arithmetic updates.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the stack, proportional to the maximum nesting depth of parentheses (at most $N/2$).

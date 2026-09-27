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

The same execution, organised by scope instead of by character, makes the stack contract explicit. The string is indexed from $0$, so the left group opens at index $0$, the inner group at index $3$, and the right group at index $14$.

| Scope | Opened at index | Frame pushed $(\text{prev\_ans}, \text{prev\_sign})$ | Expression evaluated locally | Local value | Fold applied on the closing `)` | Stack after closing |
|:---|:---:|:---|:---|:---:|:---|:---|
| Global frame (never pushed) | - | - | $9$ then $+\,14$ across the two top-level groups | - | The final value $23$ lives here | `[]` |
| Outer left group | 0 | $(0, 1)$ | `1+(4+5+2)-3` | $1 + 11 - 3 = 9$ | $0 + 1 \times 9 = 9$ | `[]` |
| Inner group | 3 | $(1, 1)$ | `4+5+2` | $4 + 5 + 2 = 11$ | $1 + 1 \times 11 = 12$ | `[0, 1]` |
| Outer right group | 14 | $(9, 1)$ | `6+8` | $6 + 8 = 14$ | $9 + 1 \times 14 = 23$ | `[]` |

Each `(` writes two entries — the running total first, then the sign — so each `)` must pop them in the opposite order: the sign is on top. The stack depth never exceeds twice the nesting depth, and the frame at index $3$ is the only one that closes while another frame is still suspended, which is why `[0, 1]` is still present after the inner fold.

---

## 5. Algorithmic Correctness

**Soundness.** Since arithmetic addition and subtraction are associative and distributive over parentheses, $A - (B + C) \equiv A + (-1) \cdot B + (-1) \cdot C$. Storing the surrounding sign on the stack and multiplying the entire parenthetical result upon closing correctly distributes negation across all nested subterms.

**Completeness.** Every character in the string is processed exactly once. Balanced parentheses guarantee that every pushed context is popped at the corresponding `)`, leaving the stack empty at termination with the full scalar answer in `ans`.

**Input boundaries, and the exact path through the machine.** Each row below is a package case, and the third column names the mechanism that produces its answer — which for several of them is the trailing accumulation rather than any operator.

| Expression | Answer | Path through the machine | Why it is a boundary worth checking |
|:---|:---:|:---|:---|
| `"1"` | 1 | The single digit leaves $\text{num} = 1$; no operator ever fires, so only the final flush $\text{ans} \mathrel{+}= \text{sign} \cdot \text{num}$ produces the answer | The shortest legal input, and the one that fails if the trailing flush is omitted |
| `"111"` | 111 | Digits accumulate as $1 \to 11 \to 111$ and no operator interrupts them | Multi-digit parsing: the value must survive an arbitrary run of digits without a flush between them |
| `"1 + 1"` | 2 | `1` parses, `+` flushes $\text{ans} = 1$ and resets, the second `1` remains pending, and the trailing flush adds it | The last operand is never followed by an operator, so this case returns 1 instead of 2 if the post-loop accumulation is missing |
| `"-2 + 1"` | $-1$ | The leading `-` sets $\text{sign} = -1$ while $\text{ans}$ is still $0$; the `+` then flushes $0 + (-1) \times 2 = -2$ and resets the sign to $+1$; the trailing flush adds 1 | Unary minus needs no special rule: it is the ordinary binary operator applied to a zero accumulator |
| `"1-(-2+3)"` | 0 | `1` and `-` set $\text{ans} = 1$ with $\text{sign} = -1$; the `(` pushes the frame $(1, -1)$; the inner frame evaluates $-2 + 3 = 1$; the fold is $1 + (-1) \times 1 = 0$ | The suspended sign is negative, so the whole group is negated. Dropping the sign multiplier would yield $1 + 1 = 2$ |
| `" 2-1 + 2 "` | 3 | Spaces are skipped wherever they appear, including both ends, so the machine reads $2 - 1 + 2$ | Whitespace must not act as a terminator; treating it as one would require an extra state for no benefit |
| `"2147483647"` | 2147483647 | Ten digits accumulate into the largest signed 32-bit value | The largest permitted number must pass through the digit accumulation unchanged |

---

## 6. Traps This Instance Exposes

- **Leading Unary Minus:** For expressions like `"- (3 + 4)"`, `ans` starts at $0$. Encountering `-` sets `sign = -1`. The parenthesized group evaluates to $7$, and the final fold computes $0 + (-1) \times 7 = -7$, naturally supporting unary signs without extra parser rules.
- **Multi-Digit Numbers:** Scanning characters individually requires shifting previous digits (`num * 10 + int(c)`). Forgetting to reset `num = 0` after applying an operator causes digits to bleed into subsequent numbers.
- **Trailing Unapplied Number:** Expressions like `"1 + 2"` have no closing parenthesis at the end. An explicit final accumulation `ans += sign * num` after the loop is required.

**Alternative formulations, and the risk each one carries.** All four methods return $23$ on the traced expression; they differ in how much grammar machinery they bring and in what limits them at the maximum input length.

| Approach | Mechanism | Time | Auxiliary space | Failure mode or tradeoff |
|:---|:---|:---:|:---:|:---|
| Single-pass sign-stack accumulation (this lesson) | Carry one running total, one pending sign and one pending number, and push $( \text{ans}, \text{sign} )$ at every `(` | $O(N)$ | $O(\text{nesting depth})$, at most $N/2$ | Depends on two details: the trailing flush after the loop, and popping the sign before the total. It also relies on `+` and `-` sharing a single precedence level, which holds for this contract |
| Recursive descent parser | One routine per grammar level; on `(` recurse and resume after the matching `)` | $O(N)$ | $O(\text{nesting depth})$ call frames | Identical asymptotics, but a maximally nested input of length $3 \times 10^5$ can nest about $150{,}000$ deep, which overruns the default interpreter recursion limit and must be rewritten with an explicit stack |
| Shunting-yard with operand and operator stacks | Push operators and apply precedence when popping | $O(N)$ | $O(N)$ | Built for general precedence, which this grammar never uses, and it still needs an explicit rule for the unary minus that the sign-stack method absorbs automatically |
| Two-pass sign propagation | First pass computes an effective sign at every position from a stack of signs; second pass accumulates each number times its sign | $O(N)$ | $O(\text{nesting depth})$, or $O(N)$ if the signs are stored | Cleaner separation of sign logic from digit scanning, at the cost of a second traversal or an extra array; the unary case becomes explicit rather than implicit |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of string $s$. The string is scanned in a single forward pass, with each character triggering $O(1)$ stack operations or arithmetic updates.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary space for the stack, proportional to the maximum nesting depth of parentheses (at most $N/2$).

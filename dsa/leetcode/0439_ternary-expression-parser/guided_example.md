# Guided Example: Ternary Expression Parser

We trace the step-by-step right-to-left stack reduction, right-associativity resolution, boolean condition resolution (`?`), operand pair collapsing (`val1 : val2`), and nested expression simplification on representative ternary strings:

- **Input:** $expression = \text{"F?1:T?4:5"}$
- **Required output:** `"4"`
  - Right-associative parsing structure:
    $$
    \text{"F ? 1 : (T ? 4 : 5)"}
    $$
  - Scanning string from right to left:
    - Char `'5'`: Push onto stack $\implies stk = [\text{'5'}]$
    - Char `':'`: Separator $\implies$ Skip
    - Char `'4'`: Push onto stack $\implies stk = [\text{'5'}, \text{'4'}]$
    - Char `'?'`: Operator encountered $\implies$ Condition flag primed
    - Char `'T'`: Condition is `'T'`.
      - Pop $v_1 = \text{'4'}$ (true branch) and $v_2 = \text{'5'}$ (false branch)
      - Condition is `'T'` $\implies$ Keep $v_1 = \text{'4'}$, discard $v_2$
      - Push `'4'` back onto stack $\implies stk = [\text{'4'}]$
      - Reset condition flag
    - Char `':'`: Separator $\implies$ Skip
    - Char `'1'`: Push onto stack $\implies stk = [\text{'4'}, \text{'1'}]$
    - Char `'?'`: Operator encountered $\implies$ Condition flag primed
    - Char `'F'`: Condition is `'F'`.
      - Pop $v_1 = \text{'1'}$ (true branch) and $v_2 = \text{'4'}$ (false branch)
      - Condition is `'F'` $\implies$ Discard $v_1$, keep $v_2 = \text{'4'}$
      - Push `'4'` back onto stack $\implies stk = [\text{'4'}]$
      - Reset condition flag
  - Traversal finishes:
    - Final element remaining in stack: **`"4"`**
- **Nested True Branch Instance:** $expression = \text{"T?T?F:5:3"} \implies \text{T ? (T ? F : 5) : 3} \implies \mathbf{\text{"F"}}$
- **Single Expression Instance:** $expression = \text{"T?2:3"} \implies \mathbf{\text{"2"}}$

This instance demonstrates right-to-left operator precedence stack parsing, mathematically proves why right-associativity is evaluated without recursion or parentheses matching, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $expression = \text{"F?1:T?4:5"}$ representing arbitrarily nested ternary expressions:
Evaluate the expression and return the resulting single character value.
- Each ternary expression has the form `condition ? value1 : value2`.
- `condition` is either `'T'` (true) or `'F'` (false).
- Ternary expressions are **right-associative**, meaning inner sub-expressions on the right are evaluated before outer expressions on the left:

```text
Expression:  F ? 1 : T ? 4 : 5

Associative Grouping (Right-to-Left):
  F ? 1 : (T ? 4 : 5)
           \_______/
           Evaluates to 4

Becomes:
  F ? 1 : 4
  \_______/
  Evaluates to 4
```

### The Right-Associative Inversion Insight
- In standard left-to-right parsing, encountering `?` requires deferring the condition while searching forward for the matching `:` among potentially dozens of nested colons.
- **The Right-to-Left Inversion:** When scanning backwards from the end of the string, the two candidate branch operands (`value1` and `value2`) are already on top of the stack by the time the `?` and its preceding condition character are reached!
- Every ternary operation can therefore be collapsed immediately in $O(1)$ operations as soon as its `?` is encountered.

---

## 2. Conceptual Foundation & Invariants

### 1. The Right-to-Left Stack Rules:
Scan characters $c$ of $expression$ in reverse from index $N-1$ down to $0$:
1. If $c == \text{':'}$: Skip (it acts merely as an operand separator).
2. If $c == \text{'?'}$: Set boolean flag `cond_pending = True`.
3. If $c$ is a regular literal (`'0' \dots '9'`, `'T'`, `'F'`):
   - If `cond_pending` is `False`:
     - Push $c$ onto the stack: $stk.\text{append}(c)$.
   - If `cond_pending` is `True`:
     - $c$ is the condition governing the most recent `?`.
     - Pop true branch value: $v_1 = stk.\text{pop}()$.
     - Pop false branch value: $v_2 = stk.\text{pop}()$.
     - If $c == \text{'T'}$: push $v_1$ back onto $stk$.
     - If $c == \text{'F'}$: push $v_2$ back onto $stk$.
     - Reset `cond_pending = False`.

> **Associativity Invariant.** Because inner sub-expressions appear to the right of outer conditions, scanning from right to left reduces every innermost ternary subsegment to its atomic value before its containing parent expression evaluates its condition.

---

## 3. Step-by-Step Worked Execution

We trace $expression = \text{"F?1:T?4:5"}$:

---

### Step 1: Push Terminal False Branch
- Char: `'5'`.
- `cond_pending` is `False`.
- Push `'5'` $\implies stk = [\text{'5'}]$.

---

### Step 2: Skip Separator
- Char: `':'`.
- Skip separator. Stack remains: $[\text{'5'}]$.

---

### Step 3: Push True Branch of Inner Expression
- Char: `'4'`.
- `cond_pending` is `False`.
- Push `'4'` $\implies stk = [\text{'5'}, \text{'4'}]$.
- Note: Top of stack is $v_1 = \text{'4'}$, second is $v_2 = \text{'5'}$.

---

### Step 4: Prime Condition Flag
- Char: `'?'`.
- Set `cond_pending = True`.

---

### Step 5: Evaluate Inner Condition
- Char: `'T'`.
- `cond_pending` is `True`.
- Pop $v_1 = stk.\text{pop}() = \text{'4'}$ (true branch).
- Pop $v_2 = stk.\text{pop}() = \text{'5'}$ (false branch).
- Condition is `'T'` $\implies$ Select $v_1 = \text{'4'}$.
- Push `'4'` $\implies stk = [\text{'4'}]$.
- Reset `cond_pending = False`.
- Inner expression `T?4:5` has collapsed to `'4'`.

---

### Step 6: Skip Separator
- Char: `':'`.
- Skip separator. Stack: $[\text{'4'}]$.

---

### Step 7: Push True Branch of Outer Expression
- Char: `'1'`.
- Push `'1'` $\implies stk = [\text{'4'}, \text{'1'}]$.
- Top is $v_1 = \text{'1'}$, second is $v_2 = \text{'4'}$.

---

### Step 8: Prime Condition Flag
- Char: `'?'`.
- Set `cond_pending = True`.

---

### Step 9: Evaluate Outer Condition
- Char: `'F'`.
- `cond_pending` is `True`.
- Pop $v_1 = \text{'1'}$.
- Pop $v_2 = \text{'4'}$.
- Condition is `'F'` $\implies$ Select $v_2 = \text{'4'}$.
- Push `'4'` $\implies stk = [\text{'4'}]$.
- Reset `cond_pending = False`.

---

### Termination:
End of reverse scan reached. Top of stack: **`"4"`**.

---

## 4. Complete Execution Trace

| Reverse Step | Scanned Char | Operator Pending? | Stack Before | Action Taken | Stack After |
|:---:|:---:|:---:|:---|:---|:---|
| **1** | `'5'` | No | `[]` | Push literal `'5'` | `['5']` |
| **2** | `':'` | No | `['5']` | Skip separator | `['5']` |
| **3** | `'4'` | No | `['5']` | Push literal `'4'` | `['5', '4']` |
| **4** | `'?'` | **Yes** | `['5', '4']` | Set `cond_pending = True` | `['5', '4']` |
| **5** | `'T'` | **Yes** | `['5', '4']` | Cond `'T'`: choose $v_1 = \text{'4'}$ | `['4']` |
| **6** | `':'` | No | `['4']` | Skip separator | `['4']` |
| **7** | `'1'` | No | `['4']` | Push literal `'1'` | `['4', '1']` |
| **8** | `'?'` | **Yes** | `['4', '1']` | Set `cond_pending = True` | `['4', '1']` |
| **9** | `'F'` | **Yes** | `['4', '1']` | Cond `'F'`: choose $v_2 = \text{'4'}$ | `['4']` |
| **End** | — | No | `['4']` | Emit root result | **Result: `"4"`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Length ($5$ characters: $T?1:2$):** Pops $1$ and $2$, selects $1 \implies \mathbf{\text{"1"}}$.
- **Deeply Nested Left Conditions ($T?T?T?1:2:3:4$):** Right-to-left scan resolves right-hand branches first, peeling layers until the outermost true condition emits $1$.
- **Boolean Return Values ($T?F:T$):** Literals can be `'T'` and `'F'` as values in addition to conditions. The parser handles them identically to numeric digits.
- **Single Character (Not possible per problem constraints):** Length is guaranteed $\ge 5$ and odd.

---

## 6. Traps & Common Anti-Patterns

- **Left-to-Right Recursive Descent:** Parsing from left to right requires tracking balance between `?` and `:` tokens to match corresponding pairs, complicating code and risking quadratic re-scanning on deeply nested chains.
- **Operand Reversal:** When popping two values from the stack, the *first* popped value is the true branch operand $v_1$ (since it appeared immediately before `:`) and the *second* popped value is the false branch operand $v_2$ (which was pushed first). Confusing the pop order inverts the condition logic.
- **String Splitting or Regex:** Ternary expressions are context-free grammars with nesting; regular expressions cannot parse arbitrarily nested parentheses or ternaries.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The expression of length $N$ is scanned once from right to left.
  - Each character is pushed and popped from the stack at most twice.
  - Total Time: $\mathcal{O}(N)$. For $N \le 10^4$, completes in under 2 ms.
- **Auxiliary Space Complexity:**
  - The stack stores at most $N$ characters in the worst case of nested expressions.
  - Total Auxiliary Space: $\mathcal{O}(N)$.

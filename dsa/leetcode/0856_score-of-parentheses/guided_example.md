# Guided Example: Score of Parentheses

We trace the step-by-step depth evaluation, algebraic expansion into powers of two, leaf-node core identification (`"()"`), and balance depth tracking on representative balanced parentheses expressions:

- **Input:**
  $$
  s = \text{"(()(()))"}
  $$
- **Required output:** `6`
  - Score rules:
    - `"()"` has score $1$.
    - $AB$ has score $A + B$, where $A$ and $B$ are balanced parentheses strings.
    - $(A)$ has score $2 \times A$, where $A$ is a balanced parentheses string.
  - Decomposition of $s = \text{"(()(()))"}$:
    - Outer wrapper encloses $A = \text{"()(())"}$.
    - Inside $A$, we have concatenation of $A_1 = \text{"()"}$ and $A_2 = \text{"(())"}$.
    - Score of $A_1 = 1$.
    - Score of $A_2 = 2 \times \text{score}("()") = 2 \times 1 = 2$.
    - Score of $A = A_1 + A_2 = 1 + 2 = 3$.
    - Outer score $= 2 \times \text{score}(A) = 2 \times 3 = \mathbf{6}$.
- **Algebraic Depth Expansion Invariant:**
  - Notice the distributive property of multiplication over addition:
    $$
    2 \times (1 + 2) = 2 \times 1 + 2 \times 2 = 2^1 + 2^2 = 2 + 4 = 6
    $$
  - Every primitive pair `"()"` contributes exactly $2^d$ to the total score, where $d$ is the number of outer pairs enclosing it!
  - More formally, every balanced string can be represented as a sum of powers of two corresponding to each contiguous `"()"` core:
    $$
    \text{score}(s) = \sum_{\substack{i \\ s[i-1..i] = \text{"()"}}} 2^{\text{depth}(i)}
    $$
  - This transforms an $\mathcal{O}(N)$ space stack problem into an $\mathcal{O}(1)$ space single-pass counter with bit-shifts.

---

## 1. Instance & Teaching Goal

Given a balanced parentheses string $s = \text{"(()(()))"}$, calculate its total score under recursive doubling and addition.

```text
String:   ( ( ) ( ( ) ) )
Index:    0 1 2 3 4 5 6 7
Depth:    1 2 1 2 3 2 1 0
              ^     ^
           Core 1  Core 2
         depth=1  depth=2
          2^1=2    2^2=4

Total = 2 + 4 = 6
```

The teaching goal is to show how tree-structured parenthesized expressions linearize into depth-weighted sums of leaf nodes, eliminating explicit stack allocation.

---

## 2. Conceptual Foundation & Invariants

### 1. Depth Counter Dynamics:
Let $d$ be the current nesting depth, initialized to $0$:
- On character `'('`: $d \leftarrow d + 1$.
- On character `')'`: $d \leftarrow d - 1$.

### 2. Leaf Core Recognition:
A closing parenthesis `')'` at index $i$ is the terminator of an elementary unit `"()"` if and only if:
$$
s[i - 1] = \text{'('}
$$
When this holds, it represents a unit of value $1$ wrapped inside $d$ layers of outer parentheses.

### 3. Contribution to Total Score:
$$
\Delta ans = 2^d = 1 \ll d
$$
Closing parentheses where $s[i - 1] == \text{')'}$ do not add value; they simply close an already evaluated compound block whose contents have already been tallied.

---

## 3. Step-by-Step Worked Execution

We process $s = \text{"(()(()))"}$ character by character:

---

### Step 1: Index 0, Character `'('`
- Increment depth: $d \leftarrow 0 + 1 = 1$.
- Accumulator: $ans = 0$.

---

### Step 2: Index 1, Character `'('`
- Increment depth: $d \leftarrow 1 + 1 = 2$.
- Accumulator: $ans = 0$.

---

### Step 3: Index 2, Character `')'`
- Decrement depth: $d \leftarrow 2 - 1 = 1$.
- Check previous character: $s[1] = \text{'('} \implies$ **Core Found!**
- Value added:
  $$
  1 \ll d = 1 \ll 1 = 2^1 = 2
  $$
- Accumulator: $ans \leftarrow 0 + 2 = \mathbf{2}$.

---

### Step 4: Index 3, Character `'('`
- Increment depth: $d \leftarrow 1 + 1 = 2$.
- Accumulator: $ans = 2$.

---

### Step 5: Index 4, Character `'('`
- Increment depth: $d \leftarrow 2 + 1 = 3$.
- Accumulator: $ans = 2$.

---

### Step 6: Index 5, Character `')'`
- Decrement depth: $d \leftarrow 3 - 1 = 2$.
- Check previous character: $s[4] = \text{'('} \implies$ **Core Found!**
- Value added:
  $$
  1 \ll d = 1 \ll 2 = 2^2 = 4
  $$
- Accumulator: $ans \leftarrow 2 + 4 = \mathbf{6}$.

---

### Step 7: Index 6, Character `')'`
- Decrement depth: $d \leftarrow 2 - 1 = 1$.
- Check previous character: $s[5] = \text{')'} \implies$ compound closure, no addition.
- Accumulator: $ans = 6$.

---

### Step 8: Index 7, Character `')'`
- Decrement depth: $d \leftarrow 1 - 1 = 0$.
- Check previous character: $s[6] = \text{')'} \implies$ compound closure, no addition.
- Accumulator: $ans = \mathbf{6}$.

---

## 4. Complete Execution Trace

| Index $i$ | Character $s[i]$ | Depth Before | Action / Rule | Depth After $d$ | Immediate Predecessor $s[i-1]$ | Added Value ($2^d$) | Running Score $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `'('` | $0$ | Push depth | $1$ | — | — | $0$ |
| $1$ | `'('` | $1$ | Push depth | $2$ | `'('` | — | $0$ |
| $2$ | `')'` | $2$ | Pop depth & leaf core | $1$ | `'('` | $2^1 = 2$ | **`2`** |
| $3$ | `'('` | $1$ | Push depth | $2$ | `')'` | — | $2$ |
| $4$ | `'('` | $2$ | Push depth | $3$ | `'('` | — | $2$ |
| $5$ | `')'` | $3$ | Pop depth & leaf core | $2$ | `'('` | $2^2 = 4$ | **`6`** |
| $6$ | `')'` | $2$ | Pop depth & compound close | $1$ | `')'` | $0$ | $6$ |
| $7$ | `')'` | $1$ | Pop depth & compound close | $0$ | `')'` | $0$ | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Pair (`"()"`):** Depth goes $0 \to 1 \to 0$, adds $2^0 = 1$. Returns $1$.
- **Pure Nested (`"((()))"`):** Only the innermost `")"` has predecessor `'('`, contributing $2^2 = 4$. Subsequent `")"` close compounds without double counting.
- **Pure Concatenation (`"()()()"`):** Three independent cores at depth $0$, each adding $2^0 = 1$, totaling $1 + 1 + 1 = 3$.

---

## 6. Traps & Common Anti-Patterns

- **Double-Counting Compound Closures:** Adding score on every `')'` rather than only when $s[i - 1] == \text{'('}$ causes nested expressions to multiply repeatedly, giving exponentially inflated answers.
- **Stack Memory Overhead:** Maintaining an explicit stack of intermediate sums requires $\mathcal{O}(N)$ space. Distributing multiplication over addition allows an $\mathcal{O}(1)$ auxiliary space solution.
- **Integer Overflow:** Maximum length is $N \le 50$. Maximum depth can be $25$. $2^{25} = 33,554,432$, which fits easily in standard 32-bit signed integer types.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass through string of length $N$: $\mathcal{O}(N)$.
  - Bit shift and addition take $\mathcal{O}(1)$ per character.
  - Total Time: $\mathcal{O}(N)$, completing in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - Two scalar integer registers ($ans, d$): $\mathcal{O}(1)$ space.

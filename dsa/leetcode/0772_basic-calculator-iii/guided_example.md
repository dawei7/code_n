# Guided Example: Basic Calculator III

We trace the step-by-step arithmetic operator precedence hierarchy, parenthetical sub-expression recursion ($dfs(q)$ on `'('`), integer literal base-10 accumulation, pending sign operand dispatch ($+ \implies +v, \; - \implies -v$), immediate multiplicative reduction ($* \implies stk.\text{pop}() \times v, \; / \implies \text{int}(stk.\text{pop}() / v)$), and additive stack summation ($\sum stk$) on representative algebraic expressions:

- **Input:** $s = \text{"2*(5+5*2)/3+(6/2+8)"}$
- **Required output:** `21`
  - Calculator evaluation semantics:
    - The expression contains non-negative integers, four binary arithmetic operators ($+$, $-$, $*$, $/$) and parentheses (`(`, `)`).
    - Operator Precedence:
      1. Parentheses `(...)` override all other operations (highest priority).
      2. Multiplicative operators ($*$, $/$) have higher priority than additive operators ($+$, $-$).
      3. Left-to-right associativity among operators of equal precedence.
      4. Division truncates strictly toward zero: $\lfloor a / b \rfloor$ for positive results, $\lceil a / b \rceil$ for negative results (e.g. $\text{int}(-7 / 3) = -2$).
    - For $\text{"2*(5+5*2)/3+(6/2+8)"}$:
      - Inner term 1: $5 + 5 \times 2 = 5 + 10 = 15$.
      - Term 1 product and quotient: $2 \times 15 / 3 = 30 / 3 = 10$.
      - Inner term 2: $6 / 2 + 8 = 3 + 8 = 11$.
      - Final sum: $10 + 11 = \mathbf{21}$.
- **Recursive Queue & Stack Dispatch Invariant:**
  - **Queue Streaming & Recursive Sub-Frames:**
    - Stream characters from a double-ended queue $q$.
    - Whenever an opening parenthesis `'('` is encountered:
      - Delegate evaluation of the entire sub-expression to a recursive child call:
        $$
        num \leftarrow dfs(q)
        $$
      - The child call consumes tokens until its matching `')'` and returns the scalar value of the parenthesized expression.
  - **Stack Multiplicative Compression:**
    - Maintain current operand $num$, pending operator $sign$ (initialized to `'+'`), and an evaluation stack $stk$.
    - When an operator $c \in \{+, -, *, /, )\}$ or end-of-string is reached:
      - Process the pending $sign$ against $num$:
        - $sign == \text{'+'}: \quad stk.\text{push}(+num)$
        - $sign == \text{'-'}: \quad stk.\text{push}(-num)$
        - $sign == \text{'*'}: \quad stk.\text{push}(stk.\text{pop}() \times num)$
        - $sign == \text{'/'}: \quad stk.\text{push}(\text{trunc}(stk.\text{pop}() / num))$
      - Reset operand $num \leftarrow 0$, and update pending sign $sign \leftarrow c$.
      - If $c == \text{')'}$, terminate loop and return $\sum stk$.
- **Step-by-Step Worked Execution Trace on $s = \text{"2*(5+5*2)/3+(6/2+8)"}$:**
  - **Frame 0: Root Expression:**
    - State: $num = 0, sign = \text{'+'}, stk = []$.
    - Char `'2'`: $num = 2$.
    - Char `'*'`:
      - Previous sign is `'+'`: push $+2 \implies stk = [2]$.
      - Reset: $num = 0, sign = \text{'*'}$.
    - Char `'('`: Opening bracket detected $\implies$ spawn child frame `dfs(q)`.
  - **Frame 1: Evaluate `5+5*2)`:**
    - State: $num = 0, sign = \text{'+'}, stk_1 = []$.
    - Char `'5'`: $num = 5$.
    - Char `'+'`:
      - Push $+5 \implies stk_1 = [5]$.
      - Reset: $num = 0, sign = \text{'+'}$.
    - Char `'5'`: $num = 5$.
    - Char `'*'`:
      - Push $+5 \implies stk_1 = [5, 5]$.
      - Reset: $num = 0, sign = \text{'*'}$.
    - Char `'2'`: $num = 2$.
    - Char `')'`:
      - Previous sign is `'*'`: pop 5, compute $5 \times 2 = 10$, push $10$:
        $$
        stk_1 = [5, \; \mathbf{10}]
        $$
      - Closing bracket `')'` hit $\implies$ return sum:
        $$
        \sum stk_1 = 5 + 10 = \mathbf{15}
        $$
  - **Resume Frame 0:**
    - Received child value: $num = 15$.
    - Next char `'/'`:
      - Pending sign was `'*'`: pop 2, compute $2 \times 15 = 30$, push 30:
        $$
        stk = [\mathbf{30}]
        $$
      - Reset: $num = 0, sign = \text{'/'}$.
    - Char `'3'`: $num = 3$.
    - Next char `'+'`:
      - Pending sign was `'/'`: pop 30, compute $\text{int}(30 / 3) = 10$, push 10:
        $$
        stk = [\mathbf{10}]
        $$
      - Reset: $num = 0, sign = \text{'+'}$.
    - Char `'('`: Opening bracket detected $\implies$ spawn child frame `dfs(q)`.
  - **Frame 2: Evaluate `6/2+8)`:**
    - State: $num = 0, sign = \text{'+'}, stk_2 = []$.
    - Char `'6'`: $num = 6$.
    - Char `'/'`: push $+6 \implies stk_2 = [6]$. Reset: $num = 0, sign = \text{'/'}$.
    - Char `'2'`: $num = 2$.
    - Char `'+'`: pop 6, compute $\text{int}(6 / 2) = 3$, push 3:
      $$
      stk_2 = [\mathbf{3}]
      $$
      Reset: $num = 0, sign = \text{'+'}$.
    - Char `'8'`: $num = 8$.
    - Char `')'`: push $+8 \implies stk_2 = [3, 8]$.
      - Closing bracket hit $\implies$ return sum:
        $$
        \sum stk_2 = 3 + 8 = \mathbf{11}
        $$
  - **Resume Frame 0 to Finish:**
    - Received child value: $num = 11$.
    - End of queue reached:
      - Pending sign was `'+'`: push $+11$:
        $$
        stk = [10, \; \mathbf{11}]
        $$
    - Compute final root total:
      $$
      ans = \sum stk = 10 + 11 = \mathbf{21}
      $$
- **Negative Division Truncation Trace (`s = "(3-10)/(4-1)"`):**
  - Left child: $3 - 10 = -7$.
  - Right child: $4 - 1 = 3$.
  - Division: $\text{int}(-7 / 3) = \mathbf{-2}$ (truncates toward zero, not $-3$).
- **Simple Precedence Trace (`s = "6-4/2"`):**
  - Read 6, see `-` $\implies stk = [6]$.
  - Read 4, see `/` $\implies stk = [6, -4]$.
  - Read 2, end $\implies$ pop $-4$, compute $\text{int}(-4 / 2) = -2$, push $-2 \implies stk = [6, -2]$.
  - Sum: $6 + (-2) = \mathbf{4}$.

This instance demonstrates recursive descent LL(1) parsing and stack-based operator precedence evaluation, mathematically proves why immediate multiplicative reduction linearizes the parse tree into pure additive summation, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an arithmetic expression string $s$ with $+$, $-$, $*$, $/$, and parentheses:
Evaluate the expression using standard precedence and **integer division truncating toward zero**.

```text
s = "2*(5+5*2)/3+(6/2+8)"

Step 1: Evaluate (5+5*2):
  5*2 = 10
  5 + 10 = 15
Step 2: 2 * 15 / 3:
  2 * 15 = 30
  30 / 3 = 10
Step 3: Evaluate (6/2+8):
  6 / 2 = 3
  3 + 8 = 11
Step 4: Combine:
  10 + 11 = 21

Result: 21
```

### The Invariant of Stack Multiplicative Compression
- Multiplicative operators ($*, /$) bind tighter than $+/-$. We resolve them immediately with the top of the stack ($stk.pop() \times num$).
- Additive operators ($+, -$) push signed values ($+num, -num$) onto the stack.
- Parentheses `(` recurse into a child frame; `)` returns the sum of the child stack.
- At the end of any frame, the entire result is simply $\sum stk$.

---

## 2. Conceptual Foundation & Invariants

### 1. Pending Sign Evaluation:
When an operator arrives, resolve the **previous sign**:
- `'+'`: $stk.\text{push}(num)$
- `'-'`: $stk.\text{push}(-num)$
- `'*'`: $stk.\text{push}(stk.\text{pop}() \times num)$
- `'/'`: $stk.\text{push}(\text{int}(stk.\text{pop}() / num))$

### 2. Parenthetical Recursion:
$$
\text{if } c == \text{'('} \implies num \leftarrow dfs(q)
$$
$$
\text{if } c == \text{')'} \implies \text{break and return } \sum stk
$$

> **Arithmetic Term Lattice Invariant.** By factoring out multiplication and division into locally reduced stack tokens, the expression is represented in the ring $\mathbb{Z}$ as a polynomial sum $\sum_{i} T_i$ of monomial evaluations, whose additive reduction $\sum stk$ yields the unique canonical value.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"2*(5+5*2)/3+(6/2+8)"}$:

---

### Step 1: Term 1 `2*(5+5*2)/3`
- `2 *`: push 2.
- `(5+5*2)`: recurse $\implies 5 + 10 = 15$.
- `* 15`: $2 \times 15 = 30$.
- `/ 3`: $30 / 3 = 10 \implies stk = [10]$.

---

### Step 2: Term 2 `(6/2+8)`
- `(6/2+8)`: recurse $\implies 3 + 8 = 11$.
- `+ 11`: push $+11 \implies stk = [10, 11]$.

---

### Step 3: Sum Stack
- $10 + 11 = \mathbf{21}$.

---

### Step 4: Output
$$
\mathbf{21}
$$

---

## 4. Complete Execution Trace

| Token Read $c$ | Current Operand $num$ | Pending Sign | Action Taken | Stack State $stk$ | Frame Level |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `'2'` | $2$ | `'+'` | Read digit | `[]` | Frame 0 |
| `'*'` | $0$ | `'*'` | Push $+2$ | `[2]` | Frame 0 |
| `'('` | — | — | Recurse into child | — | Frame 1 |
| Inner | — | — | Evaluates `5+5*2` $\to 15$ | `[5, 10]` | Frame 1 |
| Return 15 | $15$ | `'*'` | Return from child | `[2]` | Frame 0 |
| `'/'` | $0$ | `'/'` | Pop 2, compute $2 \times 15 = 30$ | `[30]` | Frame 0 |
| `'3'` | $3$ | `'/'` | Read digit | `[30]` | Frame 0 |
| `'+'` | $0$ | `'+'` | Pop 30, compute $30 / 3 = 10$ | `[10]` | Frame 0 |
| `'('` | — | — | Recurse into child | — | Frame 2 |
| Inner | — | — | Evaluates `6/2+8` $\to 11$ | `[3, 8]` | Frame 2 |
| Return 11 | $11$ | `'+'` | Return from child | `[10]` | Frame 0 |
| End | $0$ | — | Push $+11$ | **`[10, 11]`** | Frame 0 |
| **Sum** | — | — | **$10 + 11$** | — | **Result: `21`** |

---

## 5. Boundary Cases & Failure Modes

- **Negative Truncation ($(-7)/3$):** Python's `//` performs floor division (yielding $-3$), which is incorrect. Using `int(a / b)` or `math.trunc(a / b)` correctly truncates toward zero (yielding $-2$).
- **Deeply Nested Brackets ($((((1+2))))$):** Recursion unwinds correctly, passing $3$ upward.
- **Single Integer ($"0"$ or $"2147483647"$):** Loop processes single number and returns it directly.
- **Left-Associative Division/Multiplication ($5/2*2$):** Evaluates $(5/2) * 2 = 2 * 2 = 4$, correctly matching left-associativity.

---

## 6. Traps & Common Anti-Patterns

- **Python Floor Division `//` on Negative Numbers:** As noted, `-7 // 3 = -3`, but the problem requires truncation toward zero (`-2`). Must use `int(stk.pop() / num)`!
- **Not Handling the Final Number:** When string ends without a trailing operator, the final $num$ must still be pushed/applied according to the pending $sign$. Checking `not q` triggers this final flush.
- **Converting to RPN / Shunting-Yard:** Building an explicit AST or Reverse Polish Notation queue is unnecessarily complex; the recursive deque + single stack handles parentheses and precedence in a single pass.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each character in $s$ is popped from the queue exactly once.
  - Every number is pushed and popped from intermediate stacks at most twice.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 10^4$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the token queue, call stack, and evaluation stacks.

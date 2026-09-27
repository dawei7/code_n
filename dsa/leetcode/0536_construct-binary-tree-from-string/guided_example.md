# Guided Example: Construct Binary Tree from String

We trace the step-by-step root integer token extraction ($s[:p]$), balanced parenthesis matching ($cnt = 0$), recursive subproblem decomposition ($s[start+1:i]$), left-child precedence assignment, and hierarchical tree construction on representative serialized strings:

- **Input:** $s = \text{"4(2(3)(1))(6(5))"}$
- **Required output:** Binary tree with level-order serialization `[4, 2, 6, 3, 1, 5]`
  - Format grammar: `value(left_child)(right_child)`
  - Grammar rules:
    1. The string starts with an integer (possibly negative) denoting the root's value.
    2. If followed by a parenthesized block `(...)`, the first block always represents the **left subtree**.
    3. If followed by a second parenthesized block `(...)`, it represents the **right subtree**.
    4. Each subtree recursively obeys the exact same grammar.
- **Top-Down Recursive Parsing Trace:**
  - **Level 0: Parse Entire String $s = \text{"4(2(3)(1))(6(5))"}$:**
    - Find first parenthesis `(`: index $p = 1$.
    - Extract root integer:
      $$
      root.val = \text{int}(s[:1]) = \mathbf{4}
      $$
    - Scan for balanced parenthesized blocks starting from $p = 1$:
      - Maintain parenthesis balance counter $cnt$:
        - $i = 1$: `'(' \implies cnt = 1$
        - $i = 3$: `'(' \implies cnt = 2$
        - $i = 5$: `')' \implies cnt = 1$
        - $i = 7$: `'(' \implies cnt = 2$
        - $i = 9$: `')' \implies cnt = 1$
        - $i = 10$: `')' \implies cnt = 0$ (Balanced block closed!)
      - First balanced block span: $s[1 \dots 10] = \text{"(2(3)(1))"}$.
      - Strip outer parentheses: inner content is $\text{"2(3)(1)"}$.
      - Assign to left child:
        $$
        root.left \leftarrow dfs(\text{"2(3)(1)"})
        $$
      - Advance scanner to $i = 11$: Next block begins at index $11$:
        - $i = 11$: `'(' \implies cnt = 1$
        - $i = 13$: `'(' \implies cnt = 2$
        - $i = 15$: `')' \implies cnt = 1$
        - $i = 16$: `')' \implies cnt = 0$ (Second balanced block closed!)
      - Second balanced block span: $s[11 \dots 16] = \text{"(6(5))"}$.
      - Strip outer parentheses: inner content is $\text{"6(5)"}$.
      - Assign to right child:
        $$
        root.right \leftarrow dfs(\text{"6(5)"})
        $$
  - **Level 1 Left Subtree: Parse $\text{"2(3)(1)"}$:**
    - First `(` at index $p = 1 \implies root.val = \mathbf{2}$.
    - First balanced block: $s[1 \dots 3] = \text{"(3)"} \implies$ content $\text{"3"}$.
      - $dfs(\text{"3"})$: No parenthesis $\implies$ Leaf node with value $\mathbf{3}$.
      - Left child of 2 is **`3`**.
    - Second balanced block: $s[4 \dots 6] = \text{"(1)"} \implies$ content $\text{"1"}$.
      - $dfs(\text{"1"})$: Leaf node with value $\mathbf{1}$.
      - Right child of 2 is **`1`**.
  - **Level 1 Right Subtree: Parse $\text{"6(5)"}$:**
    - First `(` at index $p = 1 \implies root.val = \mathbf{6}$.
    - First balanced block: $s[1 \dots 3] = \text{"(5)"} \implies$ content $\text{"5"}$.
      - $dfs(\text{"5"})$: Leaf node with value $\mathbf{5}$.
      - Left child of 6 is **`5`**.
    - No second balanced block exists $\implies$ Right child is **`None`**.
  - **Tree Assembly Complete:**
    - Root $4$ has left child $2$ and right child $6$.
    - Node $2$ has left child $3$ and right child $1$.
    - Node $6$ has left child $5$ and no right child.
    - Level-order serialization: `[4, 2, 6, 3, 1, 5]`.
- **Negative Value Instance ($s = \text{"-4(2)(3)"}$):**
  - First `(` at index 2 $\implies s[:2] = \text{"-4"} \implies$ root value is $-4$.
- **Leaf Only Instance ($s = \text{"42"}$):**
  - No parentheses present $\implies$ returns single node with value $42$.
- **Empty String Instance ($s = \text{""}$):**
  - Returns `None`.

This instance demonstrates recursive descent parsing on context-free parenthesis grammars, mathematically proves why tracking cumulative bracket balances isolates nested subtree boundaries, and derives $O(N^2)$ worst-case / $O(N)$ stack-optimized runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a serialized string $s = \text{"4(2(3)(1))(6(5))"}$:
Reconstruct the binary tree corresponding to the nested parenthetical encoding:
- The first integer is the root value.
- The first parenthesized group is the left subtree.
- The second parenthesized group (if present) is the right subtree.
Return the root node of the binary tree.

```text
Serialized: "4(2(3)(1))(6(5))"

Decomposition:
  Root = 4
  Left Subtree  = "2(3)(1)"
  Right Subtree = "6(5)"

Left Subtree ("2(3)(1)"):
  Root = 2, Left = 3, Right = 1

Right Subtree ("6(5)"):
  Root = 6, Left = 5, Right = null

Result Tree:
        4
       / \
      2   6
     / \  /
    3  1 5
```

### Grammar Invariant
Every non-empty string adheres to:
$$
\text{Tree} \to \text{Integer} \ [ \ \text{'('} \ \text{Tree} \ \text{')'} \ ] \ [ \ \text{'('} \ \text{Tree} \ \text{')'} \ ]
$$
- The integer precedes the first `(`.
- Finding matching pairs of parentheses separates the left child from the optional right child.
- A depth counter incremented on `(` and decremented on `)` reaches $0$ exactly at the end of each complete subtree.

---

## 2. Conceptual Foundation & Invariants

### 1. Depth-First Parsing Function $dfs(s)$:
- If $s$ is empty: return `None`.
- Find the first `(` at index $p$:
  - If $p == -1$: $s$ contains no children $\implies$ return node with integer value $\text{int}(s)$.
  - Else: root value is $\text{int}(s[:p])$.
- Initialize $start = p, \; cnt = 0$.
- Iterate $i$ from $p$ to $|s| - 1$:
  - If $s[i] == \text{'('}$: $cnt \leftarrow cnt + 1$.
  - Elif $s[i] == \text{')'}$: $cnt \leftarrow cnt - 1$.
  - When $cnt == 0$ (a top-level child block has closed):
    - If $start == p$:
      This is the first block $\implies$ assign to left child:
      $$
      root.left \leftarrow dfs(s[start + 1 : i])
      $$
      Update $start \leftarrow i + 1$ for the next child.
    - Else:
      This is the second block $\implies$ assign to right child:
      $$
      root.right \leftarrow dfs(s[start + 1 : i])
      $$
- Return $root$.

> **Bracket Balancing Invariant.** The index where $cnt$ returns to $0$ strictly delimits the outermost closing parenthesis of the current child subtree, preventing inner nested parentheses from prematurely terminating the group.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"4(2(3)(1))(6(5))"}$:

---

### Step 1: Root Node
- First `(` located at index $p = 1$.
- Root value:
  $$
  s[:1] = \text{"4"} \implies \text{Node}(4)
  $$

---

### Step 2: Split Left and Right Children
Scan $i$ from $1$ to end:
- $i=1 \dots 10$:
  - Parenthesis balance reaches $0$ at index $i = 10$.
  - First child block: $s[2 \dots 9] = \text{"2(3)(1)"}$.
  - $root.left \leftarrow dfs(\text{"2(3)(1)"})$.
  - Update $start = 11$.
- $i=11 \dots 16$:
  - Balance reaches $0$ at index $i = 16$.
  - Second child block: $s[12 \dots 15] = \text{"6(5)"}$.
  - $root.right \leftarrow dfs(\text{"6(5)"})$.

---

### Step 3: Recurse into Left Child $\text{"2(3)(1)"}$
- First `(` at index $1 \implies$ value is $2$.
- Balanced blocks:
  - Block 1: $s[2 \dots 2] = \text{"3"} \implies dfs(\text{"3"}) = \text{Node}(3)$.
  - Block 2: $s[5 \dots 5] = \text{"1"} \implies dfs(\text{"1"}) = \text{Node}(1)$.
- Left subtree fully resolved: Node 2 with left 3 and right 1.

---

### Step 4: Recurse into Right Child $\text{"6(5)"}$
- First `(` at index $1 \implies$ value is $6$.
- Balanced blocks:
  - Block 1: $s[2 \dots 2] = \text{"5"} \implies dfs(\text{"5"}) = \text{Node}(5)$.
  - No second block $\implies$ right child is `None`.
- Right subtree fully resolved: Node 6 with left 5.

---

### Step 5: Assembled Hierarchy
$$
\text{Root}(4) \to \text{Left: Node}(2), \quad \text{Right: Node}(6)
$$

---

## 4. Complete Execution Trace

| Call $dfs(s)$ | Substring Input $s$ | First `(` Index $p$ | Root Value | Left Substring | Right Substring | Subtree Built |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Top** | `"4(2(3)(1))(6(5))"` | $1$ | $4$ | `"2(3)(1)"` | `"6(5)"` | $4 \to (2, 6)$ |
| **Left** | `"2(3)(1)"` | $1$ | $2$ | `"3"` | `"1"` | $2 \to (3, 1)$ |
| **L-L** | `"3"` | $-1$ | $3$ | `None` | `None` | $3$ (Leaf) |
| **L-R** | `"1"` | $-1$ | $1$ | `None` | `None` | $1$ (Leaf) |
| **Right** | `"6(5)"` | $1$ | $6$ | `"5"` | `None` | $6 \to (5, \text{null})$ |
| **R-L** | `"5"` | $-1$ | $5$ | `None` | `None` | $5$ (Leaf) |

---

## 5. Boundary Cases & Failure Modes

- **Negative Root or Child Values ($s = \text{"-4(-2)(-6)"}$):** The slice $s[:p]$ captures the negative sign (`"-4"`) and converts to $-4$ correctly.
- **Single Node Without Parentheses ($s = \text{"42"}$):** $p = -1 \implies$ immediately returns $\text{Node}(42)$.
- **Only Left Child Present ($s = \text{"1(2)"}$):** Only one balanced block is found; right child defaults to `None`.
- **Empty Input ($s = \text{""}$):** Returns `None`.

---

## 6. Traps & Common Anti-Patterns

- **Splitting on Every `(`:** Parentheses are nested arbitrarily deep (e.g. `2(3)(1)` inside `4(...)`). Splitting blindly on `(` breaks the recursive structure. The balance counter $cnt$ must reach $0$ to identify true top-level children.
- **Assuming Root is a Single Digit:** A node value can be negative or multi-digit (e.g. `"-105(2)"`). Using $s.find('(')$ correctly isolates the entire integer prefix regardless of its number of digits.
- **Assigning Second Block to Left Child:** The problem specifies that the *first* block is always the left child and the *second* block is the right child. Tracking `start == p` guarantees proper left-first assignment.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Finding the first `(` and matching parentheses takes $O(L)$ time for a substring of length $L$.
  - In a balanced tree of depth $O(\log N)$, the total work across all levels is $O(N \log N)$.
  - In a skewed line tree, string slicing and scanning takes $O(N^2)$ worst-case time. For $N \le 10^4$, recursive descent completes in $< 20$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(H)$ call stack space where $H$ is the tree height ($O(\log N)$ average, $O(N)$ worst-case).
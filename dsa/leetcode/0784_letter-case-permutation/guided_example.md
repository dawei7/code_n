# Guided Example: Letter Case Permutation

We trace the step-by-step character classification (digit invariant vs alphabetic branch), ASCII bit-5 case inversion ($\text{ord}(c) \oplus 32$), binary search decision tree branching ($2^k$ total leaves for $k$ alphabetic letters), depth-first backtracking traversal ($dfs(i)$), and leaf-state string collection on representative alphanumeric strings:

- **Input:** $s = \text{"a1b2"}$
- **Required output:**
  $$
  [\text{"a1b2"}, \; \text{"a1B2"}, \; \text{"A1b2"}, \; \text{"A1B2"}]
  $$
  - Permutation generation criteria:
    - Each letter in the string can independently take either lowercase or uppercase form.
    - Digits (`0`-`9`) are invariant and cannot be modified.
    - Objective: Generate all possible unique string permutations formed by case variations. Output can be returned in any order.
    - For $s = \text{"a1b2"}$ (length 4):
      - Position 0: `'a'` (letter $\implies$ choices: `'a'` or `'A'`).
      - Position 1: `'1'` (digit $\implies$ fixed `'1'`).
      - Position 2: `'b'` (letter $\implies$ choices: `'b'` or `'B'`).
      - Position 3: `'2'` (digit $\implies$ fixed `'2'`).
      - Total independent binary choices: $k = 2$ letters $\implies 2^2 = \mathbf{4}$ combinations:
        1. Keep both lowercase: `"a1b2"`
        2. Toggle `'b'` to uppercase: `"a1B2"`
        3. Toggle `'a'` to uppercase, `'b'` lowercase: `"A1b2"`
        4. Toggle both to uppercase: `"A1B2"`
- **ASCII Bit-5 Inversion & Binary Decision Tree Invariant:**
  - **The Power-of-Two State Tree:**
    - If a string contains $k$ letters, the combinatorial decision tree has depth $n$ and exactly $2^k$ leaf nodes.
  - **Bitwise Case Toggle ($\oplus 32$):**
    - In standard ASCII encoding:
      - Uppercase `'A'` to `'Z'` have codes $65 \dots 90$ (`01000001` to `01011010`).
      - Lowercase `'a'` to `'z'` have codes $97 \dots 122$ (`01100001` to `01111010`).
      - They differ by exactly one single bit: **bit 5** (value $2^5 = 32$).
      - Therefore, toggling case for any alphabetic character is an atomic bitwise XOR:
        $$
        \text{toggle}(c) = \text{chr}(\text{ord}(c) \oplus 32)
        $$
  - **Backtracking State Machine ($dfs(i)$):**
    - At index $i$:
      1. Base Case: If $i == n$, a full permutation is formed; append copy of buffer to output.
      2. First Branch (Keep Current Form): Call $dfs(i + 1)$.
      3. Second Branch (If Alphabetic):
         - Invert case: $t[i] \leftarrow \text{toggle}(t[i])$.
         - Call $dfs(i + 1)$.
         - Note: Backtracking automatically returns $t[i]$ to its alternate form, or toggles back after return.
- **Step-by-Step Worked Execution Trace on $s = \text{"a1b2"}$:**
  - Character buffer: $t = [\text{'a'}, \text{'1'}, \text{'b'}, \text{'2'}]$.
  - Output collector: $ans = []$.
  - **Decision Level 0 ($i = 0$, $t[0] = \text{'a'}$):**
    - **Branch 1A (Keep `'a'`):**
      - Advance to $i = 1$.
      - Level 1 ($i = 1$, $t[1] = \text{'1'}$): Digit $\implies$ only 1 branch. Advance to $i = 2$.
      - **Level 2 ($i = 2$, $t[2] = \text{'b'}$):**
        - **Branch 2A (Keep `'b'`):**
          - Advance to $i = 3$.
          - Level 3 ($i = 3$, $t[3] = \text{'2'}$): Digit $\implies$ advance to $i = 4$.
          - Level 4 ($i = 4 == n$): Leaf reached!
            $$
            ans.\text{append}(\mathbf{\text{"a1b2"}})
            $$
        - **Branch 2B (Toggle `'b'` $\implies$ `'B'`):**
          - $t[2] \leftarrow \text{'B'}$.
          - Advance to $i = 3 \implies i = 4$ (Leaf reached!).
            $$
            ans.\text{append}(\mathbf{\text{"a1B2"}})
            $$
    - **Branch 1B (Toggle `'a'` $\implies$ `'A'`):**
      - $t[0] \leftarrow \text{'A'}$.
      - Advance to $i = 1$ ($t[1] = \text{'1'}$). Advance to $i = 2$.
      - **Level 2 ($i = 2$, $t[2] = \text{'B'}$):**
        - **Branch 2C (Keep current form `'B'`, or toggle back to `'b'`):**
          - Toggle $t[2] \leftarrow \text{'b'}$.
          - Advance through digit `'2'` to leaf ($i = 4$):
            $$
            ans.\text{append}(\mathbf{\text{"A1b2"}})
            $$
        - **Branch 2D (Toggle to uppercase `'B'`):**
          - $t[2] \leftarrow \text{'B'}$.
          - Advance through digit `'2'` to leaf ($i = 4$):
            $$
            ans.\text{append}(\mathbf{\text{"A1B2"}})
            $$
  - **Assembly Complete:**
    - Exactly $2^2 = 4$ permutations collected:
      $$
      ans = [\text{"a1b2"}, \; \text{"a1B2"}, \; \text{"A1b2"}, \; \text{"A1B2"}]
      $$
- **Single Letter Trace ($s = \text{"3z4"}$):**
  - Only 1 letter `'z'`.
  - Generates $2^1 = 2$ strings: `["3z4", "3Z4"]`.
- **All Digits Trace ($s = \text{"12345"}$):**
  - $k = 0$ letters $\implies 2^0 = 1$ string.
  - Returns `["12345"]`.

This instance demonstrates binary cartesian product expansion over invariant fixed positions, mathematically proves why ASCII bit-5 symmetry induces an involution on the alphabetic alphabet, and derives $O(N \cdot 2^k)$ execution time and $O(N)$ recursion depth bounds.

---

## 1. Instance & Teaching Goal

Given an alphanumeric string $s$:
Transform each letter individually to lowercase or uppercase to generate **all possible strings**.

```text
s = "a1b2"

Characters:
  'a' -> can be 'a' or 'A'
  '1' -> fixed digit '1'
  'b' -> can be 'b' or 'B'
  '2' -> fixed digit '2'

2 letters -> 2^2 = 4 permutations:
  "a1b2", "a1B2", "A1b2", "A1B2"

Result: [ "a1b2", "a1B2", "A1b2", "A1B2" ]
```

### The Invariant of the Binary Branching Tree
- Digits have 1 branch ($dfs(i+1)$).
- Letters have 2 branches: keep current form, and toggle case via $\text{ord}(c) \oplus 32$.
- The recursion reaches leaves at $i = n$, emitting each of the $2^k$ combinations.

---

## 2. Conceptual Foundation & Invariants

### 1. ASCII Bitwise Case Involution:
$$
\text{toggle}(c) = \text{chr}(\text{ord}(c) \oplus 32) \quad \forall c \in [a-zA-Z]
$$
$$
\text{toggle}(\text{toggle}(c)) = c
$$

### 2. State Recurrence:
$$
dfs(i): \quad \text{if } i == n \implies ans.\text{append}(\text{str}(t))
$$
$$
dfs(i + 1)
$$
$$
\text{if } t[i].\text{isalpha}() \implies t[i] \leftarrow \text{toggle}(t[i]), \quad dfs(i + 1)
$$

> **Boolean Hypercube Embedding Invariant.** For an alphanumeric word of length $n$ containing $k$ alphabetic symbols, the configuration space is isomorphic to the $k$-dimensional Boolean hypercube $\{0, 1\}^k$, traversed exhaustively in pre-order by depth-first search.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"a1b2"}$:

---

### Step 1: Decision for `'a'`
- Branch 1: keep `'a'`.
- Branch 2: toggle to `'A'`.

---

### Step 2: Skip `'1'`
- Digit $\implies$ passes to index 2.

---

### Step 3: Decision for `'b'`
- Under `'a'`: forms `"a1b2"` and `"a1B2"`.
- Under `'A'`: forms `"A1b2"` and `"A1B2"`.

---

### Step 4: Output
$$
[\text{"a1b2"}, \; \text{"a1B2"}, \; \text{"A1b2"}, \; \text{"A1B2"}]
$$

---

## 4. Complete Execution Trace

| DFS Path Traversed | Letter 1 Form | Letter 2 Form | Permutation String Formed | Leaf Added to Result |
|:---:|:---:|:---:|:---:|:---:|
| Path 1 | `'a'` | `'b'` | `"a1b2"` | `"a1b2"` |
| Path 2 | `'a'` | `'B'` | `"a1B2"` | `"a1B2"` |
| Path 3 | `'A'` | `'b'` | `"A1b2"` | `"A1b2"` |
| **Path 4** | **`'A'`** | **`'B'`** | **`"A1B2"`** | **`"A1B2"`** |

---

## 5. Boundary Cases & Failure Modes

- **No Letters ($"12345"$):** Zero branches $\implies$ returns `["12345"]`.
- **All Letters ($"ab"$):** Full binary tree of depth 2 $\implies$ 4 strings.
- **Single Letter ($"z"$):** Returns `["z", "Z"]`.
- **Max Length ($N = 12$):** At most $2^{12} = 4096$ leaf nodes; finishes in $< 2$ ms.

---

## 6. Traps & Common Anti-Patterns

- **Using `.upper()` and `.lower()` with Repeated String Copies:** Creating new strings at each level creates heavy garbage collection. Modifying a single character list `t` in-place and taking a snapshot `"".join(t)` only at leaf nodes minimizes allocations.
- **Toggling Digits:** Toggling non-alphabetic characters like `'1'` produces corrupted control characters. Only toggle when `t[i].isalpha()` is true.
- **Forgetting to Recurse on Digits:** Digits must still advance the recursion pointer $i \leftarrow i + 1$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $k$ be the number of alphabetic characters ($k \le N \le 12$).
  - Total leaf nodes generated: $2^k \le 4096$.
  - At each leaf, string concatenation takes $\mathcal{O}(N)$.
  - Total Time: strictly $\mathcal{O}(N \cdot 2^k)$. Completes in $< 3$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ for the recursion depth and character buffer.

# Guided Example: Special Binary String

We trace the step-by-step Dyck path / balanced parentheses isomorphism ($1 \iff \text{'('}, \; 0 \iff \text{')'}$), prefix balance tracking ($cnt \pm 1$), irreducible component decomposition ($B_m = \text{'1'} + S_m + \text{'0'}$), recursive interior sub-tree maximization, greedy lexicographical descending sibling sorting ($sort(reverse=True)$), and canonical tree serialization on representative binary strings:

- **Input:** $s = \text{"11011000"}$
- **Required output:**
  $$
  \text{"11100100"}
  $$
  - Special binary string properties & Parenthesis Isomorphism:
    1. Equal total number of `1`s and `0`s.
    2. Every prefix has at least as many `1`s as `0`s (Dyck path condition).
    3. Translating `1` to `'('` and `0` to `')'`, every special string is an exact valid balanced parentheses string!
    4. **Permissible Move:** You can swap any two adjacent, non-empty special substrings.
       - In tree terms, this means any two adjacent sibling sub-trees under the same parent node can be swapped in order.
       - By repeated adjacent swaps (bubble sort), sibling sub-trees can be arranged in **any arbitrary permutation**!
    5. **Objective:** Maximize the string lexicographically.
    6. For $s = \text{"11011000"}$:
      - As parentheses: `"( ( ) ( ( ) ) )"`.
      - Root wraps an inner forest: `"10"` followed by `"1100"` (`"( )"` and `"( ( ) )"`).
      - Swapping the siblings puts the heavier block `"1100"` before `"10"`:
        $$
        \text{"110010"} \succ \text{"101100"}
        $$
      - Re-wrapping in the outer `1...0`:
        $$
        \text{'1'} + \text{"110010"} + \text{'0'} = \mathbf{\text{"11100100"}}
        $$
- **Irreducible Component Decomposition & Sibling Sorting Invariant:**
  - **Decomposition into Primitives:**
    - A special string can be uniquely partitioned into top-level irreducible blocks:
      $$
      s = B_1 B_2 \dots B_k
      $$
    - An irreducible block $B_m$ begins with `1` and ends with `0`, where the prefix balance $cnt = \sum (1 \text{ if } 1 \text{ else } -1)$ reaches $0$ for the very first time at the final character.
    - Stripping the outer `1` and `0` leaves an interior substring $S_m$:
      $$
      B_m = \text{'1'} + S_m + \text{'0'}
      $$
  - **Recursive Invariant:**
    - To maximize the entire string lexicographically:
      1. Recursively maximize each interior component:
         $$
         B_m' = \text{'1'} + \text{makeLargestSpecial}(S_m) + \text{'0'}
         $$
      2. Sort the maximized blocks $\{B_1', B_2', \dots, B_k'\}$ in **descending lexicographical order**:
         $$
         ans = \text{join}(\text{sort\_descending}(B_1', B_2', \dots, B_k'))
         $$
    - Placing lexicographically larger strings earlier maximizes the binary number value!
- **Step-by-Step Worked Execution Trace on $s = \text{"11011000"}$:**
  - **Level 1: Parse Root String $s = \text{"11011000"}$ (Length 8):**
    - Track balance $cnt$:
      - $i = 0$ (`'1'`): $cnt = 1$
      - $i = 1$ (`'1'`): $cnt = 2$
      - $i = 2$ (`'0'`): $cnt = 1$
      - $i = 3$ (`'1'`): $cnt = 2$
      - $i = 4$ (`'1'`): $cnt = 3$
      - $i = 5$ (`'0'`): $cnt = 2$
      - $i = 6$ (`'0'`): $cnt = 1$
      - $i = 7$ (`'0'`): $cnt = 0 \implies \mathbf{Balance\ Zero\ at\ End!}$
    - Entire string is a single irreducible block spanning $0 \dots 7$:
      - Outer prefix: `'1'` (index 0).
      - Outer suffix: `'0'` (index 7).
      - Interior substring: $S_1 = s[1 : 7] = \text{"101100"}$.
    - Recurse on interior: `makeLargestSpecial("101100")`.
  - **Level 2: Parse Interior $s_2 = \text{"101100"}$ (Length 6):**
    - Track balance $cnt$:
      - $i = 0$ (`'1'`): $cnt = 1$
      - $i = 1$ (`'0'`): $cnt = 0 \implies \mathbf{First\ Block\ Boundary\ at\ } i = 1\mathbf{!}$
        - Block 1: $s_2[0 : 2] = \text{"10"}$.
        - Interior of Block 1: $s_2[1 : 1] = \text{""}$ (empty).
        - Optimized Block 1:
          $$
          B_{2, 1} = \text{'1'} + \text{makeLargestSpecial}(\text{""}) + \text{'0'} = \mathbf{\text{"10"}}
          $$
      - Advance to next block: $j \leftarrow 2$.
      - $i = 2$ (`'1'`): $cnt = 1$
      - $i = 3$ (`'1'`): $cnt = 2$
      - $i = 4$ (`'0'`): $cnt = 1$
      - $i = 5$ (`'0'`): $cnt = 0 \implies \mathbf{Second\ Block\ Boundary\ at\ } i = 5\mathbf{!}$
        - Block 2: $s_2[2 : 6] = \text{"1100"}$.
        - Interior of Block 2: $s_2[3 : 5] = \text{"10"}$.
        - Recurse on `"10"` $\implies$ returns `"10"`.
        - Optimized Block 2:
          $$
          B_{2, 2} = \text{'1'} + \text{"10"} + \text{'0'} = \mathbf{\text{"1100"}}
          $$
    - **Sibling Sorting at Level 2:**
      - Available blocks: $ans_2 = [\text{"10"}, \; \text{"1100"}]$.
      - Compare strings: $\text{"1100"} \succ \text{"10"}$.
      - Sort descending:
        $$
        ans_2.\text{sort}(\text{reverse}=\text{True}) \implies [\mathbf{\text{"1100"}}, \; \mathbf{\text{"10"}}]
        $$
      - Concatenate:
        $$
        \text{Level 2 Result} = \text{"110010"}
        $$
  - **Level 1 Reassembly:**
    - Re-wrap Level 2 result in outer `'1'` and `'0'`:
      $$
      ans_1 = [\text{'1'} + \text{"110010"} + \text{'0'}] = [\mathbf{\text{"11100100"}}]
      $$
    - Only 1 top-level block, sorted trivially.
    - Final string:
      $$
      ans = \mathbf{\text{"11100100"}}
      $$
- **Top-Level Multi-Block Swap Trace ($s = \text{"101100"}$):**
  - Top level has 2 blocks: `"10"` and `"1100"`.
  - Sibling sort orders `"1100"` before `"10"`.
  - Returns **`"110010"`**.
- **Minimal Special String ($s = \text{"10"}$):**
  - Interior is empty.
  - Returns **`"10"`**.

This instance demonstrates Dyck language tree canonicalization and recursive lexicographical permutation, mathematically proves why sorting sibling components in descending order maximizes the binary valuation across commutative quotient monoids, and derives $O(N^2)$ runtime and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a special binary string $s$ (equal 0s and 1s, every prefix has $\ge$ 1s than 0s):
Swap adjacent special substrings to make $s$ **lexicographically largest**.

```text
s = "11011000"

Parenthesis equivalent:
  ( ( ) ( ( ) ) )

Decompose into outer '1' ... '0':
  Inner: "101100"
  Inner has two blocks: "10" and "1100"
  Sort descending: "1100" > "10" -> "110010"

Re-wrap:
  '1' + "110010" + '0' = "11100100"

Result: "11100100"
```

### The Invariant of the Canonical Tree Sibling Sort
- A special binary string is isomorphic to a rooted tree of balanced parentheses.
- Swapping adjacent substrings allows sorting any sibling sub-trees in descending lexicographical order.
- Recursively maximizing the interior of each block and sorting siblings at every level achieves the globally maximal string.

---

## 2. Conceptual Foundation & Invariants

### 1. Primitive Block Decomposition:
$$
s = B_1 B_2 \dots B_k \quad \text{where each } B_m = \text{'1'} + S_m + \text{'0'}
$$

### 2. Recursive Maximization & Sibling Order:
$$
B_m' = \text{'1'} + \text{makeLargestSpecial}(S_m) + \text{'0'}
$$
$$
\text{makeLargestSpecial}(s) = \text{join}(\text{sort}_{\downarrow}(B_1', \dots, B_k'))
$$

> **Dyck Canonical Form Invariant.** The rewrite system generated by adjacent sibling transpositions $U V \leftrightarrow V U$ over the free monoid of Dyck paths is confluent and terminating, with the unique lexicographical normal form given by descending recursive sibling tree ordering.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"11011000"}$:

---

### Step 1: Parse Outer Block
- Single block $B_1$ with interior $S_1 = \text{"101100"}$.

---

### Step 2: Recurse on Interior `"101100"`
- Decomposes into two blocks:
  - $B_{2, 1} = \text{"10"}$.
  - $B_{2, 2} = \text{"1100"}$.
- Sort descending: `["1100", "10"]` $\implies \text{"110010"}$.

---

### Step 3: Wrap Outer Block
- `'1' + "110010" + '0' = \mathbf{\text{"11100100"}}`.

---

### Step 4: Output
$$
\mathbf{\text{"11100100"}}
$$

---

## 4. Complete Execution Trace

| Recursion Depth | Substring Evaluated | Irreducible Blocks Partition | Sibling Blocks Before Sort | Sibling Blocks After Descending Sort | Result Returned |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ | `"101100"` | `B1="10", B2="1100"` | `["10", "1100"]` | `["1100", "10"]` | `"110010"` |
| **$1$ (Root)** | **`"11011000"`** | **`'1' + "110010" + '0'`**| **`["11100100"]`** | **`["11100100"]`** | **`"11100100"`** |

---

## 5. Boundary Cases & Failure Modes

- **Base String (`"10"`):** Empty interior $\implies$ returns `"10"`.
- **Multiple Disjoint Blocks at Root (`"101100"`):** Sibling sort directly swaps them to `"110010"`.
- **Deeply Nested String (`"111000"`):** $((( )))$ $\implies$ already maximally nested, returns `"111000"`.
- **Empty String:** Returns `""`.

---

## 6. Traps & Common Anti-Patterns

- **Attempting Greedy Swaps on Raw Indices:** Trying to swap arbitrary pairs without parsing the parenthesis structure will break the "special string" condition or fail to reach the global optimum.
- **Forgetting to Recurse on the Interior:** Sorting only the top-level blocks without maximizing $S_m$ inside each block misses nested optimizations (e.g. inside `1...0`).
- **Ascending Sort instead of Descending:** The problem asks for the *largest* string lexicographically, requiring `sort(reverse=True)`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Length $N \le 50$.
  - At each recursion level, finding block boundaries takes $\mathcal{O}(N)$ time.
  - Sorting at most $N / 2$ blocks takes $\mathcal{O}(N \log N)$ string comparisons of length $\le N$.
  - Recursion depth $\le N / 2$.
  - Total Time: strictly $\mathcal{O}(N^2)$. For $N = 50$, executes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ for the recursion stack and intermediate string slices.

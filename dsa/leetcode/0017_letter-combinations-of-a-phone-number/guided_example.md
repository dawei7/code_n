# Guided Example: Letter Combinations of a Phone Number

We trace the step-by-step Cartesian product expansion on a representative multi-digit keypad instance:

- **Input:** $\text{digits} = \text{"23"}$
- **Required output:** `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`

This instance demonstrates recursive decision-tree branching, prefix expansion across multiple telephone keypad sets, and exact preservation of combination cardinality without duplicates.

---

## 1. Instance & Teaching Goal

Telephone keypads map digits $2$ through $9$ to sets of English letters:

| Digit | Mapped Characters | Digit | Mapped Characters |
|:---:|:---|:---:|:---|
| 2 | `a`, `b`, `c` | 6 | `m`, `n`, `o` |
| 3 | `d`, `e`, `f` | 7 | `p`, `q`, `r`, `s` |
| 4 | `g`, `h`, `i` | 8 | `t`, `u`, `v` |
| 5 | `j`, `k`, `l` | 9 | `w`, `x`, `y`, `z` |

For $\text{digits} = \text{"23"}$:
- Digit `'2'` maps to $S_1 = \{\text{'a'}, \text{'b'}, \text{'c'}\}$ (size 3).
- Digit `'3'` maps to $S_2 = \{\text{'d'}, \text{'e'}, \text{'f'}\}$ (size 3).
- The complete set of valid strings is the Cartesian product $S_1 \times S_2$, having cardinality $3 \times 3 = 9$.

The objective is to systematically generate all 9 combinations using backtracking or breadth-first frontier expansion, while handling the boundary condition where $\text{digits} = \text{""}$ returns `[]` (empty list) rather than `[""]`.

---

## 2. Conceptual Foundation & Invariants

### Decision Tree Structure

We can view the generation process as traversing a decision tree of depth $K = |\text{digits}|$:

```text
Level 0 (Root):                     ""
                               /    |    \
Level 1 (Digit '2'):         "a"   "b"   "c"
                            / | \ / | \ / | \
Level 2 (Digit '3'):       ad ae af bd be bf cd ce cf
```

- Each layer $k$ corresponds to digit $\text{digits}[k]$.
- Every existing partial prefix of length $k$ branches into $|S_k|$ children by appending each character in $S_k$.
- When $k = K$, all leaf nodes represent complete valid combinations of length $K$.

### Frontier Invariant
Let $F_k$ be the frontier of prefixes generated after processing the first $k$ digits $\text{digits}[0 \dots k-1]$:
$$
F_0 = [\text{""}]
$$
$$
F_k = \{ p + c \mid p \in F_{k-1}, \, c \in \text{Keypad}[\text{digits}[k-1]] \}
$$

> **Invariant.** At layer $k$, $F_k$ contains exactly $\prod_{i=0}^{k-1} |\text{Keypad}[\text{digits}[i]]|$ unique prefixes of length $k$, and every prefix is an exact match for the first $k$ digits.

---

## 3. Step-by-Step Worked Execution

We trace the frontier expansion for $\text{digits} = \text{"23"}$:

### Initialization ($k = 0$)
- Check input length: $|\text{digits}| = 2 > 0$.
- Initialize frontier with the neutral empty prefix:
  $$
  F_0 = [\text{""}]
  $$

---

### Layer 1: Process Digit `'2'` ($k = 1$)
- Target digit: `'2'`.
- Letter set: $S_1 = [\text{'a'}, \text{'b'}, \text{'c'}]$.
- For each prefix $p \in F_0$ (only $\text{""}$):
  - Append `'a'`: $\text{""} + \text{'a'} = \text{"a"}$
  - Append `'b'`: $\text{""} + \text{'b'} = \text{"b"}$
  - Append `'c'`: $\text{""} + \text{'c'} = \text{"c"}$
- Resulting frontier:
  $$
  F_1 = [\text{"a"}, \text{"b"}, \text{"c"}]
  $$
- Cardinality: $1 \times 3 = 3$.

---

### Layer 2: Process Digit `'3'` ($k = 2$)
- Target digit: `'3'`.
- Letter set: $S_2 = [\text{'d'}, \text{'e'}, \text{'f'}]$.
- For each prefix $p \in F_1$:
  - From $p = \text{"a"}$:
    - Append `'d'`: $\text{"ad"}$
    - Append `'e'`: $\text{"ae"}$
    - Append `'f'`: $\text{"af"}$
  - From $p = \text{"b"}$:
    - Append `'d'`: $\text{"bd"}$
    - Append `'e'`: $\text{"be"}$
    - Append `'f'`: $\text{"bf"}$
  - From $p = \text{"c"}$:
    - Append `'d'`: $\text{"cd"}$
    - Append `'e'`: $\text{"ce"}$
    - Append `'f'`: $\text{"cf"}$
- Resulting frontier:
  $$
  F_2 = [\text{"ad"}, \text{"ae"}, \text{"af"}, \text{"bd"}, \text{"be"}, \text{"bf"}, \text{"cd"}, \text{"ce"}, \text{"cf"}]
  $$
- Cardinality: $3 \times 3 = 9$.

### Termination
All digits consumed ($k = |\text{digits}| = 2$). The leaves of the tree form the final output list of length 9.

---

## 4. Complete Execution Trace

| Step | Active Digit | Prefix Considered | Appended Character | Produced Candidate | Current Frontier State |
|:---:|:---:|:---:|:---:|:---:|:---|
| 0 (Init) | - | - | - | `""` | `[""]` |
| 1 | `'2'` | `""` | `'a'` | `"a"` | `["a"]` |
| 2 | `'2'` | `""` | `'b'` | `"b"` | `["a", "b"]` |
| 3 | `'2'` | `""` | `'c'` | `"c"` | `["a", "b", "c"]` |
| 4 | `'3'` | `"a"` | `'d'` | `"ad"` | `["ad"]` |
| 5 | `'3'` | `"a"` | `'e'` | `"ae"` | `["ad", "ae"]` |
| 6 | `'3'` | `"a"` | `'f'` | `"af"` | `["ad", "ae", "af"]` |
| 7 | `'3'` | `"b"` | `'d'` | `"bd"` | `[..., "bd"]` |
| 8 | `'3'` | `"b"` | `'e'` | `"be"` | `[..., "bd", "be"]` |
| 9 | `'3'` | `"b"` | `'f'` | `"bf"` | `[..., "be", "bf"]` |
| 10 | `'3'` | `"c"` | `'d'` | `"cd"` | `[..., "bf", "cd"]` |
| 11 | `'3'` | `"c"` | `'e'` | `"ce"` | `[..., "cd", "ce"]` |
| 12 | `'3'` | `"c"` | `'f'` | `"cf"` | `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]` |

---

## 5. Algorithmic Correctness

**Soundness.** Every emitted string has length equal to $|\text{digits}|$, and its $k$-th character belongs strictly to $\text{Keypad}[\text{digits}[k]]$. Therefore, every generated string is a valid representation of the input digits.

**Completeness.** By definition of the Cartesian product, any valid combination $C = c_0 c_1 \dots c_{K-1}$ requires $c_k \in \text{Keypad}[\text{digits}[k]]$. Because the tree branches over every member of $\text{Keypad}[\text{digits}[k]]$ at each level, the unique path leading to $C$ is traversed. No valid combination can be omitted.

---

## 6. Traps This Instance Exposes

- **Empty String Edge Case:** When $\text{digits} = \text{""}$, the mathematical Cartesian product of zero sets is $\{ \emptyset \}$, which in list terms would be `[""]`. However, the problem specification explicitly mandates returning `[]` (empty list). An early check `if not digits: return []` is required.
- **Varying Set Sizes:** Digits `7` and `9` map to 4 letters (`pqrs` and `wxyz`), whereas digits `2`, `3`, `4`, `5`, `6`, and `8` map to 3 letters. The algorithm must use the dynamic size of each letter array rather than assuming a fixed degree of 3.
- **Exponential Output Size:** For $N$ digits, the total number of combinations is up to $4^N$. Because $N \le 4$, the maximum output length is $4^4 = 256$, making complete generation feasible and optimal.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(4^N \cdot N)$, where $N = |\text{digits}|$. There are at most $4^N$ combinations. Constructing each string of length $N$ takes $O(N)$ time. Since $N \le 4$, $4^4 \cdot 4 = 1024$ operations, executing in under 1 millisecond.
- **Auxiliary Space Complexity:** $O(N)$ for recursion call stack in DFS, or $O(4^N \cdot N)$ to store the output combinations.

### 1. Description

You have `n`  `tiles`, where each tile has one letter $\text{tiles}[i]$ printed on it.

Return *the number of possible non-empty sequences of letters* you can make using the letters printed on those `tiles`.

### 2. Function Contract

**Inputs**

- `tiles`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $tiles = "AAB"$
- **Output:** `8`
- **Explanation:** The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".

#### Example 2

- **Input:** $tiles = "AAABBC"$
- **Output:** `188`

#### Example 3

- **Input:** $tiles = "V"$
- **Output:** `1`

### 4. Constraints

- $1 \le \text{tiles.length} \le 7$

- `tiles` consists of uppercase English letters.

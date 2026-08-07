### 1. Description

You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $jewels = "aA", stones = "aAAbbbb"$
- **Output:** `3`
#### Example 2

- **Input:** $jewels = "z", stones = "ZZ"$
- **Output:** `0`

### 4. Constraints

- $1 \le \text{jewels.length}, \text{stones.length} \le 50$

- `jewels` and `stones` consist of only English letters.

- All the characters of `jewels` are **unique**.
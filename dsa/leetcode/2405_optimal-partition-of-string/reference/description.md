### 1. Description

Given a string `s`, partition the string into one or more **substrings** such that the characters in each substring are **unique**. That is, no letter appears in a single substring more than **once**.

Return *the **minimum** number of substrings in such a partition.*

Note that each character should belong to exactly one substring in a partition.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "abacaba"`
- **Output:** `4`
- **Explanation:**
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.
#### Example 2

- **Input:** `s = "ssssss"`
- **Output:** `6`
- **Explanation:**
**The only valid partition is ("s","s","s","s","s","s").

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only English lowercase letters.
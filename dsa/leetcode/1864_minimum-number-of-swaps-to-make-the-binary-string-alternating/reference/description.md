### 1. Description

Given a binary string `s`, return *the **minimum** number of character swaps to make it **alternating**, or *`-1`* if it is impossible.*

The string is called **alternating** if no two adjacent characters are equal. For example, the strings `"010"` and `"1010"` are alternating, while the string `"0100"` is not.

Any two characters may be swapped, even if they are **not adjacent**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** `s = "111000"`
- **Output:** `1`
- **Explanation:** Swap positions 1 and 4: "1<u>1</u>10<u>0</u>0" -> "1<u>0</u>10<u>1</u>0"
The string is now alternating.
#### Example 2

- **Input:** `s = "010"`
- **Output:** `0`
- **Explanation:** The string is already alternating, no swaps are needed.
#### Example 3

- **Input:** `s = "1110"`
- **Output:** `-1`

### 4. Constraints

- $1 \le \text{s.length} \le 1000$

- $s[i]$ is either `'0'` or `'1'`.
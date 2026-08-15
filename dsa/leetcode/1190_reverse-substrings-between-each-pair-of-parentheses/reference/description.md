### 1. Description

You are given a string `s` that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should **not** contain any brackets.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** `s = "(abcd)"`
- **Output:** `"dcba"`

#### Example 2

- **Input:** `s = "(u(love)i)"`
- **Output:** `"iloveu"`
- **Explanation:** The substring "love" is reversed first, then the whole string is reversed.

#### Example 3

- **Input:** `s = "(ed(et(oc))el)"`
- **Output:** `"leetcode"`
- **Explanation:** First, we reverse the substring "oc", then "etco", and finally, the whole string.

### 4. Constraints

- $1 \le \text{s.length} \le 2000$

- `s` only contains lower case English characters and parentheses.

- It is guaranteed that all parentheses are balanced.

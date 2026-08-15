### 1. Description

You are given an array of strings `words` and a string `chars`.

A string is **good** if it can be formed by characters from `chars` (each character can only be used once for **each** word in `words`).

Return *the sum of lengths of all good strings in words*.

### 2. Function Contract

**Inputs**

- `words`: Input parameter (`List[str]`).
- `chars`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $words = ["cat","bt","hat","tree"], chars = "atach"$
- **Output:** `6`
- **Explanation:** The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.

#### Example 2

- **Input:** $words = ["hello","world","leetcode"], chars = "welldonehoneyr"$
- **Output:** `10`
- **Explanation:** The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.

### 4. Constraints

- $1 \le \text{words.length} \le 1000$

- $1 \le \text{words}[i].length, \text{chars.length} \le 100$

- $\text{words}[i]$ and `chars` consist of lowercase English letters.

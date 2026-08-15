### 1. Description

Given a string `s`, return `true`* if *`s`* is a **good** string, or *`false`* otherwise*.

A string `s` is **good** if **all** the characters that appear in `s` have the **same** number of occurrences (i.e., the same frequency).

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `bool`.

### 3. Examples

#### Example 1

- **Input:** `s = "abacbc"`
- **Output:** `true`
- **Explanation:** The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.

#### Example 2

- **Input:** `s = "aaabb"`
- **Output:** `false`
- **Explanation:** The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

### 4. Constraints

- $1 \le \text{s.length} \le 1000$

- `s` consists of lowercase English letters.

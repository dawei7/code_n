### 1. Description

You are given a **palindromic** string `s`.

Return the **lexicographically smallest** palindromic permutation of `s`.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `str`.

### 3. Examples

#### Example 1

- **Input:** s = "z"

- **Output:** "z"

- **Explanation:** A string of only one character is already the lexicographically smallest palindrome.

#### Example 2

- **Input:** s = "babab"

- **Output:** "abbba"

- **Explanation:** Rearranging `"babab"` → `"abbba"` gives the smallest lexicographic palindrome.

#### Example 3

- **Input:** s = "daccad"

- **Output:** "acddca"

- **Explanation:** Rearranging `"daccad"` → `"acddca"` gives the smallest lexicographic palindrome.

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of lowercase English letters.

- `s` is guaranteed to be palindromic.

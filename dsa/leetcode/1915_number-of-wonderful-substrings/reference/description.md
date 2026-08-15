### 1. Description

A **wonderful** string is a string where **at most one** letter appears an **odd** number of times.

- For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

Given a string `word` that consists of the first ten lowercase English letters (`'a'` through `'j'`), return *the **number of wonderful non-empty substrings** in *`word`*. If the same substring appears multiple times in *`word`*, then count **each occurrence** separately.*

A **substring** is a contiguous sequence of characters in a string.

### 2. Function Contract

**Inputs**

- `word`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $word = "aba"$
- **Output:** `4`
- **Explanation:** The four wonderful substrings are underlined below:
- "<u>**a**</u>ba" -> "a"
- "a<u>**b**</u>a" -> "b"
- "ab<u>**a**</u>" -> "a"
- "<u>**aba**</u>" -> "aba"

#### Example 2

- **Input:** $word = "aabb"$
- **Output:** `9`
- **Explanation:** The nine wonderful substrings are underlined below:
- "**<u>a</u>**abb" -> "a"
- "<u>**aa**</u>bb" -> "aa"
- "<u>**aab**</u>b" -> "aab"
- "<u>**aabb**</u>" -> "aabb"
- "a<u>**a**</u>bb" -> "a"
- "a<u>**abb**</u>" -> "abb"
- "aa<u>**b**</u>b" -> "b"
- "aa<u>**bb**</u>" -> "bb"
- "aab<u>**b**</u>" -> "b"

#### Example 3

- **Input:** $word = "he"$
- **Output:** `2`
- **Explanation:** The two wonderful substrings are underlined below:
- "**<u>h</u>**e" -> "h"
- "h**<u>e</u>**" -> "e"

### 4. Constraints

- $1 \le \text{word.length} \le 10^{5}$

- `word` consists of lowercase English letters from `'a'` to `'j'`.

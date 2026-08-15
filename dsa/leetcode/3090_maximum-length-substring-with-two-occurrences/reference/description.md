### 1. Description

Given a string `s`, return the **maximum** length of a substring such that it contains *at most two occurrences* of each character.

### 2. Function Contract

**Inputs**

- `s`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** s = "bcbbbcba"

- **Output:** 4

- **Explanation:** The following substring has a length of 4 and contains at most two occurrences of each character: `"bcbb<u>bcba</u>"`.

#### Example 2

- **Input:** s = "aaaa"

- **Output:** 2

- **Explanation:** The following substring has a length of 2 and contains at most two occurrences of each character: `"<u>aa</u>aa"`.

### 4. Constraints

- $2 \le \text{s.length} \le 100$

- `s` consists only of lowercase English letters.

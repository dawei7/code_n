### 1. Description

You are given a string `word`. A letter is called **special** if it appears **both** in lowercase and uppercase in `word`.

Return the number of* ***special** letters in* *`word`.

### 2. Function Contract

**Inputs**

- `word`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** word = "aaAbcBC"

- **Output:** 3

- **Explanation:** The special characters in `word` are `'a'`, `'b'`, and `'c'`.

#### Example 2

- **Input:** word = "abc"

- **Output:** 0

- **Explanation:** No character in `word` appears in uppercase.

#### Example 3

- **Input:** word = "abBCab"

- **Output:** 1

- **Explanation:** The only special character in `word` is `'b'`.

### 4. Constraints

- $1 \le \text{word.length} \le 50$

- `word` consists of only lowercase and uppercase English letters.

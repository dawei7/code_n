### 1. Description

You are given a string `word`. A letter `c` is called **special** if it appears **both** in lowercase and uppercase in `word`, and **every** lowercase occurrence of `c` appears before the **first** uppercase occurrence of `c`.

Return the number of* ***special** letters* *in* *`word`.

### 2. Function Contract

**Inputs**

- `word`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** word = "aaAbcBC"

- **Output:** 3

- **Explanation:** The special characters are `'a'`, `'b'`, and `'c'`.

#### Example 2

- **Input:** word = "abc"

- **Output:** 0

- **Explanation:** There are no special characters in `word`.

#### Example 3

- **Input:** word = "AbBCab"

- **Output:** 0

- **Explanation:** There are no special characters in `word`.

### 4. Constraints

- $1 \le \text{word.length} \le 2 * 10^{5}$

- `word` consists of only lowercase and uppercase English letters.

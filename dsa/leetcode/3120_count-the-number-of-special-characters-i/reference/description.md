### 1. Description

You are given a string `word`. A letter is called **special** if it appears **both** in lowercase and uppercase in `word`.

Return the number of* ***special** letters in* *`word`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** word = "aaAbcBC"

**Output:** 3

**Explanation:**

The special characters in `word` are `'a'`, `'b'`, and `'c'`.

</div>
#### Example 2

<div class="example-block">
**Input:** word = "abc"

**Output:** 0

**Explanation:**

No character in `word` appears in uppercase.

</div>
#### Example 3

<div class="example-block">
**Input:** word = "abBCab"

**Output:** 1

**Explanation:**

The only special character in `word` is `'b'`.

</div>

### 4. Constraints

- $1 \le \text{word.length} \le 50$

- `word` consists of only lowercase and uppercase English letters.
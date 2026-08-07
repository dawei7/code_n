### 1. Description

Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and **may** press a key for too long, resulting in a character being typed **multiple** times.

Although Alice tried to focus on her typing, she is aware that she may still have done this **at most** *once*.

You are given a string `word`, which represents the **final** output displayed on Alice's screen.

Return the total number of *possible* original strings that Alice *might* have intended to type.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** word = "abbcccc"

**Output:** 5

**Explanation:**

The possible strings are: `"abbcccc"`, `"abbccc"`, `"abbcc"`, `"abbc"`, and `"abcccc"`.

</div>
#### Example 2

<div class="example-block">
**Input:** word = "abcd"

**Output:** 1

**Explanation:**

The only possible string is `"abcd"`.

</div>
#### Example 3

<div class="example-block">
**Input:** word = "aaaa"

**Output:** 4

</div>

### 4. Constraints

- $1 \le \text{word.length} \le 100$

- `word` consists only of lowercase English letters.
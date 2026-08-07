## Description

Alice and Bob are playing a game. Initially, Alice has a string $word = "a"$.

You are given a **positive** integer `k`.

Now Bob will ask Alice to perform the following operation **forever**:

- Generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`.

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the $$k^{\text{th}}$$ character in `word`, after enough operations have been done for `word` to have **at least** `k` characters.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** k = 5

**Output:** "b"

**Explanation:**

Initially, $word = "a"$. We need to do the operation three times:

- Generated string is `"b"`, `word` becomes `"ab"`.

- Generated string is `"bc"`, `word` becomes `"abbc"`.

- Generated string is `"bccd"`, `word` becomes `"abbcbccd"`.

</div>
#### Example 2

<div class="example-block">
**Input:** k = 10

**Output:** "c"

</div>
### Constraints

- $1 \le k \le 500$
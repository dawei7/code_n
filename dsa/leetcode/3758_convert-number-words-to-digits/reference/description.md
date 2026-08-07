## Description

You are given a string `s` consisting of lowercase English letters. `s` may contain **valid concatenated** English words representing the digits 0 to 9, without spaces.

Your task is to **extract** each valid number word **in order** and convert it to its corresponding digit, producing a string of digits.

Parse `s` from left to right. At each position:

- If a valid number word starts at the current position, append its corresponding digit to the result and advance by the length of that word.

- Otherwise, skip **exactly** one character and continue parsing.

Return the resulting digit string. If no number words are found, return an empty string.
### Function Contract

**Inputs**

- `s`: A nonempty lowercase English string to parse from left to right.

The valid words are `zero`, `one`, `two`, `three`, `four`, `five`, `six`, `seven`, `eight`, and `nine`. A partial word is not a match, and a failed position advances by exactly one character rather than discarding a longer fragment.

**Return value**

Return the string formed by the corresponding digits of all matched number words, in discovery order, or `""` if there are no matches.

### Examples

#### Example 1

<div class="example-block">
**Input:** s = "onefourthree"

**Output:** "143"

**Explanation:**

- Parsing from left to right, extract the valid number words "one", "four", "three".

- These map to digits 1, 4, 3. Thus, the final result is `"143"`.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "ninexsix"

**Output:** "96"

**Explanation:**

- The substring `"nine"` is a valid number word and maps to 9.

- The character `"x"` does not match any valid number word prefix and is skipped.

- Then, the substring `"six"` is a valid number word and maps to 6, so the final result is `"96"`.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "zeero"

**Output:** ""

**Explanation:**

- No substring forms a valid number word during left-to-right parsing.

- All characters are skipped and incomplete fragments are ignored, so the result is an empty string.

</div>
#### Example 4

<div class="example-block">
**Input:** s = "tw"

**Output:** ""

**Explanation:**

- No substring forms a valid number word during left-to-right parsing.

- All characters are skipped and incomplete fragments are ignored, so the result is an empty string.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` contains only lowercase English letters.
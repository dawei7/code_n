## Description

You are given a string `s` representing a list of words. Each letter in the word has one or more options.

- If there is one option, the letter is represented as is.

- If there is more than one option, then curly braces delimit the options. For example, `"{a,b,c}"` represents options `["a", "b", "c"]`.

For example, if `s = "a{b,c}"`, the first character is always `'a'`, but the second character can be `'b'` or `'c'`. The original list is `["ab", "ac"]`.

Return all words that can be formed in this manner, **sorted** in lexicographical order.
### Function Contract

**Input**

- `s`: a valid string made from lowercase English letters, curly braces, and commas.

A lowercase letter outside braces is fixed. The distinct letters within one brace group are alternatives for a single output position, and different groups are chosen independently. Brace groups do not nest.

Let $n$ be the length of `s`, $L$ the number of output positions after each brace group is treated as one position, and $R$ the number of words represented by the expression.

**Return value**

- A list containing all $R$ possible words, sorted in lexicographical order.
- Every returned word has length $L$.

### Examples

#### Example 1

- **Input:** `s = "{a,b}c{d,e}f"`
- **Output:** `["acdf","acef","bcdf","bcef"]`
#### Example 2

- **Input:** `s = "abcd"`
- **Output:** `["abcd"]`
### Constraints

- $1 \le \text{s.length} \le 50$

- `s` consists of curly brackets `'{}'`, commas `','`, and lowercase English letters.

- `s` is guaranteed to be a valid input.

- There are no nested curly brackets.

- All characters inside a pair of consecutive opening and ending curly brackets are different.
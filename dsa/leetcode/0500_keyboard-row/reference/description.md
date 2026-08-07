## Description

Given an array of strings `words`, return *the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below*.

**Note** that the strings are **case-insensitive**, both lowercased and uppercased of the same letter are treated as if they are at the same row.

In the **American keyboard**:

- the first row consists of the characters `"qwertyuiop"`,

- the second row consists of the characters `"asdfghjkl"`, and

- the third row consists of the characters `"zxcvbnm"`.

![](images/keyboard.png)
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** words = ["Hello","Alaska","Dad","Peace"]

**Output:** ["Alaska","Dad"]

**Explanation:**

Both `"a"` and `"A"` are in the 2nd row of the American keyboard due to case insensitivity.

</div>
#### Example 2

<div class="example-block">
**Input:** words = ["omk"]

**Output:** []

</div>
#### Example 3

<div class="example-block">
**Input:** words = ["adsdf","sfd"]

**Output:** ["adsdf","sfd"]

</div>
### Constraints

- $1 \le \text{words.length} \le 20$

- $1 \le \text{words}[i].length \le 100$

- $\text{words}[i]$ consists of English letters (both lowercase and uppercase).
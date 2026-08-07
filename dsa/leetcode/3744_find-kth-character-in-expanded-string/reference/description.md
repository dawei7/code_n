## Description

You are given a string `s` consisting of one or more words separated by single spaces. Each word in `s` consists of lowercase English letters.

We obtain the **expanded** string `t` from `s` as follows:

- For each **word** in `s`, repeat its first character once, then its second character twice, and so on.

For example, if `s = "hello world"`, then $t = "heelllllllooooo woorrrllllddddd"$.

You are also given an integer `k`, representing a **valid** index of the string `t`.

Return the $$k^{\text{th}}$$ character of the string `t`.
### Function Contract

**Inputs**

- `s`: One or more lowercase words with exactly one space between adjacent words.
- `k`: A valid zero-based index into the conceptual expanded string `t`.

Character positions restart at `1` after every separator. A separator itself contributes exactly one character to `t` and is not part of either neighboring word.

Let $n=\lvert\texttt{s}\rvert$ for the complexity bounds.

**Return value**

Return the one-character string `t[k]` without requiring `t` to be materialized.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "hello world", k = 0

**Output:** "h"

**Explanation:**

$t = "heelllllllooooo woorrrllllddddd"$. Therefore, the answer is $t[0] = "h"$.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "hello world", k = 15

**Output:** " "

**Explanation:**

$t = "heelllllllooooo woorrrllllddddd"$. Therefore, the answer is $t[15] = " "$.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` contains only lowercase English letters and spaces `' '`.

- `s` **does not contain** any leading or trailing spaces.

- All the words in `s` are separated by a **single space**.

- $0 \le k < \text{t.length}$. That is, `k` is a **valid** index of `t`.
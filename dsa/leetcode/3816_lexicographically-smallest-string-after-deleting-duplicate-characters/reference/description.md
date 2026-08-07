### 1. Description

You are given a string `s` that consists of lowercase English letters.

You can perform the following operation any number of times (possibly zero times):

- Choose any letter that appears **at least twice** in the current string `s` and delete any **one** occurrence.

Return the **lexicographically smallest** resulting string that can be formed this way.

### 2. Function Contract

**Inputs**

- `s`: A non-empty string of lowercase English letters.

Let $N=\lvert\texttt{s}\rvert$. Every result is a subsequence of `s`. An occurrence can be deleted only while another copy of the same letter remains, so the final string contains every distinct letter that occurred in `s` at least once. It may retain additional copies; deleting every duplicate is not necessarily lexicographically optimal.

**Return value**

Return the lexicographically smallest subsequence reachable under the deletion rule.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** s = "aaccb"

**Output:** "aacb"

**Explanation:**

We can form the strings `"acb"`, `"aacb"`, `"accb"`, and `"aaccb"`. `"aacb"` is the lexicographically smallest one.

For example, we can obtain `"aacb"` by choosing `'c'` and deleting its first occurrence.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "z"

**Output:** "z"

**Explanation:**

We cannot perform any operations. The only string we can form is `"z"`.

</div>

### 4. Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` contains lowercase English letters only.
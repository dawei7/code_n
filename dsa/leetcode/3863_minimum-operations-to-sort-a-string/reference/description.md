## Description

You are given a string `s` consisting of lowercase English letters.

In one operation, you can select any **substring** of `s` that is **not** the entire string and **sort** it in **non-descending alphabetical** order.

Return the **minimum** number of operations required to make `s` sorted in **non-descending** order. If it is not possible, return -1.
### Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $N = \lvert\texttt{s}\rvert$. An operation selects indices `left` and
`right` with `0 <= left <= right < N`, except that `left = 0` and
`right = N - 1` may not both hold. It replaces `s[left:right + 1]` by those
same characters sorted in non-descending alphabetical order.

**Return value**

Return the minimum number of permitted operations needed to make the whole
string non-descending. Return `-1` if no sequence of permitted operations can
do so.

### Examples
#### Example 1

<div class="example-block">
**Input:** s = "dog"

**Output:** 1

**Explanation:**​​​​​​​

- Sort substring `"og"` to `"go"`.

- Now, `s = "dgo"`, which is sorted in ascending order. Thus, the answer is 1.

</div>
#### Example 2

<div class="example-block">
**Input:** s = "card"

**Output:** 2

**Explanation:**

- Sort substring `"car"` to `"acr"`, so `s = "acrd"`.

- Sort substring `"rd"` to `"dr"`, making `s = "acdr"`, which is sorted in ascending order. Thus, the answer is 2.

</div>
#### Example 3

<div class="example-block">
**Input:** s = "gf"

**Output:** -1

**Explanation:**

- It is impossible to sort `s` under the given constraints. Thus, the answer is -1.

</div>
### Constraints

- $1 \le \text{s.length} \le 10^{5}$

- `s` consists of only lowercase English letters.
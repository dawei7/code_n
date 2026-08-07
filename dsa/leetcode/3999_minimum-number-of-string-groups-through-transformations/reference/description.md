## Description

You are given an array of strings `words`.

Define a **transformation** on a string `s` as follows:

- Let `E` be the subsequence of characters at even indices of `s`.

- Let `O` be the **subsequence** of characters at odd indices of `s`.

- **Independently** cyclically shift `E` and `O` by **any** number of positions to the right, possibly zero.

- Reconstruct the string by placing the shifted `E` characters back into even indices and the shifted `O` characters back into odd indices.

Two strings are **equivalent** if one can be transformed into the other by a **single** transformation.

Partition `words` into the **minimum** number of groups such that:

- Every string belongs to **exactly** one group.

- Every pair of strings in the same group are **equivalent**.

Return an integer denoting the **minimum** number of groups.
### Function Contract

**Inputs**

- `words`: An array of nonempty strings containing lowercase English letters.

For one word `w`, its even-index sequence is $w[0], w[2], w[4], ...$, and its odd-index sequence is $w[1], w[3], w[5], ...$. Both sequences include every character of the indicated parity. Let

$S = \sum_{w \in \texttt{words}} \lvert w \rvert$

denote the total number of input characters.

**Return value**

Return an integer equal to the minimum number of groups in a partition where every two strings in the same group are equivalent.

### Examples

#### Example 1

<div class="example-block">
**Input:** words = ["ntgwz","zwntg"]

**Output:** 1

**Explanation:**

- For `"ntgwz"`, the even-index subsequence is `"ngz"` and the odd-index subsequence is `"tw"`.

- Shift `"ngz"` right by `1` position to obtain `"zng"`, and shift `"tw"` right by `1` position to obtain `"wt"`.

- After reconstructing the string, we obtain `"zwntg"`.

- Therefore, both strings are equivalent and belong to the same group.

</div>
#### Example 2

<div class="example-block">
**Input:** words = ["abc","cab","bac","acb","bca","cba"]

**Output:** 3

**Explanation:**

The strings can be partitioned into the following groups:

- `["abc","cba"]`

- `["cab","bac"]`

- `["acb","bca"]`

</div>
#### Example 3

<div class="example-block">
**Input:** words = ["leet","abb","bab","deed","edde","code","bba"]

**Output:** 5

**Explanation:**

The strings can be partitioned into the following groups:

- `["abb","bba"]`

- `["deed","edde"]`

- `["leet"]`

- `["bab"]`

- `["code"]`

​​​​​​​​​​​​​​All pairs of strings in each group are equivalent.

</div>
### Constraints

- $1 \le \text{words.length} \le 10^{5}$

- $1 \le \text{words}[i].length \le 5 * 10^{5}$

- The sum of $\text{words}[i].length$ does not exceed $5 * 10^{5}$.

- $\text{words}[i]$ consist of lowercase English letters.
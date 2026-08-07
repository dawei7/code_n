### 1. Description

You are given an array of binary strings `strs` and two integers `m` and `n`.

Return *the size of the largest subset of `strs` such that there are **at most** *`m`* *`0`*'s and *`n`* *`1`*'s in the subset*.

A set `x` is a **subset** of a set `y` if all elements of `x` are also elements of `y`.

### 2. Function Contract

**Inputs**

- `strs`: the array of nonempty binary strings
- `m`: the maximum total number of `0` characters available
- `n`: the maximum total number of `1` characters available

**Return value**

- Return the maximum cardinality of a subset whose combined zero and one counts stay within their respective
  budgets.

Unused capacity is allowed. The objective counts selected strings, not their characters, and duplicate strings at
different array positions remain separate selectable elements.

### 3. Examples

#### Example 1

- **Input:** $strs = ["10","0001","111001","1","0"], m = 5, n = 3$
- **Output:** `4`
- **Explanation:** The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
#### Example 2

- **Input:** $strs = ["10","0","1"], m = 1, n = 1$
- **Output:** `2`
- **Explanation:** The largest subset is {"0", "1"}, so the answer is 2.

### 4. Constraints

- $1 \le \text{strs.length} \le 600$

- $1 \le \text{strs}[i].length \le 100$

- $\text{strs}[i]$ consists only of digits `'0'` and `'1'`.

- $1 \le m, n \le 100$
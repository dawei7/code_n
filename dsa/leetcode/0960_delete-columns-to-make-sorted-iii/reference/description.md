### 1. Description

You are given an array of `n` strings `strs`, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have $strs = ["abcdef","uvwxyz"]$ and deletion indices `{0, 2, 3}`, then the final array after deletions is `["bef", "vyz"]`.

Suppose we chose a set of deletion indices `answer` such that after deletions, the final array has **every string (row) in lexicographic** order. (i.e., $(\text{strs}[0][0] \le \text{strs}[0][1] \le ... \le \text{strs}[0][\text{strs}[0].length - 1])$, and $(\text{strs}[1][0] \le \text{strs}[1][1] \le ... \le \text{strs}[1][\text{strs}[1].length - 1])$, and so on). Return *the minimum possible value of* `answer.length`.

### 2. Function Contract

**Inputs**

- `strs`: Input parameter (`List[str]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $strs = ["babca","bbazb"]$
- **Output:** `3`
- **Explanation:** After deleting columns 0, 1, and 4, the final array is strs = ["bc", "az"].
Both these rows are individually in lexicographic order (ie. strs[0][0] <= strs[0][1] and strs[1][0] <= strs[1][1]).
Note that strs[0] > strs[1] - the array strs is not necessarily in lexicographic order.

#### Example 2

- **Input:** $strs = ["edcba"]$
- **Output:** `4`
- **Explanation:** If we delete less than 4 columns, the only row will not be lexicographically sorted.

#### Example 3

- **Input:** $strs = ["ghi","def","abc"]$
- **Output:** `0`
- **Explanation:** All rows are already lexicographically sorted.

### 4. Constraints

- $n = \text{strs.length}$

- $1 \le n \le 100$

- $1 \le \text{strs}[i].length \le 100$

- $\text{strs}[i]$ consists of lowercase English letters.

-

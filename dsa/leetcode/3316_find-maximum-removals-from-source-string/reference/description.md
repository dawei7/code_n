### 1. Description

You are given a string `source` of size `n`, a string `pattern` that is a subsequence of `source`, and a **sorted** integer array `targetIndices` that contains **distinct** numbers in the range `[0, n - 1]`.

We define an **operation** as removing a character at an index `idx` from `source` such that:

- `idx` is an element of `targetIndices`.

- `pattern` remains a subsequence of `source` after removing the character.

Performing an operation **does not** change the indices of the other characters in `source`. For example, if you remove `'c'` from `"acb"`, the character at index 2 would still be `'b'`.

Return the **maximum** number of *operations* that can be performed.

### 2. Function Contract

**Inputs**

- `source`: Input parameter (`str`).
- `pattern`: Input parameter (`str`).
- `targetIndices`: Input parameter (`List[int]`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** source = "abbaa", pattern = "aba", targetIndices = [0,1,2]

- **Output:** 1

- **Explanation:** We can't remove $\text{source}[0]$ but we can do either of these two operations:

- Remove $\text{source}[1]$, so that `source` becomes $"a_{baa}"$.

- Remove $\text{source}[2]$, so that `source` becomes $"\text{ab}_{aa}"$.

#### Example 2

- **Input:** source = "bcda", pattern = "d", targetIndices = [0,3]

- **Output:** 2

- **Explanation:** We can remove $\text{source}[0]$ and $\text{source}[3]$ in two operations.

#### Example 3

- **Input:** source = "dda", pattern = "dda", targetIndices = [0,1,2]

- **Output:** 0

- **Explanation:** We can't remove any character from `source`.

#### Example 4

- **Input:** source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4]

- **Output:** 2

- **Explanation:** We can remove $\text{source}[2]$ and $\text{source}[3]$ in two operations.

### 4. Constraints

- $1 \le n = \text{source.length} \le 3 * 10^{3}$

- $1 \le \text{pattern.length} \le n$

- $1 \le \text{targetIndices.length} \le n$

- `targetIndices` is sorted in ascending order.

- The input is generated such that `targetIndices` contains distinct elements in the range `[0, n - 1]`.

- `source` and `pattern` consist only of lowercase English letters.

- The input is generated such that `pattern` appears as a subsequence in `source`.

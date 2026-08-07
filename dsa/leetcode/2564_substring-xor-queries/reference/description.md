## Description

You are given a **binary string** `s`, and a **2D** integer array `queries` where $\text{queries}[i] = [\text{first}_{i}, \text{second}_{i}]$.

For the $$i^{\text{th}}$$query, find the **shortest substring** of `s` whose **decimal value**, `val`, yields$\text{second}_{i}$when **bitwise XORed** with$\text{first}_{i}$. In other words,$val ^ \text{first}_{i} = \text{second}_{i}$.

The answer to the $$i^{\text{th}}$$query is the endpoints (**0-indexed**) of the substring$[\text{left}_{i}, \text{right}_{i}]$or `[-1, -1]` if no such substring exists. If there are multiple answers, choose the one with the **minimum**$\text{left}_{i}$.

*Return an array* `ans` *where* $\text{ans}[i] = [\text{left}_{i}, \text{right}_{i}]$ *is the answer to the* $$i^{\text{th}}$$ *query.*

A **substring** is a contiguous non-empty sequence of characters within a string.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** `s = "101101", queries = [[0,5],[1,2]]`
- **Output:** `[[0,2],[2,3]]`
- **Explanation:** For the first query the substring in range [0,2] is **"101"** which has a decimal value of **5**, and **5 ^ 0 = 5**, hence the answer to the first query is [0,2]. In the second query, the substring in range [2,3] is **"11",** and has a decimal value of **3**, and **3 ^ 1 = 2**. So, [2,3] is returned for the second query.
#### Example 2

- **Input:** `s = "0101", queries = [[12,8]]`
- **Output:** `[[-1,-1]]`
- **Explanation:** In this example there is no substring that answers the query, hence [-1,-1] is returned.
#### Example 3

- **Input:** `s = "1", queries = [[4,5]]`
- **Output:** `[[0,0]]`
- **Explanation:** For this example, the substring in range [0,0] has a decimal value of **1**, and **1 ^ 4 = 5**. So, the answer is [0,0].
### Constraints

- $1 \le \text{s.length} \le 10^{4}$

- $s[i]$ is either `'0'` or `'1'`.

- $1 \le \text{queries.length} \le 10^{5}$

- $0 \le \text{first}_{i}, \text{second}_{i} \le 10^{9}$
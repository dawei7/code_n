# Fair Distribution of Cookies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2305 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/fair-distribution-of-cookies/) |

## Problem Description
### Goal
`cookies[i]` is the number of cookies in bag $i$. Distribute every bag among
exactly `k` children. A bag is indivisible: all of its cookies must go to one
child, although a child may receive several bags or none.

The unfairness of a distribution is the largest total received by any one
child. Among all possible assignments of bags to children, return the minimum
achievable unfairness.

### Function Contract
**Inputs**

- `cookies`: An array of $n$ positive bag sizes.
- `k`: The number of children available to receive bags.

The contract guarantees $2\le n\le8$, $1\le\texttt{cookies[i]}\le10^5$, and
$2\le k\le n$.

**Return value**

The smallest possible value of $\max_{0\le j<k} L_j$, where $L_j$ is child
$j$'s total cookie load after assigning every bag once.

### Examples
**Example 1**

- Input: `cookies = [8, 15, 10, 20, 8]`, `k = 2`
- Output: `31`
- Explanation: Loads $31$ from `[8, 15, 8]` and $30$ from `[10, 20]` attain
  unfairness $31$.

**Example 2**

- Input: `cookies = [6, 1, 3, 2, 2, 4, 1, 2]`, `k = 3`
- Output: `7`
- Explanation: The bags can produce three loads of $7$: `[6, 1]`,
  `[3, 2, 2]`, and `[4, 1, 2]`.

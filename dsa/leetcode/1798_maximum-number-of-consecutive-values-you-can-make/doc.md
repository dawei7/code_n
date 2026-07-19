# Maximum Number of Consecutive Values You Can Make

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/) |
| Frontend ID | 1798 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You have several coins, and `coins[i]` is the value printed on the $i$-th coin. Each coin may be selected at most once. The value of a chosen subset is the sum of its coins; choosing no coins produces value $0$.

Determine the maximum number of consecutive integer values, beginning with $0$, that can be formed from subsets of the given coins. Equivalently, return the smallest nonnegative value that cannot be formed.

### Function Contract

**Inputs**

- `coins`: a list of $n$ positive integers, where $1 \le n \le 4 \cdot 10^4$ and $1 \le \texttt{coins[i]} \le 4 \cdot 10^4$.

**Return value**

- Return the number of consecutive values starting from $0$ that can be formed by selecting each coin zero or one time.

### Examples

**Example 1**

- Input: `coins = [1,3]`
- Output: `2`

The values $0$ and $1$ are formable, but $2$ is not.

**Example 2**

- Input: `coins = [1,1,1,4]`
- Output: `8`

Every value from $0$ through $7$ can be formed.

**Example 3**

- Input: `coins = [1,4,10,3,1]`
- Output: `20`

The coins can form every value from $0$ through $19$.

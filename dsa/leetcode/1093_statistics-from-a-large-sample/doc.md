# Statistics from a Large Sample

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1093 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Probability and Statistics |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open](https://leetcode.com/problems/statistics-from-a-large-sample/) |

## Problem Description

### Goal

A very large sample contains integers in the range $[0, 255]$. Rather than listing every observation, the sample is represented by an array `count` in which `count[k]` is the number of times the value `k` appears.

Calculate five statistics. The minimum and maximum are the smallest and largest observed values. The mean is the sum of all observations divided by their number. For an odd-sized sample, the median is its middle value after sorting; for an even-sized sample, it is the average of the two middle values. The mode is the most frequent value, and it is guaranteed to be unique. Return `[minimum, maximum, mean, median, mode]` as floating-point numbers; an error of at most $10^{-5}$ is accepted.

### Function Contract

**Inputs**

- `count`: an array of exactly 256 integers, where `count[k]` is the frequency of value `k`, $0 \leq \texttt{count[k]} \leq 10^9$, and the represented sample is nonempty.

Let

$$
N = \sum_{k=0}^{255} \texttt{count[k]}
$$

be the number of observations, where $1 \leq N \leq 10^9$. The histogram domain always has exactly 256 possible values.

**Return value**

A five-element list `[minimum, maximum, mean, median, mode]`. The unique mode is guaranteed by the input.

### Examples

**Example 1**

- Input: `count = [0, 1, 3, 4] + [0] * 252`
- Output: `[1.0, 3.0, 2.375, 2.5, 3.0]`

The represented sorted sample is `[1, 2, 2, 2, 3, 3, 3, 3]`. Its two middle values are 2 and 3.

**Example 2**

- Input: `count = [0, 4, 3, 2, 2] + [0] * 251`
- Output: `[1.0, 4.0, 2.1818181818, 2.0, 1.0]`

There are 11 observations, so the sixth sorted observation determines the median.

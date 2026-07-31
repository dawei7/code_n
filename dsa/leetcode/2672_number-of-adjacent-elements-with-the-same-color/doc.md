# Number of Adjacent Elements With the Same Color

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2672 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/) |

## Problem Description

### Goal

An array of length `n` begins with every position uncolored, represented by zero. Each query supplies an index and a positive color and replaces the current color at that index, even if the position was colored previously.

After every update, count adjacent index pairs whose two positions have the same nonzero color. A run of length $k$ contributes $k - 1$ pairs, and separate runs may use different colors. Return the count after each query in the original order.

### Function Contract

**Inputs**

- `n`: The array length, with $1 \le n \le 10^5$.
- `queries`: A list of $q$ updates `[index, color]`, where $1 \le q \le 10^5$, $0 \le \texttt{index} < n$, and $1 \le \texttt{color} \le 10^5$.

**Return value**

- Return an array of length $q$ whose entry `i` is the number of equal, positively colored adjacent pairs after applying `queries[i]`.

### Examples

**Example 1**

- Input: `n = 4`, `queries = [[0,2],[1,2],[3,1],[1,1],[2,1]]`
- Output: `[0,1,1,0,2]`
- Explanation: The final update joins positions 1, 2, and 3 into a run of color `1`, which contains two adjacent pairs.

**Example 2**

- Input: `n = 1`, `queries = [[0,100000]]`
- Output: `[0]`
- Explanation: A one-position array has no adjacent pair.

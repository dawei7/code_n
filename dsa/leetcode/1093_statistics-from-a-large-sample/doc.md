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

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Work with frequencies, not observations.** Expanding the histogram would require $O(N)$ time and space, even though only 256 distinct values can occur. Instead, one scan over `count` can maintain the total frequency, the weighted sum, the first and last occupied values, and the value with greatest frequency. Dividing the weighted sum by $N$ gives the mean.

**Locate the two central ranks cumulatively.** Use zero-based ranks `left_rank = (N - 1) // 2` and `right_rank = N // 2`. As the scan adds each frequency to a cumulative count, the first value whose cumulative count exceeds a rank is the observation at that sorted position. The ranks are equal when $N$ is odd; when $N$ is even, averaging their values produces the median without constructing the sample.

The first and last positive-frequency indices are exactly the sample's minimum and maximum. The weighted sum counts each value once for each occurrence, and cumulative frequencies partition the sorted sample into the same runs represented by the histogram. These facts establish every returned statistic directly from `count`.

#### Complexity detail

A generalized histogram with $K$ bins would take $O(K)$ time. Here $K=256$ is fixed by the contract, so the scan is $O(256)=O(1)$ and does not depend on $N$. Only scalar totals, ranks, and selected values are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Expand and sort the sample:** Materializing every value is straightforward, but costs $O(N \log N)$ time and $O(N)$ space and is infeasible when $N$ is near $10^9$.
- **Repeated rank scans:** Finding each statistic with a separate histogram traversal remains constant under the fixed domain, but one coordinated scan is simpler and avoids redundant work.
- **Single occupied bin:** The minimum, maximum, mean, median, and mode are all that bin's value.
- **Even sample size:** The two central ranks can fall in different bins, so both must be located before averaging.
- **Large frequencies:** Weighted sums and $N$ may exceed 32-bit integer range in other languages; use a sufficiently wide integer type before converting the mean to floating point.
- **Unique mode:** The contract removes tie-breaking ambiguity; updating the mode only for a strictly larger frequency is sufficient.

</details>

## Description

You are given an integer array `nums` of length `n` where `nums` is a permutation of the integers in the range `[1, n]`. You are also given a 2D integer array `sequences` where $\text{sequences}[i]$ is a subsequence of `nums`.

Check if `nums` is the shortest possible and the only **supersequence**. The shortest **supersequence** is a sequence **with the shortest length** and has all $\text{sequences}[i]$ as subsequences. There could be multiple valid **supersequences** for the given array `sequences`.

- For example, for $sequences = [[1,2],[1,3]]$, there are two shortest **supersequences**, `[1,2,3]` and `[1,3,2]`.

- While for $sequences = [[1,2],[1,3],[1,2,3]]$, the only shortest **supersequence** possible is `[1,2,3]`. `[1,2,3,4]` is a possible supersequence but not the shortest.

Return `true`* if *`nums`* is the only shortest **supersequence** for *`sequences`*, or *`false`* otherwise*.

A **subsequence** is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
### Function Contract

`solve(nums: list[int], sequences: list[list[int]]) -> bool`

### Inputs

- `nums`: A permutation of the integers in the inclusive range $[1,n]$.
- `sequences`: A nonempty collection of distinct, nonempty subsequences of `nums`.

Let $n = \lvert\texttt{nums}\rvert$, and let

$$
S = \sum_i \lvert\texttt{sequences}[i]\rvert.
$$

### Output

Return `true` if `nums` is the only shortest sequence that contains every row of `sequences` as a subsequence. Return `false` if `nums` is not shortest or if another shortest supersequence exists.

### Examples
#### Example 1

- **Input:** `nums = [1,2,3], sequences = [[1,2],[1,3]]`
- **Output:** `false`
- **Explanation:** There are two possible supersequences: [1,2,3] and [1,3,2].
The sequence [1,2] is a subsequence of both: [**<u>1</u>**,**<u>2</u>**,3] and [**<u>1</u>**,3,**<u>2</u>**].
The sequence [1,3] is a subsequence of both: [**<u>1</u>**,2,**<u>3</u>**] and [**<u>1</u>**,**<u>3</u>**,2].
Since nums is not the only shortest supersequence, we return false.
#### Example 2

- **Input:** `nums = [1,2,3], sequences = [[1,2]]`
- **Output:** `false`
- **Explanation:** The shortest possible supersequence is [1,2].
The sequence [1,2] is a subsequence of it: [**<u>1</u>**,**<u>2</u>**].
Since nums is not the shortest supersequence, we return false.
#### Example 3

- **Input:** `nums = [1,2,3], sequences = [[1,2],[1,3],[2,3]]`
- **Output:** `true`
- **Explanation:** The shortest possible supersequence is [1,2,3].
The sequence [1,2] is a subsequence of it: [**<u>1</u>**,**<u>2</u>**,3].
The sequence [1,3] is a subsequence of it: [**<u>1</u>**,2,**<u>3</u>**].
The sequence [2,3] is a subsequence of it: [1,**<u>2</u>**,**<u>3</u>**].
Since nums is the only shortest supersequence, we return true.
### Constraints

- $n = \text{nums.length}$

- $1 \le n \le 10^{4}$

- `nums` is a permutation of all the integers in the range `[1, n]`.

- $1 \le \text{sequences.length} \le 10^{4}$

- $1 \le \text{sequences}[i].length \le 10^{4}$

- $1 \le sum(\text{sequences}[i].length) \le 10^{5}$

- $1 \le \text{sequences}[i][j] \le n$

- All the arrays of `sequences` are **unique**.

- $\text{sequences}[i]$ is a subsequence of `nums`.
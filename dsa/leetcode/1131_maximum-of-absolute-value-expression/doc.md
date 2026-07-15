# Maximum of Absolute Value Expression

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1131 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-of-absolute-value-expression/) |

## Problem Description

### Goal

You are given two integer arrays, `arr1` and `arr2`, with the same length. For any two valid indices $i$ and $j$, consider the sum of the absolute difference between their `arr1` values, the absolute difference between their `arr2` values, and the absolute difference between the indices themselves.

Return the maximum possible value of

$$
\lvert \texttt{arr1[i]}-\texttt{arr1[j]} \rvert
+ \lvert \texttt{arr2[i]}-\texttt{arr2[j]} \rvert
+ \lvert i-j \rvert
$$

over every pair satisfying $0 \le i,j < n$. The two indices may be equal, though such a choice contributes zero and cannot beat a positive value from distinct points.

### Function Contract

**Inputs**

- `arr1`: an integer array of length $n$, where $2 \le n \le 4 \times 10^4$ and every value lies in $[-10^6,10^6]$.
- `arr2`: an integer array with the same length and value bounds as `arr1`.

**Return value**

The maximum value of the stated absolute-difference expression over all valid index pairs.

### Examples

**Example 1**

- Input: `arr1 = [1,2,3,4]`, `arr2 = [-1,4,5,6]`
- Output: `13`

**Example 2**

- Input: `arr1 = [1,-2,-5,0,10]`, `arr2 = [0,-2,-1,-7,-4]`
- Output: `20`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Expand each absolute value by signs.** For fixed indices, the expression equals the maximum over sign choices $s_1,s_2,s_3 \in \{-1,1\}$ of

$$
s_1(\texttt{arr1[i]}-\texttt{arr1[j]})
+s_2(\texttt{arr2[i]}-\texttt{arr2[j]})
+s_3(i-j).
$$

For a fixed sign triple, define $F(k)=s_1\texttt{arr1[k]}+s_2\texttt{arr2[k]}+s_3k$. The best ordered pair for that triple is simply $\max F-\min F$.

**Reduce eight forms to four.** Negating all three signs negates every $F(k)$ but leaves its range unchanged. Each form with $s_3=-1$ therefore has the same range as the all-sign-negated form with $s_3=1$. It is enough to scan the four choices for $(s_1,s_2)$ while using `+ index`.

**Track only extrema.** For each of those four forms, scan corresponding positions of the two arrays, compute `value = s1 * arr1[index] + s2 * arr2[index] + index`, and retain its minimum and maximum. Their difference is the best pair under that sign form. Taking the largest of the four ranges covers the sign pattern selected by every possible index pair, so it equals the original maximum.

#### Complexity detail

Four scans each process all $n$ positions with constant work, giving $O(n)$ time. Only the current minimum, maximum, and answer are stored for each sign choice, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Compare every index pair:** Direct evaluation is simple and correct but takes $O(n^2)$ time.
- **Store all transformed values:** Computing and sorting each sign form also works, but uses $O(n)$ space and $O(n \log n)$ time when only extrema are needed.
- **Negative array values:** Sign expansion handles them without any separate cases.
- **Equal points at distinct indices:** Even when both array coordinates match, the index term contributes their distance.
- **Repeated extrema:** Only the range matters; it is harmless if several indices attain the same minimum or maximum.

</details>

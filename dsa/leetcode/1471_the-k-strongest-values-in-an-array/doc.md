# The k Strongest Values in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1471 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/the-k-strongest-values-in-an-array/) |

## Problem Description
### Goal

For an integer array `arr`, define its median as the element at index $\lfloor (n-1)/2 \rfloor$ after the array has been sorted in ascending order, where $n$ is the array length. This is the ordinary middle element when $n$ is odd and the lower of the two middle elements when $n$ is even.

Let that median be $m$. A value $a$ is stronger than a value $b$ when $\lvert a-m\rvert > \lvert b-m\rvert$. If the two distances are equal, the larger value is stronger. Return the $k$ strongest occurrences from `arr` in any order. Repeated values remain distinct occurrences, so the result may contain duplicates.

### Function Contract
**Inputs**

- `arr`: an integer array with length $n$, where $1 \le n \le 10^5$.
- Every value satisfies $-10^5 \le \texttt{arr[i]} \le 10^5$.
- `k`: the number of occurrences to return, where $1 \le k \le n$.

**Return value**

Return an array containing exactly the $k$ strongest occurrences under the ordering induced by the pair

$$
(\lvert a-m\rvert,a).
$$

The result order is arbitrary, but its multiplicities must match those of the selected occurrences.

### Examples
**Example 1**

- Input: `arr = [1,2,3,4,5], k = 2`
- Output: `[5,1]`
- Explanation: The median is $3$. Values $5$ and $1$ both have distance $2$, and $5$ ranks ahead of $1$ because it is larger.

**Example 2**

- Input: `arr = [1,1,3,5,5], k = 2`
- Output: `[5,5]`
- Explanation: The median is $3$, and both occurrences of $5$ outrank both occurrences of $1$ on the equal-distance tie.

**Example 3**

- Input: `arr = [6,7,11,7,6,8], k = 5`
- Output: `[11,8,6,6,7]`
- Explanation: The median is $7$. The two copies of $6$ are separate selected occurrences, while either copy of $7$ may be the final occurrence.

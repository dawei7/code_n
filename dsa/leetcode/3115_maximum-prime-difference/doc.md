# Maximum Prime Difference

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3115 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [maximum-prime-difference](https://leetcode.com/problems/maximum-prime-difference/) |

## Problem Description

### Goal

You are given an integer array `nums` containing at least one prime number. Choose two indices whose values are prime and maximize the distance between those indices. The two chosen indices do not have to be different, so an array containing exactly one prime still has a valid answer of zero.

Return that maximum index distance. Since the greatest separation among qualifying positions is attained by the first and last prime-valued elements, the requested distance is their index difference. Remember that $1$ is not prime: a prime is an integer greater than $1$ whose only positive divisors are $1$ and itself.

### Function Contract

Let $n$ be the length of `nums`.

**Inputs**

- `nums`: A list of $n$ integers, where $1 \le n \le 3\cdot10^5$, $1 \le \texttt{nums[i]} \le 100$, and at least one element is prime.

**Return value**

- The maximum absolute difference between two indices containing prime values.

### Examples

#### Example 1

- **Input:** `nums = [4,2,9,5,3]`
- **Output:** `3`
- **Explanation:** Prime values occur at indices $1$, $3$, and $4$, so the largest distance is $lvert 4-1 \rvert=3$.

#### Example 2

- **Input:** `nums = [4,8,2,8]`
- **Output:** `0`
- **Explanation:** Index $2$ is the only prime-valued position and may be paired with itself.

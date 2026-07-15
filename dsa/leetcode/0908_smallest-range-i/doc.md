# Smallest Range I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 908 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-range-i/) |

## Problem Description
### Goal
You are given an integer array `nums` and a nonnegative integer `k`. For each index `i`, you may perform at most one operation that replaces `nums[i]` with `nums[i] + x`, where `x` is an integer in the inclusive range $[-k,k]$. The choice of `x` may differ between indices.

The score of the resulting array is its maximum element minus its minimum element. Choose the allowed change for every index so that this score is as small as possible, and return that minimum score.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 10^4$ and $0 \leq \texttt{nums}[i] \leq 10^4$.
- `k`: an integer with $0 \leq \texttt{k} \leq 10^4$.

**Return value**

Return the minimum possible difference between the largest and smallest array values after applying the operation at most once per index.

### Examples
**Example 1**

- Input: `nums = [1], k = 0`
- Output: `0`

A one-element array has equal maximum and minimum values.

**Example 2**

- Input: `nums = [0,10], k = 2`
- Output: `6`

Changing the array to `[2,8]` reduces the score to $8-2=6$.

**Example 3**

- Input: `nums = [1,3,6], k = 3`
- Output: `0`

All three values can be changed to `4`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**View each operation as a reachable interval**

An original value $v$ can become any integer in $[v-k,v+k]$; using $x=0$ also covers the choice to make no effective change. Let $a=\min(\texttt{nums})$ and $b=\max(\texttt{nums})$. No operation can raise the original minimum beyond $a+k$, and no operation can lower the original maximum below $b-k$. Therefore, if these endpoint intervals remain disjoint, every result has score at least

$$
(b-k)-(a+k)=b-a-2k.
$$

This bound is attainable. Raise the minimum toward $a+k$, lower the maximum toward $b-k$, and place every intermediate value inside that remaining interval; each intermediate value's reachable interval intersects it. If $a+k \geq b-k$, the reachable intervals of all elements share a common value, so every element can be made equal and the score becomes zero.

The answer is consequently $\max(0,b-a-2k)$. Only the original minimum and maximum affect it, so one scan is sufficient.

#### Complexity detail

Finding the minimum and maximum examines each of the $n$ values once, giving $O(n)$ time. Apart from those two extrema, no data structure grows with the input, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Sort the array:** The first and last sorted values give the same formula, but sorting costs $O(n\log n)$ time.
- **Compare every pair:** Computing the original spread as the largest pairwise difference is correct but takes $O(n^2)$ time.
- **Enumerate all changes:** Each index has $2k+1$ possible integer adjustments, making direct combination search exponential and unnecessary.
- **One element:** Its score is always zero regardless of `k`.
- **Zero adjustment range:** When `k = 0`, the original score cannot change.
- **Overlapping endpoint intervals:** If $b-a \leq 2k$, clamp the formula at zero because a score cannot be negative.
- **Interior values:** They cannot force a wider final range than the adjusted original extremes.
- **Duplicate extremes:** Repeated minimum or maximum values can all receive the same endpoint adjustment independently.

</details>

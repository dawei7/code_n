# Minimum Elements to Add to Form a Given Sum

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-elements-to-add-to-form-a-given-sum/) |
| Frontend ID | 1785 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

You are given an integer array `nums` and integers `limit` and `goal`. Every existing array value satisfies $\lvert\texttt{nums[i]}\rvert \le \texttt{limit}$.

You may add any integers to the array, but each new value must preserve the same absolute-value bound. Find the minimum number of elements that must be added so that the sum of the resulting array equals `goal`. Added values may be positive, negative, or zero as long as their absolute values do not exceed `limit`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 10^5$ and every value is between `-limit` and `limit`, inclusive.
- `limit`: the positive maximum absolute value of any array element, where $1 \le \texttt{limit} \le 10^6$.
- `goal`: the desired final sum, where $-10^9 \le \texttt{goal} \le 10^9$.

**Return value**

- Return the minimum number of bounded integers that must be appended to make the final array sum equal `goal`.

### Examples

**Example 1**

- Input: `nums = [1,-1,1], limit = 3, goal = -4`
- Output: `2`

The current sum is `1`. Adding `-2` and `-3` supplies the missing `-5`.

**Example 2**

- Input: `nums = [1,-10,9,1], limit = 100, goal = 0`
- Output: `1`

The current sum is `1`, so one added value `-1` is sufficient.

**Example 3**

- Input: `nums = [4,-7,3], limit = 5, goal = 0`
- Output: `0`

The array already has the requested sum.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce the array to its remaining signed gap**

First sum `nums`. Only the difference between that total and `goal` matters after this point: the individual existing values cannot be changed. Let

$$
D = \left\lvert \texttt{goal} - \sum_{x \in \texttt{nums}} x \right\rvert.
$$

The sign tells whether added values must increase or decrease the sum, while $D$ is the magnitude they must collectively supply.

**Derive an unavoidable lower bound**

One added element can change the sum toward the goal by at most `limit`. Therefore $k$ added elements can cover at most $k\cdot\texttt{limit}$ units of the gap. Any valid answer must satisfy

$$
k \ge \left\lceil \frac{D}{\texttt{limit}} \right\rceil.
$$

This proves that fewer elements cannot work.

**Show that the lower bound is attainable**

Use values with magnitude `limit` and the required sign until less than `limit` of the gap remains. If the remainder is nonzero, one final value equal to that signed remainder completes the sum and still satisfies the bound. When $D=0$, no value is needed.

Thus the lower bound is always constructible, making the minimum count $\lceil D/\texttt{limit}\rceil$. Integer arithmetic computes it as `(D + limit - 1) // limit`.

#### Complexity detail

Computing the current sum scans all $n$ values once, taking $O(n)$ time. The difference and ceiling division take constant additional time. Only scalar totals are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Repeatedly append maximal values:** Simulating each addition reaches the same answer but may take up to the returned count rather than computing it directly.
- **Dynamic programming over sums:** This treats the added values like a subset-sum problem, but arbitrary bounded integers make the simple magnitude bound exact; DP is unnecessary and potentially enormous.
- **Already at the goal:** When $D=0$, the ceiling is zero and no element should be appended.
- **Nondivisible gap:** A positive remainder requires one final partial-magnitude value.
- **Negative correction:** The same absolute-gap formula applies; only the conceptual sign of the constructed values changes.
- **Unit limit:** Each addition changes the sum by at most one, so the answer equals $D$.
- **Large totals:** Summing up to $10^5$ values of magnitude $10^6$ can exceed 32-bit range, so fixed-width implementations need a sufficiently wide integer type.

</details>

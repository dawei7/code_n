# Monotonic Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 896 |
| Difficulty | Easy |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/monotonic-array/) |

## Problem Description
### Goal
An array is monotonic when it is either monotone increasing or monotone decreasing.

The integer array `nums` is monotone increasing if every pair of indices $i \leq j$ satisfies $\texttt{nums}[i] \leq \texttt{nums}[j]$. It is monotone decreasing if every such pair satisfies $\texttt{nums}[i] \geq \texttt{nums}[j]$. Equal neighboring values are therefore allowed in either direction.

Given `nums`, determine whether at least one of these two definitions holds.

### Function Contract
Let $n$ be the length of `nums`.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 10^5$ and $-10^5 \leq \texttt{nums}[i] \leq 10^5$.

**Return value**

Return `True` if `nums` is monotone increasing or monotone decreasing; otherwise return `False`.

### Examples
**Example 1**

- Input: `nums = [1,2,2,3]`
- Output: `true`

**Example 2**

- Input: `nums = [6,5,4,4]`
- Output: `true`

**Example 3**

- Input: `nums = [1,3,2]`
- Output: `false`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track both possible directions**

Begin with two flags, one saying the sequence can still be monotone increasing and the other saying it can still be monotone decreasing. Scan adjacent pairs from left to right.

If `nums[i - 1] < nums[i]`, this rise rules out monotone decreasing. If `nums[i - 1] > nums[i]`, the drop rules out monotone increasing. Equality rules out neither direction. Once both flags are false, no later value can repair either earlier violation, so the scan may return `False` immediately.

Checking adjacent pairs is sufficient for the definitions involving every $i \leq j$. If every adjacent relation is $\leq$, chaining those relations gives $\texttt{nums}[i] \leq \texttt{nums}[j]$ for any earlier $i$ and later $j$. The same transitive argument applies to $\geq$. Thus a surviving increasing flag proves monotone increasing, a surviving decreasing flag proves monotone decreasing, and if neither survives the array is not monotonic.

#### Complexity detail

The scan examines at most $n-1$ adjacent pairs, so it takes $O(n)$ time. The two direction flags use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Infer a direction from the first unequal pair:** After skipping an equal prefix, check every later pair against that direction; this is also $O(n)$ time and $O(1)$ space.
- **Compare with sorted copies:** Testing `nums == sorted(nums)` or its reverse is concise, but sorting costs $O(n \log n)$ time and $O(n)$ additional space.
- **Check every index pair:** The definition can be evaluated literally, but the resulting $O(n^2)$ time is unnecessary because adjacent relations are transitive.
- **One element:** A singleton is both monotone increasing and monotone decreasing.
- **All values equal:** Both direction flags remain true, so the array is monotonic.
- **Late reversal:** A sequence can satisfy one direction for a long prefix and still fail; every adjacent pair must be inspected unless both flags become false earlier.
- **Boundary values:** Only comparisons are performed, so values at $-10^5$ and $10^5$ require no special arithmetic handling.

</details>

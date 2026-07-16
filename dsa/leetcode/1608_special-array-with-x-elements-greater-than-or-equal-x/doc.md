# Special Array With X Elements Greater Than or Equal X

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1608 |
| Difficulty | Easy |
| Topics | Array, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/) |

## Problem Description
### Goal
An array `nums` of non-negative integers is special when some number $x$ has exactly $x$ array elements greater than or equal to $x$. Elements below $x$ do not contribute to this count, and the number $x$ need not occur in the array itself.

Return this $x$ when it exists; otherwise return `-1`. A qualifying value is guaranteed to be unique.

### Function Contract
**Inputs**

- `nums`: an array of $n$ non-negative integers, where $1 \le n \le 100$ and $0 \le \texttt{nums[i]} \le 1000$.

**Return value**

Return the unique integer $x$ for which exactly $x$ elements are at least $x$, or `-1` if no such integer exists.

### Examples
**Example 1**

- Input: `nums = [3, 5]`
- Output: `2`
- Explanation: Both elements are at least 2, so exactly two elements meet the threshold.

**Example 2**

- Input: `nums = [0, 0]`
- Output: `-1`

**Example 3**

- Input: `nums = [0, 4, 3, 0, 4]`
- Output: `3`
- Explanation: The three values 4, 3, and 4 are at least 3.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn the count condition into a sorted boundary.** Sort the values in ascending order. At index $i$, the suffix from $i$ through the end contains exactly $x=n-i$ elements. This suffix is precisely the set of values at least $x$ when `nums[i] >= x` and either $i=0$ or `nums[i - 1] < x`.

**Check each possible suffix size once.** For every sorted index, compute `candidate = n - i` and test those two boundary inequalities. The current value proves all $x$ suffix members are at least $x$; the preceding-value test proves every element outside the suffix is smaller than $x$. Together they establish that the qualifying count is exactly $x$, not merely at least $x$.

If no boundary satisfies both conditions, no positive candidate works. The value $x=0$ cannot work for a nonempty non-negative array because all $n$ elements are at least zero, so returning `-1` is then correct.

#### Complexity detail

Sorting $n$ values costs $O(n\log n)$ time, and the boundary scan costs $O(n)$. The app-local implementation creates a sorted copy, using $O(n)$ space and leaving the supplied array unchanged.

#### Alternatives and edge cases

- **Count separately for every candidate:** Trying every $x$ from 0 through $n$ and rescanning the array is correct but takes $O(n^2)$ time.
- **Frequency buckets:** Since values are bounded, suffix counts over buckets can solve the problem in $O(n+M)$ time and $O(M)$ space for maximum value $M$.
- **Binary search with repeated lower bounds:** Sorting permits each threshold count to be found in $O(\log n)$, but the direct boundary scan is simpler and already linear after sorting.
- The candidate does not need to be present in `nums`; `[3, 5]` has answer 2.
- Elements equal to $x$ count because the comparison is greater than or equal to.
- All-zero nonempty arrays have no answer, including $x=0$.
- A one-element positive array has answer 1, while `[0]` has no answer.

</details>

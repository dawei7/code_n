# Array Partition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 561 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting, Counting Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/array-partition/) |

## Problem Description
### Goal
Given an integer array `nums` containing `2n` elements, divide all of its elements into exactly `n` pairs. Every element must belong to one pair, and the value contributed by a pair is the smaller of its two integers.

Return the maximized sum of these `n` minimum values. You may choose the pairs in any order, so the task is to arrange the elements so that pairing does not unnecessarily discard large values when each pair is reduced to its minimum.

### Function Contract
**Inputs**

- `nums`: a list containing `2n` integers

**Return value**

- The maximum possible sum of the minimum value from every pair

### Examples
**Example 1**

- Input: `nums = [1, 4, 3, 2]`
- Output: `4`

**Example 2**

- Input: `nums = [6, 2, 6, 5, 1, 2]`
- Output: `9`

**Example 3**

- Input: `nums = [-1, -2]`
- Output: `-2`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort values from smallest to largest**

After sorting, every value's closest available partner on its right is at least as large. Pairing adjacent values makes the smaller member of each pair as large as possible without wasting a larger value.

**Take every even sorted position**

Form pairs `(sorted[0], sorted[1])`, `(sorted[2], sorted[3])`, and so on. The minimum of each pair is its first element, so the answer is the sum of indices `0, 2, 4, ...`.

**Why separating adjacent values cannot help**

Consider the smallest unpaired value. It must be the minimum of whichever pair contains it, so pairing it with anything larger contributes the same smallest value. Choosing the next-smallest value as its partner leaves all larger values available to form the remaining pairs. Repeating this exchange argument produces adjacent sorted pairs without decreasing any contribution, proving the greedy arrangement is optimal.

#### Complexity detail

Sorting `2n` values takes $O(n \log n)$ time, and the stride-two sum is linear. Creating a sorted copy uses $O(n)$ space.

#### Alternatives and edge cases

- **Counting sort:** uses the bounded value range to achieve $O(n + R)$ time and $O(R)$ space for range width `R`.
- **Repeatedly extract two minima:** produces the same pairs but linear searches and removals make it $O(n^2)$.
- **Enumerate all pairings:** is correct but grows super-exponentially with the number of pairs.
- **Negative values:** sorting and adjacency remain optimal even though the result may be negative.
- **Duplicate values:** are separate elements and may be paired together.
- **One pair:** its smaller element is the entire answer.
- **Input preservation:** sorting a copy avoids changing the caller's list.

</details>

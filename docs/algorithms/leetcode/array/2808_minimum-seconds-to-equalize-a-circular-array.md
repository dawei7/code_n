# Minimum Seconds to Equalize a Circular Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2808 |
| Difficulty | Medium |
| Topics | Array, Hash Table |
| Official Link | [minimum-seconds-to-equalize-a-circular-array](https://leetcode.com/problems/minimum-seconds-to-equalize-a-circular-array/) |

## Problem Description & Examples
### Goal
Given a circular array of integers, in each second, you can replace any element with its immediate neighbors (left or right). Determine the minimum number of seconds required to make all elements in the array equal to the same value.

### Function Contract
**Inputs**

- `nums`: A list of integers representing the circular array.

**Return value**

- An integer representing the minimum seconds needed to make all elements equal.

### Examples
**Example 1**

- Input: `nums = [1, 2, 1, 2]`
- Output: `1`

**Example 2**

- Input: `nums = [2, 1, 3, 3, 2]`
- Output: `2`

**Example 3**

- Input: `nums = [5, 5, 5, 5]`
- Output: `0`

---

## Underlying Base Algorithm(s)
The problem can be solved by identifying the maximum gap between occurrences of each unique number in the circular array. For a specific value $x$, if the indices where $x$ appears are $i_1, i_2, \dots, i_k$, the time required to fill the gaps between these occurrences is $\lfloor \text{gap} / 2 \rfloor$. Because the array is circular, the gap between the last occurrence and the first occurrence (wrapping around) must also be considered. We calculate this for every unique number and return the minimum of these maximum gaps.

---

## Complexity Analysis
- **Time Complexity**: $O(n)$, where $n$ is the length of the array. We iterate through the array once to store indices and once more to calculate the gaps for each unique element.
- **Space Complexity**: $O(n)$ to store the indices of each unique element in a hash map.

# Count Elements With Maximum Frequency

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3005 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Counting |
| Official Link | [count-elements-with-maximum-frequency](https://leetcode.com/problems/count-elements-with-maximum-frequency/) |

## Problem Description & Examples
### Goal
Given an array of integers, identify the frequency of each unique element. Determine the highest frequency present in the array, and return the total count of all elements that appear with that specific maximum frequency.

### Function Contract
**Inputs**

- `nums`: A list of integers where 1 ≤ nums[i] ≤ 100.

**Return value**

- An integer representing the sum of the counts of all elements that share the maximum frequency.

### Examples
**Example 1**

- Input: `nums = [1, 2, 2, 3, 1, 4]`
- Output: `4`
- Explanation: The frequencies are: 1: 2, 2: 2, 3: 1, 4: 1. The max frequency is 2. Elements 1 and 2 both appear 2 times, so 2 + 2 = 4.

**Example 2**

- Input: `nums = [1, 2, 3, 4, 5]`
- Output: `5`
- Explanation: All elements appear once. The max frequency is 1. There are 5 such elements, so 1 * 5 = 5.

**Example 3**

- Input: `nums = [10, 12, 11, 10, 12, 11]`
- Output: `6`
- Explanation: All elements appear twice. The max frequency is 2. There are 3 such elements, so 2 * 3 = 6.

---

## Underlying Base Algorithm(s)
The problem utilizes a Frequency Map (Hash Table) to perform a single-pass counting operation. By tracking the maximum frequency encountered during the counting process, we can calculate the final result in a second pass or by maintaining a running sum of elements that match the current maximum.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of elements in the input array, as we iterate through the list once to count frequencies and once through the frequency map.
- **Space Complexity**: `O(k)`, where `k` is the number of unique elements in the array, used to store the frequency map.

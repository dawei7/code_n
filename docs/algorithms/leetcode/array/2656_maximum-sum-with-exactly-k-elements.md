# Maximum Sum With Exactly K Elements 

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2656 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [maximum-sum-with-exactly-k-elements](https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/) |

## Problem Description & Examples
### Goal
Given an array of integers `nums` and an integer `k`, the objective is to maximize a cumulative score by performing exactly `k` operations. In each operation, you must select an element `m` from the array, add `m` to your score, remove `m` from the array, and then insert `m + 1` back into the array. The task is to return the highest possible total score after `k` such operations.

### Function Contract
**Inputs**

- `nums`: A list of integers, representing the initial set of numbers. Constraints: `1 <= nums.length <= 100`, `1 <= nums[i] <= 100`.
- `k`: An integer, representing the exact number of operations to perform. Constraints: `1 <= k <= 100`.

**Return value**

- An integer, representing the maximum possible score achievable after `k` operations.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5]`, `k = 3`
- Output: `18`
- Explanation:
    1. Select `5` (the largest). Score becomes `5`. `nums` becomes `[1,2,3,4,6]`.
    2. Select `6` (the largest). Score becomes `5 + 6 = 11`. `nums` becomes `[1,2,3,4,7]`.
    3. Select `7` (the largest). Score becomes `11 + 7 = 18`. `nums` becomes `[1,2,3,4,8]`.
    The maximum score is `18`.

**Example 2**

- Input: `nums = [4,2,3,1]`, `k = 1`
- Output: `4`
- Explanation:
    1. Select `4` (the largest). Score becomes `4`. `nums` becomes `[2,3,1,5]`.
    The maximum score is `4`.

**Example 3**

- Input: `nums = [10]`, `k = 5`
- Output: `60`
- Explanation:
    1. Select `10`. Score `10`. `nums` becomes `[11]`.
    2. Select `11`. Score `10+11=21`. `nums` becomes `[12]`.
    3. Select `12`. Score `21+12=33`. `nums` becomes `[13]`.
    4. Select `13`. Score `33+13=46`. `nums` becomes `[14]`.
    5. Select `14`. Score `46+14=60`. `nums` becomes `[15]`.
    The maximum score is `60`.

---

## Underlying Base Algorithm(s)
**Greedy Approach:**
To maximize the total score, at each step, it is always optimal to select the largest available number in the `nums` array. This is because selecting a number `m` adds `m` to the score and replaces `m` with `m+1`. Since `m+1` is strictly greater than `m`, choosing the largest `m` ensures that we gain the maximum possible points in the current step, and also potentially introduce an even larger number (`m+1`) into the array for future steps. This strategy guarantees that the numbers chosen in subsequent steps are also maximized.

Following this greedy strategy:
1. Find the maximum element in the initial `nums` array. Let this be `max_val`.
2. In the first operation, we pick `max_val`, add it to the score, and `max_val + 1` is added to the array.
3. In the second operation, the largest available number will be `max_val + 1` (assuming `max_val` was unique or `max_val + 1` is now the new maximum). We pick `max_val + 1`, add it to the score, and `max_val + 2` is added to the array.
4. This pattern continues for `k` operations. The numbers picked will be `max_val`, `max_val + 1`, `max_val + 2`, ..., up to `max_val + (k - 1)`.

The total score is the sum of this arithmetic series:
`Score = max_val + (max_val + 1) + ... + (max_val + k - 1)`
This sum can be calculated efficiently using the formula for the sum of an arithmetic series, or by observing that it's `k * max_val` plus the sum of `0` to `k-1`.
`Score = k * max_val + (k * (k - 1) // 2)`

---

## Complexity Analysis
- **Time Complexity**: `O(N)` where `N` is the length of the `nums` array. This is dominated by the initial step of finding the maximum element in `nums`. The subsequent calculation of the sum is `O(1)` as it involves a simple arithmetic formula.
- **Space Complexity**: `O(1)`. Only a few variables are needed to store the maximum value and the final score, regardless of the input size.

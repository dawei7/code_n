# Minimum Size Subarray Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 209 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) |

## Problem Description
### Goal
Given a positive integer `target` and a list of positive integers `nums`, choose a nonempty contiguous subarray whose values sum to at least `target`. The interval must use consecutive positions and cannot skip elements or wrap around the array.

Return the minimum length among all qualifying intervals. A one-element interval is valid when its value already reaches the target, and positive values ensure extending an interval never decreases its sum. If even the full array cannot reach `target`, return `0` rather than an interval length. The function returns only the length, not the selected elements or their indices.

### Function Contract
**Inputs**

- `target`: a positive required sum
- `nums`: a list of positive integers

**Return value**

The minimum qualifying length, or zero when no subarray qualifies.

### Examples
**Example 1**

- Input: `target = 7, nums = [2,3,1,2,4,3]`
- Output: `2`

**Example 2**

- Input: `target = 4, nums = [1,4,4]`
- Output: `1`

**Example 3**

- Input: `target = 20, nums = [1,2,3]`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The positivity of every array value creates the monotonicity needed for a sliding window. Extending the right boundary can only increase the sum; removing the leftmost value can only decrease it.

Keep a window `[left, right]` and its running sum. Add each new right value. Whenever the sum reaches or exceeds `target`, the current window qualifies, so record its length and remove `nums[left]`, advancing `left`. Continue shrinking while the sum still qualifies: this finds the shortest qualifying window with that fixed right endpoint.

For `target = 7` and `[2,3,1,2,4,3]`, the window first qualifies at `[2,3,1,2]` with length four and shrinks. Later, ending at `4`, it finds `[1,2,4]` and then `[2,4]` where applicable; ending at the final `3`, shrinking reaches `[4,3]` of length two, the optimum.

After the shrinking loop for each right endpoint, the remaining window sum is below target. Every start position skipped during that loop was evaluated while its window still qualified, so no shorter candidate ending there is lost.

For a fixed right endpoint, increasing `left` strictly decreases the sum because all values are positive. The loop examines qualifying starts from earliest to latest and stops exactly at the first nonqualifying one, thereby recording the shortest qualifying window ending at that right endpoint. Every contiguous subarray has some right endpoint, so considering every endpoint includes the global optimum. If no window ever qualifies, the best-length sentinel remains unchanged and returning zero is correct.

#### Complexity detail

The right pointer advances `n` times. Although shrinking is nested syntactically, the left pointer also advances at most `n` times over the entire run. Total time is $O(n)$, and the two indices, sum, and best length use $O(1)$ space.

#### Alternatives and edge cases

- Prefix sums are strictly increasing here, so binary-searching a target prefix for each start gives $O(n \log n)$ time.
- Trying every start and end is $O(n^2)$.
- This sliding-window proof fails when negative numbers are allowed: removing a negative value can increase the sum, so monotonic shrinking disappears.
- One value may satisfy the target; the whole array may be the only qualifying window.
- If the total sum is below target, return zero.

</details>

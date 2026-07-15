# Check If a Number Is Majority Element in a Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1150 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/) |

## Problem Description

### Goal

Given an integer array `nums` sorted in non-decreasing order and an integer `target`, determine whether `target` is a majority element of the array. Because the input is sorted, every occurrence of a value occupies one contiguous interval.

A majority element is an element that appears more than half the array length. The comparison is strict: when `target` occurs exactly `nums.length / 2` times, it is not a majority. Return `true` only when the number of occurrences exceeds that threshold; otherwise return `false`.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$.
- `nums` is sorted in non-decreasing order.
- `target`: the value to test, with $1 \le \texttt{nums[i]}, \texttt{target} \le 10^9$.

**Return value**

`true` if `target` occurs more than $n/2$ times in `nums`; otherwise `false`.

### Examples

**Example 1**

- Input: `nums = [2,4,5,5,5,5,5,6,6], target = 5`
- Output: `true`
- Explanation: `5` occurs five times, and $5 > 9/2$.

**Example 2**

- Input: `nums = [10,100,101,101], target = 101`
- Output: `false`
- Explanation: Two occurrences equal half the array length but do not exceed it.

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Locate the first possible occurrence.** Binary search for the leftmost index `first` whose value is at least `target`. If `target` exists, this is its first occurrence because equal values are contiguous in a non-decreasing array.

**Test the majority-sized offset.** More than half of $n$ means at least $\lfloor n/2 \rfloor+1$ occurrences. Starting at `first`, that many equal values exist exactly when index `first + n // 2` is inside the array and still contains `target`. This single lookup simultaneously proves the target exists and reaches the strict-majority count.

**Why no second boundary is needed.** If the offset value is `target`, sorted contiguity guarantees every position from `first` through that offset is also `target`, establishing enough occurrences. If it is out of bounds or contains a larger value, the target's contiguous block is too short. A smaller value cannot occur there because `first` is the first value at least as large as `target`.

#### Complexity detail

The lower-bound binary search halves its remaining range each step, taking $O(\log n)$ time. The offset check is constant time, and only index variables are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Count every element:** A linear scan is straightforward but ignores the sorted order and takes $O(n)$ time.
- **Two binary searches:** Finding both lower and upper bounds also gives the exact frequency in $O(\log n)$ time, but the majority-offset test needs only the lower bound.
- **Exactly half:** The result is `false` because majority requires strictly more than half.
- **Absent target:** The lower bound may equal `n` or point to a larger value; the offset test safely returns `false`.
- **Single element:** It is a majority precisely when it equals `target`.
- **Target at an endpoint:** The same lower-bound and offset logic applies without a special case.

</details>

# Majority Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 169 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Divide and Conquer, Sorting, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/majority-element/) |

## Problem Description
### Goal
Given a nonempty list of integers, one value is guaranteed to appear more than $\left\lfloor n / 2 \right\rfloor$ times. Other values may repeat as well, and occurrences of the majority need not be adjacent or appear in any particular order.

Return the majority value itself. Its frequency must be strictly greater than half the list length, not merely tied for the highest frequency. Negative values and zero are valid candidates. Meet the intended linear-time and constant-extra-space target rather than sorting the array or building a frequency table proportional to the number of distinct values.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list containing a guaranteed majority element

**Return value**

The majority value.

### Examples
**Example 1**

- Input: `nums = [3,2,3]`
- Output: `3`

**Example 2**

- Input: `nums = [2,2,1,1,1,2,2]`
- Output: `2`

**Example 3**

- Input: `nums = [7]`
- Output: `7`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Boyer–Moore majority vote turns the strict majority guarantee into pair cancellation. Keep a `candidate` and a `balance`. When the balance is zero, adopt the current value as the new candidate. A matching value increases the balance; a different value decreases it.

A decrement conceptually removes one occurrence of the current candidate together with one occurrence of a different value. Removing unequal pairs cannot destroy a true majority: if one value originally occurs more often than all other values combined, it still does after one occurrence is removed from each side.

Trace `[2, 2, 1, 1, 1, 2, 2]`:

- The first two `2`s establish candidate `2` with balance two.
- Two `1`s cancel that balance to zero.
- The next `1` becomes the new candidate.
- The following `2` cancels it, and the final `2` becomes the surviving candidate.

Temporary candidates do not need to be the majority of the prefix. The balance summarizes only the unmatched residue after unequal-pair cancellations; the guarantee concerns what must survive after all cancellations across the complete array.

After each processed prefix, the balance represents that many uncanceled copies of the current candidate after removing pairs of unequal values. The global majority cannot be completely removed by such cancellations because it outnumbers all non-majority occurrences combined. Therefore, after processing the whole array, the surviving candidate must be the guaranteed majority element. Under this problem's guarantee, no second verification pass is necessary.

#### Complexity detail

The algorithm processes every value once, giving $O(n)$ time. It stores one candidate and one counter, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- A frequency map is straightforward and $O(n)$ time, but consumes $O(n)$ additional space in the worst case.
- Sorting places the majority at the middle index, but costs $O(n \log n)$ time and may mutate the input.
- If a majority were not guaranteed, Boyer–Moore would produce only a candidate; a second linear pass would be required to verify its frequency.
- A one-element array returns its only value. Negative numbers and zero require no special treatment.

</details>

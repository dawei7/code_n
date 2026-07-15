# Find Numbers with Even Number of Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1295 |
| Difficulty | Easy |
| Topics | Array, Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-numbers-with-even-number-of-digits/) |

## Problem Description
### Goal
Given an array `nums` of positive integers, inspect the ordinary decimal representation of every value. A number qualifies when its representation contains an even number of digits. For example, a two-digit or four-digit value qualifies, whereas a one-digit or three-digit value does not. The representations have no leading zeroes, so each value's magnitude determines its digit count unambiguously.

Return how many array elements qualify. Repeated values count separately because the question counts elements, not distinct integers.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 500$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

The number of indices whose value has two, four, or six decimal digits.

### Examples
**Example 1**

- Input: `nums = [12,345,2,6,7896]`
- Output: `2`
- Explanation: Only 12 and 7896 have even digit counts.

**Example 2**

- Input: `nums = [555,901,482,1771]`
- Output: `1`

**Example 3**

- Input: `nums = [10,100,1000]`
- Output: `2`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The constraint $1 \le x \le 100000$ permits only one through six decimal digits. The even-length ranges are therefore $[10,99]$ for two digits, $[1000,9999]$ for four digits, and the single six-digit value $100000$.

Scan the array once. Increment the answer whenever the current value lies in one of those three ranges. These ranges are disjoint and collectively contain every legal value with an even number of digits, so each qualifying element is counted exactly once and every nonqualifying element is excluded.

#### Complexity detail

The scan performs a constant number of comparisons for each of the $n$ values, giving $O(n)$ time. The counter and current value use $O(1)$ auxiliary space; no string representation or frequency table is created.

#### Alternatives and edge cases

- **String conversion:** Testing `len(str(value)) % 2` is concise, but creates a temporary representation and ignores the small fixed value domain.
- **Repeated division by ten:** Counting digits arithmetically works in $O(d)$ per value, where $d$ is its digit count, but the fixed range checks are simpler here.
- **Powers of ten:** Values 10, 1000, and 100000 begin even-digit ranges, while 100 and 10000 begin odd-digit ranges.
- **Repeated values:** Every occurrence contributes independently to the result.
- **Smallest value:** One has one decimal digit and does not qualify.

</details>

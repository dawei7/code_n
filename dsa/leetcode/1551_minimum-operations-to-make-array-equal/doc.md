# Minimum Operations to Make Array Equal

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1551 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-array-equal/) |

## Problem Description
### Goal
For a positive integer `n`, consider the length-$n$ array defined by `arr[i] = 2 * i + 1` for every zero-based index `i`. Thus, the array contains the first $n$ positive odd numbers.

In one operation, choose two indices and decrease one selected value by one while increasing the other selected value by one. Determine the minimum number of operations needed to make every array element equal. Each operation preserves the total sum, and the input guarantees that equality is achievable.

### Function Contract
**Inputs**

- `n`: the array length, where $1 \le n \le 10^4$.

**Return value**

The minimum number of paired decrement/increment operations required to make all values in the implicitly defined array equal.

### Examples
**Example 1**

- Input: `n = 3`
- Output: `2`
- Explanation: The array is `[1, 3, 5]`; transferring two units from five to one produces `[3, 3, 3]`.

**Example 2**

- Input: `n = 6`
- Output: `9`
- Explanation: The array's average is six, and the total deficit of values below six is nine.

**Example 3**

- Input: `n = 1`
- Output: `0`
- Explanation: A one-element array is already equal.

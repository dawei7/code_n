# Missing Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 268 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Binary Search, Bit Manipulation, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/missing-number/) |

## Problem Description
### Goal
Given an array `nums` of length `n`, its entries are unique values selected from the complete integer range `0` through `n`. Exactly one value from that range is absent, and the input order is arbitrary.

Return the missing value. It may be either endpoint `0` or `n`, not only a gap between two present values. Preserve the input and meet the intended linear-time, constant-extra-space requirement rather than constructing a full set proportional to the range. The function returns the omitted integer itself, not an index at which it should be inserted.

### Function Contract
**Inputs**

- `nums`: distinct values drawn from `[0,n]`, with one omitted

**Return value**

The omitted value.

### Examples
**Example 1**

- Input: `nums = [3,0,1]`
- Output: `2`

**Example 2**

- Input: `nums = [0,1]`
- Output: `2`

**Example 3**

- Input: `nums = [9,6,4,2,3,5,7,0,1]`
- Output: `8`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Supply the one range value absent from the indices**

Initialize an XOR accumulator with `n`. For every array index, XOR both the index and its stored value into the accumulator.

After processing a prefix, the accumulator is the XOR of `n`, every processed index, and every processed value. Equal range values cancel in pairs because $x \oplus x = 0$.

**Pair cancellation leaves only the missing value**

The indices contribute `0` through $n - 1$, and seeding with `n` completes the full expected range. The array contributes every member of that range except the answer. Each present value therefore occurs twice in the combined XOR and cancels with itself, while the missing value occurs only on the expected-range side and remains.

#### Complexity detail

One constant-time XOR update per element gives $O(n)$ time. A single accumulator uses $O(1)$ space.

#### Alternatives and edge cases

- **Set membership:** uses $O(n)$ extra space.
- **Test each candidate against the list:** can take $O(n^2)$.
- The missing value may be zero or `n`; a one-element input is handled identically.

</details>

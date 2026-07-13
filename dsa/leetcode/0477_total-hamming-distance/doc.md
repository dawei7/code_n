# Total Hamming Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 477 |
| Difficulty | Medium |
| Topics | Array, Math, Bit Manipulation |
| Official Link | [LeetCode](https://leetcode.com/problems/total-hamming-distance/) |

## Problem Description
### Goal
Given an array of nonnegative integers, consider every unordered pair of distinct indices $i < j$. The Hamming distance of their values is the number of binary bit positions where one value has `0` and the other has `1`.

Return the sum of these distances across all index pairs. Duplicate values at different positions still define a pair but contribute zero between themselves, while each differing bit contributes independently to every cross-group pair at that position. Leading zeroes common to all values add nothing. The function returns the aggregate total, not individual pair distances.

### Function Contract
**Inputs**

- `nums`: nonnegative integers

**Return value**

- The sum, over all index pairs $i < j$, of the bit positions where `nums[i]` and `nums[j]` differ

### Examples
**Example 1**

- Input: `nums = [4, 14, 2]`
- Output: `6`

**Example 2**

- Input: `nums = [4, 14, 4]`
- Output: `4`

**Example 3**

- Input: `nums = [0, 7]`
- Output: `3`

### Required Complexity

- **Time:** $O(n \cdot b)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Count pair contributions one bit at a time**

At one bit position, let `ones` numbers contain a one and `zeros = n - ones` contain a zero. A pair contributes one Hamming-distance unit at this position exactly when it chooses one member from each group.

**Multiply the two groups**

There are `ones * zeros` unordered cross-group pairs. Add that product for every relevant bit position. Each pair's differing bits are counted once at their own positions, so summing these independent contributions equals the total pairwise Hamming distance.

**Avoid constructing pairs**

The counting argument aggregates all pairs sharing a bit difference. This replaces quadratic pair enumeration with one scan of the array per fixed-width bit position.

#### Complexity detail

For `b` relevant bits, counting ones across `n` values takes $O(n \cdot b)$ time. Under the problem's 31-bit bound, `b` is constant. Only counters are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every pair:** XOR and population count are simple but take $O(n^2 \cdot b)$ conceptual time.
- **Accumulate bit counts in one value scan:** maintains a fixed array of `b` counters, using $O(b)$ constant-bounded space.
- **One value:** has no pair and contributes zero.
- **Duplicate values:** their mutual distance is zero but they still pair with other values separately.
- **All zeros or all equal:** every bit has an empty cross group, so the total is zero.
- **High bits:** include every significant position up to the input bound.
- **Large pair count:** use a sufficiently wide accumulator in fixed-width languages.

</details>

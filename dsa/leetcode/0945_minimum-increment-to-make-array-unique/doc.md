# Minimum Increment to Make Array Unique

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 945 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Counting |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-increment-to-make-array-unique/) |

## Problem Description

### Goal

You are given an integer array `nums`. One move chooses an index `i` and performs `nums[i] += 1`; values may only be increased, never decreased or replaced by an arbitrary number.

Find the minimum total number of these single-step increments needed so that every value in the array is unique. The final values themselves do not need to be returned, and the test data guarantees that the minimum move count fits in a 32-bit integer.

### Function Contract

Let $n$ be the length of `nums`, and define

$$
M = \max(\texttt{nums}) + n + 1,
$$

the number of value positions sufficient to distribute all duplicates.

**Inputs**

- `nums`: a list of $n$ integers with $1 \le n \le 10^5$ and `0 <= nums[i] <= 100000`.

**Return value**

Return the minimum number of unit increments required to make all array values pairwise distinct.

### Examples

**Example 1**

- Input: `nums = [1, 2, 2]`
- Output: `1`

Incrementing one copy of `2` once produces distinct values such as `[1, 2, 3]`.

**Example 2**

- Input: `nums = [3, 2, 1, 2, 1, 7]`
- Output: `6`

One minimum-cost result is `[3, 4, 1, 2, 5, 7]`; no sequence of five moves can make every value unique.

### Required Complexity

- **Time:** $O(n+M)$
- **Space:** $O(M)$

<details>
<summary>Approach</summary>

#### General

**Count how many values arrive at each position.** Allocate a frequency array covering all original values and another $n$ positions beyond the maximum. After counting `nums`, scan value positions from left to right. At a position with frequency zero or one, nothing must move. If `frequency[value]` is greater than one, keep one item there and treat all remaining copies as excess.

**Carry duplicates one unit at a time in aggregate.** Add the excess to `frequency[value + 1]` and add the same amount to the move count. This represents incrementing each excess copy once. A carried copy may meet other values at the next position and be carried again during the following iteration, with every additional unit of distance charged exactly once.

At most one item can finish at `value`, so every excess item currently there must cross from `value` to `value + 1`; that unit of cost is unavoidable in any valid result. Keeping one item and moving all excess copies to the earliest possible next position never pushes an item farther than necessary. Applying this argument from left to right proves that every charged move is necessary and that the final distinct placement has minimum total cost.

#### Complexity detail

Counting the $n$ inputs costs $O(n)$, and the frequency scan covers $M$ value positions, for $O(n+M)$ time. The frequency array contains $M$ counters, giving $O(M)$ space.

#### Alternatives and edge cases

- **Sort and raise greedily:** Sort the values, then replace each value conceptually by the greater of itself and one more than the preceding assigned value. This uses $O(n\log n)$ time and is often simpler when the numeric range is large.
- **Next-free union-find:** Map an occupied value to the next candidate position and compress paths after each placement. It avoids a range-sized array but has more bookkeeping and expected near-linear behavior.
- **Increment until a set slot is free:** For each number, repeatedly add one while the value is already used. This is correct, but many equal inputs cause $O(n^2)$ membership iterations.
- **Already unique:** Every frequency is at most one, so no item is carried and the answer is zero.
- **All values equal:** The copies occupy consecutive final positions; their move counts are $0,1,\ldots,n-1$.
- **Collisions created by carrying:** Excess from a smaller value may meet an original larger value. Adding frequencies before processing the next position handles that collision without a special case.
- **Upper input value:** The extra $n$ positions ensure enough room even when many copies begin at `100000`.

</details>

# Reduction Operations to Make the Array Elements Equal

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/) |
| Frontend ID | 1887 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given an integer array `nums`, repeatedly reduce one of its largest elements until every element has the same value. In one operation, find the largest value currently present. If that value occurs more than once, choose its smallest array index. Replace only that chosen element with the next-largest distinct value currently in the array.

For example, if the current array is `[5,1,3]`, the first operation changes `5` to `3`, because `3` is the greatest value strictly smaller than `5`. The array becomes `[3,1,3]`; subsequent operations continue under the same rule. Return the total number of operations required before all entries are equal.

### Function Contract

**Inputs**

- `nums`: an array of $N$ positive integers.
- $1 \le N \le 5 \cdot 10^4$.
- Each value lies between $1$ and $5 \cdot 10^4$, inclusive.

**Return value**

- Return the number of single-element reduction operations needed to make all values equal.

### Examples

**Example 1**

- Input: `nums = [5,1,3]`
- Output: `3`

The reductions are `[5,1,3]` to `[3,1,3]`, then `[1,1,3]`, then `[1,1,1]`.

**Example 2**

- Input: `nums = [1,1,1]`
- Output: `0`

The values are already equal.

**Example 3**

- Input: `nums = [1,1,2,2,3]`
- Output: `4`

The `3` crosses two distinct lower levels, while each `2` crosses one.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Replace the evolving process with fixed ranks**

The smallest value never changes. Every occurrence of the second-smallest distinct value must be reduced once to reach that minimum. Every occurrence of the third-smallest distinct value must be reduced twice: first to the second-smallest level and then to the minimum. More generally, an element requires one operation for each distinct array value smaller than it.

This count is independent of which equal maximum is chosen first. The smallest-index tie rule fixes the order of individual operations, but all copies at a given level eventually cross the same lower levels and therefore contribute the same amount.

**Accumulate contributions in sorted order**

Sort a copy of the array in ascending order. Maintain `smaller_levels`, the number of distinct transitions encountered so far. Whenever the current value differs from the previous sorted value, increment that counter. Add the current counter to the answer for every element.

For `[1,1,2,2,3]`, the sorted contributions are `0, 0, 1, 1, 2`, totaling `4`. These are exactly the level crossings made by the original reduction process. Since every operation moves one element down by exactly one distinct level, summing all required crossings counts every operation once and proves that the accumulated total is correct.

#### Complexity detail

Sorting $N$ values takes $O(N\log N)$ time. The subsequent scan visits each position once, adding $O(N)$ time, so the overall bound remains $O(N\log N)$. The sorted copy uses $O(N)$ auxiliary space. The answer can be as large as $\frac{N(N-1)}{2}$ when all values are distinct, so implementations in fixed-width languages need a sufficiently wide integer type.

#### Alternatives and edge cases

- **Frequency table:** Because values are bounded, count each value and scan the legal value range, adding `frequency * smaller_levels` at occupied levels. This takes $O(N+V)$ time and $O(V)$ space for value bound $V=5\cdot10^4$.
- **Literal simulation:** Repeatedly finding the largest and next-largest values follows the statement directly but can require $\Theta(N^2)$ operations even before accounting for the searches.
- **All values equal:** No distinct lower level exists and the answer is `0`.
- **Duplicate values:** Every copy contributes separately, but equal copies share the same number of smaller distinct levels.
- **Smallest-index tie rule:** It determines operation order only; it does not change the total number of level crossings.
- **Maximum operation count:** With $N$ distinct values, the answer is $0+1+\cdots+(N-1)$.

</details>

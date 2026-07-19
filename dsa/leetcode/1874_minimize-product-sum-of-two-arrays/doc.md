# Minimize Product Sum of Two Arrays

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimize-product-sum-of-two-arrays/) |
| Frontend ID | 1874 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

The product sum of two arrays of equal length is the sum of the products at corresponding indices. For example, arrays `[1,2,3,4]` and `[5,2,3,1]` have product sum `1*5 + 2*2 + 3*3 + 4*1`.

Given positive integer arrays `nums1` and `nums2`, you may rearrange the elements of `nums1` in any order while `nums2` supplies the positions to which those values are assigned. Return the smallest product sum obtainable over all such rearrangements. Duplicate values are distinct occurrences and must all be used exactly once.

### Function Contract

**Inputs**

- `nums1`, `nums2`: positive integer arrays of the same length $N$, where $1 \le N \le 10^5$ and every value is at most $100$.

**Return value**

- Return the minimum possible value of $\sum_{i=0}^{N-1}\texttt{nums1[i]}\texttt{nums2[i]}$ after arbitrarily permuting `nums1`.

### Examples

**Example 1**

- Input: `nums1 = [5,3,4,2], nums2 = [4,2,2,5]`
- Output: `40`

Pairing the values as `[3,5,4,2]` against `nums2` yields `12 + 10 + 8 + 10`.

**Example 2**

- Input: `nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]`
- Output: `65`

The largest first-array values are assigned to the smallest second-array values.

**Example 3**

- Input: `nums1 = [7], nums2 = [9]`
- Output: `63`

With one element, there is only one possible pairing.

### Required Complexity

- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Pair opposite extremes**

Sort the values of `nums1` in ascending order and the values of `nums2` in descending order. Multiply corresponding positions and sum them. Sorting `nums2` is an analytical reordering of the pairs: the resulting multiset matching can always be realized by permuting `nums1` into the corresponding original `nums2` positions.

**Why aligned ordering cannot be better**

Suppose two first-array values satisfy $a \le b$ and their paired second-array values satisfy $c \le d$. Pairing them in the same order contributes $ac+bd$. Swapping the first-array assignments contributes $ad+bc$, and

$$
(ac+bd)-(ad+bc)=(b-a)(d-c)\ge 0.
$$

Thus pairing the larger first value with the smaller second value never increases the sum.

**Remove every inversion**

Any matching that is not oppositely ordered contains a same-order pair of the form above. Swapping it does not increase the product sum. Repeating this exchange removes all such inversions and reaches the opposite-order pairing, proving that the constructed sum is globally minimal. Equal values simply make some exchanges neutral.

#### Complexity detail

Sorting both length-$N$ arrays takes $O(N\log N)$ time, and the final paired scan takes $O(N)$. Python's sorting implementation may use $O(N)$ auxiliary workspace in the worst case, so the overall space bound is $O(N)$. The returned result itself is one integer.

#### Alternatives and edge cases

- **Frequency counting:** Because values lie from `1` through `100`, two frequency arrays and opposing pointers can achieve $O(N+100)$ time and $O(100)$ space.
- **Enumerate permutations:** It checks every possible arrangement but requires factorial time.
- **Quadratic selection sort:** It produces the same optimal ordering but costs $O(N^2)$ time.
- **Duplicate values:** Preserve their multiplicities; their internal order is irrelevant.
- **All values equal:** Every rearrangement has the same product sum.
- **Single element:** Return its sole product.
- **Rearranging `nums2` in the implementation:** Only the induced matching matters, and the same matching is realizable by rearranging `nums1` alone.

</details>

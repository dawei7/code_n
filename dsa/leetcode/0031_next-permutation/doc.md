# Next Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 31 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/next-permutation/) |

## Problem Description
### Goal
An integer array `nums` represents one permutation of its multiset of values. In lexicographic order, one permutation precedes another when its first differing position contains the smaller value. Rearrange the array into the smallest permutation that is still greater than its current ordering.

If no lexicographically greater permutation exists because the array is in descending order, rearrange it into the lowest possible order, sorted in ascending order. Duplicate values remain with their original multiplicities. Perform the transformation in place with constant auxiliary space; the caller observes the mutated array rather than a separate returned permutation.

### Function Contract
**Inputs**

- `nums`: non-empty `List[int]`

**Return value**

`None`; the app and platform judge inspect the mutated `nums` array.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3]`
- Output: `nums = [1, 3, 2]`

**Example 2**

- Input: `nums = [3, 2, 1]`
- Output: `nums = [1, 2, 3]`

**Example 3**

- Input: `nums = [1, 1, 5]`
- Output: `nums = [1, 5, 1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**The longest non-increasing suffix is already maximal**

Scan from the right to find the last index `pivot` with `nums[pivot] < nums[pivot + 1]`. Everything after it is non-increasing, which is the lexicographically greatest arrangement of that suffix's multiset. Therefore the suffix cannot be rearranged into a larger permutation while leaving the earlier prefix unchanged.

If no pivot exists, the complete array is non-increasing and is already the greatest permutation. Reversing it puts the entire multiset in nondecreasing order, the required wraparound minimum.

**Increase the rightmost possible position by the smallest amount**

When a pivot exists, scan from the right for the first value greater than `nums[pivot]`. Because the suffix is non-increasing, this is the smallest suffix value that can increase the pivot, including when duplicate values are present. Swap them.

The suffix remains non-increasing after this swap. Reverse it to obtain its nondecreasing—and therefore smallest—arrangement. The result changes the latest possible position, increases it by the least possible value, and minimizes everything after it.

**Lexicographic minimality of the change**

The initial scan proves no position to the right of the pivot can be increased while keeping an earlier prefix unchanged. The chosen successor is the least value that makes the pivot larger, and the reversed suffix is the least completion after that prefix.

**Trace a representative input**

For `[1, 3, 2]`, the pivot is 1 at index 0 because suffix `[3, 2]` is non-increasing. The smallest larger suffix value is 2. Swap to `[2, 3, 1]`, then reverse the suffix to obtain `[2, 1, 3]`.

**Why the construction is the immediate successor**

The non-increasing suffix is already its greatest possible ordering, so no rearrangement confined to that suffix can increase the permutation. A greater permutation must change the pivot or an earlier position; changing an earlier position would make a larger lexicographic jump.

At the pivot, swapping in the smallest suffix value that is greater creates the smallest possible increase at the latest possible position. The remaining suffix must then be as small as possible. Reversing its known descending arrangement produces ascending order. The result is therefore the unique immediate successor. If no pivot exists, the input is globally maximal and reversal correctly wraps to the minimum permutation.

#### Complexity detail

The pivot scan, successor scan, and suffix reversal each visit at most `n` positions, so total time is $O(n)$. Swaps and indices use $O(1)$ auxiliary space, and the input is mutated in place as required.

#### Alternatives and edge cases

- **Generate and sort all permutations:** requires factorial time and storage.
- **Sort the suffix after swapping:** is correct but costs $O(n \log n)$; the suffix's known monotone order makes linear reversal sufficient.
- **Copy to a second array:** simplifies manipulation but violates constant auxiliary space.
- Duplicate values do not create a special case; the strict `>` successor test finds the smallest genuine increase.
- One-element and all-equal arrays reverse to an indistinguishable arrangement, which is both their greatest and smallest permutation.

</details>

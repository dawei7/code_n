# Sort an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 912 |
| Difficulty | Medium |
| Topics | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-an-array/) |

## Problem Description
### Goal
Given an integer array `nums`, rearrange and return its elements in ascending order. Repeated values must appear with their original multiplicities, and negative values participate in the same numeric ordering. The output must contain every original occurrence.

Do not use a built-in sorting function. The algorithm must run in $O(n\log n)$ time and should use the smallest possible amount of auxiliary space.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 5\cdot 10^4$ and $-5\cdot 10^4 \leq \texttt{nums}[i] \leq 5\cdot 10^4$.

**Return value**

Return `nums`'s values in ascending order without losing or duplicating any occurrence.

### Examples
**Example 1**

- Input: `nums = [5,2,3,1]`
- Output: `[1,2,3,5]`

**Example 2**

- Input: `nums = [5,1,1,2,0,0]`
- Output: `[0,0,1,1,2,5]`

The repeated zeroes and ones remain repeated in the result.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Build a max-heap inside the array**

Interpret `nums` as a complete binary tree: the children of index `root` are `2 * root + 1` and `2 * root + 2` when those indices exist. A max-heap requires every parent to be at least as large as both children. Starting from the last internal node and moving backward, sift each value down by repeatedly swapping it with its larger child until the heap property is restored.

After this bottom-up construction, `nums[0]` is the greatest value in the current heap. Building from the last internal node is linear because most nodes are near the leaves and move only a short distance.

**Extract the maximum into its final position**

Swap `nums[0]` with the last element of the active heap. The maximum is now fixed at the right edge of the array and must not participate in later heap operations. Reduce the active heap boundary by one and sift the new root down to restore the max-heap property.

Repeat until the active heap contains one element. On every extraction, the greatest remaining value is placed immediately before the already sorted suffix. Therefore that suffix stays in ascending order and contains exactly the largest values removed so far. When no extraction remains, the entire array is in ascending order. Every operation is a swap, so all input occurrences are preserved.

#### Complexity detail

Bottom-up heap construction takes $O(n)$ time. There are $n-1$ extractions, and each sift-down follows at most the heap height $O(\log n)$, giving $O(n\log n)$ total time. The heap is stored directly in `nums` and sift-down uses only index variables, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Merge sort:** It guarantees $O(n\log n)$ time and is stable, but its usual array implementation needs $O(n)$ merge-buffer space.
- **Randomized quicksort:** It is often fast and can be in-place, but its worst case is $O(n^2)$ and recursion consumes stack space.
- **Counting sort:** The bounded value range permits $O(n+U)$ time for range width $U$, but it uses $O(U)$ auxiliary storage and does not meet the comparison-sort framing as directly.
- **Selection sort:** It uses constant space but repeatedly scans the unsorted suffix, taking $O(n^2)$ time.
- **One element:** The heap is already sorted and no extraction occurs.
- **Duplicate values:** Either equal child may remain above the other; heap extraction still preserves every copy.
- **Negative values:** Comparisons work unchanged, including at the lower value bound.
- **Already sorted or reverse sorted:** Heap construction and extraction retain the same worst-case $O(n\log n)$ guarantee.

</details>

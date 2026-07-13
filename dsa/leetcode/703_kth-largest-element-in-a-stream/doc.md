# Kth Largest Element in a Stream

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 703 |
| Difficulty | Easy |
| Topics | Tree, Design, Binary Search Tree, Heap (Priority Queue), Binary Tree, Data Stream |
| Official Link | [LeetCode](https://leetcode.com/problems/kth-largest-element-in-a-stream/) |

## Problem Description
### Goal
A university admissions office receives applicant test scores as a stream and needs to track its cutoff dynamically. Initialize `KthLargest` with a rank `k` and any scores already received in `nums`.

Whenever `add(val)` submits another score, include it with every score seen so far and return the `k`th largest value in that combined multiset. Rank values after sorting from largest to smallest, counting duplicate score occurrences separately. The maintained state persists across additions; a returned cutoff does not remove a score.

### Function Contract
**Inputs**

- `k`: the one-based rank to maintain
- `nums`: values present before streaming begins
- `stream`: values added in order; the app-local adapter performs one native `add` operation for each value

**Return value**

- A list containing the `k`th largest value after every addition from `stream`

### Examples
**Example 1**

- Input: `k = 3, nums = [4,5,8,2], stream = [3,5,10,9,4]`
- Output: `[4,5,5,8,8]`

**Example 2**

- Input: `k = 1, nums = [], stream = [-3,-2,-4,0,4]`
- Output: `[-3,-2,-2,0,4]`

**Example 3**

- Input: `k = 2, nums = [0], stream = [-1,1,-2,-4,3]`
- Output: `[-1,0,0,0,1]`

### Required Complexity

- **Time:** $O((m + s) \log k)$
- **Space:** $O(k)$

<details>
<summary>Approach</summary>

#### General

**Keep only values that can affect rank k**

Maintain a min-heap containing the largest `k` values seen so far. Any value outside this set is no larger than the heap minimum and cannot become the `k`th largest while all retained values remain present.

**Build the bounded heap**

Offer each initial value to the heap. Push while fewer than `k` values are retained. Once full, replace the minimum only when the new value is larger.

**Process each addition identically**

Apply the same offer rule to every streamed value. After the operation, the heap contains the largest `k` values among the enlarged history, so its root is their smallest value and therefore the overall `k`th largest.

**Why discarding a value is safe forever**

When a value is rejected or removed, at least `k` seen values are no smaller. Future additions never delete those values; they can only add more competition. The discarded value can therefore never enter the largest-`k` set later.

#### Complexity detail

For `m` initial values and `s` additions, each offer costs at most $O(\log k)$, giving $O((m + s) \log k)$ total time. The heap never stores more than `k` values, so it uses $O(k)$ space beyond the returned results.

#### Alternatives and edge cases

- **Rebuild a bounded heap after each addition:** it returns the right rank but repeatedly processes the complete history, taking $O(s(m + s) \log k)$ time.
- **Sort the complete history after each addition:** it is simple and correct but can take up to $O(s(m + s) \log(m + s))$ time.
- **Balanced search tree with subtree sizes:** insert each value and select rank `k`; it supports logarithmic operations but requires an augmented ordered multiset.
- **Sorted list of the largest k values:** binary search finds an insertion point, but shifting elements can cost $O(k)$ per addition.
- When $k = 1$, the heap root is the running maximum.
- Duplicate values occupy separate rank positions and must remain separate heap entries.
- Negative values follow the same ordering rules as positive values.
- The operation contract guarantees enough total values exist whenever an answer is requested.

</details>

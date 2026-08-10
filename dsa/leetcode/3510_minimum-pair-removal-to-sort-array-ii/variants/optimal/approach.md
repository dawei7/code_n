## General

**Why a literal list simulation is too slow**

At every operation, the rules force two decisions:

1. find the adjacent pair with the smallest sum, breaking ties in favor of the leftmost pair;
2. replace that pair with its sum.

After each replacement, one element disappears and the neighboring relationships change. A straightforward simulation can scan the whole current array to find the minimum pair and then delete one list entry. Either step can cost linear time. Since there may be `n - 1` merges, that approach can require `O(n^2)` time, which is too much for `n` up to `10^5`.

The protected solution accelerates three separate needs:

- `sl`, a `SortedList` of `(adjacent_sum, left_original_index)` pairs, finds the required pair;
- `idx`, a `SortedList` of surviving original indices, represents the current logical array and finds neighbors;
- `inv` stores the number of currently decreasing adjacent pairs and tells when the array is non-decreasing.

Unlike the editorial's lazy priority-queue implementation, this source removes obsolete pair entries eagerly. Its correctness argument should therefore follow the two ordered lists actually used by the code, not stale-heap validation.

**Representing the changing array with stable indices**

Every current element is stored at the original index of the leftmost element that was merged into it. Initially, all indices `0, 1, ..., n - 1` are active, so `idx = SortedList(range(n))`. The current array is obtained by reading `nums[i]` for active indices `i` in `idx` order.

When adjacent active indices `i` and `j` are merged, the sum survives at `i`:

`nums[i] = nums[i] + nums[j]`.

Then `j` is removed from `idx`. No remaining original index changes. This stable coordinate system is valuable because the numerical order of original indices is always the current left-to-right order.

Suppose `i` is at position `pos` in `idx`. Then:

- `idx[pos - 1]`, when it exists, is its current left neighbor;
- `idx[pos + 1]` is its current right neighbor `j`;
- `idx[pos + 2]`, when it exists, is the neighbor immediately after `j`.

This supplies linked-list-like neighbor access while retaining ordered indices.

**Selecting the exact required pair**

For every currently adjacent pair, `sl` contains one tuple:

`(nums[left] + nums[right], left)`.

`SortedList` orders tuples lexicographically. Therefore, `sl.pop(0)` returns the pair with minimum sum; when sums tie, it returns the smallest surviving left original index. Because original indices preserve left-to-right order, that is exactly the problem's leftmost tie-break.

If the popped tuple is `(s, i)`, the source finds `i` in `idx` and takes the next active index as `j`. The invariant that `sl` contains exactly current adjacent pairs guarantees that `j` is the right endpoint belonging to that entry and that `s = nums[i] + nums[j]`.

There is no need to choose among operations beyond this ordering: the problem prescribes the minimum-sum, leftmost pair. The algorithm simulates that deterministic sequence efficiently and stops at the first non-decreasing state.

**Recognizing a non-decreasing current array**

An array is non-decreasing exactly when none of its adjacent pairs decreases. The variable `inv` counts current active adjacencies satisfying

`left_value > right_value`.

Despite its short name, it does not count all inversions between arbitrary positions. It counts only decreasing neighboring pairs. Initially, the source scans the original array once and increments `inv` for every `nums[i] > nums[i + 1]`.

The main loop continues while `inv` is nonzero. This is an exact condition:

- if `inv = 0`, every current neighbor relation is non-decreasing, so the whole current array is non-decreasing;
- if `inv > 0`, at least one required adjacent comparison fails, so another forced merge is necessary.

Keeping this count avoids rescanning the changing array after each operation.

**Updating only the relationships touched by a merge**

Merging `i` and `j` changes at most three old adjacencies:

- the internal pair `(i, j)` disappears;
- the left pair `(h, i)` changes to `(h, i)` with a new value at `i`, where `h` is the predecessor;
- the right pair `(j, k)` changes to `(i, k)`, where `k` is the successor.

All other active values and adjacencies remain exactly as they were, so their entries in `sl` and their contribution to `inv` need no work.

First, if `nums[i] > nums[j]`, the disappearing internal pair contributed one to `inv`, so the source decrements the count.

If a left neighbor `h` exists, the source:

- subtracts the old contribution when `nums[h] > nums[i]`;
- removes the old ordered-list entry `(nums[h] + nums[i], h)`;
- adds the new contribution when `nums[h] > s`;
- inserts the new entry `(nums[h] + s, h)`.

If a right neighbor `k` exists, it similarly:

- subtracts the old contribution when `nums[j] > nums[k]`;
- removes `(nums[j] + nums[k], j)`;
- adds the new contribution when `s > nums[k]`;
- inserts `(s + nums[k], i)`.

Only after these comparisons does the source assign `nums[i] = s` and remove `j` from `idx`. It deliberately uses the old `nums[i]` and `nums[j]` while removing old relationships, and the already computed `s` while adding new ones.

For each completed merge, `ans` increases by one. The removed index `j` may still hold a stale number in the physical `nums` list, but it is never active again and is ignored by both ordered structures.

**Why the maintained representation remains exact**

Initially, `idx` contains every array position, `sl` contains every original adjacent pair once, and `inv` counts precisely the decreasing ones.

Assume those statements hold before a merge. `sl.pop(0)` selects the required pair because its tuple ordering encodes both rules. The source removes precisely the old pair entries incident to `i` or `j` and inserts precisely the new entries created by replacing them with their sum. No nonlocal adjacency changes. Removing `j` makes `i` and `k` adjacent exactly when `k` exists. The analogous statement holds on the left. The old decreasing contributions are subtracted and the new ones are added, so `inv` remains the exact count.

By induction, the structures accurately simulate every forced operation. The first time `inv` reaches zero is the first time the current array is non-decreasing. Returning the number of merges performed at that moment is therefore the minimum required count: stopping earlier would leave a decreasing adjacency, while performing more operations would be unnecessary.

**A small structural trace**

For `[5, 2, 3, 1]`, the initial pair entries are `(7, 0)`, `(5, 1)`, and `(4, 2)`. The smallest tuple chooses indices `2` and `3`, producing value `4` at index `2`. Index `3` disappears, and the old pair from indices `1,2` is replaced with sum `6`. The active sequence is now `[5, 2, 4]`.

The smallest current entry is then `(6, 1)`, so indices `1` and `2` merge into `6`. The active sequence becomes `[5, 6]`, its adjacent-decrease count is zero, and the source returns two.

## Complexity detail

Let `n` be the original array length. Initialization inserts `n - 1` pair tuples into `sl`, constructs `idx` with `n` indices, and counts adjacent decreases. This costs `O(n \log n)` with individual ordered-list insertions as written; constructing `idx` from already sorted data may be faster internally, but the overall bound remains `O(n \log n)`.

Each merge removes one active index, so there can be at most `n - 1` iterations. An iteration performs a constant number of `SortedList` operations: pop the minimum, locate an index, inspect neighboring indices, remove up to two obsolete pair tuples, insert up to two new tuples, and remove one active index. Each ordered operation costs `O(\log n)`, while comparisons and arithmetic are constant time. Total time is therefore `O(n \log n)`.

At any moment, `idx` contains one entry per active element and `sl` contains one entry per active adjacency. Their sizes are at most `n` and `n - 1`. The source reuses `nums` for merged values and keeps only constant scalar state besides the ordered lists. Auxiliary space is `O(n)`.

The source mutates `nums`. That does not change the asymptotic auxiliary-space claim, but it is an observable implementation detail if a caller expected the input list to remain unchanged.

## Alternatives and edge cases

- **Lazy minimum heap plus linked neighbors:** This is the editorial strategy and also achieves `O(n \log n)`. It leaves obsolete pair entries in the heap and validates them when popped, whereas the protected `SortedList` source eagerly removes the two obsolete neighboring sums.
- **Ordinary array simulation:** Repeatedly scanning for the minimum pair and deleting an element is simple and suitable for tiny constraints, but it can take `O(n^2)` time here.
- **Only a heap without neighbor structure:** A heap finds a small stored sum but cannot by itself determine whether the endpoints are still adjacent or locate the new predecessor and successor efficiently.
- **Recheck the whole array after every merge:** This replaces the constant-size `inv` update with an `O(n)` scan per operation and loses the desired bound.
- **Count all inversions:** Full inversion counting is unnecessary. Non-decreasing order is characterized completely by adjacent comparisons, and only those local comparisons change during a merge.
- **Equal minimum sums:** Tuple ordering by `(sum, left_index)` is not incidental; the second field implements the required leftmost tie-break.
- **Negative numbers:** Pair sums can decrease or increase after a merge, so monotonic assumptions about sums would be unsafe. The ordered set is updated with the exact new values and handles negative keys naturally.
- **Already non-decreasing input:** `inv` starts at zero, the loop never pops `sl`, and the answer is `0`.
- **Single element:** There are no adjacent pairs and `inv = 0`. Although the documented constraint allows this case through `n \ge 1`, the initialization still returns `0` safely.
- **Two elements in decreasing order:** The only pair must be merged once. Removing its internal decrease makes `inv` zero, and the one-element result is non-decreasing.
- **Merge at the left boundary:** There is no predecessor entry to remove or recreate; only the internal and possible right relationships change.
- **Merge at the right boundary:** There is no successor, so only the internal and possible left relationships change.
- **Stale values in `nums`:** A removed right index is intentionally left untouched in the physical list. Membership in `idx`, not the raw list position alone, determines whether a value is part of the current array.
- **External ordered-container dependency:** The protected code assumes `SortedList` is available from the execution harness or imports. Replacing it with a standard Python list would make insertion, deletion, and index removal linear and invalidate the stated time bound.

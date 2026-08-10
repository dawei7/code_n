## General

Every window needs its middle value or values after sorting, but sorting each group of `k` numbers independently would repeat nearly all the work when the window shifts by one position. Consecutive windows differ in only two events: one incoming value is added and one outgoing value is removed. The solution maintains enough ordered information to process those events and read the median without rebuilding the whole window.

**Split the valid window around its median.** `MedianFinder` uses two heaps. `small` represents the lower half as a max-heap, implemented in Python by pushing negated values into a min-heap. Therefore `-small[0]` is the largest valid value in the lower half. `large` is an ordinary min-heap, so `large[0]` is the smallest valid value in the upper half.

The logical, or valid, heap sizes obey two rules after rebalancing:

- `small_size == large_size` when the number of valid elements is even.
- `small_size == large_size + 1` when it is odd.

All valid values represented by `small` are no greater than all valid values represented by `large`. These rules place the median directly at the heap boundaries. For odd `k`, the lower half has the extra element, so `-small[0]` is the single middle value. For even `k`, `-small[0]` and `large[0]` are the two middle values, and their average is the median.

**Insert according to the current boundary.** `add_num` sends `num` to `small` when the lower heap is empty or `num <= -small[0]`; otherwise it sends it to `large`. This comparison preserves the ordering division. The corresponding logical size is incremented, and `rebalance` repairs a possible one-element size violation. If `small` has more than one extra valid element, its maximum moves to `large`. If `large` has more valid elements, its minimum moves to `small`. Moving exactly a boundary value preserves the ordering property while restoring the required size relationship.

**Delay physical deletion without delaying logical deletion.** A binary heap can efficiently remove its root, but it cannot efficiently locate an arbitrary outgoing occurrence. `delayed` solves this by recording how many occurrences of each value have left the window but remain physically buried in a heap. `remove_num` increments that count and immediately decreases either `small_size` or `large_size`. The heaps may still contain the stale value, but the balancing mathematics stops counting it at once.

The outgoing value is classified with `num <= -small[0]`, the same lower-half boundary used for insertion. Duplicates do not break this reasoning. If a value equal to the boundary has occurrences in both heaps, treating the removed occurrence as belonging to `small` is a valid accounting choice: equal copies are interchangeable. The delayed count is by value, and a matching stale occurrence will eventually be discarded from whichever relevant heap exposes it.

`prune` performs that physical cleanup. For `small`, `sign = -1` converts the stored negative root back to its real value; for `large`, `sign = 1` leaves the root unchanged. While the real root exists in `delayed`, the method decrements its pending count, removes a zero count from the dictionary, and pops the heap root. It stops as soon as the root is valid. Stale values below a valid root can safely remain because neither median reading nor a cross-heap move needs them yet.

Cleanup happens at exactly the points where a root must be trusted. Removing an outgoing value prunes immediately if that value is already at its heap root. Rebalancing moves a root across heaps and then prunes the source heap, revealing a valid new root. By the time `find_median` runs, the accessible heap tops represent live window values.

**Process the sliding windows in their natural order.** The solution first adds `nums[:k]`, so both heaps represent the initial window. It records that median. For each later index `i`, it adds `nums[i]`, removes `nums[i - k]`, and records the new median. Temporarily adding first means there are `k + 1` valid elements, but the add operation rebalances them; removal then returns the count to `k` and rebalances again. The invariants hold before the median is read. There are exactly `len(nums) - k + 1` readings, one for every legal window.

These invariants establish correctness by induction. After initial insertion, rebalancing gives the required heap sizes and ordered halves. Each later insertion, logical deletion, root pruning, and boundary transfer preserves the partition and restores those sizes. Thus the heap tops are exactly the middle ordered value or pair for the current valid multiset, including duplicate and negative values. The formula in `find_median` therefore returns the required median for every window.

## Complexity detail

Let $n$ be `len(nums)`. Each of the $n$ values is pushed into a heap once. A value may move between heaps during rebalancing, and after it leaves the window it is eventually popped once through lazy deletion. Heap work costs logarithmic time. The manifest states $O(n \log k)$ time because the maintained logical window contains $k$ valid elements and each window update performs only a constant number of heap operations, with stale elements removed amortically across the full traversal.

There is a subtle implementation detail: lazy entries can remain physically buried, so the Python heap arrays can exceed `k` on adversarial orderings. Under a strict bound on the actual heap-array length, an operation can be $O(\log n)$ and retained stale entries can raise physical storage toward $O(n)$. The stated $O(n \log k)$ time and $O(k)$ space are the intended window-data-structure bounds from the optimal manifest; the lazy-deletion implementation achieves constant amortized removals but may retain stale physical nodes longer than the logical window lifetime.

The result list contains $n-k+1$ floating-point medians. Complexity conventions normally exclude required output storage; including it adds $O(n-k+1)$ space. The two logical heap halves, their valid-size counters, and pending deletion counts describe $O(k)$ live window information.

## Alternatives and edge cases

- **Sort every window independently:** This is easy to reason about but costs $O((n-k+1)k\log k)$ time and repeats sorting for the `k-1` elements shared by neighboring windows.
- **Maintain one sorted Python list:** Binary search locates insertion and deletion positions in $O(\log k)$ time, but shifting list elements costs $O(k)$ per update, producing $O(nk)$ time in the worst case.
- **Balanced multiset or order-statistic tree:** A language with an efficient duplicate-aware ordered multiset can insert, erase one occurrence, and access middle positions in $O(\log k)$ time while keeping physical storage at $O(k)$. Python's standard library does not provide that structure directly.
- **Immediate arbitrary heap deletion:** Searching a heap array for the outgoing item and repairing it loses the desired logarithmic update bound because locating that arbitrary occurrence can take linear time. Lazy deletion avoids the search.
- **Duplicate boundary values:** Equal copies may live in either heap. Logical sizes and count-based delayed deletion make the occurrences interchangeable, so `<= -small[0]` remains safe.
- **`k = 1`:** Every value is its own median. `small` holds the one live value, and add/remove/prune operations still preserve the invariants.
- **Even `k`:** Both heaps contain the same number of valid elements. The code averages the maximum lower-half value and minimum upper-half value rather than choosing either one alone.
- **Negative and 32-bit extreme values:** Negating values is only the max-heap representation; Python integers do not overflow. The average also uses Python division, producing the required floating-point result.

## General

**Sort so the best partner can be found by boundary search**

For a fixed value `x`, a partner `y` is valid when `x + y < k`, which is equivalent to `y < k - x`. After sorting `nums`, the greatest valid partner to the right of `x` is immediately before the first value that is at least `k - x`.

The method sorts the input list in place. This changes the caller’s element order, but the result depends only on values and distinct positions, not original ordering. Sorting preserves multiplicity, so two equal values at different indices remain two selectable elements.

**Restrict the search to a distinct later position**

The loop visits sorted index `i` with value `x`. `bisect_left(nums, k - x, lo=i + 1)` searches only the suffix beginning after `i`. It returns the first index whose value is greater than or equal to the exclusive complement limit.

Subtracting one yields `j`, the greatest index in that suffix whose value is strictly less than `k - x`. Therefore, if such a suffix element exists, `x + nums[j]` is strictly less than `k`.

The check `i < j` confirms that the binary search actually found an element in the allowed suffix. If the insertion position was `i + 1`, subtraction produces `i` and there is no valid later partner. This also enforces two distinct array positions even when the desired numeric values are equal.

**Why only that partner matters for one left index**

Within the sorted suffix, every earlier candidate is no greater than `nums[j]`. Pairing `x` with any of them produces a sum no larger than `x + nums[j]`. Every later element is at least the threshold and therefore makes the sum greater than or equal to `k`.

Thus `j` gives the maximum legal sum among all pairs whose first sorted index is `i`. Taking `max` across every `i` then gives the maximum over all legal pairs.

Sorting changes indices, but any two positions in the sorted array correspond to two original occurrences. The condition `i < j` is only a canonical way to consider each unordered pair once; it still covers every possible pair of distinct input elements.

**Preserve the failure result**

`ans` starts at `-1`. Input values are positive, so every valid pair sum is positive and necessarily greater than `-1`. If at least one legal pair is found, `ans` is replaced. If none exists, no update occurs and the required sentinel remains.

The inequality is strict throughout. `bisect_left` finds the first partner equal to or above `k - x` and stepping left excludes equality, so a pair whose sum is exactly `k` is never accepted.

## Complexity detail

Let $n$ be the number of values. Sorting costs $O(n\log n)$ time. The loop executes $n$ times, and each `bisect_left` over a suffix costs $O(\log n)$ time. The combined search work is $O(n\log n)$, so total time remains $O(n\log n)$.

Python’s list sort is in place from the caller’s perspective but may use $O(n)$ temporary memory in the worst case. The package therefore records $O(n)$ space. The binary searches and scalar variables themselves use $O(1)$ extra space.

For the official maximum of one hundred elements, a quadratic scan would also be small, but the sorted boundary method explains a scalable approach.

## Alternatives and edge cases

- **Two pointers after sorting:** Put one pointer at each end. If the sum is below `k`, record it and move the left pointer right; otherwise move the right pointer left. This reduces the post-sort scan to $O(n)$ and keeps the same $O(n\log n)$ total.
- **Brute force:** Check every pair in $O(n^2)$ time and $O(1)$ auxiliary space. It is simplest for small constraints but scales worse.
- **Counting array:** Values are bounded by one thousand, so frequency counts can search value pairs without comparison sorting. Duplicate handling and distinct-occurrence checks require care.
- **Array length one:** Every suffix is empty, `i < j` never holds, and the answer remains `-1`.
- **Sum exactly `k`:** It is invalid. The left-boundary search and one-step retreat enforce the strict inequality.
- **Repeated values:** They may form a pair only when at least two occurrences exist. Searching from `i + 1` guarantees a separate occurrence.
- **No valid pair:** Every computed candidate fails the index check, so the sentinel `-1` is returned.
- **Several pairs with the same best sum:** The algorithm stores only the numeric maximum, which is all the contract requests.
- **Very large complement:** `bisect_left` can return the list length; subtracting one correctly chooses the last suffix value.
- **Very small complement:** It can return `i + 1`; subtracting one gives `i` and the distinct-position check rejects the nonexistent partner.
- **Input mutation:** `nums.sort()` permanently reorders the supplied list. If caller-visible order had to be preserved, use `sorted(nums)` and accept an explicit $O(n)$ copy.
- **Positive-value guarantee:** It makes `-1` an unambiguous failure sentinel below every real pair sum.

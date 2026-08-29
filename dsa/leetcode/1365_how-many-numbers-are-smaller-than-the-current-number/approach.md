## General

**Turn a counting question into a position question**

For every original value `x`, the task asks how many array elements are strictly smaller than `x`. Comparing `x` with every other element would answer the question directly, but it repeats much of the same work. The exact solution instead creates `arr = sorted(nums)`. In this sorted copy, every value smaller than `x` must appear before the first occurrence of `x`.

That observation gives a direct equivalence:

$$
\text{number of elements smaller than }x
=
\text{index of the first }x\text{ in sorted order}.
$$

For example, sorting `[8, 1, 2, 2, 3]` produces `[1, 2, 2, 3, 8]`. The first `1` is at index zero, so nothing is smaller than one. The first `2` is at index one, so exactly one element is smaller. The first `3` is at index three, so three elements are smaller. The first `8` is at index four, so four elements are smaller.

**Why it must be the first occurrence**

Duplicates are the reason an ordinary successful search is not enough. Both copies of `2` in the example need the answer one. If a search returned the second copy's index, it would incorrectly count the first `2` as smaller even though equal values do not satisfy the strict relation.

`bisect_left(arr, x)` finds the leftmost insertion position for `x`: the first index at which `x` could be inserted while keeping `arr` sorted. Every element before that position is strictly less than `x`. Every element from that position onward is greater than or equal to `x`. Thus its return value is exactly the desired count, including when `x` occurs many times.

It may help to separate an index from an element count. Python uses zero-based indices. If the first `x` is stored at index $k$, there are exactly $k$ slots before it, numbered from zero through $k-1$. Therefore the index itself is already the count; there is no need to add or subtract one.

**Preserving the original order**

Sorting rearranges values, but the result must align with the original `nums` positions. The solution therefore keeps `arr` only as a search structure and iterates through `nums` in its original order:

`[bisect_left(arr, x) for x in nums]`.

For each original `x`, it searches the same sorted copy and appends the count. This is why the answer for the sample is `[4, 0, 1, 1, 3]` rather than the counts in sorted-value order. Because `sorted(nums)` returns a new list, the caller's input list is not modified.

**How binary search finds the boundary**

Binary search repeatedly discards half of the remaining sorted range. `bisect_left` looks for a boundary, not merely for any matching element. When the middle value is less than `x`, that middle position and everything before it cannot be the answer, so the search continues to the right. When the middle value is at least `x`, the first valid position may be the middle or somewhere to its left, so the search keeps the left half. When the range becomes empty, the remaining insertion position is the first position holding a value at least `x`.

This boundary definition also works when a searched value is absent, although every searched `x` in this solution came from `nums` and is therefore present in `arr`. For a value smaller than everything, the boundary is zero. For one larger than everything, the boundary is the array length.

**Why the complete algorithm is correct**

Fix any original index $i$ and let $x=\texttt{nums[i]}$. Sorting preserves all values and their multiplicities; it changes only their order. In `arr`, strict sorted order guarantees that every value before the leftmost position of `x` is smaller than `x`, and no value at or after that position is smaller. Hence `bisect_left(arr, x)` equals the number of qualifying array elements. The comprehension performs this valid calculation once for every original position and emits answers in the same order. Therefore every output entry has exactly the required count.

Notice that the condition $j\ne i$ needs no special handling. The current element equals itself, so it is never among the strictly smaller elements counted before the left boundary. Other equal elements are excluded for the same reason.

## Complexity detail

Let $n$ be the length of `nums`. Creating `arr` with comparison sorting takes $O(n\log n)$ time. Each call to `bisect_left` takes $O(\log n)$ time, and the comprehension makes $n$ calls, adding another $O(n\log n)$. The exact implementation therefore takes $O(n\log n)$ time overall.

The sorted copy uses $O(n)$ space. The returned answer also contains $n$ integers. Depending on whether output storage is counted as auxiliary space, one can describe the additional working space as $O(n)$ for `arr` and the total newly allocated space as $O(n)$ as well.

The Optimal manifest lists $O(n+U)$ time and $O(U)$ space, where $U$ is the bounded value universe. Those bounds describe the frequency-counting alternative made possible by $0\le\texttt{nums[i]}\le100$; they do not describe the actual sort-and-`bisect_left` statements in this solution file. For understanding or analyzing this exact code, $O(n\log n)$ time and $O(n)$ extra storage are the accurate bounds. The chosen implementation is nevertheless simple, robust, and independent of the small numeric range.

## Alternatives and edge cases

- **Frequency array and prefix counts:** Because every value lies between zero and one hundred, count each value and convert frequencies into counts of smaller values. This achieves the manifest's $O(n+U)$ time and $O(U)$ space, but it is tied to a small known universe.
- **Brute-force comparisons:** For every position, scan the whole array and count smaller values. It is easy to derive but costs $O(n^2)$ time.
- **First-rank dictionary:** Sort once and record the index only when a value is first encountered, then look up each original value. This has the same $O(n\log n)$ sorting cost and can avoid $n$ binary searches, at the price of a dictionary.
- **Duplicate values:** Every equal value receives the same answer because `bisect_left` always returns the shared first position, never an arbitrary duplicate position.
- **All values equal:** The first position of that value is zero, so every output entry is zero.
- **Smallest value:** Its left boundary is zero even if it appears several times, correctly showing that no value is strictly smaller.
- **Largest value:** Its first sorted index counts every smaller element but excludes all copies equal to it.
- **Original order:** Searching values from `nums` rather than iterating through `arr` is essential; otherwise the counts would be returned in sorted order.
- **Input mutation:** `sorted` creates a copy, so the method leaves `nums` unchanged. Using `nums.sort()` without retaining the original order would make constructing the correctly ordered result harder.
- **Import expectation:** The code calls `bisect_left` directly, so the execution environment must make that name available, commonly through `from bisect import bisect_left`.
- **Values outside the stated range:** The sort-and-binary-search method still works for arbitrary mutually comparable numbers; unlike the frequency-array alternative, it does not depend on the zero-to-one-hundred constraint.

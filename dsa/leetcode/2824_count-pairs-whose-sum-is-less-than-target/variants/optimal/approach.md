## General

**Sort so each pair can be counted through one endpoint.** The original index order does not affect whether two values sum below `target`; the condition only requires two distinct positions. Sorting rearranges positions but preserves the multiset of values and therefore preserves the number of unordered index pairs satisfying the sum inequality.

The exact source sorts `nums` in place. It then treats each sorted index `j` as the right endpoint of a pair and counts how many earlier indices `i < j` work with it.

**Turn the sum condition into a threshold for the left value.** For current value `x = nums[j]`,

$$
\texttt{nums}[i]+x<\texttt{target}
$$

is equivalent to

$$
\texttt{nums}[i]<\texttt{target}-x.
$$

The prefix `nums[0:j]` is sorted. Therefore, all prefix values satisfying the strict threshold form one contiguous block at the beginning.

**Use lower bound to count that block.** `bisect_left(nums, target - x, hi=j)` searches only indices before `j`. It returns the first index where `target - x` could be inserted while maintaining sorted order. Equivalently, it returns the number of prefix values strictly less than `target - x`.

That returned index is stored in `i` and added directly to `ans`. If it is zero, no earlier value works. If it is `j`, all `j` earlier positions work.

Using `bisect_left` rather than `bisect_right` implements strict inequality correctly. Values exactly equal to `target - x` would create a pair sum equal to target and must not be counted. Lower bound stops before those values.

**Count every unordered pair once.** Any two distinct sorted positions have a unique larger index `j`. The iteration for that `j` searches only the earlier prefix, so the pair can be counted there and nowhere else. It is never counted in reverse, and an element is never paired with itself because `hi=j` excludes the current index.

For each `j`, binary search counts exactly the earlier positions that satisfy the inequality. Summing those disjoint per-right-endpoint counts therefore gives exactly the total number of valid pairs.

**Example of the boundary.** Suppose the sorted values are `[-1, 1, 1, 2, 3]` and target is two. At the right endpoint containing two, the left value must be below zero. Lower bound for zero within the earlier prefix is one, so only negative one is counted. Values equal to zero, if present, would be excluded because their pair sum would equal two.

**Duplicates represent different positions.** Sorting keeps all occurrences. If three equal values lie below the threshold, lower bound counts all three indices. This is necessary because the problem counts index pairs, not distinct value combinations.

**Why sorting is safe despite the index wording.** There is a one-to-one correspondence between original element occurrences and sorted element occurrences, even when values repeat. Each unordered pair of occurrences has the same two values before and after sorting, so its sum status is unchanged. Only the labels of its positions change, and the condition $i<j$ merely chooses one orientation for the unordered pair.

**The implementation is a binary-search variant, not the whole-range two-pointer count in the manifest.** The manifest summary describes moving left and right pointers and counting a block of partners at once. The exact source performs one lower-bound query for every right index. Both take $O(n\log n)$ overall once sorting is included, though the post-sort two-pointer phase is linear and this post-sort phase is $O(n\log n)$.

**Input mutation.** `nums.sort()` changes the caller's array order. The method needs no copy for correctness, but callers that require the original sequence must provide one or restore it afterward.

## Complexity detail

Let $n$ be the number of values. Python sorting takes $O(n\log n)$ worst-case time. The loop runs $n$ times, and every `bisect_left` over a prefix takes $O(\log n)$ time. The counting phase is therefore $O(n\log n)$, and total time remains $O(n\log n)$.

The scalar variables use $O(1)$ explicit space. Python's in-place list sort may allocate $O(n)$ temporary references in the worst case because Timsort merges runs. The manifest reports $O(n)$ space, which is a safe language-level bound. If sorting workspace is ignored by convention, the algorithm's own post-sort auxiliary space is $O(1)$.

The maximum answer is $n(n-1)/2$. Python integers cannot overflow, and the given $n\le 50$ makes the value small anyway.

An alternative two-pointer scan would reduce the work after sorting to $O(n)$, but sorting would still dominate the overall asymptotic time.

## Alternatives and edge cases

- **Two pointers after sorting:** If the smallest plus largest value is below target, that smallest value pairs with every position through the largest, so count the whole range and advance the left pointer; otherwise decrease the right pointer. This gives $O(n)$ after sorting and matches the manifest's summary.
- **Brute-force nested loops:** It takes $O(n^2)$ time and $O(1)$ space. The small $n\le50$ bound makes it feasible, but it does not exploit ordering.
- **Frequency table over the small value range:** Since values lie between negative fifty and fifty, counts can be combined in constant-range time, with careful handling of equal-value pairs.
- **Strict inequality:** A sum exactly equal to target must be excluded; `bisect_left` enforces this boundary.
- **Negative target and values:** The algebraic threshold and sorted order work without any positivity assumption.
- **Duplicate values:** Every occurrence is a separate index, and lower bound counts each eligible occurrence.
- **First sorted position:** Its prefix is empty, binary search returns zero, and no pair is added.
- **All pairs valid:** For every `j`, the returned count is `j`, summing to $n(n-1)/2$.
- **No pairs valid:** Every lower bound is zero and the answer remains zero.
- **Single-element array:** There are no two-index pairs, so the one loop iteration adds zero.
- **Input order:** Sorting mutates `nums`, even though the returned count does not depend on order.
- **Current index exclusion:** The `hi=j` argument is necessary; searching the entire list could count the current element or later elements and duplicate pairs.

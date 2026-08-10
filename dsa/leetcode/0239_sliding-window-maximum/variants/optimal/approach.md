## General

The array contains $n-k+1$ consecutive windows. Recomputing the maximum by scanning all $k$ elements of every window repeats almost the same work after each one-position slide and can take $O(nk)$ time. The exact solution instead keeps a priority queue containing candidates seen so far. Python's `heapq` is a min-heap, so the solution stores each value as `-value`; the smallest stored negative number then represents the largest original value.

Each heap entry is a pair `(-value, index)`. The value determines priority, while the index answers a separate and essential question: is that occurrence still inside the current window? Storing only values would be insufficient when equal values occur, and it would provide no reliable way to tell whether a maximum came from an index that the window has already passed.

**The window boundaries**

When the loop is processing index `i`, that index is the right endpoint of the current window. A window of length `k` ending at `i` begins at

$$
i-k+1.
$$

Therefore, a heap entry at index `j` is current exactly when

$$
j \ge i-k+1,
$$

or equivalently when $j>i-k$. Any entry satisfying $j\le i-k$ is stale.

The code uses precisely this test in `while q[0][1] <= i - k`. Notice the non-strict comparison. At the moment the right endpoint advances to `i`, the old index `i - k` is one position before the new window's left boundary, so it must no longer influence the answer.

**Build just before the first complete window**

The initial comprehension inserts indices `0` through `k - 2`, the first `k - 1` elements. `heapify(q)` converts those pairs into a heap in linear time with respect to the number inserted. The main loop then begins at `i = k - 1`. It pushes the last element needed for the first full window before reading a maximum.

This division of work means every answer is produced by the same loop body:

1. Add the new rightmost element.
2. Remove stale entries from the top until the top belongs to the current window.
3. Convert the top's negated value back to its original sign and append it.

For `k = 1`, the initial slice `nums[:0]` is empty, so heapifying it is valid. Each main-loop iteration pushes the one visible element, removes any older top entries if necessary, and returns that element. Thus the same structure handles the smallest window without a separate branch.

**Why stale entries can be removed lazily**

The heap may contain indices that have left the window. The solution does not search through the heap to delete every such entry because a binary heap supports efficient removal at the root, not efficient arbitrary removal by index. Instead, it performs lazy deletion: an expired entry is tolerated until it reaches the root.

This is safe because only the root is ever used as the answer. If a stale entry is buried below another entry, it cannot affect the reported maximum at that moment. When it eventually becomes the root, the `while` loop checks its index and discards it before any answer is appended. Several expired entries can surface consecutively, which is why the code uses `while` rather than `if`.

**Why the heap top is the current maximum**

After `heappush`, the heap contains the new element and every earlier element not previously removed. In particular, it contains every index in the current window: current entries were inserted when encountered, and the cleanup rule removes an entry only after its index is too small for the current window. It may additionally contain expired entries.

The cleanup loop ends only when the root's index lies inside the current window. Since the root has the smallest `-value`, it has the greatest original value among **all** entries still in the heap. It is therefore at least as large as every current entry. Because the root itself is current, it is exactly a maximum of the present window. Appending `-q[0][0]` consequently returns the correct value.

Tie-breaking does not invalidate this reasoning. Python compares pair elements lexicographically, so equal negated values are ordered by index. Either occurrence has the same maximum value. If the chosen occurrence is expired, cleanup removes it and checks again; if it is current, reporting its value is correct.

**Trace on the first example**

For `nums = [1, 3, -1, -3, 5, 3, 6, 7]` and `k = 3`, initialization inserts `1` at index `0` and `3` at index `1`.

- At `i = 2`, insert `-1`. No root is older than the window `[0, 2]`. The greatest value is `3`, so append `3`.
- At `i = 3`, insert `-3`. Index `0` has expired, but it is not the maximum and can remain buried. The root is the current `3` at index `1`, so append `3`.
- At `i = 4`, insert `5`. It immediately becomes the root and is inside `[2, 4]`, so append `5`.
- At `i = 5`, insert `3`. The root remains the current `5`, so append `5`.
- At `i = 6`, insert `6`; it becomes the root, producing `6`.
- At `i = 7`, insert `7`; it becomes the root, producing `7`.

The result is `[3, 3, 5, 5, 6, 7]`. This trace also exposes lazy deletion: the expired `1` need not be removed because it never threatens to become the reported maximum while larger current values remain above it.

**Important distinction from the manifest summary**

The exact protected solution uses a heap, not a monotonic deque. A monotonic deque can achieve worst-case $O(n)$ time and $O(k)$ space, but those are not the bounds of this implementation. An accurate explanation must follow the executable source: lazy heap entries can remain after leaving the window, so the heap may grow beyond `k`, and heap operations introduce logarithmic time.

## Complexity detail

Let $n$ be the length of `nums`. Constructing and heapifying the first $k-1$ entries costs $O(k)$. Every one of the $n-k+1$ main iterations performs one heap insertion. A heap can contain as many as $O(n)$ entries, so an insertion costs $O(\log n)$ in the worst case.

Each entry is removed at most once by the cleanup loop. Although one iteration may pop many entries, there are at most $n$ pops over the entire execution. Each pop costs $O(\log n)$ in the worst case. The total running time is therefore $O(n\log n)$, not the manifest's stated $O(n)$.

Lazy deletion also affects memory. Expired values that never rise to the root are retained. For a strictly increasing array, new values continually become the root, while many older values remain stored below; the heap can grow to $n$ entries. Thus the heap uses $O(n)$ auxiliary space in the worst case, rather than a guaranteed $O(k)$. The returned list has $n-k+1$ elements and requires $O(n)$ output space separately.

## Alternatives and edge cases

- **Monotonic decreasing deque:** Store useful indices in increasing index order and decreasing value order. Remove expired indices from the front and values dominated by the newcomer from the back. Each index enters and leaves once, giving $O(n)$ time and $O(k)$ auxiliary space; this is the stronger asymptotic solution described by the local editorial and manifest, but it is not what the exact optimal source implements.
- **Balanced multiset:** Insert the entering value, erase the leaving occurrence, and query the greatest value. This gives $O(n\log k)$ time and $O(k)$ space in languages with an ordered multiset, provided duplicates are represented correctly.
- **Direct scan of every window:** It uses only constant auxiliary space but costs $O(nk)$ in the worst case because it rediscovers nearly the same maximum repeatedly.
- **Lazy heap expiration:** Arbitrary expired entries do not need immediate deletion. Only an expired root can corrupt the answer, so root cleanup is sufficient for correctness, though it permits $O(n)$ memory growth.
- **Several stale roots:** The cleanup must be a `while` loop. Removing just one stale root may expose another stale entry before any current entry reaches the top.
- **Duplicate maximum values:** Pairing each value with its index distinguishes occurrences. Expiration is decided per occurrence, while either current occurrence yields the same maximum value.
- **`k = 1`:** The initial heap is empty, and every element becomes the maximum of its one-element window.
- **`k = n`:** Initialization loads the first $n-1$ values, the loop adds the last, and exactly one maximum is returned.
- **Negative values:** Negation still reverses priority correctly. For example, original `-3` is stored as `3`, while original `-1` is stored as `1`, so `-1` is recovered as the larger value.
- **Expired non-root entries:** Their presence is harmless for correctness but important for complexity analysis. Claiming the heap always contains only the current window would be inaccurate for this implementation.

## General

**Rephrase “second greater” as an ordered-index query**

For index `i`, consider all indices to its right whose values are strictly greater than `nums[i]`. Sort those qualifying indices by their natural array order. The first is the first greater element; the second, if it exists, is exactly the requested second greater element.

The exact solution processes elements from larger value to smaller value while maintaining a sorted set of indices already processed. When handling `i`, that set represents positions with values strictly greater than `nums[i]`. It can then select the second stored index greater than `i`.

This differs from the manifest summary's two-monotonic-stack $O(n)$ method. The protected source uses sorting plus a `SortedList` and therefore takes $O(n\log n)$ time.

**Sort values in descending order**

`arr = [(x,i) for i,x in enumerate(nums)]` creates value-index pairs. Sorting with `key=lambda x: -x[0]` processes larger values first.

Python's sort is stable. Equal values retain their original increasing-index order from `enumerate`. This stability is important because equal values are not strictly greater and should not act as candidates for one another.

When an equal-valued earlier index has already been added to `sl`, it lies to the left of the current index. The later equal-valued indices, which would lie to its right, have not yet been processed. Thus positions in `sl` to the right of current `i` all have strictly greater values.

Without stable tie ordering or explicit equal-value batching, inserting one equal value before another could incorrectly treat it as greater if its index were to the right.

**Locate the first two greater positions**

`sl` stores processed indices in ascending order. For current index `i`,

`j = sl.bisect_right(i)`

returns the list position of the first stored index strictly greater than `i`. If it exists, `sl[j]` is the first greater element to the right. The requested answer is the next qualifying index, `sl[j+1]`.

The condition `j + 1 < len(sl)` checks that this second index exists. If so, `ans[i] = nums[sl[j+1]]` stores its value. Otherwise the initial -1 remains.

After answering the current index, `sl.add(i)` makes it available as a greater-value position for later-processed smaller values.

**Trace the first example**

For `nums=[2,4,0,9,6]`, values are processed in order 9 at index 3, 6 at index 4, 4 at index 1, 2 at index 0, and 0 at index 2.

- Index 3 sees no greater processed index to its right and remains -1.
- Index 4 also has none to its right.
- For index 1 with value 4, stored greater positions to the right are 3 and 4. The second is index 4, whose value is 6.
- For index 0 with value 2, greater positions to the right in order include indices 1, 3, and 4. The second is index 3, value 9.
- For index 2 with value 0, greater positions to the right are indices 3 and 4. The second is index 4, value 6.

The result is `[9,6,6,-1,-1]`.

**Connect the query to the formal definition**

Let `p1 < p2` be the first two indices greater than `i` stored to its right. Both values exceed `nums[i]`. Exactly one qualifying index lies between `i` and `p2`, namely `p1`; if another existed, it would appear before `p2` in the sorted index set. Hence `nums[p2]` satisfies the definition.

Conversely, any index satisfying the definition must be the second qualifying index in rightward order. The bisect lookup returns precisely that index when it exists.

**Why answer before insertion**

Adding `i` before querying would place the current index in `sl`. `bisect_right(i)` would skip it, so it might not directly corrupt this query, but answering first cleanly preserves the invariant that `sl` contains only previously processed values. More importantly, insertion afterward lets current `i` participate only in queries for smaller values processed later.

The result list begins with -1 at every position, exactly matching the required sentinel for fewer than two greater values.

## Complexity detail

Let $n$ be the array length. Building pairs takes $O(n)$ time and space. Sorting them takes $O(n\log n)$ time. Each of the $n$ iterations performs one `bisect_right` and one `SortedList.add`, each $O(\log n)$ for the balanced sorted-container implementation. Total time is $O(n\log n)$.

The pair array, sorted index structure, and answer list each contain $O(n)$ entries, so space is $O(n)$. This time bound contradicts the manifest's $O(n)$ two-stack claim, though the space bound agrees.

The source depends on `SortedList` being available in the execution environment, typically from a sorted-container library. A plain Python list would make insertion $O(n)$ and degrade total time to $O(n^2)$.

## Alternatives and edge cases

- **Two monotonic stacks:** Move indices from a stack awaiting their first greater value to one awaiting their second, resolving the second stack as new values arrive. This matches the manifest and achieves $O(n)$ time.
- **Batch equal values:** Process all indices of one value by querying first and adding the entire group afterward. This removes reliance on stable tie order and is often clearer for strict comparisons.
- **Balanced tree of indices:** Any ordered set supporting successor queries and insertion can replace `SortedList` with the same $O(n\log n)$ structure.
- **Duplicate values:** Equal values do not count as greater. Stable ascending-index tie processing prevents later equals from appearing in the queried right-side set.
- **Fewer than two greater elements:** The answer remains the initialized -1.
- **Greater values before `i`:** They are stored but ignored by `bisect_right(i)` because only positions to the right matter.
- **Second qualifying index:** Its numeric value can be smaller than the first greater value; only both must exceed `nums[i]`.
- **Strict comparison:** Values equal to `nums[i]` must never count, which is the subtle reason tie handling matters.
- **Single element:** The sorted set is initially empty, so the sole answer is -1.
- **Metadata mismatch:** The exact implementation is sorting plus ordered-index queries in $O(n\log n)$, not the documented two-stack linear scan.

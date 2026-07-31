## General

Two independent facts are needed for each creator: the sum of all their view counts and which one of their videos wins the individual-video comparison. Maintain `totals[creator]` for the first fact and `best[creator] = (view_count, video_id)` for the second.

Process the three aligned arrays together. Add every `view_count` to its creator's total. Replace that creator's best pair when the current video has more views, or when it has the same number of views and a lexicographically smaller identifier. This comparison depends on the array entry rather than identifier uniqueness, so repeated IDs still contribute as distinct videos.

After this pass, each total includes exactly all videos from its creator, and each saved identifier is the required maximum-view, minimum-ID choice. Find the largest creator total, then emit the saved pair for every creator whose total equals it. Iterating through a hash map determines only output order, which the contract leaves unrestricted.

## Complexity detail

Let $n$ be the common length of `creators`, `ids`, and `views`. Both the aggregation pass and the final creator scan take $O(n)$ expected time under standard hash-table behavior, so total time is $O(n)$.

There can be $O(n)$ distinct creators. The two maps and the returned answer therefore require $O(n)$ space under the repository's reference-solution accounting.

## Alternatives and edge cases

- **Sort by creator:** Sorting aligned video records can group creators and solve the problem in $O(n\log n)$ time, but hashing avoids the sort.
- **Rescan for every creator:** Computing each creator's total and best video by repeatedly scanning all videos is correct but takes $O(n^2)$ time when creators are distinct.
- **Heap for popular creators:** A heap is unnecessary because the result needs every creator tied at one maximum, which a final linear scan finds directly.
- **Creator-total ties:** Emit every creator at the maximum rather than resolving the tie between creators.
- **Video-view ties:** Resolve ties only within the same creator, choosing the lexicographically smallest identifier.
- **Duplicate identifiers:** Equal IDs do not merge videos; each array position contributes its own view count.
- **Zero views:** A creator with only zero-view videos is valid, and all creators can tie at total zero.
- **Single video:** Its creator is necessarily most popular and that video's identifier is selected.
- **Output order:** The list of creator pairs is unordered, but each inner pair must keep creator first and identifier second.

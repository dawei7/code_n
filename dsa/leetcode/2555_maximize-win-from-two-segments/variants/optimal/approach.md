## General

Because the positions are sorted, the prizes covered by one segment form a contiguous index window. Move a right endpoint through the array and advance `left` only while the coordinate span exceeds $k$. The resulting window $[left,right]$ is the largest segment-covered suffix ending at `right`.

Store `best_prefix[i]` as the greatest number of prizes one segment can cover using only indices before `i`. The current window contributes `right - left + 1` prizes, and `best_prefix[left]` supplies the best earlier segment whose prizes are disjoint from it. Their sum is therefore a valid union size without double counting.

Although the statement permits intersecting segments, overlap never improves the union beyond this combination. Any prizes covered twice add nothing, and the same collected union can be represented by assigning its left group to one segment and its right group to the other. Taking the maximum over every right endpoint consequently considers an optimal placement.

The left pointer moves only forward, and each prefix entry is updated from the previous best and the current window size. Thus every prize enters and leaves the active window at most once.

## Complexity detail

Let $n$ be the number of prizes. The right pointer visits all $n$ indices and the left pointer advances at most $n$ times, giving $O(n)$ time. The prefix-best array contains $n+1$ integers and uses $O(n)$ space.

## Alternatives and edge cases

- **Binary search per endpoint:** Finding every left boundary with lower-bound search is correct and takes $O(n \log n)$ time, but the monotone boundary makes a sliding window faster.
- **Restarted boundary scan:** Scanning from index zero for every right endpoint can take $O(n^2)$ time when valid windows are short.
- **Duplicate coordinates:** Every duplicate represents a separate prize and must remain a separate array entry in the window count.
- **Zero-length segments:** When $k=0$, a segment covers all prizes at one coordinate; the two best occupied coordinates may both contribute.
- **Intersecting segments:** A prize in the overlap counts once, so simply adding two arbitrary window sizes can overcount.
- **One segment already covers all prizes:** The second segment may overlap it, and the answer is still $n$, never more.

## General

**The answer is peak overlap.** Every set of intervals containing a common
point requires different groups, giving a lower bound equal to the maximum
number simultaneously active. Conversely, inclusive intervals form an
interval graph, whose intervals can be greedily assigned using exactly that
many groups. It is therefore enough to measure peak concurrency.

**Process starts in chronological order.** Sort intervals by left endpoint.
Maintain a min-heap containing the right endpoints of intervals still active
when the next interval starts.

**Release only strictly earlier ends.** Before inserting `[left,right]`, remove
every heap minimum with end `< left`. Those intervals have ended before the
new one begins and their groups can be reused. An end equal to `left` remains
active because both intervals include that point. Push `right` and update the
largest heap size.

The heap contains exactly the processed intervals intersecting the current
start point. Its size after insertion is thus the concurrency at that point,
and the maximum observed size is the peak overlap lower bound. Reusing groups
whenever an end is strictly earlier constructs an assignment using no more
than that peak, so the recorded maximum is also achievable and therefore
optimal.

## Complexity detail

Let $n$ be the number of intervals. Sorting costs $O(n\log n)$. Each right
endpoint is pushed once and popped at most once, adding $O(n\log n)$ heap
work. Total time is $O(n\log n)$ and the sorted list plus heap use $O(n)$
auxiliary space.

## Alternatives and edge cases

- **Two sorted endpoint arrays:** Sweep sorted starts and ends with two
  pointers, treating a start equal to an end as occurring first; this has the
  same $O(n\log n)$ time and $O(n)$ space.
- **Difference array:** Add one at `left` and subtract one at `right + 1`,
  then take the maximum prefix sum. It can be linear in the coordinate range
  but depends on the bounded endpoint domain.
- **Scan existing groups:** Try each group until finding an end below the new
  start; this is correct but can take $O(n^2)$ time when all intervals overlap.
- **Touching endpoints:** Equal end and start values intersect because the
  intervals are inclusive.
- **Point intervals:** `[x,x]` is active at exactly `x` and conflicts with
  every other interval containing `x`.
- **Duplicate intervals:** Each copy needs a distinct group while they overlap.
- **Disjoint intervals:** Every prior end is released, keeping the answer at
  one.

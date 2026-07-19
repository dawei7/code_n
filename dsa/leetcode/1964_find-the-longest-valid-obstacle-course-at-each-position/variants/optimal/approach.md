## General
**Keep the smallest tail for each length**

Maintain `tails`, where `tails[length - 1]` is the smallest ending height found
for any non-decreasing course of that length in the processed prefix. Smaller
tails are never worse: they permit every future obstacle that a larger tail
would permit. These representative heights stay sorted.

**Extend through equal heights**

For a new height, use an upper-bound search to find the first tail strictly
greater than it. Every preceding tail is less than or equal to the new height,
so the longest extendable course has length equal to that insertion index.
Appending the new obstacle produces the reported length `index + 1`.

If the index is new, append the height; otherwise replace the larger existing
tail at that index. The replacement preserves the best achievable lengths and
improves or retains their extension opportunities. Because the current
obstacle is explicitly appended to the chosen predecessor course, the reported
value ends at the required index. Using upper bound rather than lower bound is
essential: equal heights are allowed to extend a non-decreasing course.

## Complexity detail
Each of the $N$ obstacles performs one binary search in a `tails` array of
length at most $N$, giving $O(N\log N)$ time. The tails and answer arrays each
store at most $N$ integers, so the auxiliary and output storage are $O(N)$.

## Alternatives and edge cases
- **Predecessor dynamic programming:** For each index, inspect every earlier
  height no greater than the current height. This is direct and correct but
  takes $O(N^2)$ time.
- **Fenwick tree over compressed heights:** Query the best length at heights
  no greater than the current one and update its height. This also takes
  $O(N\log N)$ time but needs coordinate compression and more machinery.
- Equal consecutive heights produce increasing answers because equality is
  valid in a non-decreasing course.
- A strictly decreasing array gives answer one at every position.
- The smallest-tail representatives need not describe one single course;
  each position represents the best tail among courses of that length.

## General
At position `i`, only equal values among the previous `k` positions can form an allowed pair. Maintain a set representing
that sliding prefix window rather than retaining information about values that are already too far away.

Before inserting `nums[i]`, test whether it is in the set. A hit witnesses an earlier equal value whose position differs
from `i` by at most `k`, so return `true`. Otherwise insert the current value. If `i >= k`, remove `nums[i - k]` after the
test and insertion so that the set is ready for the next position.

The removal order matters. Position `i - k` is still exactly distance `k` from `i` and must participate in the current
membership test. It becomes too old only for position `i + 1`, which is why it is removed at the end of the iteration.

For `[1,2,1,1]` with $k = 1$, the set before position 2 contains only `2`, so the earlier `1` at position 0 is correctly
ignored. After processing position 2, the window becomes `{1}`; the `1` at position 3 is then detected at distance one.

Assume no pair has yet been returned. Before position `i`, the set contains exactly the values at positions
$\max(0, i-k)$ through $i-1$. Those values are distinct—otherwise an earlier iteration would already have returned. A
membership hit is therefore precisely an equal value at an allowed earlier position. After a miss, adding the current
value and removing the position that will be too old next restores the window invariant. If the scan finishes, no legal
pair exists.

## Complexity detail
Each element is inserted once and removed at most once. Expected $O(1)$ set operations give expected $O(n)$ time. The
set contains at most `k` previous values, and never more than the input length, so it uses $O(\min(n,k))$ auxiliary space.

## Alternatives and edge cases
- **Latest-position map:** Recording the most recent position of every distinct value also gives expected $O(n)$ time,
  but can retain $O(n)$ entries even when `k` is small.
- **Preceding-window scan:** Comparing each position with up to `k` predecessors takes $O(nk)$ time.
- **First occurrence only:** Retaining only the earliest equal value can miss a closer later pair.
- **Zero distance:** When $k = 0$, each inserted value is removed in the same iteration, so two distinct positions can
  never qualify.
- **Adjacent duplicates:** They are detected whenever $k \ge 1$.

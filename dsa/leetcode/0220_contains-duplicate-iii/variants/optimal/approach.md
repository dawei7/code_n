## General
Both constraints must hold simultaneously, so maintain only the values at indices close enough to the current index and organize those values by numeric proximity.

Choose bucket width `w = valueDiff + 1`. Under floor division, any two integers in the same bucket differ by at most `w - 1 = valueDiff`, so a same-bucket value is an immediate match. Values within `valueDiff` but separated by a bucket boundary can lie only in adjacent buckets; buckets two or more apart are at least $w + 1$ apart in the relevant direction and cannot qualify.

For current value `x` with bucket $b = \left\lfloor x / w \right\rfloor$:

1. If bucket `b` is occupied, return true.
2. Compare `x` with the stored value in $b - 1$, if any, and verify the actual difference.
3. Do the same for $b + 1$.
4. Store `x` in `b`.
5. Remove the value whose index will be more than `indexDiff` away on the next iteration.

The explicit neighbor difference check is necessary because adjacent buckets can contain values farther apart than `valueDiff`. At most one active value occupies a bucket: inserting a second would already have triggered the same-bucket success.

**Window timing**

When processing index `i`, the active buckets contain earlier indices from `i - indexDiff` through $i - 1$, so distance exactly `indexDiff` is included. Removing `nums[i - indexDiff]` after the current comparisons keeps it available for index `i` but excludes it before index $i + 1$. For `indexDiff = 0`, each value is inserted and immediately removed, so no value can pair with itself.

Negative values require floor-consistent bucket ids. Python's `//` already floors; languages whose integer division truncates toward zero need an adjusted bucket formula, otherwise values around zero may be grouped inconsistently.

Every stored value has an index within the allowed window. If the algorithm accepts a same-bucket pair, its difference is at most `valueDiff`; for a neighboring bucket it verifies that bound explicitly, so every accepted pair satisfies both constraints. Conversely, consider a qualifying earlier value. It is still active because its index distance is allowed. Its value must lie in the current bucket or one of the two neighboring buckets, so the corresponding lookup and comparison finds it. Therefore no valid pair is missed.

## Complexity detail
Each index performs a constant number of expected $O(1)$ dictionary operations, giving expected $O(n)$ time. The active dictionary contains at most `indexDiff` prior values, bounded by `n`, so space is $O(\min(n, indexDiff))$.

## Alternatives and edge cases
- An ordered multiset over the active window can find a value in `[x - valueDiff, x + valueDiff]` in $O(\log k)$ time.
- Comparing against every active value costs $O(n \cdot indexDiff)$ in the worst case.
- Truncating negative division without adjustment breaks bucket adjacency reasoning.
- `valueDiff = 0` reduces to nearby equality; `indexDiff = 0` always returns false.
- Use a wide enough numeric type for differences and `valueDiff + 1` in fixed-width languages.

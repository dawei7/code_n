## General

Choosing a starting tree and moving right while taking every fruit means the collected trees always form one contiguous subarray. Two baskets that each hold one type mean this subarray may contain at most two distinct fruit types. The problem is therefore:

> Find the longest contiguous subarray containing at most two distinct values.

The solution maintains a sliding window `fruits[j:i+1]` with a Counter storing the frequency of each fruit type currently inside.

**Expand the right edge.** The for-loop advances `i` through every tree. When fruit type `x` enters, `cnt[x]` is incremented. This considers every possible window ending at `i`.

**Shrink only when the basket rule is violated.** If adding `x` creates more than two Counter keys, the current window uses too many types. The while-loop repeatedly removes the leftmost fruit `fruits[j]` and advances `j`.

Decrementing a count is not enough when it reaches zero. A zero-count type is no longer present and must be removed with `cnt.pop(y)`; otherwise `len(cnt)` would still report a nonexistent third type.

Shrinking stops as soon as at most two types remain. The resulting window is valid.

**Why the resulting window is the longest valid one ending at `i`.** Before the new fruit arrived, `j` was the smallest left boundary needed for the previous valid window. If the expanded window remains valid, keeping the same `j` obviously gives the longest current ending window considered by this process.

If it becomes invalid, every left boundary before the final `j` still includes all three types and is invalid. The loop stops at the first boundary that removes one type completely. Thus no valid window ending at `i` starts earlier, and `i - j + 1` is the maximum valid length for that right endpoint.

Taking the maximum across every endpoint gives the global optimum.

**Why moving `j` forward never misses an answer.** Once a prefix has been removed because a window ending at some `i` contained three types, restoring an earlier left boundary for a later, even farther-right endpoint cannot remove that violation; it only includes more old fruits. Any future optimum starting there would have had to pass through an already invalid configuration unless types disappear by moving the left edge, which is exactly what `j` records. Sliding windows exploit this monotonic left-boundary behavior.

For `[0,1,2,2]`:

- Windows ending at indices 0 and 1 contain at most two types.
- Adding 2 creates types 0, 1, and 2. The loop removes 0 and moves `j` to 1.
- Window `[1,2]` is valid, and extending with the final 2 yields length 3.

This corresponds to starting at tree 1 and collecting `[1,2,2]`.
After the shrink loop for each `i`:

- `cnt` contains exactly the frequencies in `fruits[j:i+1]`;
- it has at most two keys;
- any earlier left boundary would be invalid if shrinking was required;
- `ans` is the longest valid window seen through endpoint `i`.

Initialization satisfies the invariant for an empty processed prefix. Expansion, frequency-aware shrinking, and the maximum update preserve it. At loop end, `ans` is the maximum number of collectable fruits.

## Complexity detail

Let $n$ be the number of trees. The right pointer advances $n$ times. The left pointer also advances at most $n$ times across the entire execution, because it never moves backward.

- **Time complexity:** $O(n)$ expected with hash-based Counter operations.
- **Space complexity:** $O(1)$ with respect to $n$ because the valid Counter contains at most two types after shrinking, and temporarily at most three while a violation is repaired.

The fruit type values can range with $n$, but only the types in the current window occupy the Counter.

## Alternatives and edge cases

- **Try every starting tree:** Extending separately from every start can cost $O(n^2)$.
- **General at-most-$K$ window:** The same frequency-map technique works for any fixed number of baskets $K$.
- **Track only two recent types and the final run:** A specialized constant-state solution can avoid a Counter, but its update invariant is less intuitive.
- **Remove a Counter key too early:** A type remains in the window until its count reaches zero; removing it on the first left occurrence would be wrong.
- **Leave zero-count keys:** Then `len(cnt)` overstates distinct types and shrinks too far.
- **One fruit type:** The entire array fits in one basket.
- **Exactly two types:** The entire array fits in the two baskets.
- **Every tree a new type:** The maximum window length is at most two.
- **Long repeated suffix:** Shrinking preserves all remaining copies and can yield a long later window.
- **One tree:** The initial window length one is valid.
- **Contiguity:** The rules do not allow skipping a tree, so a subsequence solution would be incorrect.
- **Unlimited capacity:** Counts affect window maintenance but never fill a basket; only distinct types matter.
- **Any starting point:** Maximizing all valid windows considers every possible start implicitly.

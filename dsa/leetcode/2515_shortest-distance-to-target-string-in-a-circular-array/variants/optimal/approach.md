## General

**Every target occurrence is a possible destination**

The target may appear multiple times. The closest occurrence is not necessarily the first one in ordinary array order, so the method scans all indices and evaluates every word equal to `target`.

For an occurrence at index `i`, there are two directions around the circular array:

- move directly along the index gap;
- wrap around the other side of the circle.

The shorter of these is the distance to that occurrence.

**Compute the two circular distances**

Let

`t = abs(i-startIndex)`.

This is the number of steps between the indices without crossing the array boundary. The circular route in the opposite direction uses the remaining edges of the `n`-node cycle, so its length is

`n-t`.

The shortest distance to occurrence `i` is therefore

$$
\min(t,n-t).
$$

The update

`ans = min(ans,t,n-t)`

compares both routes with the best target occurrence found earlier.

**Why the two choices are exhaustive**

Between two vertices on a simple cycle, there are exactly two simple paths: clockwise and counterclockwise. Any route that reverses direction or loops around more than once repeats edges and is no shorter than one of those two simple paths.

The direct index difference measures one path, and `n-t` measures the complement. Their minimum is exactly the shortest possible movement distance.

**Use `n` as a safe “not found” sentinel**

`ans` starts at `n`. A real shortest distance in a non-empty circular array is always less than `n`:

- direct difference is at most `n-1`;
- the shorter circular distance is at most $\lfloor n/2\rfloor$.

Therefore, `ans==n` after the scan means no matching word ever triggered an update. The method returns `-1` in that case.

There is no ambiguity between the sentinel and a legitimate answer.

**Trace the first sample**

For five words and `startIndex=1`, target `"hello"` occurs at indices 0 and 4.

At index 0:

$$
t=\lvert0-1\rvert=1,
$$

so the two routes have lengths 1 and 4. The best becomes one.

At index 4:

$$
t=\lvert4-1\rvert=3,
$$

so the routes have lengths 3 and 2. This occurrence's best is two, which does not improve the global answer one.

Returning one correctly chooses index 0, even though index 4 may be encountered later.

**Target at the starting index**

If `words[startIndex]==target`, then `t=0` and `ans` becomes zero. No movement is required.

The scan continues, but no nonnegative distance can improve zero. An early return would be possible, yet the exact source keeps one simple uniform loop.

**One-element circular array**

When `n=1`, the only valid start index is zero. If its word matches, direct distance is zero. Otherwise the sentinel remains one and the method returns $-1$.

Modulo-index simulation is unnecessary because the closed distance formula already captures wraparound.

**Why absolute difference is the correct non-wrapping length**

If `i` lies to the right of `startIndex`, moving right without wrapping takes `i-startIndex` steps. If `i` lies to the left, moving left without wrapping takes `startIndex-i` steps. The absolute value combines these two cases into one nonnegative quantity.

The complete circle contains exactly `n` neighbor-to-neighbor edges. Once one route uses `t` of them, the other route must use the remaining `n-t` edges. This complementary-edge view is why the formula works without separately writing four cases for left, right, left with wraparound, and right with wraparound.

For positions exactly opposite each other in an even-length array, `t=n-t`. Both directions are equally short, and taking the minimum correctly returns their common length.

**String equality**

Only exact whole-string matches count. A word containing the target as a substring or differing in case is not accepted. The lowercase contract avoids case-normalization questions.


For each matching index, the algorithm computes its exact shortest circular distance by considering the two cycle paths. Taking the minimum over every matching index gives the shortest distance to the target string anywhere in the array.

If there is no matching index, no path can reach the nonexistent target, and the unchanged sentinel produces `-1`.

The input array and starting position are never modified.

## Complexity detail

Let $n$ be the number of words. The loop examines every word once, so there are $O(n)$ comparisons and constant-time index calculations.

If string-comparison cost is included, let $C$ be the total number of compared characters before equality decisions; runtime is $O(C)$, bounded by $O(nL)$ for maximum word length $L\le100$. Under the usual bounded-string convention, this is reported as $O(n)$.

Only `n`, `ans`, `i`, `w`, and `t` are stored. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Bidirectional step simulation:** Move left and right from the start until finding the target. It can return early but requires modular indexing.
- **Preindexed positions:** Store occurrence indices per word for many repeated queries, but one query does not justify the extra structure.
- **Target at start:** Return distance zero.
- **Multiple occurrences:** Evaluate all or stop only when the theoretical minimum zero is found.
- **No occurrence:** The sentinel remains `n` and becomes `-1`.
- **One-element array:** The result is zero on a match and `-1` otherwise.
- **Wraparound shorter:** `n-t` captures movement across the end-to-start boundary.
- **Direct route shorter:** `t` captures movement without wrapping.
- **Exact match:** Substrings do not count.
- **Sentinel safety:** No valid shortest circular distance can equal `n`.

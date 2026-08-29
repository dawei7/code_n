## General

**Exploit the two sorted halves**

A mountain array is strictly increasing up to one interior peak and strictly decreasing afterward. It is not globally sorted, but once the peak index is known, each side is monotonic and can be searched with binary search.

The solution therefore performs three logarithmic searches: locate the peak, search the increasing side including the peak, and only if necessary search the decreasing side excluding the peak. Searching the left side first is essential because the same target can appear once on each slope and the contract asks for the minimum index.

**Find the peak from the local slope**

Start with the inclusive interval from zero through `n - 1`. At midpoint `mid`, compare `mountain_arr.get(mid)` with `mountain_arr.get(mid + 1)`. The loop condition `l < r` ensures `mid < r`, so `mid + 1` is always valid.

If the midpoint value is greater than its right neighbor, `mid` is either the peak or lies on the decreasing slope. The peak cannot be to its right, so `r = mid` retains `mid` as a possible peak.

Otherwise, strict mountain structure means the midpoint lies on the increasing slope. It cannot be the peak, and the peak is strictly to its right, so `l = mid + 1` safely discards the left half.

Each update preserves the peak inside the interval and makes the interval smaller. When `l == r`, that one index must be the peak.

**Use one helper for both slope directions**

`search(l, r, k)` is a lower-bound binary search over an inclusive monotonic segment. For the increasing side, `k = 1` leaves values unchanged. For the decreasing side, `k = -1` negates both array values and the target. Negating a strictly decreasing sequence makes it strictly increasing, so the same comparison works.

The condition can be read as:

`k * value_at_mid >= k * target`

When true, midpoint is a possible first occurrence in transformed sorted order, so `r = mid` keeps it. When false, midpoint is too small in transformed order, and every position through it can be discarded with `l = mid + 1`.

When the interval collapses, `l` is the only lower-bound candidate. The helper performs one final interface call and returns `l` only if its actual value equals the target; otherwise it returns `-1`. This final equality check is required because lower bound returns an insertion position even when the target is absent.

**Search the left side before the right side**

The first call is `search(0, peak, 1)`. The peak is included so a target equal to the maximum can be found. If the target occurs on both slopes, the occurrence on the strictly increasing side has the smaller index, and this call returns it.

Only if the first result is `-1` does the code call `search(peak + 1, n - 1, -1)`. Excluding the peak avoids checking it twice. A valid mountain has an interior peak, so this decreasing interval is nonempty.

If neither monotonic segment contains the target, the second helper returns `-1` and that becomes the final answer.

**Respect the interactive access budget**

The method never reads the underlying array directly. It obtains the length once and uses only `mountain_arr.get` for values. Every binary-search iteration halves its interval. Peak search makes two `get` calls per iteration, and each slope search makes one per iteration plus one final equality check.

For at most ten thousand elements, each search needs about fourteen iterations. Even without caching repeated indices, the combined number of calls remains below the allowed one hundred. A linear scan could exceed the budget, which is why logarithmic access is part of correctness for this interface problem.

## Complexity detail

Let $n$ be the mountain length and assume each interface call is $O(1)$. Peak discovery takes $O(\log n)$ iterations. Each of the at most two target searches also takes $O(\log n)$. Their sum is still $O(\log n)$ time.

All searches are iterative and retain only bounds, a midpoint, the direction multiplier, and scalar results. Auxiliary space is $O(1)$. The remote array storage belongs to the interface and is not copied.

The number of `get` calls is also $O(\log n)$, not merely the local arithmetic time. This is the practically important resource enforced by the judge.

## Alternatives and edge cases

- **Two separate binary-search helpers:** Write ordinary comparisons for the increasing and decreasing sides. This may be easier to read, while the multiplier formulation avoids duplicated control flow.
- **Cache interface reads:** A dictionary from index to value can avoid repeated `get` calls, especially around the peak and final checks. It uses $O(\log n)$ extra space but provides more budget margin.
- **Linear scan:** It would find the minimum index directly in $O(n)$ time, but up to ten thousand interface calls violates the one-hundred-call limit.
- **Ternary search for the peak:** Mountain unimodality permits variants, but the adjacent-slope binary search is simpler and halves the interval deterministically.
- **Target equals the peak:** The increasing-side search includes the peak and returns it; the decreasing search is never called.
- **Target on both slopes:** Searching indices zero through the peak first guarantees the smaller left occurrence is returned.
- **Target below every value on one side:** Lower bound collapses to a boundary candidate, and the final equality check correctly rejects it.
- **Target above the peak:** Neither side can contain it. Both final equality checks fail and the result is `-1`.
- **Peak near the left boundary:** The peak is still at least index one, and both the peak comparison and right-side interval remain valid.
- **Peak near the right boundary:** The peak is at most `n - 2`, so `mid + 1` and the decreasing search remain valid.
- **Strict monotonicity:** Equal adjacent values cannot occur under the mountain definition. The peak-direction test relies on this guarantee.
- **Inclusive intervals:** Assigning `r = mid` keeps a midpoint that may be the answer; using `mid - 1` would risk discarding it.
- **Final equality check:** A lower-bound position is only a candidate. Returning it without checking could report an index whose value merely surrounds the absent target.
- **Interface-only access:** The solution must not convert the mountain to a normal list, both because direct access is forbidden and because doing so would consume too many calls.

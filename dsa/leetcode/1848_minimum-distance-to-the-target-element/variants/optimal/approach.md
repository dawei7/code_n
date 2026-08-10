## General

**Evaluate every valid target occurrence.** The target may appear once or many times. For any index `i` where `nums[i] == target`, its distance from the starting index is `abs(i - start)`. The required answer is simply the minimum of those distances.

The exact solution expresses that definition as one generator passed to `min`:

`min(abs(i - start) for i, x in enumerate(nums) if x == target)`.

Although compact, it has a clear data flow. `enumerate(nums)` yields each index `i` together with its value `x`. The filter `if x == target` discards nonmatching values. For each retained pair, `abs(i - start)` produces one candidate distance. Finally, `min` returns the smallest candidate.

**Why absolute difference is the correct distance.** Array indices lie on a one-dimensional number line. Moving from `start` to `i` takes `i - start` steps if `i` is to the right and `start - i` if it is to the left. `abs(i - start)` combines both cases into the non-negative number of index steps.

An occurrence at `start` has distance zero, which is the smallest possible answer. The generator still continues through the array because Python’s `min` consumes it fully, but no later candidate can improve below zero.

**The guarantee makes `min` safe.** Calling `min` on an empty generator would raise a `ValueError`. The contract explicitly guarantees that `target` exists in `nums`, so at least one pair passes the filter and at least one distance is generated. No sentinel or failure branch is needed.

**Trace a single occurrence.** For `nums = [1, 2, 3, 4, 5]`, `target = 5`, and `start = 3`, only index four passes the filter. Its distance is `abs(4 - 3) = 1`, so the minimum is one.

**Trace several occurrences on both sides.** Suppose `nums = [7, 2, 7, 4, 7]` and `start = 3`. Target seven occurs at indices zero, two, and four, producing distances three, one, and one. `min` returns one. The problem asks only for the distance, so a tie between indices two and four requires no tie-breaking.

**Why scanning all indices is sufficient.** Every possible answer must come from an index holding `target`. The generator includes every such index exactly once and includes no other index. Its candidates are therefore exactly the complete feasible set, and taking their minimum is the mathematical definition of the requested result.

**Why no sorting or search structure helps for one query.** The array is not promised to be sorted, and this method is called for only one target-start pair. Building a map from values to positions would also require a full scan and extra memory. Direct enumeration obtains the result with the least state.

**Generator behavior matters for space.** Parentheses create a lazy generator expression rather than a list of all distances. A candidate is produced only when `min` asks for it, used in the running comparison, and then discarded. This is why the method can inspect many target occurrences without storing them.

**Alternative outward scan intuition.** One could test distance zero, then one position left and right, then distance two, and stop at the first target. That may terminate early and is also linear in the worst case. The exact implementation instead follows array order and keeps the minimum implicitly inside `min`. Both are correct; the generator version is especially direct because it mirrors the specification.

## Complexity detail

Let `n = nums.length`. `enumerate` visits all `n` elements, and each equality test and distance calculation is constant time. Python’s `min` consumes the entire filtered generator, so the running time is `O(n)` even when `nums[start]` already equals the target.

The generator, current tuple, and running minimum use constant storage. No list of indices or distances is created, so auxiliary space is `O(1)`.

## Alternatives and edge cases

- **Expand outward from `start`:** Check equal-distance positions on both sides and stop at the first target. It can return early but needs boundary handling.
- **Explicit running minimum:** Initialize a sentinel and update it inside a loop. This is longer but may be more familiar to beginners.
- **Map values to sorted positions:** Useful for many repeated queries on the same array, but unnecessary extra `O(n)` storage for one query.
- **Target at `start`:** Zero is generated and returned, the minimum possible distance.
- **Target only to the left:** Absolute value converts the negative index difference to the correct positive distance.
- **Target only to the right:** The ordinary positive difference is returned.
- **Several equally close occurrences:** They generate the same minimum; only distance is requested, so no index tie rule is needed.
- **Every element equals target:** The occurrence at `start` produces zero.
- **Single-element array:** The guaranteed target is at index zero and the result is zero.
- **Guaranteed existence:** Without it, `min` on the empty generator would fail and a default or explicit branch would be required.
- **Lazy evaluation:** The generator avoids allocating a length-`n` candidate list.
- **No early exit in exact code:** Even after seeing distance zero, `min` finishes consuming the generator, preserving `O(n)` runtime.

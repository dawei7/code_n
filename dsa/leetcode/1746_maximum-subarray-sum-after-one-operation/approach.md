## General

**Add one state to Kadane's algorithm**

Ordinary Kadane's algorithm keeps the best sum of a non-empty subarray ending at the current index. This problem needs to remember one additional fact: whether the required squaring operation has already been used inside that ending subarray.

The exact solution maintains two rolling values after processing each element:

- `f` is the maximum sum of a non-empty subarray ending at the current element with no element squared.
- `g` is the maximum sum of a non-empty subarray ending at the current element with exactly one squared element.

Only ending-at-the-current-index states are needed because any contiguous subarray either starts at the current element or extends a subarray that ended immediately before it. The global answer `ans` remembers the best completed candidate across all ending positions.

**Update the state with no operation**

Before processing current value `x`, the old `f` describes the best unchanged subarray ending at the previous position. There are two sensible choices:

- Extend it if its sum is positive.
- Discard it and start a new subarray at `x` if its sum is zero or negative.

The source combines these choices as:

`ff = max(f, 0) + x`.

Using zero does not create an empty final subarray. It means “take no prefix and begin with the current element,” so `x` is always included. This is the usual space-optimized Kadane recurrence.

The new value is stored temporarily in `ff` because the update of `g` must still read the previous iteration's `f`. Assigning to `f` too early would mix states from different ending positions.

**Update the state with exactly one operation**

A subarray ending at `x` with one square has exactly two possible histories.

First, the operation can be used on the current element. Any prefix immediately before it must then contain no squared element, so its best helpful sum is `max(f, 0)`. This produces:

`max(f, 0) + x * x`.

The zero option again permits the operated subarray to start at the current position. This is necessary when every preceding unchanged suffix has a negative sum.

Second, the operation may already have been used in the best previous `g` subarray. The current value must then remain unchanged, giving:

`g + x`.

Taking the maximum of those exhaustive cases yields:

`gg = max(max(f, 0) + x * x, g + x)`.

No third case is needed. Squaring neither the current element nor any previous element would belong to `f`, while squaring both would violate the exactly-one rule.

**Why zero initialization still represents a required operation**

Before the first element, the source sets `f = g = 0`. For `f` this is a standard empty-prefix sentinel. For `g`, zero initially does not literally describe a non-empty subarray that has used an operation, so it deserves careful examination.

At the first value, the two `g` candidates are `x * x` and `x`. For every integer $x$, $x^2 \ge x$. Therefore the squared-current candidate is never worse. If equality occurs for zero or one, performing the square changes no numeric value but still legally uses the operation. The resulting `g` value can always be interpreted as an exactly-one-operation subarray.

After that first step, extending old `g` is valid because it already has such an interpretation. By induction, initialization never causes an illegal operation-free value to dominate `g`.

**Track a result that may end anywhere**

After calculating `ff` and `gg` from the old states, the parallel assignment `f, g = ff, gg` advances both states to the current position. Then:

`ans = max(ans, f, g)`

records the best sum seen so far. `ans` starts at negative infinity rather than zero, which guarantees that the returned subarray is non-empty even if all ordinary values are negative.

The inclusion of `f` in the maximum is harmless but mathematically redundant for integer inputs. At each current position, `x * x >= x`, so the “square current” candidate for `g` is at least `ff`. Thus `g >= f`. The exact source nevertheless compares both states explicitly, making its data flow clear and preserving the ordinary Kadane candidate.

**Trace the first example**

For `[2,-1,-4,-3]`, the unchanged state begins with two. The operated state can square two and becomes four.

At minus one, `f` becomes one by extending two. `g` chooses between extending four to three and extending the positive unchanged prefix with the square of minus one, also three.

At minus four, `f` becomes minus three, while `g` can take the previous positive `f = 1` and add sixteen, reaching seventeen. This represents subarray `[2,-1,-4]` with minus four replaced by sixteen. The final minus three does not improve that candidate, so `ans` remains seventeen.

**Why the recurrence and answer are correct**

Assume the old states have their stated meanings. Every unchanged subarray ending at the current index either starts at `x` or extends the best positive unchanged suffix, exactly matching `ff`.

Every valid operated subarray ending there either squares `x` and has an operation-free prefix, or keeps `x` and extends a prefix where the operation was already used. These disjoint cases are exactly the two candidates for `gg`. Therefore the new states retain their meanings.

Every non-empty subarray ends at some index. At that index, its best exactly-one-operation sum is represented by `g`, and `ans` examines every such ending position. The final value is consequently the maximum possible sum after the required operation.

## Complexity detail

Let $n$ be the number of array elements. The solution performs one left-to-right pass and a constant number of arithmetic operations and comparisons per element, so its time complexity is $O(n)$.

It stores only `f`, `g`, `ff`, `gg`, `ans`, and the current `x`. Their count does not grow with the input, giving $O(1)$ auxiliary space as stated in the manifest. The input is read without modification, and no DP array is allocated.

Python integers expand automatically for squares up to $10^8$ and accumulated sums. In a fixed-width implementation, the maximum possible total requires a sufficiently wide integer type.

## Alternatives and edge cases

- **Square each index and rerun Kadane:** Trying $n$ modified arrays at $O(n)$ each costs $O(n^2)$ time.
- **Prefix and suffix Kadane arrays:** Combine the square at each index with positive left and right contributions in $O(n)$ time, but use $O(n)$ space.
- **Two-column DP table:** Store the same `f` and `g` states for every index. It is educational but unnecessary because only the preceding row is used.
- **Top-down memoization:** It can express whether squaring remains available, but adds recursion depth and memo storage.
- **Single element:** `g` becomes its square, satisfying both non-empty and exactly-one requirements.
- **Negative element:** Squaring makes it nonnegative, and the operated state can start there by choosing the zero prefix.
- **Zero or one:** Squaring leaves the numeric value unchanged but still counts as performing the operation.
- **All negative values:** Negative unchanged prefixes are discarded; the best squared element can stand alone.
- **Positive prefix before the square:** `max(f, 0)` keeps it when it increases the operated sum.
- **Negative prefix before the square:** The zero option starts fresh and prevents that prefix from lowering the result.
- **Values after the square:** The `g + x` transition extends the already-operated subarray contiguously.
- **Temporary variables:** `gg` must use the old `f` and `g`, so simultaneous state advancement is essential.
- **Negative-infinity answer:** It prevents an empty subarray with sum zero from being returned.
- **Input preservation:** Squaring is modeled in DP arithmetic; `nums` itself is never changed.

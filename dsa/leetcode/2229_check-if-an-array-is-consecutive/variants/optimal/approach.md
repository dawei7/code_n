## General

**A consecutive array must satisfy two independent facts**

Let `n = len(nums)`, `mi = min(nums)`, and `mx = max(nums)`. If the array contains every integer from `mi` through `mi + n - 1` exactly once, then:

- it has `n` distinct values; and
- its numeric span contains exactly `n` integers, so `mx - mi + 1 = n`.

Both facts matter. A correct span without distinctness can hide a missing number behind a duplicate. Distinctness without the correct span can leave a gap between values.

The exact solution obtains the bounds with

`mi, mx = min(nums), max(nums)`

and checks both requirements in one chained comparison:

`len(set(nums)) == mx - mi + 1 == len(nums)`.

**Understand Python's chained equality**

Python interprets `a == b == c` as “`a == b` and `b == c`,” not as comparing a Boolean result with `c`. Here the three quantities are:

- the number of distinct values;
- the number of integer positions in the inclusive minimum-to-maximum interval;
- the number of array entries.

Returning true means all three are equal.

Since a set removes duplicates, `len(set(nums)) == len(nums)` proves every input element is unique. The equality `mx - mi + 1 == len(nums)` proves that the inclusive span has exactly as many integer positions as the array has elements.

**Why these conditions are sufficient**

Every array value lies between `mi` and `mx` by definition. The interval contains exactly `n` possible integers when `mx - mi + 1 = n`. The array also supplies exactly `n` distinct values.

It is impossible to choose `n` distinct integers from an `n`-integer interval while omitting one of the interval's values: omitting one would leave only `n - 1` possible selected values. Therefore, the set of array values must be the entire interval `[mi, mx]`, which equals `[mi, mi + n - 1]`. The array is consecutive.

Order is irrelevant. The definition says the array contains the range; it does not require the elements to appear in increasing order. The set and extrema deliberately ignore arrangement.

**Why these conditions are necessary**

If `nums` is consecutive, it contains each value in a range of `n` consecutive integers. Those values are all distinct, so its set size is `n`. Its minimum is the range start and maximum is the range end, whose inclusive width is `n`. Both equalities must hold.

Thus, a true result is exactly equivalent to the definition, not merely a shortcut that works for typical examples.

**Examples of why one check alone fails**

For `[1, 1, 3]`, the minimum-to-maximum span has three integer positions, matching the array length, but the set has only two values. The missing `2` is hidden by the duplicate `1`. The chained comparison returns false.

For `[1, 2, 4]`, all three values are distinct, but the span contains four integers. The missing `3` makes `mx - mi + 1` larger than `n`, so the result is false.

For `[3, 5, 4]`, the set size, span size, and list length are all three. The order differs from sorted order, but the values are exactly `3, 4, 5`, so the method correctly returns true.

**Nonempty input makes extrema safe**

The constraints guarantee at least one element, so `min` and `max` are always defined. A one-element array has equal minimum and maximum, distinct count one, span size one, and length one. It is consecutive because it contains the only value in its one-element required range.

The method does not mutate or sort `nums`. It creates only the set needed for distinctness and reads the extrema independently.

## Complexity detail

Let `n = len(nums)`. `min(nums)` and `max(nums)` each scan the array in `O(n)` time. Constructing `set(nums)` performs `n` expected constant-time hash insertions, also `O(n)` expected time. Sequential linear passes remain `O(n)`.

The set can hold all `n` values when they are distinct, so auxiliary space is `O(n)`. The extrema and lengths use constant additional storage.

Hash-set construction has expected linear time under normal hashing. The input integer range and Python's integer behavior make this the standard analysis.

## Alternatives and edge cases

- **Sort and compare neighbors:** Sort the values and require each next value to equal the previous plus one. This is correct but costs `O(n \log n)` time and may mutate the input unless a copy is made.
- **Boolean presence array:** The bounded value range permits marking seen values by index. It can run in linear time but allocates according to the value universe rather than the actual input size.
- **Check only `mx - mi + 1 == n`:** Duplicates can replace missing interior values while preserving the span, so distinctness is essential.
- **Check only set size `n`:** Unique values can still contain gaps and have a span wider than `n`.
- **One element:** It is consecutive by definition, and all three compared quantities equal one.
- **Unsorted consecutive values:** Ordering does not matter; set membership and extrema still recognize the complete range.
- **Duplicate at an endpoint:** The set count falls below list length and the method returns false.
- **Missing interior value:** Either a duplicate reduces distinctness or another value widens the span; the chained test catches both.
- **Zero as the minimum:** No offset or special handling is required.
- **Large gaps:** They increase `mx - mi + 1` beyond `n` and fail immediately in the final Boolean expression.
- **Input preservation:** Unlike in-place sorting, this method leaves `nums` unchanged.
- **Chained-comparison semantics:** Rewriting it in a language without Python-style chaining requires two explicit conjunctions; evaluating equality left to right as ordinary binary operations could be wrong.

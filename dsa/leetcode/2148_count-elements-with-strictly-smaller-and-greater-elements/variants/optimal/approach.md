## General

For one occurrence `x` to count, the array must contain some value strictly smaller than `x` and some value strictly greater than `x`. It may seem necessary to search for two witnesses separately for every occurrence, but the global minimum and maximum already provide the strongest possible witnesses.

**Use the global minimum as the smaller witness**

Let `mi = min(nums)`. If `x > mi`, then an occurrence of `mi` appears somewhere in the array and is strictly smaller than `x`. This proves the first requirement.

If `x == mi`, no array value can be strictly smaller by the definition of a minimum. Therefore no occurrence equal to `mi` can count.

There is no possibility that `x < mi` because `x` itself is an array element.

Thus “a strictly smaller element exists” is exactly equivalent to `mi < x`.

**Use the global maximum as the greater witness**

Let `mx = max(nums)`. If `x < mx`, an occurrence of `mx` supplies a strictly greater element. If `x == mx`, no greater value exists. Therefore the second requirement is exactly `x < mx`.

Combining the two independent requirements gives one complete condition:

`mi < x < mx`.

An element counts if and only if its value lies strictly inside the open interval between the array’s global minimum and maximum.

**Count occurrences, not distinct values**

The generator `(mi < x < mx for x in nums)` visits every array occurrence. Python’s chained comparison checks both inequalities for that occurrence and returns a boolean.

The outer `sum(...)` uses the fact that `True` behaves like integer one and `False` like zero. Every qualifying occurrence adds one.

This correctly handles duplicates. In `[-3,3,3,90]`, both occurrences of three satisfy `-3 < 3 < 90`, so both count. The task asks for the number of elements, meaning positions or occurrences, not the number of distinct qualifying values.

**Why equal extrema do not count**

Strictness is essential. A minimum occurrence cannot use another equal minimum as a strictly smaller witness. Likewise, repeated maximum values are not strictly greater than one another. The open inequalities deliberately exclude every occurrence of either extreme, no matter how many copies exist.

For `[11,7,2,15]`, `mi = 2` and `mx = 15`. Values 11 and 7 lie strictly between them, while 2 lacks a smaller witness and 15 lacks a greater witness. The result is two.


If the code counts `x`, then `mi < x` and `x < mx`. Since both extrema occur in `nums`, `mi` and `mx` are explicit smaller and greater witnesses, so `x` satisfies the problem.

If an occurrence satisfies the problem, some array value is strictly smaller, so `x` cannot equal the global minimum and must have `mi < x`. Similarly, the existence of a greater value forces `x < mx`. The generator therefore counts it. The condition is necessary and sufficient.

**Why sorting is unnecessary**

Sorting would place the extrema at the ends, but the task does not ask for output order. The built-in minimum and maximum scans discover exactly the two boundary values needed while preserving linear time and leaving the input unchanged.

## Complexity detail

Let $n$ be the array length. `min(nums)` scans all $n$ elements, and `max(nums)` performs another $n$-element scan. The generator used by `sum` performs one final scan. Three linear passes are still $O(n)$ time.

The generator is lazy, so it produces one boolean at a time rather than allocating an $n$-element boolean list. The method stores only `mi`, `mx`, `x`, and summation state. Auxiliary space is $O(1)$.

The input array is read only. Built-in extrema and the generator do not reorder or modify it.

## Alternatives and edge cases

- **Sort the array:** After sorting, count elements strictly between the first and last values. This costs $O(n\log n)$ time and may mutate the input, offering no benefit over extrema.
- **Compare every pair:** For each element, search the array for smaller and greater witnesses. This can cost $O(n^2)$ even though the global extrema answer every witness query.
- **Frequency map:** Counts of the minimum and maximum can be subtracted from $n$. This is correct but uses $O(n)$ space unless a second extrema-based pass is still used.
- **Formula using counts:** After finding `mi` and `mx`, one may return `n - count(mi) - count(mx)` when `mi != mx`. The exact generator is clearer and naturally handles all cases.
- **One element:** Minimum and maximum are equal, so the strict chained comparison is false and the result is zero.
- **All values equal:** No value has either strict witness; every comparison fails.
- **Exactly two distinct values:** Every element equals one of the extrema, so the answer is zero.
- **Repeated interior value:** Every occurrence counts separately, as in the two threes from Example 2.
- **Repeated minimum:** None of those occurrences count because equality is not strict.
- **Repeated maximum:** None count for the symmetric reason.
- **Negative values:** Ordering works identically; no sign-specific handling is needed.
- **Minimum and maximum each occur once:** They serve as witnesses for every interior occurrence but do not count themselves.
- **Boolean summation:** In Python, `sum` counts true generator results without an explicit integer conversion.
- **Input preservation:** Unlike sorting, the three scans leave `nums` in its original order.

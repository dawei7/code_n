## General

**Identify the two forbidden values**

The answer may be any array value except the global minimum and global maximum. Because all values are distinct, there is exactly one occurrence of each forbidden extreme.

The exact implementation first computes:

`mi, mx = min(nums), max(nums)`.

Once those two values are known, every other element automatically satisfies the requirement. There is no need to determine which interior element is second-smallest, a median, or in any particular rank.

**Scan until the first allowed value**

The generator expression:

`(x for x in nums if x != mi and x != mx)`

visits values in original array order and yields only values different from both extremes. `next(..., -1)` returns the first yielded value. If the generator is exhausted without yielding, `next` returns its default `-1`.

The contract accepts any valid interior value, so stopping at the first one is optimal. The solution does not sort or modify `nums`.

**Why a different value from both extremes is sufficient**

Every element of a finite set lies between its minimum and maximum. With distinct values, an element that equals neither extreme must satisfy:

$$
\texttt{mi}<x<\texttt{mx}.
$$

It is therefore neither the minimum nor maximum. Conversely, any valid requested value must be unequal to both `mi` and `mx`, so the filter captures exactly the allowed elements.

Positivity is not needed for this reasoning, but it makes `-1` a safe failure sentinel because `-1` cannot be a legal array value.

**When no answer exists**

If the array has one value, that value is simultaneously the minimum and maximum. The generator rejects it and returns `-1`.

If the array has two distinct values, one is the minimum and the other is the maximum. Again, no generator item survives.

If the array has at least three distinct values, at most two are forbidden, leaving at least one valid element. The generator must find one.

Thus the existence condition is exactly $n\ge3$ under the distinctness guarantee, even though the code does not need an explicit length check.

**Trace the examples**

For `[3,2,1,4]`, `mi=1` and `mx=4`. The generator examines three first. Three is neither extreme, so the exact implementation returns three. The example displays two, but the contract allows either two or three.

For `[1,2]`, both values are filtered out and the default `-1` is returned.

For `[2,1,3]`, the first value two survives the filter, so it is returned. It is the unique interior value.

**Why no sorting is necessary**

Sorting would put a valid value at any interior position, but it costs $O(n\log n)$ time and changes the array unless copied. The task does not require the smallest or largest valid interior value; it permits any. Two extreme scans plus an early-exit filter are enough.

**The exact implementation differs from the manifest summary**

The manifest summary describes returning the median of any three distinct values, which is another clever approach. The protected source does not do that. It computes the global minimum and maximum over the complete array and then scans for a value unequal to them.

Consequently, the implementation is not constant time: `min` and `max` each inspect the array, and the generator may inspect it again. Its correctness is based on knowing the actual global extremes, not on the three-element lemma.

**Why repeated scans remain efficient**

There are at most three passes: one for `min`, one for `max`, and a partial or full pass for `next`. A fixed number of linear passes is still linear. The code favors clarity and direct agreement with the definition.

The generator is lazy. It does not allocate a list of all interior values; it evaluates predicates only until the first success.


`min(nums)` and `max(nums)` return the two globally forbidden values. If the generator yields `x`, its predicate proves `x` equals neither, so it is a valid answer. If the generator yields nothing, every array element equals one of those two extremes. Distinctness then means the array has at most two elements and no valid answer exists, so returning `-1` is correct.

## Complexity detail

Let $n$ be `nums.length`. The `min` scan takes $O(n)$ time, the `max` scan takes $O(n)$ time, and the generator takes up to $O(n)$ time. The total is $O(n)$, not $O(1)$.

Only `mi`, `mx`, the current generator value, and generator bookkeeping are retained, so auxiliary space is $O(1)$. The generator is lazy and does not materialize another array.

The manifest's stated $O(1)$ complexity belongs to its described “median of any three values” strategy, not to this exact implementation. The approach document follows the exact source and therefore reports the actual $O(n)$ bound.

## Alternatives and edge cases

- **Median of the first three distinct values:** The median of any three distinct array values cannot be a global minimum or maximum, giving an $O(1)$ solution when $n\ge3$.
- **Sort the array:** Any interior sorted element works, but sorting costs $O(n\log n)$ and may mutate the input.
- **Track min, max, and candidate in one pass:** Can reduce the number of traversals while preserving $O(n)$ time.
- **Length one:** Its sole value is both extremes, so return `-1`.
- **Length two:** The two distinct values are exactly the minimum and maximum, so return `-1`.
- **Length at least three:** Distinctness guarantees at least one interior value.
- **First element valid:** The generator stops immediately after the two extreme scans.
- **Example permits several answers:** Returning three instead of the sample's two is still correct.
- **Positive values:** Ensure the failure sentinel `-1` cannot collide with a valid returned number.
- **Input preservation:** Neither `min`, `max`, nor the generator changes `nums`.

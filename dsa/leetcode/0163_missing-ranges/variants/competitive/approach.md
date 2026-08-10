## General

**Use virtual values outside both boundaries**

The competitive algorithm avoids separate leading and trailing checks by
introducing conceptual sentinels:

- `pre = lower - 1` acts as a present value immediately before the interval;
- on the final loop iteration, `cur = upper + 1` acts as a present value
  immediately after it.

Every real `nums[i]` is processed as `cur` between those sentinels. A missing
range exists whenever `cur - pre >= 2`, because at least one integer lies
strictly between the two present or virtual boundary values.

The missing endpoints are always `pre + 1` and `cur - 1`. This one formula
handles the beginning, middle, and end uniformly.

**Walk one extra iteration**

The loop runs over `range(len(nums) + 1)`. For indices inside `nums`, `cur` is
the current array value. At `i == len(nums)`, there is no real element, so the
source substitutes `upper + 1`.

After checking the gap, `pre = cur` advances the previous-present boundary.
Since the input is sorted and unique, each later real `cur` is greater than
`pre`. The final virtual value is also greater than or equal to the last real
value plus one.

For an empty array, the loop still executes once. `pre` is `lower - 1` and
`cur` is `upper + 1`, so their difference is at least two and the whole
interval is emitted as one range.

**Understand the gap threshold**

If `cur - pre == 1`, the values are consecutive and there is no integer
between them. If the difference is at least two, the sequence

$$
\texttt{pre}+1,\ldots,\texttt{cur}-1
$$

contains every missing number in that location.

Using `>= 2` rather than `> 0` avoids generating invalid ranges at present
boundary values. For example, if the first real number equals `lower`, then
`cur - pre` equals one and no leading gap is appended.

Because the loop follows sorted real values, emitted gaps are disjoint and
already sorted.

**Trace all sentinel roles**

For `[0,1,3,50,75]` inside `[0,99]`, initial `pre` is `-1`.

- Current zero is consecutive with the lower sentinel, so no range appears.
- Current one is consecutive with zero.
- Current three is two away from one, so the missing endpoints are two and
  two.
- Current 50 produces endpoints four and 49.
- Current 75 produces endpoints 51 and 74.
- The final virtual current value 100 produces endpoints 76 and 99.

This is the same maximal-gap decomposition as explicit boundary handling, but
with fewer control-flow cases.

**Why sentinels are safe in this Python source**

`lower` can be $-10^9$ and `upper` can be $10^9$, so subtracting or adding one
remains within common 32-bit signed range here. More generally, Python integers
are arbitrary precision, so sentinel arithmetic cannot overflow. A translation
with bounds at a fixed-width type's extrema would need explicit boundary checks
or a wider type.

The virtual values are never returned themselves. The formula immediately
moves one position inward, ensuring every output endpoint lies inside
`[lower, upper]`.

**Material return-format mismatch**

The helper `getRange` returns text. A singleton becomes `"2"`, while a longer
gap becomes a string such as `"4->49"`. Consequently the selected source
returns `List[str]`, exactly as its docstring says.

The current local Reference requires `List[List[int]]`, for example
`[[2,2],[4,49]]`. Therefore this implementation's gap logic is correct, but
its result shape does not satisfy the current package contract. To conform, the
append should use `[pre + 1, cur - 1]` directly instead of `getRange`.

This is not a cosmetic representation difference. A judge comparing numeric
nested lists will reject strings even when they describe the same mathematical
ranges.

**Why the mathematical ranges are minimal**

Between two consecutive real or virtual present values, every interior integer
is missing and no exterior integer can join without crossing a listed value or
the interval boundary. Thus each detected gap is maximal.

Every missing number belongs between exactly one consecutive pair in this
augmented sequence. The scan covers it once, and one output per maximal run is
the smallest possible count. This proves the underlying algorithm independent
of the source's outdated serialization.

## Complexity detail

Let $n$ be the number of real array values. The loop has $n+1$ iterations and
constant work per iteration, so time is $O(n)$.

Excluding the returned ranges, only `pre`, `cur`, the index, and helper-local
values are stored, giving $O(1)$ auxiliary space. The required result can hold
$O(n)$ ranges. Formatting each range creates output strings; their total
character storage is part of the returned result. The manifest's bounds
describe auxiliary space and match the scanning method.

## Alternatives and edge cases

- **Explicit boundary checks:** Handle the prefix, every adjacent real pair, and the suffix separately; this directly produces numeric range pairs.
- **Numeric sentinel output:** Keep the uniform loop but append `[pre + 1, cur - 1]` to satisfy the current contract.
- **Enumerate the domain:** Can be infeasible when the numeric interval is huge but `nums` is short.
- **Empty array:** The two sentinels produce one full missing range.
- **Fully covered interval:** Every consecutive difference is one, so no mathematical gap is emitted.
- **Single missing number:** The helper serializes it as one number rather than an arrow string, but the current contract still expects `[x, x]`.
- **Negative values:** Sentinel and difference arithmetic behave normally.
- **Fixed-width translation:** Avoid overflow when bounds can equal the numeric type's extrema.
- **Sorted unique input:** It is required for consecutive-pair gaps to be disjoint and ordered.
- **Return schema:** The exact selected source is incompatible with `List[List[int]]` until its string formatter is replaced.

## General
**Build two consecutive copies**

The result has two consecutive regions, each with exactly $N$ positions. Copy
`nums` into the first region, then copy the same sequence into the second
region. Array concatenation expresses precisely this construction: it
preserves every element and its relative order in each copy.

**Why every result position is correct**

For any valid source index $i$, the first copy places `nums[i]` at index $i$
and the second places it at index `i + N`. These are exactly the two required
positions, and together the two index ranges cover all $2N$ positions without
overlap or omission. The constructed array therefore satisfies the contract.

## Complexity detail
Here $N$ is the length of `nums`. Producing the returned array requires writing
$2N$ values, so the running time is $O(N)$. The returned list itself stores
$2N$ integers and therefore uses $O(N)$ space. Apart from that required output,
the direct construction needs only constant auxiliary state.

## Alternatives and edge cases
- **Two explicit copy loops:** Preallocate $2N$ positions and assign each
  source value to indices `i` and `i + N`. This has the same asymptotic costs
  and can avoid incremental resizing, but is more verbose than direct
  concatenation.
- **Repeated growing-list concatenation:** Rebuilding a larger list for every
  individual element remains correct, but repeatedly copies the existing
  prefix and can take $O(N^2)$ time.
- A one-element input still produces two elements; neither copy may be omitted.
- Duplicate values remain duplicate values. Their positions, rather than
  uniqueness, determine the result.
- The second copy starts only after all $N$ elements of the first copy, so
  interleaving each value with itself would not satisfy the required order.

## General

**Do not construct the quadratic list of pair results.** A direct solution would calculate `arr1[i] & arr2[j]` for every pair and XOR all those values. With both arrays as long as 100,000, that could mean ten billion pairs. The exact solution instead uses a distributive identity:

`XOR over all i and j of (arr1[i] AND arr2[j])`

equals

`(XOR of all arr1 values) AND (XOR of all arr2 values)`.

The code computes the two array XORs as `a` and `b` with `reduce(xor, ...)`, then returns `a & b`.

**Understand the identity one bit at a time.** Bitwise XOR and AND operate independently at every bit position, so it is enough to prove what happens to one fixed bit. A pairwise AND has a one in that bit exactly when both chosen array values have a one there.

Let `c1` be the number of values in `arr1` with that bit set, and let `c2` be the corresponding count in `arr2`. There are `c1 * c2` pairs whose AND has that bit set. XORing all pair results leaves the bit as one exactly when this number of one bits is odd.

A product `c1 * c2` is odd exactly when both `c1` and `c2` are odd. Meanwhile, the bit in the XOR of `arr1` is one exactly when `c1` is odd, because equal one bits cancel in pairs. The bit in the XOR of `arr2` is one exactly when `c2` is odd. ANDing those two aggregate bits produces one exactly when both counts are odd—the same condition as the full pairwise XOR.

Since this equivalence holds independently for every bit, the complete integers are equal.

**What `reduce(xor, arr1)` does.** Reduction combines the array from left to right using XOR, producing

`arr1[0] ^ arr1[1] ^ ...`.

The same happens for `arr2`. The constraints guarantee both arrays contain at least one element, so calling `reduce` without an explicit initializer is safe. On an empty array it would raise an error, but empty arrays are outside the contract.

The names `a` and `b` are aggregate XOR values, not sums and not individual elements. Once these two values have been computed, the original arrays no longer need to be compared pair by pair.

**A bit-level trace of the first sample.** For `arr1 = [1, 2, 3]`, the aggregate is `1 XOR 2 XOR 3 = 0` because `1 XOR 2` equals three and three XOR three cancels to zero. For `arr2 = [6, 5]`, the aggregate is `6 XOR 5 = 3`. Their AND is `0 AND 3 = 0`, matching the XOR of all six pairwise AND values.

For `arr1 = [12]` and `arr2 = [4]`, the aggregates are simply 12 and four. Their AND is four, identical to the only pair result.

**Why ordinary arithmetic distribution is not being assumed.** This optimization is not a vague analogy to multiplication over addition. It follows from a precise Boolean-algebra property: AND distributes over XOR. For a fixed value `x`,

`(x & y1) ^ (x & y2) = x & (y1 ^ y2)`.

Applying that repeatedly collapses the inner XOR over `arr2`. Applying it again across `arr1` produces the two aggregate XORs. The parity proof above gives the same result without relying on memorizing the algebraic identity.

**Duplicates and cancellation.** If a value occurs twice in one array, its contribution to that array’s aggregate XOR cancels. In the original pair list, each of its AND results also occurs twice for every value in the other array and cancels there. The compressed formula therefore handles duplicates exactly rather than losing information.

Zeros behave naturally as well. A zero contributes nothing to an aggregate XOR, and every pairwise AND involving zero is zero. No special branch is necessary.

**A direct correctness proof.** Consider any bit position `k`. The returned value’s bit `k` is one if and only if the count of set bits at `k` in each array is odd. The requested pairwise XOR’s bit `k` is one if and only if an odd number of pairs have both input bits set, which occurs if and only if the product of those two counts is odd. Those conditions are identical. Therefore every bit of the returned value equals the corresponding bit of the requested XOR sum, proving the result correct.

The solution’s elegance comes from changing the unit of reasoning. Instead of asking what every pair produces as a whole integer, it asks only whether each bit appears an odd or even number of times. XOR cares exclusively about parity, allowing billions of conceptual pairs to collapse into two linear reductions.

## Complexity detail

Let `p = arr1.length` and `q = arr2.length`. Reducing `arr1` takes `O(p)` time, reducing `arr2` takes `O(q)` time, and the final AND is constant time under the bounded integer sizes in the problem. Total running time is `O(p + q)`.

The implementation stores only the two aggregate integers `a` and `b`. `reduce` does not create a list of intermediate values, so auxiliary space is `O(1)`. The inputs are not modified, and the quadratic pairwise list is never materialized.

Python integers safely hold all values. Since inputs are at most one billion, their relevant bit width is small and the bitwise operations are constant for this problem’s bounds.

## Alternatives and edge cases

- **Enumerate every pair:** This directly follows the definition but costs `O(pq)` time and is infeasible at maximum lengths.
- **Materialize pair results:** Storing all AND values adds `O(pq)` space on top of the already excessive time; XOR can be accumulated without storage even in the brute-force version.
- **Count set bits explicitly:** For each bit position, count ones in both arrays and set the answer bit when both counts are odd. This is correct but adds a factor for the bit width and is more verbose than two XOR reductions.
- **Repeated values:** Even multiplicities cancel in both the aggregate formula and the conceptual pair list.
- **All zeros in one array:** Its aggregate XOR is zero, so the final AND and every pairwise AND XOR sum are zero.
- **Single element in each array:** Each reduction returns that element, and the formula becomes the one pair’s AND.
- **One single-element array:** The identity reduces to distributing that one value’s AND across the XOR of the other array.
- **Aggregate XOR zero:** The final result is zero even if many individual pairwise AND values are nonzero; those contributions cancel by parity.
- **Non-negative values:** The contract avoids complications from language-specific signed bit representations. The identity itself is bitwise and still holds with consistent fixed-width representations.
- **Nonempty-array dependency:** `reduce` has no initializer in the exact code, so the guaranteed minimum length of one is necessary.
- **No input mutation:** Both reductions only read their arrays, and the method returns one computed integer.
- **Operator distinction:** The final operation must be AND, not XOR or addition; it represents the requirement that a result bit needs odd parity in both arrays.

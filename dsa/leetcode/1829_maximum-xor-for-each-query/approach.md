## General

**Reduce each query to the XOR of the current array.** XOR is associative and commutative, so the value

`nums[0] XOR nums[1] XOR ... XOR nums[last] XOR k`

can be viewed as `xs XOR k`, where `xs` is the XOR of every value still present. The solution first computes the XOR of the complete input with `reduce(xor, nums)`. It then maintains that aggregate as last elements are removed, rather than recomputing a prefix XOR from scratch for every query.

The array being sorted is not needed for this reasoning. XOR does not depend on element order, and the removals are explicitly from the last position. The algorithm would produce the same query answers for any array with the same ordered removal sequence.

**The maximum possible result has every allowed bit set.** The constraint `0 <= k < 2^maximumBit` means `k` may use bit positions zero through `maximumBit - 1` and no higher position. Every number in `nums` also lies below that same power of two. XORing such values cannot create a higher bit, so `xs` is confined to those positions as well.

For a fixed bit position, XOR produces one when its two input bits differ. To maximize the complete integer, the best possible outcome is therefore one in every allowed position. Its value is `2^maximumBit - 1`. Each bit of `k` can be chosen independently:

- If the corresponding bit of `xs` is zero, set that bit of `k` to one.
- If the corresponding bit of `xs` is one, leave that bit of `k` at zero.

This makes `k` the bitwise complement of `xs` within exactly the permitted width. Then `xs XOR k` is all ones, which is the largest number representable with `maximumBit` bits. No other legal `k` can produce a larger result.

**How the exact code builds `k`.** For each query, `k` starts at zero. The inner loop examines positions from `maximumBit - 1` down to zero. The expression

`xs >> i & 1`

shifts bit `i` into the least-significant position and masks away everything else, yielding that bit as zero or one. When it is zero, `k |= 1 << i` sets bit `i` in `k`. When it is one, the code makes no change, so the bit remains zero.

Scanning from high to low is intuitive because high bits contribute more to an integer, but independence means low-to-high order would produce the same `k`. The important part is visiting every allowed bit exactly once and never setting a position at or above `maximumBit`. Thus the constructed value automatically satisfies the bound on `k`.

**Answer queries in the required removal order.** The loop uses `nums[::-1]`, the values from last to first. Before removing its current `x`, it constructs and appends the best `k` for the existing `xs`. This ordering matters: the first query uses all values, so removal must occur only after its answer has been recorded.

After appending, the statement `xs ^= x` removes the current last value from the aggregate. XORing a value with itself gives zero, and XORing with zero changes nothing. If

`xs = remaining_prefix_XOR XOR x`,

then XORing `x` again cancels the two copies and leaves `remaining_prefix_XOR`. The next iteration therefore begins with exactly the XOR of the shortened array.

**A trace for the first sample.** For `nums = [0, 1, 1, 3]` and `maximumBit = 2`, the complete XOR is three. In two bits, three is `11`, so the complement is `00` and the first answer is zero. The loop then cancels the last value three, leaving zero as the XOR of `[0, 1, 1]`. The complement of `00` is `11`, so the next answer is three. Canceling the next value one leaves one, whose two-bit complement is two. Canceling the next one leaves zero, whose complement is three. The answers are consequently `[0, 3, 2, 3]`.

**Why the bitwise greedy choice is globally optimal.** Binary integers are ordered by their highest differing bit. At every allowed position, the algorithm attains outcome bit one, the best possible value for that position. In fact, it attains one at all positions simultaneously because selecting one bit of `k` has no effect on any other XOR bit. The resulting value is the absolute upper bound `2^maximumBit - 1`, so no tradeoff between bit positions or alternative candidate search is necessary.

**Why the maintained aggregate remains correct.** Initially, `xs` is the XOR of the full array. Assume it is the XOR of the current prefix at the beginning of an iteration. The generated `k` is optimal for precisely that aggregate, so the appended answer is correct for the current query. The loop variable `x` is the last element of that prefix because the copied traversal is reversed. Canceling it leaves the XOR of the prefix with its last element removed, which is the required state for the next query. This induction covers all `n` queries.

The exact implementation spells out the complement bit by bit. A shorter expression using a mask exists, but the explicit loop makes the allowed-width restriction visible and avoids Python’s infinite-width behavior for a direct `~xs` operation.

## Complexity detail

Let `n = nums.length` and `b = maximumBit`. Computing the initial aggregate takes `O(n)` time. For each of the `n` queries, the code examines exactly `b` bit positions, so its exact running time is `O(nb)`. Since the constraints cap `b` at 20, it is a small fixed bound and the runtime is commonly simplified to `O(n)` for this problem.

The answer list contains `n` required results. In addition, the exact expression `nums[::-1]` creates a reversed copy of all `n` references, so this Python implementation uses `O(n)` auxiliary space as well as `O(n)` output space. Iterating with `reversed(nums)` would avoid the copy and reduce non-output auxiliary storage to `O(1)` without changing the algorithm. Scalars `xs`, `k`, `x`, and `i` take constant space.

## Alternatives and edge cases

- **Mask expression:** With `mask = (1 << maximumBit) - 1`, the same answer is `xs ^ mask`. It computes the width-limited complement in constant arithmetic work per query and makes the total time `O(n)` without relying on the bound of 20.
- **Prefix XOR array:** Precomputing every prefix XOR lets queries read aggregates in reverse order, but it uses another `O(n)` array when one rolling XOR is enough.
- **Recompute XOR for every shortened array:** This direct simulation takes `O(n^2)` time because almost the same prefix is scanned repeatedly.
- **Direct bitwise NOT:** In Python, `~xs` represents an unbounded signed complement and becomes negative. It must be masked to the lowest `maximumBit` bits before it can be a legal `k`.
- **Aggregate XOR equals zero:** Every allowed bit of `k` is set, producing the maximum mask.
- **Aggregate XOR already equals the mask:** Every bit of `k` remains zero, and the XOR result is already maximal.
- **Single-element input:** The first and only query complements that element, then cancellation leaves zero after the answer has already been appended.
- **Duplicate values:** Equal values cancel in pairs in the aggregate, and individual removals are still updated correctly with `xs ^= x`.
- **Zero values:** Canceling zero leaves `xs` unchanged, which correctly reflects that removing zero does not change an XOR.
- **Sortedness:** The implementation does not use ascending order; correctness depends only on the specified last-to-first removal order.
- **Reversed-slice memory:** `nums[::-1]` is convenient but allocates a copy. `reversed(nums)` would preserve behavior with constant auxiliary traversal space.
- **Legal width:** Every set bit of `k` comes from an index below `maximumBit`, so `0 <= k < 2^maximumBit` always holds.

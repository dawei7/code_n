## General

**Begin with the smallest and largest candidates**

The competitive solution places `start` at index zero and `end` at the final
index. At every iteration it examines `nums[start] + nums[end]`.

Sorted non-decreasing order makes this pair informative. If the sum is too
small, only replacing the smaller endpoint with a larger value can help. If
the sum is too large, only replacing the larger endpoint with a smaller value
can help. This allows one entire row or column of possible pairs to be
discarded with each pointer move.

The interval invariant is that the unique solution pair, if not already
returned, has both indices between `start` and `end`.

**Discard the left endpoint when the sum is small**

Suppose:

`nums[start] + nums[end] < target`.

`nums[end]` is the largest value still available. Pairing `nums[start]` with
any index before `end` produces a value no larger than the current sum, so none
of those pairs can reach the target. Therefore `start` cannot belong to the
solution and can be incremented safely.

This is stronger than merely saying “a larger number might help.” It proves
every pair using the discarded left index is impossible.

**Discard the right endpoint when the sum is large**

If:

`nums[start] + nums[end] > target`,

`nums[start]` is the smallest value still available. Pairing `nums[end]` with
any later possible left index produces a sum no smaller than the current one.
Thus no pair using `end` can equal the smaller target, and decrementing `end`
is safe.

When the sum equals the target, the source returns the two indices after adding
one, satisfying the one-based output convention.

**Trace pointer movement**

For `[2,7,11,15]` and target nine, the first sum is seventeen, so `end` moves
left. The next sum is thirteen, moving it left again. The pair two and seven
then sums to nine, returning `[1,2]`.

For `[2,3,4]` and target six, the initial endpoints already sum to six, so
`[1,3]` is returned.

For a mixture such as `[-5,-2,1,4,8]` with target two, the first sum three is
too large, so the right endpoint moves from eight to four. The sum of negative
five and four is too small, so the left endpoint moves. The pair negative two
and four then succeeds. Negative values do not alter the elimination proofs.

**Why pointers cannot skip the solution**

Assume the unique solution lies within the current boundaries.

On a too-small sum, every pair involving `start` is too small because `end`
already supplies the largest partner. The solution therefore does not use
`start`, and incrementing it preserves the invariant.

On a too-large sum, every pair involving `end` is too large because `start`
already supplies the smallest partner. The solution does not use `end`, and
decrementing it preserves the invariant.

Each non-returning step removes one impossible endpoint. Because the contract
guarantees a solution using distinct indices, the pointers encounter it before
they meet.

**Respect distinct and one-based indices**

The loop condition is `start != end`. Initially `start < end`, and updates move
them inward one position at a time, so they remain ordered until equality.
The method never combines an element with itself.

The source returns `[start + 1, end + 1]` because the problem's public indices
begin at one even though Python list indices begin at zero.

There is no explicit return if the pointers meet without a match. Valid inputs
never take that path. With an invalid no-solution input, the method would
implicitly return `None`.

**Exact variable naming**

The local name `sum` shadows Python's built-in `sum` function. This does not
affect the algorithm because the method never needs the built-in afterward,
but a name such as `current_sum` would be clearer.

The input list is read-only; moving cursor variables does not rearrange or
modify values.

## Complexity detail

Let $n$ be the number of elements. Every unsuccessful iteration moves exactly
one pointer inward. `start` can advance at most $n-1$ times and `end` can
retreat at most $n-1$ times, with fewer than $n$ total eliminations before they
meet. Time is $O(n)$.

Only two indices and one sum are stored, so auxiliary space is $O(1)$. The
two-element returned list is fixed-size output. These bounds match the
manifest and satisfy the explicit constant-space requirement.

## Alternatives and edge cases

- **Binary search per left index:** Search the sorted suffix for each complement in $O(n\log n)$ time and $O(1)$ space.
- **Hash map:** Expected linear time but linear extra space, which the contract forbids.
- **Nested loops:** Constant extra space but quadratic time.
- **Duplicate values:** Two pointers operate on indices, so equal values at different positions are allowed.
- **Negative values:** Monotonic pair-sum reasoning remains valid.
- **Solution at endpoints:** It is returned on the first comparison.
- **Adjacent solution indices:** The loop still examines them before pointer equality.
- **Exactly one solution:** It permits immediate return and guarantees the implicit no-result path is unreachable.
- **One-based contract:** Add one to both zero-based cursor positions.
- **Built-in shadowing:** Naming the local variable `sum` is harmless here but can be avoided for clarity.

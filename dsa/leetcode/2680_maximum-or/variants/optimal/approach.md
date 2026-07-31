## General

Multiplying by 2 is a one-bit left shift, so applying all `k` operations to one value transforms it into `value << k`. An optimal allocation can be chosen with every operation on one element: if operations are split, moving the shifts from a less-shifted chosen value onto a most-shifted one does not lose any bit position that the less-shifted value contributes through its original unshifted bits, because those original values still participate in the OR comparison for the concentrated candidate. Repeating this exchange leaves one shifted candidate to test.

For candidate index `i`, the resulting value is the OR of three parts: every element before `i`, `nums[i] << k`, and every element after `i`. Recomputing the unchanged elements for every candidate would be quadratic. Instead, build `suffix[i]` as the OR of `nums[i:]`, and maintain a running prefix OR while moving left to right.

At index `i`, `prefix` is exactly the OR of indices below `i`, and `suffix[i + 1]` is exactly the OR of indices above it. Thus `prefix | (nums[i] << k) | suffix[i + 1]` is precisely the result of concentrating all operations on candidate `i`. Taking the maximum over all indices examines every possible optimal candidate and returns the global optimum.

## Complexity detail

Let $n$ be `len(nums)`. Building the suffix ORs and scanning all candidates each take $O(n)$ time. The suffix array occupies $O(n)$ space, while the prefix, candidate, and answer values use $O(1)$ additional space.

## Alternatives and edge cases

- **Prefix and suffix arrays:** Storing both sides gives the same $O(n)$ time with $O(n)$ space, but the prefix side can be accumulated in one variable.
- **Recompute the other elements:** OR-ing all indices except the candidate inside every iteration is correct but costs $O(n^2)$ time.
- **Choose the numerically largest value:** This is not sufficient because the best result depends on which bit positions a shifted candidate adds alongside the other elements' bits.
- **Single element:** There are no unchanged elements, so the answer is simply `nums[0] << k`.
- **Duplicate and overlapping bits:** OR is idempotent; repeated set bits do not add numeric weight, but shifting one copy can expose higher bits while another copy preserves the originals.

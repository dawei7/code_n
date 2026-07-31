## General

**Count how often each source value appears.** Expanding one pairing gives `nums1[i] ^ nums2[j]`. Across the full Cartesian product, every value in `nums1` appears once for each of the $m$ values in `nums2`, while every value in `nums2` appears once for each of the $n$ values in `nums1`.

XORing a value an even number of times cancels it to zero, while an odd number of copies leaves one copy. Consequently, `nums1` contributes its array-wide XOR exactly when $m$ is odd, and `nums2` contributes its array-wide XOR exactly when $n$ is odd.

Start the answer at zero. If `nums2` has odd length, XOR every value from `nums1` into it. If `nums1` has odd length, XOR every value from `nums2` into it. These are precisely the uncancelled contributions from the conceptual pair array, so the final accumulator equals the requested XOR without materializing any pair.

## Complexity detail

In the worst case both input arrays are scanned once, taking $O(n+m)$ time. The algorithm stores only the result and loop values, so it uses $O(1)$ auxiliary space. When an opposite length is even, the corresponding scan can be skipped, but the stated bound covers all parity combinations.

## Alternatives and edge cases

- **Enumerate all pairings:** Directly XORing every `nums1[i] ^ nums2[j]` is correct but takes $O(nm)$ time.
- **Build the conceptual third array:** Materializing all pair values adds $O(nm)$ space without changing the quadratic work.
- **Both lengths even:** Every source value cancels, so the answer is 0.
- **Only `nums1` has odd length:** Only the XOR of `nums2` contributes.
- **Only `nums2` has odd length:** Only the XOR of `nums1` contributes.
- **Both lengths odd:** The answer is the XOR of both complete arrays.
- **Singleton arrays:** Their one explicit pairing is returned.
- **Zero values:** XORing zero has no effect, and the parity argument remains unchanged.

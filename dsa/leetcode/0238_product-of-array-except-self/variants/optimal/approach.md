## General
**Split every answer around its index**

For index `i`, the answer is the product of values strictly to its left times the product of values strictly to its right.

**Store left products directly in the result**

Scan left to right while maintaining the product seen so far. Store that product at each index before multiplying by the current value.

**Fold in right products on the return pass**

Scan right to left with a second running product. Multiply each stored prefix by the current suffix, then extend the suffix with the current input value.

During the first pass, output index `i` equals the product of `nums[0:i]`. During the second, the suffix variable equals the product of values after `i`; their multiplication therefore excludes exactly `nums[i]`.

Every index other than `i` lies uniquely to its left or right, so the two running products include every required factor exactly once and omit the current factor. This remains valid when values are zero or negative.

## Complexity detail
Two linear scans take $O(n)$ time. Excluding the required output array, only two scalar products are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Division by the total product:** violates the contract and needs special handling for zeros.
- **Recompute each product independently:** takes $O(n^2)$ time.
- One or multiple zeros and negative signs are handled naturally by prefix/suffix multiplication.

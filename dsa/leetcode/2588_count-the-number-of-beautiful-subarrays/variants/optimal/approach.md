## General

Each operation removes one occurrence of the same set bit from two different elements. Therefore, for every bit position, the number of set occurrences across a reducible subarray must be even. This condition is also sufficient: pair the elements containing a chosen bit and subtract that bit from each pair, then repeat independently for every bit. Subtracting a set bit does not borrow from other positions.

The XOR of all elements has a bit set exactly when that bit occurs an odd number of times. A subarray is consequently beautiful if and only if its XOR is zero.

Let `prefix_xor` be the XOR of all values processed so far, with an initial empty-prefix value of zero. The XOR of a subarray between two prefix boundaries is zero precisely when the prefix XOR values at those boundaries are equal. Maintain a frequency map of earlier prefix values. At each element, every prior occurrence of the current `prefix_xor` identifies one beautiful subarray ending here, so add its frequency to the answer before recording the current boundary.

Initializing the frequency of zero to one represents the empty boundary before the array and correctly counts beautiful subarrays that start at index zero.

## Complexity detail

Let $n$ be the length of `nums`. The algorithm performs one expected-constant-time hash-map lookup and update per value, taking $O(n)$ expected time. At most $n+1$ distinct prefix XOR values are stored, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Enumerate all subarrays:** Extending every starting position while maintaining a running XOR is correct but requires $O(n^2)$ time.
- **Count bit occurrences directly:** Recomputing parity vectors for every range obscures the equivalent XOR condition and is also quadratic without prefix-state pairing.
- **All-zero ranges:** Every subarray of $z$ zeros is beautiful, contributing $z(z+1)/2$ to the answer.
- **Single nonzero element:** Its XOR is nonzero, and its set bits cannot be removed because each operation needs two indices.
- **Overlapping ranges:** Equal prefix values may form several different boundary pairs; all such subarrays must be counted.
- **Answer width:** Up to $n(n+1)/2$ subarrays can qualify, which exceeds a 32-bit signed integer when $n=10^5$.

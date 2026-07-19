## General
**View legal swaps as connectivity.** Two values sharing a prime factor may swap directly. More importantly, values connected through a chain of shared factors can be permuted within the same connected component: adjacent swaps along paths can transport values through that component. A direct greatest common divisor greater than one is therefore not required between every pair that ultimately exchanges positions.

**Connect values through prime-factor nodes.** Build a disjoint-set structure indexed by every integer through $M$. Use a smallest-prime-factor sieve, then factor each array value. Union that value with each distinct prime dividing it. Values that share a factor—or are linked through other values and factors—then receive the same representative.

**Compare with the unique sorted target.** Let `target = sorted(nums)`. At position $i$, the original value must be able to move within its component to supply `target[i]`. Thus require `find(nums[i]) == find(target[i])` for every position. If all comparisons pass, each component contains exactly the multiset needed at its target positions, so its values can be rearranged to realize the sorted array. If one comparison fails, no allowed swap crosses the two components, making that target impossible.

## Complexity detail
The smallest-prime-factor sieve costs $O(M\log\log M)$ time and $O(M)$ space. Factoring all values through that table and performing disjoint-set operations costs $O(N\log M)$ time under the displayed elementary bound. Sorting costs $O(N\log N)$ time. The disjoint-set and sieve arrays dominate the $O(M)$ space usage.

## Alternatives and edge cases
- **Compare every pair with `gcd`:** Building connectivity from all value pairs is correct but takes $O(N^2\log M)$ time.
- **Require a direct common factor at each mismatched position:** This misses transitive swap chains in which the original and target values are coprime but connected through intermediates.
- An already non-decreasing array is valid even when every value is isolated.
- Duplicate values are interchangeable and naturally belong to the same value component.
- A prime value can move only if another present value is divisible by that prime.
- The array of length one is always sortable because no operation is needed.

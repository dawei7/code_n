## General

A valid permutation must alternate odd and even values. Backtracking can enforce that rule while constructing the permutation, so it never spends time completing an invalid prefix. A bit mask records which values already occur in the current path.

After an odd value, consider only unused even values; after an even value, consider only unused odd values. At the first position, an even $n$ permits either parity. When $n$ is odd, however, there is one more odd value than even values, so every full alternating permutation must begin and end with an odd value. Starting with an even value would inevitably run out of even values before the path is complete, so that entire branch is omitted.

Candidate values are visited in increasing numeric order. Depth-first search therefore completes every permutation under a smaller prefix before advancing to a larger prefix, which is precisely lexicographic order. Every emitted path contains all values exactly once because the bit mask forbids reuse, and every adjacent pair has opposite parity by construction. Conversely, following the values of any valid permutation selects an available candidate at every depth, so the search emits all valid answers.

## Complexity detail

Let $A$ be the number of returned permutations. If $n$ is odd, $A=\lceil n/2\rceil!\,\lfloor n/2\rfloor!$; if $n$ is even, $A=2((n/2)!)^2$. Materializing each length-$n$ answer costs $O(n)$, so the total time is $O(A n)$. Excluding the returned arrays, the recursion path and call stack use $O(n)$ space; the integer bit mask is constant-sized for the stated constraint.

## Alternatives and edge cases

- **Generate all permutations and filter:** This is correct but explores $n!$ complete arrangements even though most violate the alternating-parity rule.
- **Build odd and even permutations separately:** Interleaving every ordering of the two parity groups also reaches the output-sensitive bound, but requires extra machinery to preserve global lexicographic order.
- **Single value:** For `n = 1`, the only permutation is valid because it has no adjacent pair.
- **Odd number of values:** The path must start and end with an odd value because the odd group contains one additional element.
- **Lexicographic ordering:** Iterating eligible numeric values in ascending order makes a separate result sort unnecessary.

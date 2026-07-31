## General

Only parity matters: replacing a value by any other value with the same parity cannot change whether an adjacent pair is valid. Two neighboring values have different parity exactly when their remainders modulo $2$ differ.

Scan from the second element to the end and compare each value with its immediate predecessor. Before index `i` is checked, every pair ending before `i` has already been shown to alternate. If the two remainders at `i - 1` and `i` are equal, that pair directly violates the definition, so the whole array is not special and the scan can stop.

If the scan reaches the end, it has checked every adjacent pair and none has equal parity. Therefore every pair contains one even and one odd value, which is exactly the condition for the array to be special.

## Complexity detail

For $n = \lvert\texttt{nums}\rvert$, the scan examines at most $n-1$ adjacent pairs, so the running time is $O(n)$.

The algorithm keeps only the current index and parity comparison, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Parity-bit XOR:** `(nums[i - 1] ^ nums[i]) & 1` is one exactly when the parity bits differ. It has the same $O(n)$ time and $O(1)$ space, but comparing remainders states the definition more directly.
- **Build a parity array:** Mapping every value to its remainder before checking neighbors is correct, but it uses $O(n)$ extra space without reducing the running time.
- **Check every pair of positions:** Nonadjacent pairs are irrelevant to the definition; examining all pairs wastes $O(n^2)$ time and is the principal slower benchmark comparison.
- A one-element array is special because it contains no adjacent pair that could violate the condition.
- A violation at the first pair permits an immediate `false`; a violation at the final pair must still be detected.
- The values are positive, but their magnitudes do not matter once their parities are known.

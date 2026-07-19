## General
**Preserve the initial configuration**

Store a private copy of `nums` at construction. A reset returns a new copy of this snapshot, so neither a caller's later mutation nor a previous shuffle can alter the required original order.

**Commit one position at a time**

To shuffle, copy the original array and process positions from left to right. At position $i$, choose an index uniformly from the still-uncommitted range $[i,n-1]$ and swap its value into position $i$. This is the Fisher-Yates shuffle.

**Why every permutation has equal probability**

Any target permutation requires one particular choice among `n` candidates for position zero, then one among $n - 1$ for position one, continuing to the final forced choice. Its probability is therefore $1 / n \cdot 1 / (n - 1) \cdot \ldots \cdot 1 = 1 / n!$. Every permutation follows exactly one such choice sequence, so none is favored.

**Validate structure without prescribing randomness**

A shuffle is allowed to return the original order, especially for short arrays. The package checks that each shuffle preserves all values and multiplicities and that each reset exactly restores the snapshot; the Fisher-Yates selection rule supplies the uniformity guarantee.

## Complexity detail
For an array of length `n`, either public operation copies `n` values. Shuffle also performs $n - 1$ constant-time random choices and swaps, so both operations take $O(n)$ time and return $O(n)$ output space. The object retains an additional $O(n)$ snapshot.

## Alternatives and edge cases
- **Built-in shuffle on a fresh copy:** is concise and normally implements an equivalent linear-time algorithm, but hides the uniformity argument.
- **Repeatedly choose and remove from a shrinking list:** can be uniform, but middle removals make it $O(n^2)$.
- **Random-key sorting:** costs $O(n \log n)$ and can introduce bias when random keys collide.
- A one-element array has exactly one permutation.
- Duplicate values must preserve their full multiplicities even though several position permutations look identical.
- A shuffle may legally equal the original array.
- Reset must return the original order after any number of shuffles and should not expose mutable internal storage.

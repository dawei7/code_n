## General
**Encode each index selection as a bitmask.** A mask from $0$ through $2^N-1$ identifies one subsequence in source order. Determine whether it is palindromic by comparing the characters at its lowest and highest selected indices and consulting the already computed mask with those two bits removed. Single-bit and empty masks are base palindromes. Record the selected-bit count for palindromic masks and zero for all others.

**Precompute the best palindrome inside every available set.** Let `best[mask]` be the greatest palindromic length obtainable from any submask of `mask`. Initialize it with the exact-mask palindrome lengths. For each bit, propagate `best[mask ^ bit]` into `best[mask]` whenever the bit is present. After all bits, every submask possibility has contributed.

**Pair a selection with its complement.** For a first subsequence mask $A$, the second subsequence may use only indices in `full_mask ^ A`. Multiplying the palindrome length of $A$ by `best[full_mask ^ A]` therefore gives the best disjoint partner for that exact first selection. Taking the maximum over all masks examines every valid pair: any pair's second mask is a submask of the first mask's complement, while the table never admits an overlapping index.

## Complexity detail
There are $2^N$ masks. The outer-character recurrence classifies them in $O(2^N)$ time. The submask-maximum transform performs $N2^N$ constant-time updates, and the final scan takes $O(2^N)$ time, giving $O(N2^N)$ overall. The mask tables use $O(2^N)$ space.

## Alternatives and edge cases
- **Assign every character to the first subsequence, second subsequence, or neither:** This backtracking explores $3^N$ assignments and then checks the resulting strings.
- **Compare every pair of palindromic masks:** Testing disjointness across all mask pairs can take $O(4^N)$ time; the submask-maximum transform removes that extra factor.
- Two equal characters at the same source index cannot be shared; disjointness concerns indices, not values.
- A two-character string always permits two one-character palindromes, giving product $1$.
- When all characters are equal, the best split balances the two subsequence lengths.
- Characters not used by either subsequence are allowed.

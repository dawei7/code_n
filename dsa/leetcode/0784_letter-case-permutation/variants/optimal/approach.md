## General
**Branch only at letters**

Walk through a mutable character array. A digit has only one continuation, while a letter creates two recursive branches: place its lowercase form, then its uppercase form. When the index reaches the end, join the current characters into one complete result.

**Cover every independent choice once**

If the string contains `l` letters, a root-to-leaf path records one of the two case decisions at each letter and no decision at a digit. Every possible sequence of `l` binary choices therefore reaches one leaf, and two different paths differ at some letter, so they cannot emit the same string. This proves that all $2^{l}$ permutations are produced exactly once.

The algorithm restores a letter after exploring its branches, keeping the shared character buffer valid for the caller. No generated string needs to be searched for duplicates because the recursion tree itself establishes uniqueness.

## Complexity detail
There are $2^{l}$ output strings, and materializing each length-`n` string takes $O(n)$, for $O(n \cdot 2^l)$ time. The returned strings occupy $O(n \cdot 2^l)$ space; the recursion and mutable buffer add $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Iterative expansion:** Start with one empty prefix and duplicate the prefix list at each letter; this has the same output-sensitive complexity.
- **Bitmask choices:** Map the set bits of a mask to uppercase choices for the `l` letter positions; this also enumerates exactly $2^{l}$ results.
- **Enumerate masks for every character:** Treating digits as branch positions performs unnecessary work exponential in `n` instead of `l`.
- **Duplicate filtering:** Generating candidates and scanning an output list before insertion can add quadratic work in the number of permutations.
- **No letters:** Return a one-element list containing the original string.
- **Initially uppercase letters:** Both normalized lowercase and uppercase variants must still appear.
- **Output order:** Any ordering is valid, but every permutation must occur exactly once.

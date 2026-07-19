## General
**Partition subsequences by their final character.** Maintain one count for each lowercase letter. The count for a letter represents how many distinct non-empty subsequences of the processed prefix end with that letter. These 26 groups are disjoint, so their sum is the total number currently known.

**Append the current character to every existing result.** Suppose the next character is `c` and the current total is `total`. Appending `c` to every existing distinct subsequence creates `total` strings ending in `c`; the one-character string `"c"` contributes one more. Therefore the complete new group ending in `c` has size `total + 1`.

**Replace instead of adding the same ending group.** Any strings previously counted as ending in `c` are duplicates of strings in the newly constructed group: each was already obtainable at the earlier occurrence of `c`, while the new occurrence recreates it. Assign `ending[c] = total + 1` rather than adding to the old value. Groups ending in other letters remain unchanged. Consequently, after every prefix, each distinct non-empty subsequence occurs in exactly the group named by its final character. Apply the modulus after each update and sum the 26 groups at the end.

## Complexity detail
Each of the $N$ characters performs a sum over the fixed 26-letter alphabet and one replacement, so the running time is $O(N)$. The 26 ending counts use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Quadratic prefix recomputation:** Store the net number of new distinct results contributed at every position and rescan all earlier contributions to obtain each prefix total. This preserves the same duplicate correction but costs $O(N^2)$ time and $O(N)$ space.
- **Explicit subsequence set:** Generate strings by extending every existing subsequence and deduplicate them in a set. This can require exponential time and space and is infeasible at the maximum length.
- **Repeated character:** A string such as `"aaa"` has only one distinct subsequence of each possible positive length; replacing the previous ending group prevents overcounting.
- **Modulo subtraction:** Implementations using a subtractive recurrence must normalize negative intermediate values before returning them.
- **Empty subsequence:** It is useful conceptually as the source of each one-character subsequence, but it must not be included in the returned count.

## General

**What can survive the operations.** Removing characters only from the two ends of `initial` can leave either nothing or one contiguous substring. Later additions at the ends cannot change the surviving characters or place new characters between them. Consequently, every character retained from `initial` must form a contiguous substring that also occurs in `target`.

Suppose a common substring has length $L$. Remove the other $m-L$ characters from `initial`, then add the $n-L$ target characters lying before and after that occurrence. This constructs `target` in exactly

$$
(m-L)+(n-L)=m+n-2L
$$

operations. Conversely, every valid transformation retaining $L$ original characters needs at least those removals and additions. Minimizing the operation count is therefore equivalent to maximizing $L$, so the retained block must be a longest common substring of the two strings.

**Finding the longest common substring.** Use dynamic programming where the cell for positions `i` and `j` records the length of the longest equal suffix ending at those positions. If `initial[i] == target[j]`, that suffix extends the equal suffix ending at the preceding pair of positions by one. If the characters differ, its length is zero because a common substring cannot skip either character.

Only the previous row is needed to build the current row. Track the largest cell value while processing all $mn$ position pairs, then substitute that length into `m + n - 2 * longest`. The construction above achieves this count, while the survival argument proves that no transformation can use fewer operations.

## Complexity detail

The dynamic program examines every pair consisting of one position in `initial` and one position in `target`, taking $O(mn)$ time. Two rows of $n+1$ integers are stored, for $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Three-dimensional start-pair expansion:** Try every pair of starting positions and scan forward while characters match. It is correct but can take $O(mn\min(m,n))$ time on repetitive strings.
- **Enumerate and search substrings:** Generate every substring of one string and test whether it occurs in the other. This creates many temporary strings and can require cubic or worse total work.
- **Binary search with rolling hashes:** Search for the largest common length using hashed windows. It can be faster on large strings, but collision-free verification complicates the method and is unnecessary for the $1000$-character limits.
- **Longest common subsequence:** A subsequence may skip interior characters, but the allowed end operations cannot preserve separated pieces. Using an LCS would underestimate the required operations.
- **Already equal strings:** The longest common substring is the whole string, so the formula returns zero.
- **No common character:** Then $L=0$; every original character must be removed and every target character added, for $m+n$ operations.
- **Repeated characters:** Multiple common occurrences may tie for the maximum length, but only that length affects the answer.

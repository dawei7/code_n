## General

**Reduce each palindrome to its first half**

A palindrome exists only when at most one character count is odd. That odd character, if present, is forced into the center. Every remaining count contributes half of its copies to the first half, and the second half is its reverse. Consequently, lexicographic order among the palindromes is determined by the first-half multiset permutation.

**Reuse as much of the target prefix as possible**

Greedily consume the target's first-half characters while the required copies remain. If the entire prefix is available, mirror it with the forced center. Return that palindrome immediately when it is already strictly greater than the full `target`; the equal first half is lexicographically smaller than every alternative first half that must be increased.

Otherwise, move right to left through the matched prefix. At each position, restore its character to the remaining multiset and look for the smallest available character strictly greater than the target character there. Once found, place it and fill the rest of the first half in ascending order. This is the rightmost possible increase, uses the smallest increasing character, and minimizes every later position, so its completed palindrome is the smallest one greater than `target`.

If no position can be increased, no qualifying palindrome exists.

## Complexity detail

Let $n$ be the common string length. Character counting, prefix matching, backtracking, suffix construction, and mirroring each process at most $O(n)$ characters. Scans over the 26-letter alphabet are constant-width, so total time is $O(n)$ and auxiliary space is $O(n)$ for the constructed strings and half representation.

## Alternatives and edge cases

- **Enumerate palindromic permutations:** Generating and sorting all half permutations is factorial in the half length.
- **Generate successive multiset permutations:** Repeatedly advancing until the target is exceeded may traverse exponentially many palindromes.
- **More than one odd count:** No palindromic permutation exists.
- **One-character string:** Its sole permutation qualifies only when that character is strictly greater than `target`.
- **Equal first half:** The center and mirrored half must still be compared with the remainder of `target` before backtracking.
- **Strict comparison:** A palindrome equal to `target` cannot be returned.
- **Repeated letters:** Counts, rather than distinct character choices, determine valid half permutations.

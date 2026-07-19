## General
**Reduce the answer to a palindrome test**

If `s` is already a palindrome, removing the whole string is a legal single step. Because the input is non-empty, zero steps cannot suffice, so the optimum is exactly 1.

If `s` is not a palindrome, one step is impossible: the only way to empty the string in one removal is to choose every character, but that complete subsequence is not palindromic. Two steps always suffice because the alphabet contains only two letters. Select every `a` in their existing order; a sequence made from one repeated letter is a palindrome. Then do the same for every `b`. Empty selections may simply be omitted, and a non-palindrome over this alphabet necessarily contains both letters. Therefore every non-palindromic input has optimum 2.

Use two pointers from the ends to determine which of these cases applies. Return 2 at the first mismatch; if the pointers cross without one, return 1.

## Complexity detail
At most $\lfloor n/2\rfloor$ mirrored pairs are compared, so the running time is $O(n)$. The two indices require $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Reverse-and-compare:** Comparing `s` with `s[::-1]` is equally direct and takes $O(n)$ time, but materializes a reversed string and therefore uses $O(n)$ auxiliary space in Python.
- **Longest palindromic subsequence dynamic programming:** Checking whether its length is $n$ also distinguishes the two answers, but spends $O(n^2)$ time and $O(n)$ or $O(n^2)$ space on information the binary-alphabet argument makes unnecessary.
- **Single character:** It is already a palindrome, so the answer is 1.
- **Only one letter:** Any number of identical characters forms a palindrome and can be removed together.
- **Subsequence versus substring:** The two-step upper bound depends on selecting all occurrences of one letter even when they are separated.

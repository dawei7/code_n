## General
**Match the forced cross-string exterior.** First consider candidates formed from a prefix of `a` and a suffix of `b`. Place `left` at the start and `right` at the end. While `a[left] == b[right]`, those characters can serve as the next mirrored outer pair of such a candidate. Move both pointers inward. This comparison does not require choosing the exact split yet: every successful `a`-prefix/`b`-suffix palindrome must use these sources on its exterior until the pointers meet or a cross-string mismatch appears.

**Reduce the unresolved center to one source.** Suppose the first mismatch occurs between indices `left` and `right`. The split boundary cannot make those unequal cross-source characters mirror one another. To remain viable, it must place the whole unresolved interval on one side of the boundary. Consequently, either `a[left:right + 1]` itself must be a palindrome or the corresponding interval of `b` must be a palindrome. A direct inward check of those two intervals determines whether this source direction can work.

**Check both prefix directions.** Repeat the same reasoning with `b` supplying the prefix and `a` supplying the suffix. If either directional check succeeds, its matching exterior plus its palindromic center gives a valid split. If both fail, each possible source direction has a forced mismatch and neither available center is palindromic, so no common split can form a palindrome.

## Complexity detail
Each directional cross-check moves its pointers inward at most $n/2$ times, and its center checks together take $O(n)$ time. Running both directions therefore remains $O(n)$. Only pointer and Boolean state is stored, so auxiliary space is $O(1)$; no concatenated candidate string is created.

## Alternatives and edge cases
- **Enumerate every split:** Construct both cross-string candidates for all $n+1$ split positions and compare each with its reverse. This is straightforward but takes $O(n^2)$ time and creates temporary strings.
- **Rolling hashes:** Forward and reverse hashes can test every candidate more quickly, but they require extra storage and collision handling for a task solvable deterministically with two pointers.
- A one-character string is always a palindrome, regardless of which source supplies it.
- Splits at index 0 and index $n$ are legal; therefore, either input already being a palindrome is sufficient.
- The two source directions are distinct. A split may work for `a_prefix + b_suffix` while every `b_prefix + a_suffix` choice fails.
- Equal-length inputs are essential because the same split index must partition both strings.
- When the cross pointers meet or pass without a mismatch, the candidate exterior already proves success.

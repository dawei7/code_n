## General
**Why ordinary center expansion repeats work**

Every palindrome has a center, so expanding around every character and every gap is a natural solution. On a repetitive string such as `aaaaaaaa`, however, neighboring centers compare most of the same pairs again and the total work becomes quadratic.

Manacher's algorithm avoids that repetition. It remembers the palindrome reaching farthest to the right and uses symmetry to initialize radii for centers already inside that proven region. Direct comparison resumes only where the known symmetry ends.

**Represent odd and even palindromes uniformly**

The candidate constructs

`transformed = "^#" + "#".join(s) + "#$"`.

The separator `#` turns every palindrome into an odd-length interval in the transformed string: an original character centers an odd palindrome, while a separator centers an even one. The distinct `^` and `$` sentinels stop expansion without boundary checks. They and `#` are safe because the contract restricts `s` to English letters and digits.

For example:

```text
original:       a b b a
transformed: ^ # a # b # b # a # $
```

Let `radius[i]` be the number of matching transformed positions on either side of center `i`. That radius is also the length of the corresponding palindrome in the original string. Thus the separator between the two `b` characters in `cbbd` has radius 2 and represents `bb`.

**Reuse the rightmost palindrome through its mirror**

The variables `center` and `right` describe the known palindrome whose matched interval reaches farthest right; `right` is its rightmost matched transformed position. For a new center `i < right`, the reflected center is `mirror = 2 * center - i`.

Reflection proves matches only inside the known interval, so the candidate starts with

`radius[i] = min(right - i, radius[mirror])`.

If the mirrored palindrome stays inside the known boundary, its radius transfers completely. If it reaches or crosses that boundary, only `right - i` positions are already proved. The outward `while` loop then tests the first unknown pair and continues until a mismatch. When `i + radius[i]` passes `right`, the candidate updates both rightmost-palindrome variables.

**Why the scan is linear**

Copied radii require constant time. Every successful comparison that extends beyond the previous `right` boundary advances that boundary permanently, so all boundary-extending comparisons total $O(n)$. Each of the $O(n)$ transformed centers can also cause at most one terminating mismatch. The complete scan is therefore linear, including on repetitive inputs.

**Recover the original substring**

The candidate retains `best_center` and `best_length`, updating them only for a strictly larger radius. The original start position is

`start = (best_center - best_length) // 2`.

Subtracting the radius reaches the transformed left edge, and division by two removes the separators preceding the original substring. Returning `s[start : start + best_length]` works for both parities because the transformed radius already equals the original palindrome length.

Every original palindrome maps to exactly one transformed center and radius. Mirror initialization assumes only pairs already proved by symmetry, and direct expansion verifies every remaining pair until the first mismatch, so each stored radius is exact. Selecting the greatest radius therefore returns a longest palindromic substring. Keeping the first radius on ties is deterministic but not required by the contract.

## Complexity detail
Let $n$ be the length of `s`. The transformed string and radius array contain $2n+3$ positions, using $O(n)$ space. Construction and coordinate recovery are linear or constant, and the amortized scan above takes $O(n)$ time.

## Alternatives and edge cases
- **Expand around every center:** is much simpler and uses $O(1)$ auxiliary space, but takes $O(n^2)$ time on repetitive inputs.
- **Dynamic programming:** records palindromic intervals explicitly and requires $O(n^2)$ time and space.
- **Enumerate and check substrings:** can require $O(n^3)$ time.
- **Single character:** has transformed radius 1 and is returned unchanged.
- **Even-length palindrome:** is centered on a `#` separator and needs no separate expansion formula.
- **Tied maximum lengths:** any longest palindrome is valid; the strict best update retains the first one found.

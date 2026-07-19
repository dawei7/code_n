## General
Every palindrome of length three has the form $x y x$: its two outer
characters agree, while its middle character may be any lowercase letter. Fix
one possible outer letter $x$. A subsequence $x y x$ exists exactly when some
occurrence of $y$ lies strictly between two occurrences of $x$.

The widest useful pair of occurrences is the first and last $x$ in the
string. If a letter $y$ can lie between any pair of occurrences of $x$, it
also lies between this first and last pair. Conversely, every letter strictly
between that pair directly supplies indices for $x y x$. Therefore the number
of distinct middle letters in that interval is exactly the number of unique
palindromes whose outer letter is $x$.

Repeat this calculation for each of the 26 lowercase letters and add the
interval's distinct-letter count. Palindromes counted for different outer
letters cannot be identical, and using a set of middle letters counts each
$x y x$ only once even when many index triples produce it.

## Complexity detail
Here $N$ is the length of `s`. Finding the first occurrence, last occurrence,
and intervening distinct letters takes $O(N)$ work for each of 26 possible
outer letters. Since 26 is a fixed alphabet size, the total is $O(N)$. The
middle-letter set and the outer-letter loop each hold at most 26 letters, so
their storage is $O(1)$ with respect to $N$.

## Alternatives and edge cases
- **Prefix and suffix letter masks:** Precompute which letters occur on each
  side of every index, then use each position as the middle character. This is
  also linear and fixed-space for a 26-letter alphabet, but needs more
  bookkeeping.
- **Rebuild both sides for every middle index:** Intersecting
  `set(s[:i])` and `set(s[i + 1:])` is correct, but repeatedly scans prefixes
  and suffixes and can take $O(N^2)$ time.
- An outer letter occurring fewer than twice cannot form a length-three
  palindrome.
- Three equal letters are valid: the outer and middle letters are allowed to
  match.
- Multiple index triples producing the same three letters still contribute
  only one unique palindrome.
- The middle character must occur strictly between the selected outer
  occurrences; merely having all three letters somewhere in the string is not
  sufficient.

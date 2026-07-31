## General

**Match the two sides by reversed words**

A two-letter word `"ab"` placed on the left side of a palindrome requires
`"ba"` in the mirrored position on the right. Maintain counts of unmatched
words. For each new word, consume one unmatched reverse if available and add
four characters to the answer; otherwise store the new word as unmatched.
Matching immediately cannot reduce future choices because every occurrence of
the same word and reverse is interchangeable.

Words such as `"aa"` are their own reverses. Every two occurrences form a
four-character mirrored pair exactly as above. After all possible pairs are
formed, at most one remaining equal-letter word may occupy the palindrome's
center, adding two characters. A non-symmetric word cannot be central because
its two letters would already disagree under reversal.

Every counted reverse pair can be placed symmetrically, and the optional
equal-letter word can be inserted between all pairs, so the count is
constructible. Conversely, every noncentral word in any palindrome must have
an occurrence of its reverse across the center, while the center can contain
only one word. The greedy count therefore uses the maximum possible number of
characters.

## Complexity detail

Let $n$ be the number of words. Each word performs constant-time operations on
one of only $26^2$ possible keys, giving $O(n)$ time. Because the lowercase
two-letter domain has a fixed 676 keys, the counter uses $O(1)$ space.

## Alternatives and edge cases

- **Search the remaining array for every reverse:** Greedily marking explicit
  pairs is correct but can take $O(n^2)$ time.
- **Sort the words:** Reverse groups can be paired after sorting, but this
  takes $O(n\log n)$ time.
- Duplicate non-symmetric words contribute only up to the number of available
  reverse occurrences.
- Equal-letter words contribute in pairs, with at most one unpaired occurrence
  used as the center.
- If no reverse pair or equal-letter word exists, the answer is `0`.

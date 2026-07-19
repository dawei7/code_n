## General
**Remember the outer character, not just the interval length**

An ordinary longest-palindromic-subsequence table is insufficient: two palindromes of the same length can differ in whether a new equal pair may wrap around them. The decisive information is the character at the two current ends. For an interval, keep one value for each lowercase letter: the longest good palindrome inside that interval whose outer pair uses that letter. A two-character palindrome `"xx"` is a valid center and initializes the construction.

Process intervals by increasing length. For every boundary letter, an interval can inherit the best value from the interval that omits its left endpoint or from the one that omits its right endpoint. These transitions cover every optimum that does not use both current endpoints.

**Wrap only around a different boundary letter**

If the endpoints contain the same letter `x`, they may form a new outer pair. The inner palindrome must either be empty or have an outer letter other than `x`; otherwise the newly adjacent pairs at both sides would repeat `x` away from the center. Thus the candidate is two plus the best inner-interval state over all letters different from `x`. When the inner value is zero, the candidate is the valid middle pair `"xx"` itself.

The transition is exhaustive. If an optimum skips at least one endpoint, an inheritance transition contains it. If it uses both endpoints, they must match, and removing them leaves either an empty center or a smaller good palindrome whose boundary differs from the removed letter. Conversely, wrapping precisely such a state preserves the palindrome, even length, and neighbor rule. Induction over interval length therefore proves that the maximum state for the full string is the requested answer.

**Discard interval lengths that are no longer needed**

A length-$L$ state reads only length $L-1$ states for endpoint omission and the length $L-2$ state for wrapping. Retain those two layers and replace them after finishing the current length. No later transition needs an older layer.

## Complexity detail
There are $O(n^2)$ intervals. Each transition scans the fixed 26-letter lowercase alphabet, so the total time is $O(26n^2)=O(n^2)$. A rolling layer contains $O(n)$ intervals with 26 values each, and only three layers coexist, giving $O(26n)=O(n)$ auxiliary space.

## Alternatives and edge cases
- **Memoized endpoints plus previous letter:** a recursive state can choose matching pairs while carrying the forbidden outer letter; it has the same quadratic asymptotic time but may store $O(n^2)$ states and consume recursion depth.
- **Full three-dimensional interval table:** retaining every interval-letter state simplifies random access but uses $O(n^2)$ auxiliary space when rolling is sufficient.
- **Ordinary palindromic-subsequence DP:** recording only one length per interval loses the boundary letter and can incorrectly accept equal neighbors outside the middle.
- **No repeated character:** no two-character center exists, so the answer is zero rather than one because a good palindrome must have even length.
- **All characters equal:** any equal pair is valid, but no good palindrome of length at least four can be formed.
- **Subsequence semantics:** selected characters preserve their original order but need not be contiguous in `s`.

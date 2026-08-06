## General

**A palindrome is determined by one half and its center**

Count characters. More than one odd count makes a palindrome impossible; the lone odd character, if present, is the
center. Store half of each character's count in `half_counts`, and sort its distinct keys once so generation is
deterministic.

**Choose directly from the remaining multiset**

At each depth, try every distinct `character` whose remaining half-count is positive. Decrement that count, append the
character to `path`, recurse, and restore both pieces of state on return. Once `path` reaches `half_length`, mirror it
around `center` and append the resulting palindrome.

The mutable counts always equal the original half-multiset minus the characters in `path`. Choosing a character value,
rather than one of several identical positions, creates exactly one branch for each distinct next prefix.

**Mirroring gives a bijection from halves to answers**

Every complete path uses exactly half of each paired character count. Mirroring it around the forced center therefore
restores all original counts and produces a palindrome. Conversely, the left half of any valid answer is one distinct
permutation of this same multiset. Count-based branching reaches each such permutation once, so every valid answer
appears exactly once and no duplicate is emitted.

## Complexity detail

Counting costs $O(n)$, and sorting the $k \le 26$ distinct lowercase characters costs $O(k \log k)$. Every visited
prefix can be extended to an output, and each recursion node scans at most 26 keys. Across $p$ outputs of length $n$,
generation and string construction therefore take $O(p \cdot n)$ time, for $O(n + p \cdot n)$ overall. The counts,
path, and recursion stack use $O(n)$ auxiliary space, excluding the returned strings.

## Alternatives and edge cases

- **Permute the full string:** explores up to $n!$ arrangements and filters afterward.
- **Position-based half backtracking:** can skip equal unused neighbors correctly, but still scans duplicate positions at every depth and needs a parallel `used` array.
- **Multiple odd counts:** no center can absorb more than one unpaired character, so the candidate returns immediately.
- **Empty input:** the candidate returns `[""]` defensively, although the native contract requires a nonempty string.

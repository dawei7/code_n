## General
**A palindrome is determined by one half and its center**

Count characters. More than one odd count makes a palindrome impossible; the lone odd character, if present, is the center. Put half of every even remainder into a sorted list.

**Skip duplicate choices at the same recursion depth**

Backtrack over the sorted half. At each depth, skip an unused character equal to the previous unused choice. Mirror each complete half around the fixed center.

The partial half contains exactly the selected multiset elements. Duplicate skipping chooses each distinct remaining character value once at a depth, so no two recursion branches represent the same half prefix.

**Mirroring gives a bijection from halves to answers**

Every complete half uses exactly half of each paired character count. Mirroring it around the forced center therefore restores all original counts and produces a palindrome. Conversely, the left half of any valid answer is one distinct permutation of that same multiset. Depth-local duplicate skipping enumerates each such permutation once, so every answer appears exactly once.

## Complexity detail
Counting costs $O(n)$. Constructing each of `p` output strings costs $O(n)$, giving $O(n + p \cdot n)$ time. The half, path, counts, and recursion use $O(n)$ auxiliary space, excluding output.

## Alternatives and edge cases
- **Permute the full string:** explores up to $n!$ arrangements and filters afterward.
- **Generate duplicate half permutations then deduplicate:** performs factorial redundant work on repeated characters.
- Empty input has one palindromic permutation: the empty string.

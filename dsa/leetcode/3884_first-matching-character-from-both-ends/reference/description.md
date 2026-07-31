## Description

You are given a string `s` of length $n$ containing only lowercase English letters.

Indexing is zero-based. At each position, the comparison uses the two characters placed the same distance from their respective ends of the string.

For an index `i`, compare `s[i]` with the character equally far from the other end, at index `n - i - 1`. Return the smallest index whose two compared characters are equal.

If no index satisfies that equality, return `-1`.

## Description

A generalized abbreviation of a word is formed by selecting any number of substrings that neither overlap nor touch one another, then replacing every selected substring with its length.

For `"abcde"`, the following are valid abbreviations:

- `"a3e"`: replace `"bcd"` with its length `3`.
- `"1bcd1"`: independently replace `"a"` and `"e"` with `1`.
- `"5"`: replace the entire word with its length.
- `"abcde"`: select no substring.

The following forms are invalid:

- `"23"`: the substrings `"ab"` and `"cde"` are adjacent, so they must not be encoded as separate neighboring numbers.
- `"22de"`: the proposed substrings `"ab"` and `"bc"` overlap.

Given `word`, return every possible generalized abbreviation. The result may use any order.

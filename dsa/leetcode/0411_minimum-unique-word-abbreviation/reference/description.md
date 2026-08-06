## Description

A string may be abbreviated by replacing any number of non-adjacent, non-empty substrings with their decimal
lengths. For example, `"substitution"` has these valid abbreviations among others:

- `"s10n"` keeps `s` and `n` while replacing `"ubstitutio"`.
- `"sub4u4"` replaces `"stit"` and `"tion"`, separated by the literal `u`.
- `"12"` replaces the entire string.
- `"su3i1u2on"` replaces `"bst"`, `"t"`, and `"ti"`, with literal characters between those substrings.
- `"substitution"` replaces no substring.

By contrast, `"s55n"` is invalid because it represents two adjacent replaced substrings. The length of an
abbreviation counts every unreplaced letter and every replaced substring as one token, not the number of printed
digits. Thus, `"s10n"` has length $3$, while `"su3i1u2on"` has length $9$.

Given a string `target` and an array `dictionary`, return a shortest abbreviation of `target` that is not an
abbreviation of any dictionary word. When several shortest valid answers exist, return any one of them.

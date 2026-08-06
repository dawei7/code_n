## Description

An abbreviation of a string may replace any number of non-adjacent, non-empty substrings with their decimal
lengths. Characters outside those replacements remain literal and keep their original order. A replacement length
cannot have a leading zero.

For example, `"substitution"` has each of these valid representations:

- `"s10n"` keeps `s` and `n` while replacing `"ubstitutio"` with its length.
- `"sub4u4"` replaces `"stit"` and `"tion"`, with the literal `u` separating the two replacements.
- `"12"` replaces the entire word.
- `"su3i1u2on"` replaces `"bst"`, `"t"`, and `"ti"`; every pair of replacements is separated by a literal
  character.
- `"substitution"` replaces no substring.

These forms are invalid:

- `"s55n"` represents two adjacent replaced substrings rather than non-adjacent replacements.
- `"s010n"` starts a replacement length with zero.
- `"s0ubstitution"` uses zero as though an empty substring had been replaced.

Given `word` and `abbr`, determine whether `abbr` is a valid abbreviation of `word`. A substring is a contiguous,
non-empty sequence of characters within a string.

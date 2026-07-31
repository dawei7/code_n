## Description

A string `s` can be scrambled into a string `t` by applying this recursive process:

1. If the current string has length `1`, stop processing it.
2. Otherwise, split it at some index into two non-empty substrings `x` and `y`, so the current string is `x + y`.
3. Either keep those two substrings in the order `x + y` or swap them to `y + x`.
4. Apply the same process recursively to both `x` and `y`.

Given equal-length strings `s1` and `s2`, return whether `s2` can result from scrambling `s1` in this way.

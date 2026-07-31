## Description

You receive two binary strings, `s1` and `s2`, with the same length $n$. Starting from `s1`, you may perform either operation any number of times and in any order. A single-position operation chooses a character currently equal to `'0'` and changes it to `'1'`. An adjacent-pair operation chooses neighboring positions that are both currently `'1'` and changes both characters to `'0'` together.

Find the fewest operations that make the evolving `s1` exactly equal to `s2`. Return `-1` when no legal sequence can reach the target. Operation preconditions apply to the current string, so an earlier operation may enable or disable a later adjacent-pair choice.

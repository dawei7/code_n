## Description

You are given two binary strings `s` and `t` of the same length $n$, together with three positive integers: `flipCost`, `swapCost`, and `crossCost`.

You may perform any of the following operations any number of times, in any order:

- Choose an index `i` and flip either `s[i]` or `t[i]`, changing `'0'` to `'1'` or `'1'` to `'0'`. This costs `flipCost`.
- Choose two distinct indices `i` and `j`, then swap `s[i]` with `s[j]` or swap `t[i]` with `t[j]`. This costs `swapCost`.
- Choose an index `i` and swap `s[i]` with `t[i]`. This costs `crossCost`.

Return the minimum total cost required to make `s` and `t` equal.

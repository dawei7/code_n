## Description

Given integers `n`, `l`, and `r`, count the arrays of length `n` whose entries all belong to the inclusive integer interval `[l, r]` and whose neighboring entries are always different.

The direction of consecutive changes must also alternate. In particular, no three consecutive entries may be strictly increasing, and no three consecutive entries may be strictly decreasing. Equivalently, after one adjacent pair rises, the next pair must fall; after one pair falls, the next must rise.

Return the number of arrays satisfying all of these conditions modulo $10^9+7$.

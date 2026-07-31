## Description

An Android lock screen uses a $3 \times 3$ grid of dots. An unlock pattern is a sequence of dots connected by straight segments between consecutive selections. A sequence of $k$ dots is valid only when both rules hold:

- Every selected dot is distinct.
- If a segment between two consecutive selections passes through the center of another dot, that intermediate dot must already have appeared earlier in the sequence.

For example, moving directly from dot `2` to dot `9` is valid even when dots `5` and `6` have not been used, because that segment passes through neither center. Moving from `1` to `3` before selecting `2` is invalid because the segment crosses dot `2`.

Number the grid as follows:

```text
1 2 3
4 5 6
7 8 9

invalid: [4,1,3,6]       1 -> 3 skips unused 2
invalid: [4,1,9,2]       1 -> 9 skips unused 5
valid:   [2,4,1,3,6]     2 was selected before 1 -> 3
valid:   [6,5,4,1,9,2]   5 was selected before 1 -> 9
```

Given integers `m` and `n`, return the number of distinct valid unlock patterns containing at least `m` and at most `n` dots. Two patterns differ if their selected dot sets differ or if they visit the same dots in a different order.

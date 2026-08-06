## Hints

1. One option is to binary-search every row for its first `1` and retain the smallest resulting column.
2. For the optimal method, place a pointer at the top-right corner and allow only left and downward moves: move down after reading `0` and left after reading `1`. Determine why those moves are safe and how many calls they require.

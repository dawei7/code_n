## Description

You are given an $m \times n$ grid whose cells contain only `0`, `1`, or `2`, together with an integer budget `k`.

Begin at the top-left cell `(0,0)` and reach the bottom-right cell `(m - 1,n - 1)`. Every move must go exactly one cell to the right or exactly one cell down.

Each visited cell adds score and cost according to its value:

- A `0` adds `0` to the score and costs `0`.
- A `1` adds `1` to the score and costs `1`.
- A `2` adds `2` to the score and costs `1`.

Return the greatest score obtainable by a path whose total cost does not exceed `k`. Return `-1` if no such path reaches the destination.

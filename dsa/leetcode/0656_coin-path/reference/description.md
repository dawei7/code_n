## Description

An integer array `coins` of length `n` is viewed as **1-indexed**, and `maxJump` limits each forward move. A position with value `-1` is blocked and cannot be visited. Landing on any other position `i` costs `coins[i]`. From `i`, the next position may be `i + k` only when $1 \le k \le \texttt{maxJump}$ and $i + k \le n$.

You begin at position `1`, which is guaranteed not to be blocked. Find a path to position `n` whose sum of visited-position costs is minimum. Return the visited indices in order. If several paths have that minimum cost, return the **lexicographically smallest** one; if the destination cannot be reached, return an empty array.

To compare two paths, locate their first differing entries. The path containing the smaller index there is lexicographically smaller. If no differing entry exists before one path ends, the shorter path is lexicographically smaller.

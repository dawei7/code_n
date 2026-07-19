## General
**Choosing the final word of each row**

Let `best[i]` be the least cost for placing the first `i` words, with `best[0] = 0`. For every possible row start, extend its end one word at a time while maintaining the row length. Adding the first word contributes its letters; each later word contributes one separating space plus its letters. Stop extending as soon as the width exceeds `k`.

**Charging every row except the last**

For each valid interval from `start` through `end`, relax `best[end + 1]` from `best[start]`. Its added cost is `(k - row_length) ** 2`, except when `end` is the sentence's final word, in which case it is zero. Incremental length maintenance avoids reconstructing or rejoining the same word intervals.

Every legal layout ends its first row at some enumerated word and leaves the same optimization problem on the remaining suffix. Conversely, each relaxation appends one width-valid row to an already valid optimal prefix. Considering every possible end therefore covers all layouts, and taking the minimum at each prefix yields the global optimum.

## Complexity detail
There are $w$ possible row starts and at most $w$ ends examined from each start, so the running time is $O(w^2)$. The dynamic-programming array contains $w+1$ values and uses $O(w)$ space.

## Alternatives and edge cases
- **Top-down memoization:** Recursing on the next word with memoized suffix costs has the same state space, but a sentence with many short words can exceed Python's recursion depth.
- **Rebuild each candidate row:** Calling a join or summing a slice for every start/end pair preserves correctness but adds another factor of $w$, producing $O(w^3)$ time.
- The last row always costs zero; applying the squared penalty to it changes the optimization.
- A space is counted only between two words on the same row, never at either row boundary.
- A single word produces cost zero because its row is necessarily final.

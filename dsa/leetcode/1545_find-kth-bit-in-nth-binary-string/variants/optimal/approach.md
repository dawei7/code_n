## General
**Use the recursive symmetry instead of constructing strings**

The length of `Sn` is $2^n - 1$, so its middle position is $2^{n-1}$. The construction places `"1"` exactly there. Positions to the left are unchanged positions of `S(n - 1)`, so a left-side query can descend to the previous level with the same `k`.

**Reflect a right-side query into the left half**

The right half is the reversed, inverted copy of `S(n - 1)`. Reflecting position `k` across the full string maps it to position $2^n-k$ in the previous string. Recursively find that source bit, then invert it. This reduces the level by one without allocating either half.

**Reach a directly known bit**

At each level, the query is either the known middle bit, a left query, or an inverted reflected right query. Every recursive call decreases `n`, so it must reach a middle position or the base string `S1 = "0"`. These cases exactly mirror the three parts of the defining concatenation, which proves that the returned bit is the requested character.

## Complexity detail
Each recursive call performs constant arithmetic and reduces $n$ by one, producing at most $n$ calls. The time is therefore $O(n)$. The recursion stack holds at most $n$ frames, so auxiliary space is $O(n)$. No string of length $2^n-1$ is constructed.

## Alternatives and edge cases
- **Construct every sequence string:** direct simulation is easy to verify, but its time and memory grow as $O(2^n)$ even though only one bit is requested.
- **Iterative reflection:** track whether the answer is inverted while repeatedly reflecting right-half positions; this keeps $O(n)$ time and reduces auxiliary space to $O(1)$.
- At $n=1$, the only legal query returns `"0"`.
- Every level's middle position returns `"1"` without further recursion.
- The first position remains `"0"` at every level.
- A right-half reflection must both reverse the position and invert the resulting bit.
- Positions are one-indexed, so the middle is $2^{n-1}$ rather than an array-style zero-based index.

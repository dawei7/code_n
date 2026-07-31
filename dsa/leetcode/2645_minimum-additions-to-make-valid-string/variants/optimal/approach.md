## General

Inside one `"abc"` group, retained letters must appear in strictly increasing order: `a`, then `b`, then `c`. Missing letters can be inserted between them. Whenever the next existing character is less than or equal to the previous one, the two cannot belong to the same group, so a new `"abc"` copy is unavoidable.

Start with one group and count every such non-increasing adjacent transition. These boundaries are sufficient as well as necessary: within each resulting segment the letters are strictly increasing and can be completed to `"abc"` by inserting its missing letters. If there are $g$ groups, the shortest valid result has length $3g$. Since all $n$ original characters are retained, exactly $3g-n$ insertions are required.

## Complexity detail

The scan examines each adjacent pair once, giving $O(n)$ time for a word of length $n$. It stores only the group counter and the current pair, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Expected-character pointer:** Cycling a pointer through `a`, `b`, and `c` and counting mismatches also produces the optimum in $O(n)$ time, but requires careful completion of the final group.
- **Dynamic programming:** A position-and-expected-letter state can minimize insertions explicitly, but uses $O(n)$ states for a deterministic transition pattern that the boundary observation handles directly.
- **Repeated prefix recomputation:** Recounting groups for every prefix is correct but takes $O(n^2)$ time.
- A word already equal to one or more copies of `"abc"` needs no insertions.
- Equal adjacent letters must belong to different groups because each group contains each letter only once.
- A one-character word always needs the other two letters of its group.

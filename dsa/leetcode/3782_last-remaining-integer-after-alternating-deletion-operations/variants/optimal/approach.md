## General

After any sweep, the survivors remain in increasing order and their count becomes $\lceil m/2\rceil$, where $m$ is the number of integers before that sweep. Therefore, the actual sequence never has to be constructed: it is enough to locate the survivor within the smaller, renumbered sequence and map that position back through the sweep.

Number positions in the current increasing sequence from `1` through `m`. A left-to-right sweep retains positions `1, 3, 5, ...`, so reduced position `j` came from position `2 * j - 1`.

For a right-to-left sweep, the retained positions depend on parity. If `m` is odd, the rightmost position is odd and the survivors are again `1, 3, 5, ...` in increasing order, giving `2 * j - 1`. If `m` is even, the rightmost position is even and the retained positions are `2, 4, 6, ...`, giving `2 * j`.

Recursively find the final position among the $\lceil m/2\rceil$ survivors with the opposite sweep direction, then apply the appropriate mapping above. The base case is a one-element sequence, whose survivor position is `1`. Because every mapping identifies exactly the positions retained by its sweep, composing the mappings returns the sole original integer that survives every operation.

## Complexity detail

Let $N=n$. Each recursive call replaces the current length by $\lceil N/2\rceil$, so there are $O(\log N)$ calls. Every call performs constant work, for $O(\log N)$ time and $O(\log N)$ recursion-stack space.

## Alternatives and edge cases

- **Iterative affine mapping:** Track the first value and spacing of the current arithmetic progression while alternating directions. This can also achieve $O(\log N)$ time and $O(1)$ auxiliary space, but its parity updates are easier to misapply.
- **Explicit sequence simulation:** Building `[1, ..., n]` and slicing after each sweep reproduces the rules directly, but it requires $O(N)$ time and space and is impossible near the $10^{15}$ limit.
- **Singleton:** When `n = 1`, no sweep occurs and the result is immediately `1`.
- **Ceiling after deletion:** Each operation keeps the first number visited, so a sequence of odd length retains $\lceil m/2\rceil$ elements rather than $\lfloor m/2\rfloor$.
- **Right-to-left parity:** A right sweep retains odd positions in increasing order when `m` is odd, but even positions when `m` is even.
- **Direction alternation:** The first operation is always left-to-right, and the direction must flip after every sweep.

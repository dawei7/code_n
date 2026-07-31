## General

If the array sum is negative, transfers cannot help: every move preserves the total, whereas non-negative entries would require a non-negative total. Conversely, when no entry is negative, the requested state already holds and costs zero moves.

Suppose the unique negative entry is at index `d` and needs $D=-\texttt{balance[d]}$ units. A unit originating at index `i` can reach `d` along either direction of the circle. Its minimum transfer cost is therefore

$$
\min\bigl(\lvert i-d\rvert,\;N-\lvert i-d\rvert\bigr).
$$

Record every positive balance together with that circular distance, then sort the donors from nearest to farthest. Consume as much as possible from each donor until all $D$ units have been supplied.

Every supplied unit must cross at least the shortest-path distance from its origin to `d`. If a plan uses a farther available unit while leaving a nearer unit unused, exchanging those two choices cannot increase the delivered amount and strictly decreases or preserves the move count. Repeating that exchange yields the distance-ordered greedy choice, so the accumulated cost is minimal. A non-negative total guarantees that the donors contain at least $D$ units.

## Complexity detail

Let $N=\lvert\texttt{balance}\rvert$. Building the donor list takes $O(N)$ time, sorting it takes $O(N\log N)$ time, and the greedy scan takes $O(N)$ time. The donor list requires $O(N)$ auxiliary space.

## Alternatives and edge cases

- **Expand by circular distance:** Visit the one or two indices at each distance from the deficit instead of sorting. This improves the bound to $O(N)$ time and $O(1)$ auxiliary space but requires more careful handling of the single opposite index when $N$ is even.
- **Repeated nearest-donor search:** Rescanning all remaining donors before every transfer choice is correct but can take $O(N^2)$ time when many donors are needed.
- **Negative total:** Since a move preserves the sum, a negative total makes the target state impossible and requires `-1`.
- **No negative entry:** The answer is `0`; “at most one” does not guarantee that a deficit exists.
- **Circular boundary:** Indices `0` and `N - 1` are adjacent, so raw absolute index difference is not always the transfer distance.
- **Equal shortest paths:** For an index opposite the deficit in an even-length circle, either direction has the same cost and either is optimal.
- **Large balances:** The answer can exceed a 32-bit integer because a balance unit may travel many edges.

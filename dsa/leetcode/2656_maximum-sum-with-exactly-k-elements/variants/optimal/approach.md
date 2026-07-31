## General

Let $M$ be the largest original array value. Choosing a smaller value cannot improve the current score, and it inserts a value that remains smaller than the value obtained by choosing $M$ instead. Therefore an optimal first operation selects $M$.

After selecting $M$, the inserted value $M+1$ is strictly greater than every untouched original value. The same reasoning applies again, so every subsequent optimal operation selects the value just inserted. The `k` score contributions are consequently

$$
M, M+1, M+2, \ldots, M+k-1.
$$

Any strategy that first differs at some operation selects a value no larger than the greedy choice and creates a successor no larger than the greedy successor, so it cannot recover a higher later score. The maximum total is the arithmetic-series sum

$$
kM+\frac{k(k-1)}{2}.
$$

## Complexity detail

Let $n$ be the length of `nums`. Finding $M$ takes $O(n)$ time, after which the score uses a constant number of arithmetic operations. The algorithm uses $O(1)$ auxiliary space.

The benchmark scales `size` as both $n$ and `k`. A literal simulation that searches and replaces the current maximum on every operation completes all legal tiers but takes $O(nk)=O(n^2)$ time when both quantities scale together.

## Alternatives and edge cases

- **Literal array simulation:** Repeat the stated removal and insertion operation `k` times. This is correct but repeatedly finding or updating the maximum can cost $O(nk)$ time.
- **Max heap:** A heap simulates each choice in $O(\log n)$ time for $O(n+k\log n)$ total work, but the chosen value follows a closed-form progression after the first maximum is known.
- Equal maximum values do not change the answer; selecting any one of them creates the same strictly increasing sequence.
- When `k = 1`, the answer is simply the largest input value.
- A one-element array still follows the same progression because its replacement is available immediately.
- The operation must be performed exactly `k` times, even though all values and score contributions are positive.

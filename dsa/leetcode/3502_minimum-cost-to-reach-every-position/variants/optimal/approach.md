## General

To reach target position $i$, consider the first paid swap. It must be with somebody at a position $j \le i$: paying a person farther back than $i$ cannot move you far enough forward. Once you have paid `cost[j]` and moved to $j$, every position from $j+1$ through $i$ is behind you. The rules allow those later swaps for free, so the one payment is sufficient to reach $i$.

Conversely, every route to $i$ must include a paid swap with some person at or before $i$. Its total cost is therefore at least the cheapest such price. Combining necessity with the one-payment construction gives

$$
\texttt{answer[i]} = \min_{0 \le j \le i} \texttt{cost[j]}.
$$

Scan `cost` from left to right while keeping the smallest value seen so far. After processing index $i$, that value is exactly the displayed prefix minimum, so append it as the answer for position $i$. The maintained value can only stay unchanged or decrease, which also explains why the returned sequence is non-increasing.

## Complexity detail

Let $n=\lvert\texttt{cost}\rvert$. The scan examines each entry once, taking $O(n)$ time. The returned list occupies $O(n)$ space, while the running minimum uses $O(1)$ auxiliary space beyond that required output.

Producing $n$ answers already requires $\Omega(n)$ time, so the scan is asymptotically optimal. The benchmark varies $n$ and contrasts the single pass with a correct method that recomputes each prefix minimum from the beginning, which takes $\Theta(n^2)$ total time.

## Alternatives and edge cases

- **Recompute every prefix:** Evaluating `min(cost[0:i + 1])` independently is correct and simple, but repeated scans raise the total time to $O(n^2)$.
- **Prefix-minimum array library operation:** A cumulative-minimum primitive expresses the same $O(n)$ algorithm, but the explicit scan makes the invariant and auxiliary storage clear.
- **Single position:** The only reachable target costs exactly `cost[0]`.
- **First value is globally smallest:** Every answer equals `cost[0]` because that one paid swap makes all later positions reachable for free.
- **Strictly decreasing costs:** Each position introduces a cheaper direct swap, so every output equals the corresponding input value.
- **Repeated minima:** Encountering the current minimum again does not change the best cost, and all later positions retain it until a smaller value appears.
- **Positive costs:** No combination of multiple paid swaps can improve on the cheapest single eligible swap; extra payments only increase the total.

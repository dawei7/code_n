## General

Begin with the score obtained by assigning every task to technique 2. Switching task `i` to technique 1 changes that baseline by

$$
g_i = \texttt{technique1[i]} - \texttt{technique2[i]}.
$$

Every positive gain should be taken, even if the quota is already satisfied, because the requirement is **at least** $K$. A zero gain can count toward the quota at no cost. If at least $K$ gains are nonnegative, the optimum is therefore the technique-2 baseline plus the sum of all positive gains.

Otherwise, fewer than $K$ free or profitable switches exist. The remaining mandatory switches must use negative gains, and choosing anything other than the largest available gains would be suboptimal: replacing a selected smaller gain by an unselected larger gain can only increase the score. Maintain the largest $K$ gains in a min-heap while scanning the arrays. When the nonnegative count is below $K$, that heap contains every nonnegative gain plus precisely the least harmful negative gains needed to reach the quota.

## Complexity detail

Let $N$ be the number of tasks and $K = \texttt{k}$. Each gain causes at most one heap operation on a heap of size $K$, so the running time is $O(N\log(K+1))$; writing $K+1$ keeps the bound meaningful when $K=0$. The heap stores at most $K$ gains and therefore uses $O(K)$ auxiliary space.

## Alternatives and edge cases

- **Sort every gain:** Sorting differences in descending order and taking the first $K$ plus every later positive gain is straightforward, but costs $O(N\log N)$ time and $O(N)$ storage in the usual implementation.
- **Repeatedly choose the best remaining gain:** Selecting one maximum at a time is correct but can rescan the remaining gains $K$ times and approach $O(NK)$ work.
- **Exactly versus at least:** Stopping after exactly $K$ selections loses points whenever an unselected gain is positive.
- **Zero quota:** When `k = 0`, select technique 1 only for positive gains; no mandatory heap contribution is needed.
- **Full quota:** When `k = n`, every task must use technique 1, so the result is `sum(technique1)`.
- **Equal scores:** A zero gain may be treated as technique 1, allowing it to satisfy the quota without changing the total.
- **Negative mandatory gains:** When too few tasks favor technique 1, choose the negative gains closest to zero because they sacrifice the fewest points.
- **Large total:** The answer can reach $10^{10}$, so fixed-width implementations need a 64-bit integer.

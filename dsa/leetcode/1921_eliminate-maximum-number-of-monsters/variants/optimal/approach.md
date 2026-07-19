## General
**Convert arrival times into integer firing deadlines**

Monster `i` reaches the city after $\texttt{dist[i]}/\texttt{speed[i]}$ minutes. A shot at integer minute $m$ is safe only when

$$
m < \frac{\texttt{dist[i]}}{\texttt{speed[i]}}.
$$

Its latest safe integer firing minute is therefore `((dist[i] - 1) // speed[i])`. This integer formulation handles both fractional arrivals and the rule that an exact-minute arrival happens before a shot.

**Schedule the earliest deadlines first**

Sort all latest-safe minutes. Try to shoot the monster at sorted position `minute` at that same minute. If its deadline is smaller than `minute`, it has already arrived and the game ends; return `minute`, the number previously eliminated.

This order is optimal by exchange. If a schedule shoots a later-deadline monster before an earlier-deadline one, swapping them cannot make the later monster late and can only help the urgent monster. Repeating such swaps produces sorted deadline order without reducing the number of feasible shots. Consequently, the first failed sorted deadline proves that no schedule can eliminate more monsters.

## Complexity detail
Computing $N$ integer deadlines takes $O(N)$ time. Sorting them costs $O(N\log N)$ time, and the final feasibility scan is $O(N)$. The deadline array occupies $O(N)$ space.

## Alternatives and edge cases
- **Repeatedly choose the next arrival:** Scanning all remaining monsters before every shot implements the same greedy choice in $O(N^2)$ time.
- **Sort floating-point arrival times:** This can work but introduces unnecessary precision concerns at exact integer boundaries.
- **Use floor division without subtracting one:** `dist // speed` is wrong when the quotient is exact because arrival at that minute prevents firing.
- **Several deadline-zero monsters:** Only one can be destroyed at minute zero.
- **Tied later deadlines:** At most one monster can be assigned to each minute, so a tie may still cause failure.
- **All deadlines feasible:** Return $N$ after the scan completes.

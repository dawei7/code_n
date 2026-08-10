## General

**Define a day-and-destination state.** `f[i][j]` is the maximum score after completing exactly $i$ days and ending in city $j$. The answer requires exactly $k$ days, so the final result is the maximum entry in row `f[k]`.

Before any day, the tourist may choose any starting city for free. The assignment `f[0] = [0] * n` represents every possible start simultaneously: score zero is reachable in every city.

All other cells begin at negative infinity so an unreachable state cannot win a maximum. In this complete-city setting every state becomes reachable after one day, but the sentinel makes the recurrence logically safe.

**Enumerate the previous city.** To compute `f[i][j]`, the source tries every city `h` where the tourist could have ended after day $i-1$.

If `j == h`, the tourist stays in the same city on zero-based day `i - 1` and earns `stayScore[i - 1][j]`. If `j != h`, the tourist travels from $h$ to $j$ and earns `travelScore[h][j]`.

The transition is therefore

$$
f[i][j]=
\max_h\left(
f[i-1][h]+
\begin{cases}
\texttt{stayScore}[i-1][j],&h=j,\\
\texttt{travelScore}[h][j],&h\ne j.
\end{cases}
\right).
$$

The ternary expression in the source implements these mutually exclusive choices. It does not use `travelScore[j][j]` for a stay, even though that diagonal is zero, because staying has its own day-dependent reward.

**Why the state contains all necessary history.** Future rewards depend on the day and current city only. The route used to reach that city affects the accumulated score but not legal next moves or reward tables. Retaining only the best score for each ending city is therefore safe: any lower-scoring route to the same state can never outperform it under identical future options.
Row zero correctly represents all free starting choices. Assume row $i-1$ contains exact best scores. Any $i$-day itinerary ending at $j$ has one previous city $h$ and performs exactly the stay or travel action represented by the transition. Its prefix score is at most `f[i-1][h]`, so the recurrence is at least as good as every itinerary. Conversely, every transition combines a real optimal prefix with one legal action, so it constructs a legal itinerary. The computed maximum is exact.

After $k$ days, the tourist may finish anywhere. `max(f[k])` chooses the best final city without adding an unrequested return trip.

**Example interpretation.** With one day, every `f[1][j]` compares starting in $j$ and staying for `stayScore[0][j]` against starting in any other city $h$ and traveling for `travelScore[h][j]`. This correctly includes choosing a start specifically to exploit a day-zero travel edge.

**The source is not rolling-space.** The manifest summary says rolling dynamic programming with $O(n)$ space, but the code allocates all `k + 1` rows before filling them. Only the previous row is needed, so compression is possible, but the protected implementation's actual auxiliary table is $O(kn)$.

## Complexity detail

There are $k$ non-base days, $n$ destination cities, and $n$ previous cities examined per destination. Total time is $O(kn^2)$, matching the manifest.

The table contains $(k+1)n$ numeric entries, so exact auxiliary space is $O(kn)$, not the listed $O(n)$. Loop variables are constant-size. A two-row or one-new-row implementation would achieve $O(n)$ space.

## Alternatives and edge cases

- **Rolling two rows:** Keep only `previous` and `current` because transitions read row $i-1$ only. This preserves time and realizes the manifest's $O(n)$ space claim.
- **Memoized recursion:** It expresses the same state graph but adds call overhead and still needs $O(kn)$ cached states.
- **Greedy best reward each day:** It fails because moving to a city changes which travel rewards are available on later days.
- **One city:** Every action is a stay, and the answer is the sum of its $k$ daily stay scores.
- **One day:** Free starting-city choice is correctly represented by all-zero base states.
- **Travel to same city:** The source deliberately treats `h == j` as staying and uses the stay score, not diagonal travel score.
- **Finish anywhere:** Taking the maximum final row is necessary; fixing one destination could lose the optimum.
- **All travel scores zero:** Staying may dominate, but moving can still position the tourist for later stay rewards, which DP evaluates.
- **Day-dependent stay rewards:** The day index is why a single static best-city calculation is insufficient.
- **Negative-infinity sentinel:** It prevents impossible prefixes from contributing; the snippet assumes `inf` is imported.
- **Nonnegative rewards:** Scores do not require special overflow handling in Python, though totals can reach $100k$.
- **Full-table inspection:** Keeping every row could help reconstruct or analyze intermediate scores, but the method returns only a total and does not use old rows.
- **Manifest discrepancy:** Time is correct, while exact source space is $O(kn)$ rather than rolling $O(n)$.
- **Starting city:** Initializing every base-state city to zero is what permits any free start; initializing only one city would silently restrict the problem.

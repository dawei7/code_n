## General

The only information from earlier days that affects the next choice is the current city and the best score accumulated there. Let `best[city]` be the maximum score obtainable immediately before the current day while located in `city`. Initially every entry is zero because any city may be selected as the starting point without spending a day or earning points.

For a fixed day and destination city, there are exactly two ways to finish that day at the destination. The tourist can already be there and stay, or can begin the day in a different source city and travel:

$$
\texttt{next\_best[dest]}
=
\max\left(
\texttt{best[dest]}+\texttt{stayScore[day][dest]},
\max_{\texttt{source}\ne\texttt{dest}}
\left(\texttt{best[source]}+\texttt{travelScore[source][dest]}\right)
\right).
$$

Evaluate this recurrence for every destination, using only the unchanged previous-day array. This separation is essential: updating `best` in place could combine two actions during one day. Once all destinations are complete, replace the previous layer with the new layer.

The state is correct by induction over the days. The initial layer represents every permitted starting city with score zero. Assuming each previous entry is the best score for its city, the recurrence considers every legal final action leading to a destination and chooses the best predecessor. It therefore produces the best score for every city after the current day. After exactly $k$ layers, the maximum entry covers every possible final city and is the required journey score.

## Complexity detail

There are $k$ days and $n$ destination cities per day. Each destination examines all $n$ possible source cities, so the running time is $O(kn^2)$. The two dynamic-programming layers each contain $n$ scores, giving $O(n)$ auxiliary space. The input matrices are not counted as auxiliary storage.

## Alternatives and edge cases

- **Full dynamic-programming table:** Storing every day-city state uses the same $O(kn^2)$ time but $O(kn)$ space; older layers are unnecessary once the next layer is complete.
- **Enumerate complete itineraries:** Exploring every stay-or-travel sequence grows exponentially with $k$ and repeatedly solves identical day-and-city suffixes.
- **Update one array in place:** This can use a score earned earlier on the same day as another transition and therefore model multiple actions in one day.
- **Travel versus stay:** A move earns only `travelScore[source][destination]`; adding `stayScore[day][destination]` to the same action overcounts.
- **Any starting city:** Initializing every city to zero includes both a day-$0$ stay and a day-$0$ trip from any chosen origin.
- **One city:** Travel is impossible, so the answer is the sum of that city's $k$ stay scores.
- **Directed scores:** `travelScore[a][b]` and `travelScore[b][a]` may differ and must be evaluated separately.

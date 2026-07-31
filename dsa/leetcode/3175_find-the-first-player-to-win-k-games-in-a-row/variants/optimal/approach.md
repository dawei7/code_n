## General

The player at the front is the current champion. Every game pits that champion against the next player who has not yet challenged them in the original order. If the champion has the larger skill, the champion remains at the front and gains one consecutive win. Otherwise, the challenger becomes the champion, and their streak starts at one because they have just won the takeover game.

Track the champion's original index and consecutive-win count while scanning `skills[1:]`. After processing index $i$, the tracked champion is the most skilled player among indices $0$ through $i$. This follows because each challenger either loses to that prefix maximum or replaces it with a larger value. At the same time, the counter is exactly the number of consecutive games won by that champion since their most recent takeover.

If the counter reaches $k$, that player is the first competition winner and can be returned immediately. If the scan finishes first, the tracked champion is the global maximum. No player can ever defeat that champion, so they will remain at the front and eventually accumulate any still-required number of wins. Returning their index therefore also handles values of $k$ far larger than $n$ without simulating repeated queue cycles.

## Complexity detail

Let $n$ be the number of players. Each challenger is examined once, so the running time is $O(n)$. The scan keeps only two integers in addition to the input, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Literal queue simulation:** A deque can reproduce each game directly, but it may require up to $k$ games after the maximum reaches the front; because $k$ can be $10^9$, stopping only when the streak reaches $k$ is not viable.
- **Repeated prefix-maximum search:** Recomputing the best player seen so far gives the same champion but costs $O(n^2)$ time instead of maintaining that state incrementally.
- **Required streak of one:** The winner of the very first comparison must be returned, whether that player began first or second in the queue.
- **Winner before the global maximum appears:** An early champion can reach $k$ before a stronger unprocessed player ever competes, so returning the global maximum unconditionally is incorrect.
- **Huge required streak:** Once the global maximum is the champion, future queue order is irrelevant because that player cannot lose.

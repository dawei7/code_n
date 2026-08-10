## General

**View the front element as the current champion**

In every round, the element at the front competes against the next element. The larger one stays in front, while the smaller one moves behind all still-waiting players.

Call the front winner `mx`. Initially `mx = arr[0]`. The stored solution then visits the original remaining elements in order through `arr[1:]`. Each visited `x` is the next challenger that has not yet faced the current champion.

The important simplification is that a loser need not actually be appended to a queue. Before the global maximum first becomes champion, every element that loses moves behind all unprocessed original challengers. It cannot return to the front before those challengers have played. Once the global maximum becomes champion, it can never lose, so delayed losers can never change the eventual winner.

Therefore, a single left-to-right pass reproduces every relevant championship change without physically rotating the array.

**Maintain the consecutive-win count**

`cnt` records the current champion's consecutive victories.

If `mx < x`, the challenger is larger and wins this round. It becomes the new champion through `mx = x`. Its streak is exactly one because the just-completed round is its first consecutive win, so the code assigns `cnt = 1`.

Otherwise `mx > x` because all values are distinct. The champion wins again and `cnt += 1` extends its streak.

There is no equality branch to define because the distinct-values guarantee prevents a tied round.

**Why breaking at k victories is correct**

After each simulated relevant round, the code checks `cnt == k`. At that moment `mx` has won exactly $k$ consecutive rounds, so the game ends under the stated rule. Breaking the loop and returning `mx` yields the actual winner.

The check uses equality rather than greater-than-or-equal because `cnt` increases by one per round. It cannot jump over $k$.

For `k = 1`, the first comparison immediately identifies the winner: either the initial champion defeats `arr[1]`, or that challenger replaces it. The count becomes one and the loop stops.

**Why returning after the pass is also valid**

The loop may finish before `cnt` reaches a very large `k`. By then, every original array element has been compared along the champion chain. The maintained `mx` is consequently the maximum element of the entire array.

The global maximum can never lose a later round because every opponent is smaller. It will keep accumulating consecutive wins until it reaches any finite required $k$. There is no need to simulate those repeated rotations. Returning `mx` after the loop predicts the guaranteed eventual winner.

This is why the running time does not depend on $k$, even though $k$ may be as large as one billion.

**Champion invariant**

After processing `arr[1:]` through some challenger position $i$:

- `mx` is the maximum value among `arr[0]` through `arr[i]`.
- `cnt` is the number of consecutive relevant rounds won by the current `mx` since it most recently became champion.
- Every processed loser is queued behind all not-yet-processed original challengers and cannot affect the champion before those challengers are considered.

Initially the first property holds for the one-element prefix, and the streak is zero because no round has occurred. Comparing the next challenger preserves the maximum-prefix property: the larger of old `mx` and `x` becomes the new `mx`. The two count updates exactly match whether the champion stayed or changed.

**Tracing the first example**

Start with champion two and streak zero. Challenger one loses, so two's streak becomes one. Challenger three wins, becomes champion, and has streak one. Challenger five then replaces three with streak one.

Challenger four loses to five, raising five's streak to two. Since `k = 2`, the pass stops and returns five. The elements that previously lost would be at the back of a literal queue, but none needs to be moved in memory.

**Why the algorithm is correct**

The invariant proves that the pass simulates the same winner and streak as the game through every first encounter with an original challenger. If the streak reaches $k$, the returned champion satisfies the stopping rule at the same round as the game.

If it does not, completing the pass makes `mx` the global maximum. That value is unbeatable and must eventually achieve $k$ consecutive wins. These two exhaustive cases prove the returned value is always the game's winner.

## Complexity detail

Let $N$ be the array length. At most $N-1$ challengers are examined, each with constant work, so time is $O(N)$. Early termination can use fewer iterations, but the worst case still scans the array.

The manifest reports $O(1)$ auxiliary space for the no-queue idea. However, the exact Python source iterates over `arr[1:]`, and a list slice creates a new list containing $N-1$ references. Therefore this stored implementation uses $O(N)$ auxiliary space in Python.

Replacing the slice with an index loop such as iterating from one through $N-1$, or with an iterator that does not copy, would realize the manifest's $O(1)$ auxiliary-space bound without changing the algorithm. The scalar variables `mx`, `cnt`, and `x` themselves use constant space.

## Alternatives and edge cases

- **Literal deque simulation:** It mirrors the rules directly but uses $O(N)$ queue space; stopping when the maximum becomes champion is necessary to avoid dependence on huge $k$.
- **Rotate a Python list:** Removing and appending can make rounds expensive because front deletion shifts elements.
- **Index-based champion pass:** It is algorithmically identical and avoids the linear list slice, achieving true $O(1)$ auxiliary space.
- **k equals one:** The winner of the first comparison is returned immediately.
- **k larger than the array length:** The pass reaches the global maximum and returns it without simulating all required future wins.
- **Initial element is maximum:** It defeats every challenger and is returned either when its streak reaches $k$ or when the pass ends.
- **Maximum appears later:** Every earlier champion eventually loses when the scan reaches that maximum.
- **Strictly increasing array:** Each challenger becomes the new champion with streak one; the final element is the global maximum.
- **Strictly decreasing array:** The first element remains champion throughout.
- **Distinctness:** It removes the need for a tie rule and makes the `else` branch a strict champion victory.
- **Count reset:** A new champion starts at one, not zero, because becoming champion happened by winning the current round.
- **No explicit maximum call:** Completing the running comparisons computes the maximum naturally, so a separate `max(arr)` pass is unnecessary.
- **Guaranteed winner:** Once the maximum is champion, repeated victories ensure termination for every positive finite $k$.

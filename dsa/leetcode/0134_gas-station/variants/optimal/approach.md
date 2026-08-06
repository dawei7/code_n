## General
**Total net fuel decides whether any circuit can exist**

At station $i$, define the net change as `gas[i] - cost[i]`. A complete circuit visits every station once, so its final tank balance is the sum of all net changes regardless of the chosen start. A negative total makes every start impossible.

**A failed candidate eliminates the whole interval just scanned**

Scan from left to right while `tank` holds the accumulated net fuel since `start`. Suppose it first becomes negative at station $i$. Every proper prefix from `start` through a station before $i$ had nonnegative balance; beginning at any such later station would discard that nonnegative prefix and therefore leave no more fuel upon reaching $i$. Thus every start from `start` through $i$ is impossible, and the next possible candidate is $i + 1$.

The candidate resets `tank` to zero after such a failure but keeps `total`, because the discarded deficit still determines whether the entire circuit has enough fuel. The candidate implementation performs this update directly while enumerating paired gas and cost values.

**The final surviving candidate completes the wraparound segment**

After the scan, every earlier start has been eliminated and the local balance from the final `start` through station $n - 1$ never becomes negative. If `total` is nonnegative, the surplus on that suffix is large enough to absorb the net balance of the skipped prefix, so the candidate can also traverse the wraparound segment. Therefore return `start` exactly when `total >= 0`; otherwise return `-1`.

## Complexity detail
Each of the $n$ stations is processed once, giving $O(n)$ time. `total`, `tank`, `start`, and the loop values are scalar state, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Simulate from every station:** is straightforward but can require $O(n^2)$ time.
- **Choose the station with the most gas:** ignores outgoing costs and accumulated deficits.
- **Store all prefix sums:** can recover a valid rotation but uses unnecessary $O(n)$ space.
- A single station succeeds exactly when its gas covers its outgoing cost.
- Zero total gain can still produce a valid circuit; only a negative total rules every start out.
- The platform guarantees that a feasible start is unique, so returning the final noneliminated candidate is unambiguous.

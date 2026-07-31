## General

The number of chairs currently occupied changes by exactly one at every event: add one for `E` and subtract one for `L`. Track that occupancy while scanning the string, and after every entry update the largest value seen.

For any prefix of events, the running value equals the number of people in the room after that prefix because it begins at zero and applies the stated effect of every event exactly once. A room with fewer chairs than the maximum running value must fail at the entry that first reaches that occupancy. Conversely, a room with exactly that many chairs always has enough capacity because the occupancy never exceeds the recorded maximum. Therefore, this maximum is precisely the minimum sufficient number of chairs.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. The scan processes each event once, so the time complexity is $O(n)$. Only the current occupancy and the maximum occupancy are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Prefix-sum construction:** Convert entries to $+1$ and exits to $-1$, build all prefix sums, and take their maximum. This expresses the same invariant but uses $O(n)$ extra space unnecessarily.
- **Try increasing chair counts:** Simulate the sequence repeatedly with one chair, then two, and so on until a capacity succeeds. It is correct but can require $O(n^2)$ time.
- **All entries:** With no departures, occupancy rises at every second and the answer equals the full string length.
- **Alternating events:** A sequence such as `ELEL` reuses one chair, so its answer is one.
- **Room not empty at the end:** Validity prevents impossible exits but does not require a final occupancy of zero.
- **Departures:** An `L` reduces current occupancy but never reduces the maximum already observed.

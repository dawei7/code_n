## General

**Reduce the game after the first elimination**

This is the Josephus problem. After the first friend is removed, the remaining friends still form the same kind of circular game with one fewer participant and the same step size $k$.

The only complication is translating the winner's position from that smaller circle back to the original numbering.

**Base case**

With one friend, that friend wins. The protected recursive function returns one for `n == 1`.

This is a one-based result because the problem labels friends from 1.

**How the smaller circle is renumbered**

In a circle of $n$ friends, counting from friend 1 removes the $k$th counted position, wrapping as needed.

The next round begins immediately clockwise from the removed friend. If we conceptually renumber that next friend as position 1 of a new circle, the remaining game is exactly the problem for $n-1$ friends.

Suppose the recursive call returns one-based winner position $p$ in this rotated smaller circle. Mapping it back to the original circle shifts by $k$ positions with wraparound.

The exact source computes

`ans = (k + p) % n`

and returns `n` when that remainder is zero, otherwise `ans`.

**Derive the one-based recurrence carefully**

The standard zero-based recurrence is

$$
f(n)=(f(n-1)+k)\bmod n,
$$

with $f(1)=0$.

If the recursive one-based result is $p=f(n-1)+1$, then the new one-based result is

$$
((p-1+k)\bmod n)+1.
$$

For nonzero remainders, this equals $(p+k)\bmod n$. When $(p+k)\bmod n=0$, the one-based label must be $n$, not zero. That is exactly the source's conditional return.

**Following the first example from small circles upward**

For `n = 5` and `k = 2`:

- one friend has winner 1;
- for two friends, `(2 + 1) % 2 = 1`, so winner is 1;
- for three, `(2 + 1) % 3 = 0`, mapped to friend 3;
- for four, `(2 + 3) % 4 = 1`;
- for five, `(2 + 1) % 5 = 3`.

The returned winner is friend 3, matching direct simulation.

**Why the recurrence represents repeated counting**

Removing one participant and rotating the next participant to local position 1 preserves clockwise order among all survivors. All future eliminations depend only on that order, the current start, and $k$, not on original labels.

The recursive subproblem therefore finds the correct survivor in local coordinates. The modular shift restores the original label. Applying this reasoning inductively through every circle size produces the true final friend.

**Why counting may wrap many times without extra work**

Modulo $n$ handles any $k$, including values larger than the current remaining circle size in a generalized setting. The source constraints give $k\leq$ original $n$, but after eliminations $k$ may exceed the smaller size. The same formula still models repeated wraparound.

**Why no circle data structure is needed**

Simulation stores participants and removes one at a time. The recurrence summarizes the effect of all eliminations using only the winner index for the smaller size.

The exact source uses recursion to build from $n$ down to one and translate results while returning.

**Why the result is correct**

The base case is exact. Assume the recursive result for $n-1$ correctly identifies the winner in the rotated remaining circle. The first elimination of the $n$-friend game leaves precisely that subproblem, and the source's modular formula maps its winner back to the original one-based labels.

By induction, the returned friend wins the full game.

## Complexity detail

The method makes one recursive call for every circle size from $n$ down to one. Each level performs constant arithmetic, so time complexity is $O(n)$, matching the manifest.

However, the exact protected source retains $n$ recursive stack frames, so its auxiliary space is $O(n)$, not the manifest's stated $O(1)$. The iterative form that starts with zero and applies `winner = (winner + k) % size` for sizes 2 through $n$ achieves $O(1)$ space.

With $n\leq500$, recursion depth remains below Python's typical default limit, though iteration is more robust for larger variants.

## Alternatives and edge cases

- **Iterative Josephus recurrence:** It attains the manifest's $O(n)$ time and $O(1)$ space without changing the mathematics.
- **List simulation:** Repeated middle deletion can cost $O(n^2)$ time and requires $O(n)$ storage.
- **Queue rotation:** It models the rules clearly but takes $O(nk)$ time and $O(n)$ space.
- **`n = 1`:** The sole friend wins immediately.
- **`k = 1`:** Friends leave in current order, so friend $n$ wins.
- **Remainder zero:** It represents one-based label $n$, which the explicit conditional restores.
- **Large `k` relative to remaining size:** Modulo handles multiple wraps.
- **One-based labels:** The zero remainder conversion prevents returning invalid friend zero.
- **Recursive depth:** Safe under the current constraint but not constant space.
- **No elimination-order storage:** Only the final survivor is required.
- **Clockwise rotation:** Renumbering begins at the friend after the eliminated one, which creates the $+k$ shift.
- **Original start friend:** The top-level numbering already begins at friend 1.
- **Deterministic game:** No tie or choice affects the recurrence.
- **Input scalars:** The function mutates no external state.

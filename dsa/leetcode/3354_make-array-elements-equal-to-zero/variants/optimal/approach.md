## General

**Replace the movement simulation with mass on each side.** A valid starting position must contain zero. For such a position, let $L$ be the sum of all values strictly to its left and $R$ the sum strictly to its right. Because the starting value itself is zero, the total array sum is $S=L+R$.

Each unit of value represents one decrement the moving process must eventually perform. The exact locations within one side affect travel distance, but not the order in which the two sides receive decrements.

**Positive encounters force alternating sides.** Whenever the cursor reaches a positive element, it subtracts one and reverses direction. It then travels across any intervening zeros until it finds positive mass on the opposite side or leaves the array. Therefore successful decrements alternate between the right side and the left side.

If the initial direction is right, the decrement sequence has the form

$$
R,L,R,L,\ldots
$$

where these symbols identify the side, not a particular index. A process beginning left has the symmetric sequence $L,R,L,R,\ldots$.

Zeros do not consume a turn and do not cause reversal. They only let the cursor continue in its current direction, so multiple zero positions can be assessed using the same left/right sums.

**Derive the valid balance conditions.** When $L=R$, an alternating sequence can remove all mass regardless of which side goes first. The final decrement occurs on the opposite side from the first, after which the cursor crosses the now-zero array and exits. Both initial directions are valid, so this starting index contributes two selections.

When $R=L+1$, only starting to the right works. The right side receives the first and last decrements, so it may contain exactly one more unit. Starting left would exhaust the left side first and eventually exit while one right-side unit remains. Symmetrically, when $L=R+1$, only the initial left direction works.

If $\lvert L-R\rvert>1$, strict alternation cannot consume the heavier side's extra units. After the lighter side has no positive value left, the next reversal toward it carries the cursor out of the array, leaving positive mass behind. Neither direction is valid.

Thus a zero position contributes:

- two when $L=R$;
- one when $\lvert L-R\rvert=1$;
- zero otherwise.

**Compute every left sum in one pass.** The source first calculates `s = sum(nums)`. Variable `l` begins at zero and equals the sum of positive values strictly before the current scan position. When the current `x` is positive, `l += x` prepares the invariant for later positions.

When `x == 0`, the current left sum is `l` and the right sum is `s - l`. Equality $L=R$ is equivalent to

$$
2L=S,
$$

which is checked by `l * 2 == s`. A one-unit imbalance is equivalent to $\lvert2L-S\rvert=1$, checked by `abs(l * 2 - s) == 1`.

The equal case adds two before the code considers the one-difference case. These conditions cannot overlap, so the `elif` chain exactly implements the three outcomes.

**Trace a useful balance.** Suppose a zero has left sum four and right sum five. Starting right yields decrement sides $R,L,R,L,R,L,R,L,R$: five right decrements and four left decrements, removing all mass. Starting left would require a fifth left decrement that does not exist; the cursor instead leaves while one right unit remains. The source sees $\lvert2L-S\rvert=\lvert8-9\rvert=1$ and adds one.

If both sides sum to three, either direction gives three decrements per side, so the position contributes two. Importantly, the individual distributions could be `[3]` on one side and `[1,0,2]` on the other; the repeated travel still alternates total decrements by side, so only sums matter.

**Why the formula exactly replaces simulation.** Every decrement forces a reversal, making alternation unavoidable. The balance conditions are therefore necessary. They are also sufficient: while a side has remaining positive mass, moving toward that side eventually reaches some positive entry, decrements it, and reverses. With equal masses or a one-unit advantage on the starting side, the alternating schedule consumes both totals exactly before exiting.

## Complexity detail

Let $n$ be `len(nums)`. Computing `s` takes $O(n)$ time, and the second pass takes another $O(n)$ time. The total is $O(n)$.

Only `s`, `ans`, `l`, and the current value are stored, so auxiliary space is $O(1)$. The algorithm does not decrement or otherwise mutate `nums`.

## Alternatives and edge cases

- **Direct simulation:** Copy the array and simulate both directions from every zero. It follows the statement literally but can require $O(n^2m)$ time when values are as large as $m$.
- **Prefix-sum array:** It provides $L$ and $R$ in constant time per zero but spends $O(n)$ space; the running sum is sufficient.
- **Equal side sums:** Both starting directions are distinct valid selections and contribute two.
- **Right side heavier by one:** Only starting right is valid.
- **Left side heavier by one:** Only starting left is valid.
- **Imbalance greater than one:** Alternation guarantees failure in both directions.
- **All values zero:** Every index is a legal start and both directions immediately leave an already-zero array, so the answer is $2n$.
- **Zero at the first index:** Its left sum is zero; it is valid only when the right sum is zero or one.
- **Zero at the last index:** The symmetric right sum is zero.
- **Consecutive zeros:** Each zero is a different starting-position choice and must be counted separately, even though their side sums may match.
- **Positive values only affect sums:** Their exact distances from the start change the path length but not validity.
- **Nonnegative constraint:** The mass interpretation relies on values never being negative.
- **Input preservation:** Using arithmetic conditions avoids the copies and mutations required by simulation.
- **At least one zero:** The contract guarantees a possible starting position to inspect, though it does not guarantee any valid selection.

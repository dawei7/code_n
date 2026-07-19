## General
**Reduce every position to its parity.** A free move changes a position by two, so repeated free moves can carry a chip to any other position of the same parity. They can never change an odd position into an even one or vice versa. Thus the exact coordinate and the distance between coordinates do not affect the paid cost.

**Choose which parity receives all chips.** If the common destination is even, every even-positioned chip arrives for free and every odd-positioned chip needs exactly one paid one-unit move before free moves finish the journey. The total is therefore the number of odd chips. An odd destination symmetrically costs the number of even chips, so return the smaller count.

**Why no cheaper arrangement exists.** Every chip whose starting parity differs from the destination's parity must cross between parity classes at least once, and only a one-unit move can do that, establishing the stated lower bound. One such paid move per mismatched chip followed by free two-unit moves attains the bound. Comparing the only two destination parities is consequently sufficient for the global minimum.

## Complexity detail
One pass counts the $n$ chip parities, taking $O(n)$ time. Only the odd and even counts are stored, so the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Evaluate every occupied destination:** Computing the cost for each chip position is correct but repeats the parity count and takes $O(n^2)$ time.
- **Simulate individual moves:** Distances can be as large as $10^9$, so step-by-step movement performs unnecessary work and hides the parity invariant.
- **All positions share a parity:** Every chip can reach one of the occupied positions for free, so the answer is `0` even when the coordinates are far apart.
- **One chip:** It is already gathered and costs `0`.
- **Duplicate positions:** Each list entry is a separate chip and must contribute independently to its parity count.
- **Equal parity counts:** Either an odd or even destination attains the same minimum.

## General

Positions where `s[i] == t[i]` need no repair. Split the mismatches into two orientations: let $a$ count positions with `(s[i], t[i]) = ('0', '1')`, and let $b$ count positions with `(s[i], t[i]) = ('1', '0')`.

One mismatch of each orientation can be repaired together. Swapping their two positions within either string fixes both for `swapCost`; flipping one bit at each position costs `2 * flipCost`. Thus each opposite-orientation pair costs

$$
P = \min(\texttt{swapCost}, 2\,\texttt{flipCost}).
$$

Pair all $min(a,b)$ such mismatches. This is never worse than reserving them for same-orientation pairs: the same-orientation repair cost defined below cannot be smaller than $P$ because `crossCost` is positive.

The remaining $lvert a-b\rvert$ mismatches all have one orientation. For any two of them, cross-swap one position to reverse its orientation, then use an ordinary within-string swap to fix the now-opposite pair. This costs `crossCost + swapCost`. The alternative is to flip one bit at each position, so a same-orientation pair costs

$$
Q = \min(\texttt{crossCost}+\texttt{swapCost}, 2\,\texttt{flipCost}).
$$

After taking as many such pairs as possible, an odd final mismatch must be repaired by one flip. A within-string swap can only move a lone mismatch, and a cross-swap only reverses its orientation, so neither can eliminate it by itself. The resulting formula is

$$
\min(a,b)P
+ \left\lfloor\frac{\lvert a-b\rvert}{2}\right\rfloor Q
+ (\lvert a-b\rvert \bmod 2)\,\texttt{flipCost}.
$$

These choices provide a legal construction attaining the formula. The pair classifications also give matching lower bounds for every mismatch: opposite pairs cannot be eliminated more cheaply than $P$, same-orientation pairs cannot be eliminated more cheaply than $Q$, and a lone remainder requires a flip. Therefore the total is minimal.

## Complexity detail

Let $N$ be the common string length. One simultaneous scan counts the two mismatch orientations in $O(N)$ time. The final arithmetic uses constant time and no data structure that grows with the input, so the auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over string states:** Exploring possible intermediate strings models the operations directly but has an exponential state space and ignores that only mismatch orientations matter.
- **Always use swaps:** An ordinary swap is useful for opposite mismatches, but two flips can be cheaper; same-orientation mismatches additionally require a cross-swap before an ordinary swap can fix the pair.
- **Always flip mismatches:** This is correct but can overpay when `swapCost` or `crossCost + swapCost` is smaller than two flips.
- **Already equal strings:** Both mismatch counts are zero, so the formula returns zero without performing an operation.
- **One remaining mismatch:** No swap alone can remove it; exactly one bit flip is necessary.
- **Large costs:** The answer can exceed 32-bit range, so implementations should use an integer type capable of holding values on the order of $N\cdot10^9$.

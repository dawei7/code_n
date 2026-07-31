## General

**Handle the already-complete circle.** When `n = 1`, the uncut circle is the required single slice, so the minimum is zero rather than one radius mark.

**Pair opposite slices when possible.** A diameter is one straight cut whose two rays point in opposite directions. It creates two sector boundaries at once. If `n` is even, the desired boundaries occur in opposite pairs, so $n / 2$ evenly spaced diameter cuts create all $n$ slices.

That count is minimal because one valid cut contributes at most two required radial boundaries, making $n / 2$ a lower bound that the construction attains.

**Use individual radii for an odd count.** For odd `n` greater than one, the boundaries cannot all be paired with diametrically opposite boundaries: pairing would produce an even number of sectors. Each boundary must therefore be placed with a radius cut, requiring `n` cuts. Equally spacing those radii achieves `n` equal slices.

## Complexity detail

The algorithm performs a fixed number of comparisons, a parity check, and at most one integer division. Its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$.

## Alternatives and edge cases

- **Always return `n / 2`:** This works only for even `n`; an odd number of equal sectors cannot be assembled from opposite boundary pairs.
- **Always return `n`:** This produces valid radial boundaries for `n > 1` but uses twice as many cuts as necessary when `n` is even.
- **One requested slice:** No cut is required; applying the odd-number rule without this exception incorrectly returns one.
- **Two requested slices:** A single diameter is sufficient and establishes the smallest nonzero answer.
- **Integer division:** Divide only after confirming that `n` is even, so `n // 2` represents an exact count of diameters.

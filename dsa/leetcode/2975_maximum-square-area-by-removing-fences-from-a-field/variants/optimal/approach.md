## General

Removing fences allows a square side to span across any number of former
strips. Consequently, every distance between two horizontal fence coordinates
is a realizable vertical side length, and every distance between two vertical
fence coordinates is a realizable horizontal side length. Include the
unremovable boundaries `1`, `m` and `1`, `n` before computing these distances.

**Represent attainable lengths as sets.** Enumerate all pairs of horizontal
coordinates and insert their positive differences into one set. Do the same
for vertical coordinates. A length can be the side of a square exactly when it
belongs to both sets: its two horizontal fences and two vertical fences bound
the square, and every internal fence between them may be removed.

Choose the largest common length because area grows with the positive side
length. Square it and apply the modulus only to the returned area. If the sets
have no common member, no choice of removals can make equal side lengths, so
return `-1`.

## Complexity detail

With $H$ horizontal and $V$ vertical coordinates including boundaries, pair
enumeration takes $O(H^2+V^2)$ time. In the worst case the two distance sets
also occupy $O(H^2+V^2)$ space.

## Alternatives and edge cases

- **Compare every horizontal and vertical pair:** Testing each pair of distances directly takes $O(H^2V^2)$ time.
- **Sort distance lists:** Sorting both complete lists and intersecting them is correct, but hash sets avoid the additional sorting factor and deduplicate repeated spans naturally.
- **Boundary-only side:** The largest square may use opposite unremovable field boundaries after all intervening fences are removed.
- **Remove no fence:** Adjacent existing fences already count as a valid span.
- **Repeated distances:** Different fence pairs may produce the same length; only the length matters for feasibility.
- **Modulo timing:** Compare original side lengths and maximize before reducing the squared area modulo $10^9+7$.
- **No common distance:** Return `-1`, not zero.

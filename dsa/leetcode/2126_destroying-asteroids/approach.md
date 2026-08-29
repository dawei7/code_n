## General

**Choose the easiest remaining asteroid first**

The planet may collide with asteroids in any order. Destroying an asteroid never decreases planet mass; it adds that asteroid's mass.

This makes ascending order the safest greedy choice. The source sorts `asteroids` and processes them from smallest to largest.

At asteroid mass `x`:

- if `mass < x`, the planet cannot destroy it and returns false;
- otherwise, it destroys the asteroid and updates `mass += x`.

The comparison permits equality, matching the rule that greater than or equal mass succeeds.

**Why failure at the smallest remaining asteroid is final**

Suppose the sorted scan reaches `x` with planet mass smaller than `x`. Every unprocessed asteroid has mass at least `x`.

The planet cannot destroy any of them, so it has no way to gain additional mass. No different ordering of the remaining asteroids can help. Returning false is therefore a proof of impossibility, not merely failure of this particular order.

**Why successful small collisions never hurt**

If the planet can destroy the smallest remaining asteroid, doing so increases its mass. Any asteroid that was already destroyable remains destroyable, and some larger asteroids may become newly possible.

There is no resource consumed by a collision and no penalty for gaining mass. Thus postponing a destroyable small asteroid offers no advantage over taking its gain immediately.

**Exchange argument for sorted order**

Consider any successful ordering with an inversion: a larger asteroid `b` is destroyed before a smaller asteroid `a`.

At the moment `b` is destroyed, the planet's mass is at least `b` and therefore also at least `a`. Swapping `a` before `b` succeeds; after absorbing `a`, the planet has even more mass before meeting `b`.

Repeatedly removing inversions transforms a successful ordering into non-decreasing order without making it fail. Therefore, if any order works, the sorted order works.

**Trace a successful case**

For initial mass 10 and sorted asteroids `[3, 5, 9, 19, 21]`:

- absorb 3 to reach 13;
- absorb 5 to reach 18;
- absorb 9 to reach 27;
- absorb 19 to reach 46;
- absorb 21 to reach 67.

Every test succeeds, so all asteroids can be destroyed.

The order shown in the problem need not match this exact sequence; any valid ordering is enough, and sorting constructs one.

**Trace a failure**

For mass 5 and sorted `[4, 4, 9, 23]`:

- masses become 9, then 13, then 22;
- 22 is less than 23.

Since 23 is the only and therefore smallest remaining asteroid, no gain remains available. The answer is false.

**Why the algorithm is correct**

The exchange argument proves sorted order succeeds whenever any successful order exists. The loop accurately simulates that order, using the exact collision condition and mass gain.

If it finishes, it has destroyed every asteroid and returns true. If it stops, the smallest remaining asteroid is too large, which proves no remaining collision and no alternative completion is possible.

The source sorts the input list in place, so the caller observes ascending asteroid order afterward.

**Invariant during the sorted scan**

Before processing sorted asteroid `x`, every smaller asteroid has been destroyed and `mass` equals the initial mass plus all of those absorbed masses.

If `mass >= x`, the update maintains the invariant for the next asteroid. If not, the invariant also proves the planet has already collected every gain available from smaller asteroids. Nothing remaining is easier than `x`, so no hidden alternative gain exists.

This makes the early false return especially strong: it occurs only after the planet has accumulated the maximum mass it could obtain before confronting that threshold.

**Why sorting cost buys a global decision**

Without sorting, a failed collision against a large asteroid does not prove impossibility because smaller unprocessed asteroids might provide enough mass. Sorting changes every failed comparison into a conclusive proof, allowing immediate termination.

The ordering step is therefore not just a convenient traversal; it supplies the monotonic structure used by correctness.

## Complexity detail

Let $n$ be the number of asteroids.

Sorting costs $O(n\log n)$. The scan is $O(n)$, so total time is $O(n\log n)$.

Python's Timsort may use $O(n)$ temporary space in the worst case, matching the manifest's $O(n)$ space statement. The loop itself uses constant additional state.

The accumulated mass can exceed the original input bound; Python integers grow as needed.

## Alternatives and edge cases

- **Repeatedly search for any destroyable asteroid:** It may work but can cost $O(n^2)$. Sorting establishes a definitive order once.
- **Max-heap:** Choosing the largest currently destroyable asteroid can also gain mass, but requires maintaining eligibility. The ascending proof is simpler.
- **Original input order:** It may fail even when another ordering succeeds, so reordering is essential.
- **Equal mass:** The planet succeeds because the rule is `>=`.
- **One asteroid:** Return whether the initial mass covers it.
- **Duplicate masses:** They are processed separately and each contributes its mass.
- **Failure at smallest remaining:** Immediately proves all larger remaining asteroids are impossible too.
- **Large accumulated mass:** Use a sufficiently wide type outside Python.
- **Already huge planet:** Every sorted test succeeds.
- **Positive masses:** Every successful collision strictly increases planet mass.
- **Input mutation:** `asteroids.sort()` changes the caller's list order.
- **Early return:** Avoids scanning asteroids after impossibility is established.
- **Mass invariant:** Before each asteroid, all smaller available gains have already been collected.
- **Failure in unsorted order:** Would not be conclusive, which is why sorting is essential.

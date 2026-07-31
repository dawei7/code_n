## General

Store the current color of every position and maintain one running count of qualifying adjacent pairs. Recoloring index `i` cannot affect any pair except `(i - 1, i)` and `(i, i + 1)`, so rescanning the rest of the array would repeat unchanged work.

Before writing the new color, inspect the existing color at `i`. If it is nonzero and matches either in-bounds neighbor, subtract that old pair from the count. Then write the requested color and add each in-bounds neighboring pair that now has the same color. Append the updated total.

Every pair not incident to `i` has the same endpoints before and after the update. The algorithm removes exactly the previously counted incident pairs and then adds exactly the newly valid ones, so the maintained total remains equal to the full-array count after every query.

## Complexity detail

Initializing the color array takes $O(n)$ time. Each of the $q$ queries inspects at most two neighbors and therefore takes $O(1)$ time, for $O(n + q)$ total time. The color array and returned answers use $O(n + q)$ space.

## Alternatives and edge cases

- **Rescan after every query:** Recounting every adjacent pair is direct but costs $O(nq)$ time in the worst case.
- **Store the set of matching edges:** Updating membership for the two incident edges also works in expected $O(1)$ per query, but the running integer alone is simpler.
- Recoloring a position with its current color removes and then restores the same incident pairs, leaving the total unchanged.
- Index zero has no left pair, and index $n - 1$ has no right pair.
- Zero represents an uncolored position and never forms a qualifying pair, even beside another zero.

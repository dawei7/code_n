## General

The numerical ordering of `friends` is irrelevant to the requested result; only membership matters. Put all friend IDs into a set, then scan `order` from first finisher to last.

Append a participant exactly when that ID belongs to the set. Each friend appears once in the permutation and is guaranteed present, so every friend is appended exactly once. No non-friend passes the membership test. Because appends occur during the original left-to-right scan, their relative order is precisely the race's finishing order.

This is a stable filter: it changes which elements remain but never reorders retained elements. The resulting list therefore satisfies both required properties—correct membership and correct finish order.

## Complexity detail

Let $n$ be the number of participants and $f$ the number of friends. Building the membership set takes $O(f)$ expected time, and filtering takes $O(n)$ expected time. The contract caps $f$ at eight, so total time is $O(n)$ and auxiliary space is $O(1)$ under the fixed friend bound. The output uses $O(f)$ required result space.

The package uses an asymptotic-optimality certificate. In an arbitrary permutation, even locating one specified friend requires examining $\Omega(n)$ positions in the worst case because the friend may occupy the final uninspected position. The accepted stable filter examines each position once and matches that lower bound.

## Alternatives and edge cases

- **Sort friends by order.index:** This is correct and costs $O(fn)$ time; because $f\le8$, it is still asymptotically $O(n)$ but repeats scans.
- **Build a full position map:** Mapping all participant IDs and sorting friends by their positions works, but stores $O(n)$ data instead of the bounded friend set.
- **Use the numerical friend order:** This is incorrect because increasing IDs do not imply finishing order.
- **One participant:** The sole friend is returned unchanged.
- **Friend finishes last:** The scan must continue through the final position.
- **All participants are friends:** The returned sequence equals `order`.
- **Boundary IDs:** IDs $1$ and $n$ are ordinary participants whose placement depends only on `order`.
- **Non-friends between friends:** Filtering removes them without changing the friends' relative positions.

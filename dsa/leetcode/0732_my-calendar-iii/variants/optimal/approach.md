## General
**Turn each booking into a range increment**

Use a dynamic lazy segment tree covering integer coordinates from `0` through $10^{9} - 1$. The half-open interval `[start, end)` maps to the inclusive range `[start, end - 1]`, and booking it adds one to every represented point in that range.

**Keep the maximum at every sparse node**

Each node stores the maximum overlap anywhere in its segment and a lazy increment that applies to its whole segment. A full-cover update increments both values and stops. A partial update creates only the children it needs, recurses across the intersecting halves, and recomputes the node maximum as its lazy value plus the larger child maximum. An absent child contributes zero beyond the parent's lazy increment.

**Read the answer from the root**

After updating one booking, the root maximum is the greatest overlap across the entire coordinate domain, so `book` returns it immediately. No query or rollback is needed because every request is accepted permanently.

**Why the reported overlap is exact**

The tree begins with zero coverage everywhere. Each range update adds one at precisely the integer time points belonging to the new half-open interval. Lazy values preserve increments shared by a whole segment, and child maxima preserve any additional increments within subranges. Therefore each node maximum equals the true maximum coverage of its segment, making the root value the requested calendar-wide answer after every call.

## Complexity detail
Let `q` be the number of calls and $C = 10^{9}$ the coordinate-domain size. Each range increment follows $O(\log C)$ boundary paths, so all bookings take $O(q \log C)$ time. A booking creates at most $O(\log C)$ new nodes, for $O(q \log C)$ space.

## Alternatives and edge cases
- **Sweep-line endpoint deltas:** record `+1` at every start and `-1` at every end, then sort and scan all endpoints after each call; it is easy to verify but costs up to $O(q^2 \log q)$ overall.
- **Augmented ordered map:** a balanced tree whose nodes maintain prefix sums and subtree maxima can support online updates efficiently, but it is substantially more intricate and Python has no built-in augmented tree.
- **Offline coordinate compression:** compress all endpoints and use an array-backed lazy segment tree when the complete operation list is available; the native class, however, receives bookings online.
- **Touching endpoints:** `[a,b)` and `[b,c)` do not overlap, so booking both can leave the maximum at one.
- **Duplicate intervals:** every duplicate is accepted and raises the maximum over that interval by one.
- **Nested intervals:** the innermost common region accumulates every containing booking.
- **Maximum monotonicity:** because bookings are never removed, the returned value can stay equal or increase but never decrease.
- **Coordinate extremes:** `start = 0` and `end = 10 ** 9` map exactly to the root's two boundaries.

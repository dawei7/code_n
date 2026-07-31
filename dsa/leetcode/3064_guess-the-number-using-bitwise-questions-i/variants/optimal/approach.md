## General

**Isolate one bit per question.** For each position $i$ from $0$ through $29$, query the singleton mask `1 << i`. Its binary representation has exactly one set bit. Consequently, `n & (1 << i)` is either zero when bit $i$ of $n$ is clear or the singleton mask itself when that bit is set. The API response is therefore exactly zero or one for this query.

**Assemble the detected pattern.** Start the answer at zero. Whenever a singleton query returns a positive count, incorporate that mask with bitwise OR. A clear bit leaves the answer unchanged.

After processing positions $0$ through $i$, the accumulated answer agrees with $n$ at every one of those positions and has no bits set elsewhere except positions already confirmed by the API. The next singleton query determines bit $i+1$ independently, so the same relationship continues. Once all 30 legal positions have been queried, the accumulated bit pattern matches $n$ everywhere it can contain a set bit and must equal the hidden number.

## Complexity detail

The legal number domain has a fixed width of 30 bits. The method always makes exactly 30 API calls, performs constant work per call, and stores only the current mask and answer. Under this fixed-width contract, both time and auxiliary space are $O(1)$. For a generalized $B$-bit interface, the method would use $O(B)$ calls and time with $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Query every prefix mask:** Differences between successive population counts can reveal bits, but singleton masks give each response a direct interpretation and avoid subtracting prior results.
- **Enumerate candidate numbers:** Testing possible hidden values is unnecessary and does not follow from the limited information returned by one API call.
- **One all-bits query:** `commonSetBits((1 << 30) - 1)` reveals only how many bits are set, not their positions, so many different numbers remain possible.
- **Lowest legal value:** For `n = 1`, only the query for bit zero returns one.
- **Highest bit:** Position 29 must be included; iterating only through position 28 fails for values at least $2^{29}$.
- **Maximum hidden value:** When $n=2^{30}-1$, every singleton query is positive and all 30 answer bits are set.
- **Query range:** Every singleton mask from `1 << 0` through `1 << 29` lies within the API's reliable interval.

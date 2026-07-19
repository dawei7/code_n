## General
**Classify one pair for every target.** For a mirrored pair with values $a$ and $b$, any target from $2$ through $2L$ is possible. Without changing either value, only target $a+b$ costs zero. By changing one endpoint, every target from $1+\min(a,b)$ through $L+\max(a,b)$ costs at most one. Targets outside that interval require changing both endpoints and cost two.

**Encode the piecewise cost with boundaries.** Create a difference array over target sums. For each pair, add a baseline of two moves starting at target $2$. Subtract one at the beginning of its one-move interval, subtract another at its exact zero-move sum, then add those units back immediately after the exact sum and immediately after the one-move interval. Five constant-time boundary updates encode the pair's full cost function without visiting every target.

**Combine all pairs by prefixing.** Prefix-sum the difference array from target $2$ through $2L$. At each target, the running value is the sum of the costs contributed by all mirrored pairs. The minimum running value is therefore the fewest moves over every possible common sum.

**Why the intervals are complete.** Changing $a$ while keeping $b$ can produce sums from $1+b$ through $L+b$; changing $b$ while keeping $a$ produces $1+a$ through $L+a$. These intervals overlap because both original values lie within $[1,L]$, and their union is exactly $[1+\min(a,b), L+\max(a,b)]$. Thus the encoded zero-, one-, and two-move regions classify every legal target correctly.

## Complexity detail
The pair loop performs constant work for each of the $n/2$ mirrored pairs, and the prefix scan visits $2L-1$ target sums. Total time is $O(n+L)$. The difference array has $O(L)$ entries and no other growing state is stored.

## Alternatives and edge cases
- **Enumerate every target and pair:** Directly compute whether each pair needs zero, one, or two changes for every sum. This is correct but costs $O(nL)$ time.
- **Hash maps of exact sums and interval events:** Sparse maps can store the same boundaries, but all target sums still need ordered processing and an array is simpler within the bounded domain.
- **Choose the most common current sum:** This accounts only for zero-change pairs and can miss a different target reachable by one change for many more pairs.
- A single mirrored pair is already complementary and requires zero moves.
- Target sums range from $2$ through $2L$, including both endpoints.
- Equal pair values and duplicate pairs contribute independently.
- A pair may need two changes when the chosen target lies outside both one-endpoint ranges.
- The optimal target need not equal any pair's original sum.

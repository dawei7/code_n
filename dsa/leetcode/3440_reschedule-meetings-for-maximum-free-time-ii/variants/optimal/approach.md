## General

Represent the schedule by its $n+1$ free gaps: one before the first meeting, one between each adjacent pair, and one after the last meeting. Consider moving meeting $i$, whose duration is $d$. Its neighboring gaps are `gaps[i]` and `gaps[i + 1]`.

If the meeting remains within its original surrounding span, packing it against either neighbor joins its two adjacent gaps and yields `gaps[i] + gaps[i + 1]` continuous free time. The meeting itself still occupies $d$ units inside that span.

The stronger possibility is to place the meeting into some other gap of length at least $d$. Its entire original span then becomes free, producing `gaps[i] + d + gaps[i + 1]`. The destination cannot be either adjacent gap because those are precisely the spaces being merged. Prefix and suffix maximum arrays reveal in constant time the largest gap strictly before `gaps[i]` or strictly after `gaps[i + 1]`.

Evaluate both possibilities for every meeting. These are exhaustive: any move either places the meeting elsewhere, freeing its full old span, or leaves it inside that span, where the most free time comes from packing it against one boundary. Taking the maximum therefore gives the optimum even when relative order changes.

## Complexity detail

Let $n$ be the number of meetings. Building the gaps, prefix maxima, suffix maxima, and evaluating all meetings each take $O(n)$ time. The three arrays use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Scan every other gap per meeting:** This directly checks relocation capacity but costs $O(n^2)$ time.
- **Use the global largest gap without exclusions:** An adjacent gap cannot simultaneously receive the moved meeting and become part of the fully vacated span.
- **No remote gap fits:** The meeting can still slide within its old span, joining only its two adjacent free gaps.
- **Exact fit:** A non-adjacent gap whose size equals the duration is a valid destination.
- **Packed schedule:** When every gap is zero, moving a positive-duration meeting cannot create free time.
- **Event boundaries:** The gaps before the first and after the last meeting are valid relocation destinations and merged-gap components.

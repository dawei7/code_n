## General

**Split consecutive stones between the two directions.** Send the frog outward through one parity of intermediate indices and back through the other parity. Each direction then usually skips exactly one stone at a time. Consequently, every non-endpoint jump has the form `stones[i] - stones[i - 2]`; the two paths share only the required endpoints and use each intermediate stone once.

**Why no route can do better.** Consider any three consecutive stones at indices `i - 2`, `i - 1`, and `i`. The outward and return paths have disjoint intermediate landings. If one path uses the middle stone, the other must cross from a stone at or left of `i - 2` to a stone at or right of `i`; if neither path uses the middle stone, both paths make such a crossing. Thus every legal round trip contains a jump of length at least `stones[i] - stones[i - 2]` for each `i >= 2`.

The alternating construction makes its longest jump exactly the maximum of those two-index spans, so it meets this lower bound and is optimal. With exactly two stones there is no such span; the only possible jump length is the distance between the endpoints.

Adjacent endpoint gaps do not need separate checks when there are at least three stones. Each is strictly smaller than a two-index span containing it because positions are strictly increasing.

## Complexity detail

Let $n = \lvert\texttt{stones}\rvert$. Inspecting each two-index span once takes $O(n)$ time. The scan retains only the current maximum and index, so it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Binary search on the answer:** A feasibility test can determine whether two disjoint directional paths stay within a proposed jump limit, but this adds a logarithmic factor and more intricate state.
- **Explicit route construction:** Building the two alternating index lists demonstrates the strategy but uses $O(n)$ extra space when only the maximum span is needed.
- **Exactly two stones:** Return the endpoint distance directly because no two-index span exists.
- **Exactly three stones:** One direction can use the middle stone, forcing the other to jump the full endpoint span.
- **Highly uneven gaps:** The decisive value is still a two-index span; a large adjacent gap participates in at least one such span.
- **Large coordinates:** Only subtraction and comparison are used, so no accumulation can overflow the intended integer range.

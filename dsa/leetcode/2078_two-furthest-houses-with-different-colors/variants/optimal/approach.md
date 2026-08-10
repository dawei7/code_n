## General

**Start with the largest distance that could possibly exist**

For an array of length `n`, no two indices can be farther apart than 0 and `n - 1`. Their distance is $n-1$. The solution therefore compares the colors at the two endpoints first.

If `colors[0] != colors[-1]`, the endpoint pair is valid and already reaches the absolute maximum possible distance. No scan or further proof of a better pair is needed, so the code immediately returns `n - 1`.

This early return handles every input whose outermost houses have different colors, regardless of what appears between them.

**When endpoint colors match, find the first disagreement from each side**

The more interesting case is

`colors[0] == colors[-1]`.

Call this shared endpoint color $c$. A valid pair cannot use both endpoints because they have the same color. However, the problem guarantees that at least two houses have different colors, so at least one interior house has a color different from $c$.

The first loop starts `i` at 1 and advances while `colors[i] == colors[0]`. When it stops, `i` is the smallest index whose color differs from $c$.

Pairing this house with the right endpoint is valid:

- house `i` has a color different from $c$;
- house `n - 1` has color $c$;
- their distance is `n - 1 - i`, written by the source as `n - i - 1`.

Because `i` is the earliest disagreement, no different-colored house lies farther left. Therefore, among all valid pairs using the right endpoint, this pair has the greatest possible distance.

The second loop starts `j` at `n - 2` and moves left while `colors[j] == colors[0]`. When it stops, `j` is the largest index whose color differs from $c$.

Pairing this house with the left endpoint is valid, and its distance from index 0 is simply `j`. Because `j` is the latest disagreement, it is the farthest valid partner for the left endpoint.

The answer is the larger of these two endpoint-based candidates:

`max(n - i - 1, j)`.

**Why an optimal pair always touches an endpoint**

The key greedy fact is that some maximum-distance valid pair uses index 0 or index `n - 1`.

Consider any valid pair with indices $a<b$ and different colors. If `colors[a]` differs from the right endpoint's color, then `(a, n-1)` is also valid and its distance is at least $b-a$, because $n-1\ge b$.

Otherwise, `colors[a]` equals the right endpoint's color. Since `colors[a] != colors[b]`, house `b` must differ from the right endpoint.

- If the two endpoint colors differ, pair `(0, n-1)` is already the global maximum, which the early return handles.
- In the remaining case, the endpoints share color $c$. Then `colors[a] = c` and `colors[b] != c`, so pair `(0, b)` is valid and has distance $b$, which is at least $b-a$.

Thus an interior valid pair can always be extended to an endpoint without decreasing its distance. Searching the best valid partner for each endpoint is sufficient.

The exact source makes this even simpler by separating the two endpoint-color cases. When endpoints differ, use both. When they match, every house with a non-$c$ color is a valid partner for either endpoint, so only the leftmost and rightmost such houses matter.

**A concrete trace**

Take `colors = [1, 1, 1, 6, 1, 1, 1]`. Both endpoints have color 1, so there is no early return.

The left scan starts at index 1. It passes indices 1 and 2 because they contain 1, then stops at `i = 3` because that house has color 6. Its distance to the right endpoint is $6-3=3$.

The right scan starts at index 5. It passes indices 5 and 4 because they contain 1, then stops at `j = 3`. Its distance to the left endpoint is 3. The maximum is 3.

For `colors = [1, 8, 3, 8, 3]`, the endpoint colors 1 and 3 differ. The method returns 4 immediately, which is the distance between indices 0 and 4.

**Why the scans cannot run out of bounds**

The loops do not contain explicit boundary tests, so their safety depends on the input guarantee. In the matching-endpoint case, at least two houses in the whole array have different colors. Since both endpoints have the same color $c$, some interior house must differ from $c$.

The left scan encounters such a house before passing the right endpoint, and the right scan encounters one before passing the left endpoint. Both loops therefore stop at a valid array index. For an array of length two, the endpoints must differ under the same guarantee, so the early return occurs and neither scan runs.

**Why the returned maximum is correct**

When endpoint colors differ, `n - 1` is both valid and the largest distance any index pair can have.

When endpoint colors match, `i` is the closest non-$c$ house to the left edge, making `n - 1 - i` the best valid distance ending at the right edge. Similarly, `j` is the closest non-$c$ house to the right edge, making `j` the best valid distance starting at the left edge. The endpoint lemma proves that an optimal pair must be represented by one of these two categories. Taking their maximum therefore returns the global optimum.

The source reads the array only. It never sorts, recolors, or otherwise mutates the houses.

## Complexity detail

Let $n$ be the number of houses.

The endpoint comparison takes constant time. If the colors differ, the method returns in $O(1)$ time for that input.

Otherwise, `i` moves only from left to right until the first different color, and `j` moves only from right to left until the last different color. Each pointer advances at most $n$ positions, so the worst-case time complexity is $O(n)$.

The algorithm stores `n` and two indices. It does not allocate a copy, a map, or a set, so its auxiliary space complexity is $O(1)$.

Although the two scans can inspect overlapping positions, each performs at most one monotonic pass. Their combined work remains linear rather than quadratic.

## Alternatives and edge cases

- **Enumerating every pair:** Testing all $O(n^2)$ pairs is straightforward and correct, but the endpoint lemma makes almost all of those comparisons unnecessary.
- **One editorial-style pass:** One can scan all indices and update endpoint-based candidate distances whenever a color differs from an endpoint color. That is also $O(n)$; the exact source instead uses an early return plus two boundary searches.
- **Tracking positions for every color:** A map from color to extreme indices can solve the problem, but the answer needs only disagreement with the endpoints, so the extra storage and bookkeeping are unnecessary.
- **Different endpoint colors:** Return `n - 1` immediately. No interior pair can exceed the full-array span.
- **Matching endpoint colors:** Some interior position must differ under the problem guarantee. The two scans locate the extreme such positions safely.
- **Exactly two houses:** Their colors must differ, so the answer is 1 and the early-return branch handles it.
- **Only one exceptional house:** Both scans stop at that same index. The algorithm compares its distance to each endpoint and chooses the farther one.
- **Several non-endpoint colors:** Their identities relative to one another do not matter. Every color different from the common endpoint color is a valid endpoint partner, so only their extreme positions matter.
- **Long equal-color prefix:** The left scan skips it once. The first disagreement is the best partner for the right endpoint because moving farther right can only shorten that distance.
- **Long equal-color suffix:** The right scan skips it once. The final disagreement is the best partner for the left endpoint.
- **Input guarantee is essential:** If every house had the same color, the unguarded scans could leave the array bounds and no valid answer would exist. The stated guarantee rules out that invalid domain.
- **No input mutation:** Because the array is only inspected, callers retain the original color ordering after the result is computed.

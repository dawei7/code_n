## General

**Paint symmetric house pairs from the outside inward.** Because $n$ is even, houses can be grouped as

$$
(0,n-1),(1,n-2),\ldots,(n/2-1,n/2).
$$

The two houses in each pair are equidistant from the ends and must receive different colors. Processing one entire pair at a time makes this condition local.

At the same time, left-side pairs move through houses $0,1,2,\ldots$, so consecutive left choices must differ to satisfy adjacency. Right-side pairs move through houses $n-1,n-2,\ldots$, so consecutive right choices must also differ.

**Define the constant-size state.** `dp[left_color][right_color]` is the minimum cost after painting all processed outer pairs, where the innermost painted house on the left has `left_color` and the innermost painted house on the right has `right_color`.

There are only three colors, so the table contains nine states regardless of $n$. Invalid states hold infinity.

For the outermost pair $(0,n-1)$, the source tries every two colors. Only choices with `left_color != right_color` satisfy the equidistant condition. Their cost is

`cost[0][left_color] + cost[n - 1][right_color]`.

This fully initializes the state for one painted pair. When $n=2$, that is also the center pair and no further iteration is needed.

**Add the next inner pair.** For `left` from $1$ through $n/2-1$, the symmetric right index is

`right = n - 1 - left`.

The source builds a fresh `next_dp` so every new state is based only on the preceding outer layer, never on another partially updated state from the same layer.

For every finite state `(previous_left, previous_right)`, it tries new colors.

The condition `left_color != previous_left` prevents adjacent houses `left - 1` and `left` from matching.

The condition `right_color != previous_right` prevents adjacent houses `right` and `right + 1` from matching. Although indices on the right decrease as processing moves inward, these are still consecutive physical houses.

The condition `right_color != left_color` enforces that the current symmetric pair uses different colors.

If all conditions hold, the candidate cost is the old state plus the two new painting costs. The minimum is stored under the current color pair.

**The center pair needs no extra rule.** Since $n$ is even, the final pair is $(n/2-1,n/2)$. Its two houses are both equidistant from the ends and adjacent to each other. The condition `right_color != left_color` simultaneously satisfies both constraints. There is no unpaired middle house.

For $n=4$, initialization paints houses $0$ and $3$. The single transition paints houses $1$ and $2$, checks each against its outer neighbor, and checks the center pair against each other. Every condition in the statement is then covered.

**Why the state contains enough history.** When choosing colors for a new inner pair, the only already painted houses adjacent to it are the immediately preceding left and right houses. Their colors are exactly the two state indices. More distant colors can no longer affect any future adjacency decision. Equidistant constraints are handled inside each pair when it is created. Therefore, no other history is needed.

Inductively, every finite state represents a valid coloring of the processed outer houses and stores the least cost among colorings with those two boundary colors. Each valid extension appears in the nested loops, and every loop extension obeys all newly introduced constraints. After the last pair, every house is painted, so the smallest entry in `dp` is the global optimum.

The source uses zero-based color indices $0,1,2$, corresponding to the statement's colors $1,2,3$. Costs are read directly from those zero-based columns.

## Complexity detail

There are $n/2$ symmetric pairs. For each transition layer, the source loops over $3^4=81$ combinations of previous and current color pairs. This is a fixed constant, so total time is $O(n)$.

`dp` and `next_dp` each contain nine numeric entries. Loop variables require constant space. Total auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **House-by-house DP with first-half history:** A standard last-color state cannot enforce colors of mirrored houses much later. Pairing symmetric positions makes both relevant colors available together.
- **Backtracking all colorings:** Trying three colors for every house is exponential. The nine-state DP merges histories with identical boundary colors.
- **Full \(n\times3\times3\) table:** It is correct but stores every layer. Only the immediately previous pair layer is needed.
- **Two houses:** Initialization alone enforces that the only symmetric/adjacent pair has different colors, and `min` returns the cheaper valid assignment.
- **Center adjacency:** The final symmetric pair consists of neighboring houses. The within-pair inequality is essential and already covers it.
- **Zero painting costs:** Infinity distinguishes impossible states from valid zero-cost ones, so free colors are handled correctly.
- **Equal-cost alternatives:** The DP may retain any coloring achieving the same minimum because only total cost is requested.
- **Even \(n\):** The pair construction relies on the guarantee. An odd number would leave a center house needing a different state transition.
- **Right-side orientation:** Comparing the new right color with `previous_right` is correct even though right indices decrease, because those houses are adjacent.
- **Fresh transition table:** Updating `dp` in place could reuse colors from the current layer and effectively paint a pair more than once.

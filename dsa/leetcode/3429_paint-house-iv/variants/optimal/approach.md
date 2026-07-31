## General

Pair house $i$ with house $n-1-i$ and process these pairs from the outside toward the center. A state `dp[left_color][right_color]` records the minimum cost of all pairs processed so far when the innermost processed houses use those two colors. Only the six states with distinct colors are legal, because the two houses in every mirrored pair must differ.

For the next pair, choose a new left color different from the preceding left color and a new right color different from the preceding right color. These two restrictions enforce adjacency on the two sides independently. Requiring the new colors to differ enforces the equidistant-house rule for this pair. Add both painting costs and retain the cheapest transition into each of the nine possible new states.

The outermost pair initializes the table directly. Inductively, every finite state represents exactly the valid colorings of the processed outer segment with its stated boundary colors: every transition adds a legal pair, and every legal coloring has a transition from its preceding outer pair. After $n/2$ pairs, the minimum table entry therefore gives the cheapest valid coloring of all houses.

## Complexity detail

There are $n/2$ mirrored pairs. Each pair examines at most $3^4=81$ combinations of previous and new colors, which is a fixed constant, so the running time is $O(n)$. Two $3\times3$ tables are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate every coloring:** Trying all color sequences is exponential even after rejecting adjacent equal colors, so it cannot handle $n=10^5$.
- **Dynamic programming from only one end:** A state containing just the latest color cannot determine whether a future house violates the mirrored-pair restriction.
- **Full pair-index table:** Keeping all nine states for every processed pair is correct but uses $O(n)$ space unnecessarily; only the previous layer is needed.
- **Two houses:** There is one mirrored pair and no transition step; the initialization already selects its cheapest two distinct colors.
- **Tied or zero costs:** The state constraints, rather than cost comparisons, enforce legality, so ties and zero-cost colors require no special handling.
- **Large costs:** The answer can exceed a 32-bit integer when $n$ and individual costs are maximal.

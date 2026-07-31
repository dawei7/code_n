## General

The ball-label range can be as large as $10^9$, so allocating an array for every possible ball is not viable. Only balls mentioned by queries need state. Maintain `ball_colors`, which maps each colored ball to its current color, and `color_counts`, which maps each active color to the number of balls currently using it.

For a query `[ball, color]`, first remove the ball's contribution to its previous color if it has one. When that previous color's count becomes zero, delete the key because the color is no longer present. Then record the new color, increment its count, and append the number of keys in `color_counts`.

After every update, `ball_colors` gives exactly one current color for each colored ball, and `color_counts[c]` equals the number of those balls mapped to `c`. Removing zero counts means its keys are precisely the colors present among the balls, so their count is the required answer.

## Complexity detail

Let $n$ be the number of queries. Each query performs a constant expected number of hash-map operations, so the expected time complexity is $O(n)$. At most $n$ balls and $n$ colors have entries at once, giving $O(n)$ auxiliary space. The numerical value of `limit` does not affect storage.

## Alternatives and edge cases

- **Recount after every query:** Store ball colors and compute `len(set(ball_colors.values()))` after each update. It is correct but can take $O(n^2)$ total time.
- **Array indexed by ball label:** Direct indexing works only for small `limit`; allocating up to $10^9 + 1$ entries violates practical memory limits.
- **Repeated identical assignment:** Temporarily decrementing and then incrementing the same color preserves its owner count and the distinct total.
- **Last owner changes color:** Delete the old color exactly when its count reaches zero, or inactive colors would be overcounted.
- **Shared colors:** Recoloring one ball does not remove a color while another ball still uses it.
- **Uncolored balls:** They never enter either map and do not count as a color.

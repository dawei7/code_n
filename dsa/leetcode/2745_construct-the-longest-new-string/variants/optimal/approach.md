## General

The `"AA"` and `"BB"` pieces regulate one another. Two `"AA"` pieces cannot be adjacent because their join contains `"AAA"`; the same is true for two `"BB"` pieces. Alternating these two kinds avoids both forbidden substrings, so every matched pair contributes two usable pieces. If their counts differ, exactly one additional piece from the more plentiful kind can be placed at an end of the alternating sequence. Any further surplus piece would have to sit beside the same kind and would create three equal consecutive characters.

Every `"AB"` piece can also be used. Consecutive `"AB"` pieces form `"ABAB"`, and their boundaries never create `"AAA"` or `"BBB"`. They can be positioned between the alternating equal-letter pieces so that all `z` copies are included without reducing the best usable counts of the other two kinds.

Therefore the number of selected pieces is

$$
2\min(x,y)+z+\begin{cases}1,&x\ne y,\\0,&x=y.\end{cases}
$$

The alternating construction shows that this many pieces are attainable. The adjacency restriction proves that no construction can use more than one unmatched `"AA"` or `"BB"` piece, so the count is also an upper bound. Multiplying by $2$ converts pieces to characters.

## Complexity detail

The algorithm evaluates a fixed arithmetic expression, so it takes $O(1)$ time and $O(1)$ auxiliary space. The fixed legal domain is covered by a bounded-domain complexity certificate rather than a misleading runtime-scaling benchmark.

## Alternatives and edge cases

- **Dynamic programming over remaining counts:** A memoized search can model the last characters and try every next piece, but it uses many states to recover a result available from the alternating-count observation.
- **Explicit greedy construction:** Building an actual valid string can demonstrate attainability, but the problem requests only its maximum length and the construction performs unnecessary work.
- **Use every equal-letter piece:** This fails when $\lvert x-y\rvert>1$ because surplus pieces of the same kind cannot all be separated.
- Every `"AB"` piece is usable, including when many copies are concatenated consecutively.
- When $x=y$, no extra equal-letter piece is available beyond the matched alternating pairs.
- When $x\ne y$, one and only one piece from the larger side can be added.
- The answer counts characters, not pieces, so the final piece count must be doubled.

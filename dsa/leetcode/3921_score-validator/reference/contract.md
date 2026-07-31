## Function Contract

**Inputs**

- `events`: A list whose entries are the allowed numeric or symbolic event strings. Their order is significant.

Let $n=\lvert\texttt{events}\rvert$. Only the prefix ending at the tenth `"W"`, inclusive, is processed when that event exists; every later entry is ignored.

**Return value**

Return `[score, counter]`, where `score` is the sum contributed by processed numeric, `"WD"`, and `"NB"` events, and `counter` is the number of processed `"W"` events. The counter never exceeds `10`.

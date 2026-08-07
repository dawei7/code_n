## Function Contract

**Inputs**

- `keyboard`: A length-$26$ string that lists every lowercase English letter exactly once in its row position.
- `word`: The lowercase English string to type.

Let $m = \lvert\texttt{word}\rvert$. The finger starts at keyboard position `0`; after typing each character, its destination becomes the starting position for the next move.

**Return value**

- The integer sum of the absolute distances for all $m$ moves.

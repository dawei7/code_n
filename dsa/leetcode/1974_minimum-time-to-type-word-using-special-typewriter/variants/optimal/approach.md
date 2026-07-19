## General
**Choose the shorter arc for each next letter**

Represent each letter by its position from `0` through `25`. If the pointer is
at position `previous` and the next character is at `current`, their direct
linear separation is

$$
d=\lvert \texttt{current}-\texttt{previous}\rvert.
$$

Moving along that direct arc costs $d$ seconds. Moving around the other side
of the circle costs $26-d$, so the minimum movement cost is
$\min(d,26-d)$. Add this cost and one second to type the character, then make
that character the new pointer position.

**Why local shortest moves are globally optimal**

The pointer must reach each requested character before it can be typed, and
typing fixes the pointer at exactly that character regardless of which
direction reached it. Therefore the chosen route to the current character
cannot change the starting position for the next character. Replacing any
route by the shorter circular arc never harms a later decision and minimizes
that transition independently. Summing these minimum transitions plus exactly
one typing operation per character gives the global minimum.

## Complexity detail
The scan processes each of the $N$ characters once and performs constant work
per transition, giving $O(N)$ time. The total, previous position, and current
distance use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Step-by-step pointer simulation:** Move one circle position at a time
  along the shorter arc. This is correct, but calculating the distance
  directly is simpler; with a fixed 26-letter alphabet both remain linear in
  $N$.
- **Recompute every prefix:** Recalculate the complete typing time after each
  next character is appended and keep the final prefix total. This remains
  correct but repeats earlier transitions and takes $O(N^2)$ time.
- Repeated letters require no movement, but each occurrence still costs one
  second to type.
- Moving between `a` and `z` costs one second because the alphabet is circular.
- At separation 13, clockwise and counterclockwise routes tie; either direction
  has the same minimum cost.
- The pointer begins at `a`, so the first character's movement is measured from
  `a`, not from an unspecified position.

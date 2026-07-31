## Function Contract

**Inputs**

- `nums`: The integer array on which Alice and Bob play the deletion game.

Let $N = \lvert\texttt{nums}\rvert$ be the initial array length.

Every move acts on the current array: it removes one nonempty, proper, contiguous subarray. Elements outside that block keep their relative order when they are joined together. Alice moves first, and both players choose optimally for their opposing objectives.

**Return value**

Return the value of the sole remaining element when Alice maximizes the outcome and Bob minimizes it.

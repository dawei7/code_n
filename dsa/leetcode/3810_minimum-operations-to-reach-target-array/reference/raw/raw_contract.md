## Function Contract

**Inputs**

- `nums`: A non-empty integer array representing the current values.
- `target`: An integer array of the same length representing the required values.

Let $N=\lvert\texttt{nums}\rvert=\lvert\texttt{target}\rvert$. One operation chooses a value from the current `nums` and simultaneously replaces every element in every maximal segment of that value with the corresponding element of `target`.

**Return value**

Return the fewest operations required to transform `nums` into `target` exactly.

## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers to order.

Let $N=\lvert\texttt{nums}\rvert$. For each value $x$, let $R(x)$ denote the decimal value represented by the reversed binary digits of $x$.

**Return value**

Return an array containing every input occurrence, ordered by the key $(R(x),x)$ in ascending lexicographic order. Repeated equal values remain repeated in the result.

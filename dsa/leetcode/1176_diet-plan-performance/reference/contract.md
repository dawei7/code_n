## Function Contract

**Inputs**

- `calories`: The array of nonnegative daily calorie counts.
- `k`: The exact number of consecutive days in every evaluated window.
- `lower`: The inclusive lower endpoint of the no-change interval.
- `upper`: The inclusive upper endpoint of the no-change interval.

Let $n = \lvert\texttt{calories}\rvert$. The valid windows have start positions $0 \leq i \leq n-k$, and the total for start `i` is the sum of `calories[i]` through `calories[i + k - 1]`.

**Return value**

- Return the integer score after all $n-k+1$ windows have been evaluated. Each total below `lower` contributes `-1`, each total above `upper` contributes `1`, and every other total contributes `0`.

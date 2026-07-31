## Function Contract

**Inputs**

- `s`: A nonempty binary string in which `"1"` denotes a sensitive element.
- `encCost`: The positive multiplier used by any segment containing at least
  one sensitive element.
- `flatCost`: The cost of a segment containing no sensitive elements.

Let $N = \lvert\texttt{s}\rvert$. For a current segment with length $L$ and
$X$ occurrences of `"1"`, keeping it intact costs

$$
\begin{cases}
\texttt{flatCost}, & X = 0, \\
L X \cdot \texttt{encCost}, & X > 0.
\end{cases}
$$

A segment may remain intact. When $L$ is even, it may instead be replaced by
its left and right contiguous halves, each of length $L/2$, and those halves
follow the same rule independently. An odd-length segment cannot be split.

**Return value**

Return the minimum possible sum of final-segment costs over every valid
recursive equal-halving partition.

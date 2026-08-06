## Constraints

- $1 \le n \le 10^4$
- `0 <= edges.length <= 10^4`
- Every edge row has exactly two entries. The live source renders this row-shape constraint as `edges.length == 2`; its preceding definition `edges[i] = [a_i, b_i]` makes clear that the length-two object is each edge row.
- $0 \le a_i, b_i \le n - 1$
- $0 \le \texttt{source} \le n - 1$
- $0 \le \texttt{destination} \le n - 1$
- The graph may contain self-loops and parallel edges.

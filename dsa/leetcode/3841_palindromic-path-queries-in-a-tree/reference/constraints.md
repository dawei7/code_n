## Constraints

- $1 \le n = \texttt{s.length} \le 5\cdot 10^4$
- `edges.length == n - 1`
- Every edge has the form `edges[i] = [u_i, v_i]`.
- $0 \le u_i, v_i \le n-1$
- `s` consists of lowercase English letters.
- The input guarantees that `edges` represents a valid tree.
- $1 \le \texttt{queries.length} \le 5\cdot 10^4$

Each command additionally follows the source's query-specific rules:

- `queries[i] = "update u_i c"`, or
- `queries[i] = "query u_i v_i"`.
- $0 \le u_i, v_i \le n-1$
- `c` is a lowercase English letter.

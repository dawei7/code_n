## Constraints

- $2 \le n \le 2 \cdot 10^4$
- `n == parent.length == gates.length`
- `parent[0] == -1`
- $0 \le \texttt{parent[i]} < n$ for every $i$ in $[1, n - 1]$
- `gates[i] == [red_i, blue_i, white_i]`
- $0 \le \texttt{red_i}, \texttt{blue_i}, \texttt{white_i} \le 10$
- $1 \le \texttt{queries.length} \le 2 \cdot 10^4$
- `queries[i] == [aNode_i, aCard_i, bNode_i, bCard_i]`
- $0 \le \texttt{aNode_i}, \texttt{bNode_i} \le n - 1$
- $0 \le \texttt{aCard_i}, \texttt{bCard_i} \le 1$
- `parent` represents a valid tree.

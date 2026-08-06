## Constraints

- $1 \le n \le 10^4$
- $1 \le \lvert\texttt{connections}\rvert \le 10^4$
- `connections[i].length == 3`
- $1 \le x_i, y_i \le n$
- $x_i \ne y_i$
- $0 \le \textit{cost}_i \le 10^5$

Taken together, these source constraints admit no schema-valid instance for `n = 1`: at least one connection is required, but two distinct endpoint labels cannot be chosen from the single available city. The smallest valid instance therefore has `n = 2`.

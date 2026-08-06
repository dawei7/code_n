## Constraints

- $1 \le n \le 5000$
- $1 \le \lvert\texttt{relations}\rvert \le 5000$
- `relations[i].length == 2`
- $1 \le \textit{prevCourse}_i, \textit{nextCourse}_i \le n$
- $\textit{prevCourse}_i \ne \textit{nextCourse}_i$
- Every pair `[prevCourse_i, nextCourse_i]` is unique.

Taken together, these source constraints admit no schema-valid instance for `n = 1`: at least one relationship is required, but its two course labels must differ. The smallest valid instance therefore has `n = 2`.

## Constraints

- $1 \le \texttt{id} \le 500$
- $2000 \le \texttt{Year} \le 2017$
- $1 \le \texttt{Month} \le 12$
- $1 \le \texttt{Day} \le 31$
- $0 \le \texttt{Hour} \le 23$
- $0 \le \texttt{Minute}, \texttt{Second} \le 59$
- `granularity` is one of `["Year", "Month", "Day", "Hour", "Minute", "Second"]`.
- At most `500` calls are made to `put` and `retrieve` in total.

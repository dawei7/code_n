## Function Contract

**Input**

- `Sessions(session_id, duration)` contains one uniquely identified session per row;
- `duration` is expressed in seconds.

Let $n$ be the number of rows in `Sessions`.

**Return value**

Return exactly the columns `bin` and `total`, with exactly these four bins:

- `[0-5>` for $0 \le \texttt{duration} < 300$;
- `[5-10>` for $300 \le \texttt{duration} < 600$;
- `[10-15>` for $600 \le \texttt{duration} < 900$;
- `15 or more` for $\texttt{duration} \ge 900$.

`total` is the number of sessions in the corresponding interval, including zero for an empty interval. Result order is unrestricted.

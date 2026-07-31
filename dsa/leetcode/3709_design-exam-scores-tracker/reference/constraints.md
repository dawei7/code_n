## Constraints

- $1 \le \texttt{time} \le 10^9$
- $1 \le \texttt{score} \le 10^9$
- $1 \le \texttt{startTime} \le \texttt{endTime} \le t$, where $t$ is the time of the most recent `record` call.
- Calls to `record` use strictly increasing `time` values.
- The first call after `ExamTracker()` is always `record`.
- Across `record` and `totalScore`, at most $10^5$ calls are made.

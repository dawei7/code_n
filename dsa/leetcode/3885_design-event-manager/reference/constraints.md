## Constraints

- $1 \le \texttt{events.length} \le 10^5$
- `events[i] = [eventId, priority]`
- $1 \le \texttt{eventId} \le 10^9$
- $1 \le \texttt{priority} \le 10^9$
- All initial `eventId` values are unique.
- $1 \le \texttt{newPriority} \le 10^9$
- Every `updatePriority` call names an active event.
- At most $10^5$ calls in total are made to `updatePriority` and `pollHighest`.

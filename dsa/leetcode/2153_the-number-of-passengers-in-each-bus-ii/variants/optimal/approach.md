## General

**Count cumulative passenger arrivals at every bus**

Combine passenger and bus arrivals into one event stream. Passenger events add
one; bus events add zero. Sort passengers before a bus at the same time so the
running sum includes the inclusive condition $t_p \leq t_b$. Retain the bus
events with their capacities, chronological row numbers, and cumulative
arrived-passenger counts.

**Carry cumulative boarded passengers through the buses**

Process buses in arrival order with a recursive CTE. If $A_i$ passengers have
arrived by bus $i$ and $D_{i-1}$ passengers have already departed, then
$A_i-D_{i-1}$ are waiting. The bus boards

$$
B_i=\min(\texttt{capacity}_i,\ A_i-D_{i-1}),
$$

and the cumulative departed total becomes $D_i=D_{i-1}+B_i$. This recurrence
preserves excess waiting passengers without identifying individuals. Finally,
project each bus's $B_i$ and order by `bus_id`.

## Complexity detail

Let $N$ be the combined number of bus and passenger rows. Sorting the event
stream takes $O(N\log N)$ time, while windowing and the recursive bus scan take
$O(N)$ time. Materialized events and ordered bus state use $O(N)$ execution
space. Exact physical costs remain database-engine dependent.

## Alternatives and edge cases

- **Correlated cumulative counts:** Recounting all passengers eligible by each
  bus and then applying the same recurrence is correct but can take $O(N^2)$
  time.
- **Assign passengers independently to the first later bus:** This ignores
  capacity and cannot carry rejected passengers forward correctly.
- Passenger events at a bus's exact arrival time must precede that bus event.
- A bus boards zero when no passengers are waiting.
- Excess passengers remain available to every later bus until they board.
- Passengers arriving after the final bus never depart.
- Arrival time controls boarding; final rows are ordered by `bus_id`.

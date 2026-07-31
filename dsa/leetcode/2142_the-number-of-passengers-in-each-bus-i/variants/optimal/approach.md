## General

**Represent arrivals as one event stream**

Project each passenger as an event contributing `1` and each bus as an event
contributing `0`, then combine them with `UNION ALL`. Sort by `arrival_time`,
placing passenger events before a bus event at the same time. That tie order
implements the inclusive rule $t_p \leq t_b$.

**Count all passengers waiting by each bus**

A running sum of passenger contributions gives the cumulative number of
passengers who have arrived at every event. Retain the bus events; each now
holds the number of passengers eligible for some bus up to and including its
arrival.

**Subtract the previous bus's cumulative count**

Order retained buses by arrival time and subtract the preceding cumulative
count with `LAG()`. Passengers counted at the previous bus have already boarded,
so the difference is exactly the passengers using the current bus. Use zero
before the first bus, and finally order the projected result by `bus_id`.

## Complexity detail

Let $N$ be the combined number of bus and passenger rows. Sorting the event
stream takes $O(N\log N)$ time, and the two window scans take $O(N)$ time.
Materialized events and window state use $O(N)$ execution space. Exact physical
costs remain database-engine dependent.

## Alternatives and edge cases

- **Correlated interval count:** For every bus, find the preceding arrival and
  count passengers in that interval. It is direct but can repeatedly scan both
  tables and take quadratic time.
- **Assign each passenger with `MIN(bus arrival_time)`:** Grouping a range join
  identifies the first eligible bus correctly, but can materialize many
  passenger-bus pairs.
- Passenger events must sort before a bus at the same time because equality is
  eligible.
- Buses with no newly arrived passengers must remain in the output with count
  zero.
- Passengers after the final bus never contribute to a bus difference.
- Arrival order determines boarding, while the final presentation order is
  ascending `bus_id`.

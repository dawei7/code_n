## Description

The `Buses` table records each bus's unique `bus_id` and `arrival_time` at a
station. Bus arrival times are also unique. The `Passengers` table records each
passenger's unique `passenger_id` and arrival time.

When a bus arrives at time $t_b$, every passenger who arrived at time $t_p$
with $t_p \leq t_b$ and has not already taken an earlier bus boards this bus.
Thus each passenger uses the first bus whose arrival is not earlier than the
passenger's arrival; passengers arriving after the final bus use none.

Report every bus together with the number of passengers who use it. Order the
result by `bus_id` in ascending order.

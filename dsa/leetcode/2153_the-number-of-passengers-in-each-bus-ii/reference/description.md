## Description

The `Buses` table records each bus's unique identifier, distinct arrival time,
and positive passenger capacity. The `Passengers` table records each
passenger's unique identifier and arrival time.

At a bus arrival time $t_b$, passengers who arrived at times $t_p \leq t_b$
and have not boarded an earlier bus are waiting. At most the bus's `capacity`
of those passengers board; any excess remains for later buses. Report how many
passengers use every bus, including buses that take nobody, and order the
result by `bus_id` in ascending order.

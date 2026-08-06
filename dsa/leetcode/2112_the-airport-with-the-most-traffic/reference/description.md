## Description

The `Flights` table summarizes directed airport routes. Each row identifies one departure airport, one arrival airport, and the number of flights recorded for that ordered pair. The two airport columns together form the table's primary key.

An airport's traffic is the total `flights_count` over every route departing from it plus every route arriving at it. Report the `airport_id` of each airport whose traffic equals the largest total among all airports. All ties must be retained, and the result rows may appear in any order.

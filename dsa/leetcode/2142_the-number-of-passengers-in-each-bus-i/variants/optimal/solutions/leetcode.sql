WITH events AS (
    SELECT bus_id, arrival_time, 1 AS event_kind, 0 AS passenger_delta
    FROM Buses

    UNION ALL

    SELECT NULL AS bus_id, arrival_time, 0 AS event_kind, 1 AS passenger_delta
    FROM Passengers
),
running AS (
    SELECT
        bus_id,
        arrival_time,
        SUM(passenger_delta) OVER (
            ORDER BY arrival_time, event_kind
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS arrived_passengers
    FROM events
),
bus_totals AS (
    SELECT bus_id, arrival_time, arrived_passengers
    FROM running
    WHERE bus_id IS NOT NULL
),
counts AS (
    SELECT
        bus_id,
        arrived_passengers
            - COALESCE(
                LAG(arrived_passengers) OVER (ORDER BY arrival_time),
                0
            ) AS passengers_cnt
    FROM bus_totals
)
SELECT bus_id, passengers_cnt
FROM counts
ORDER BY bus_id;

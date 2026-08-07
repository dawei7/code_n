WITH RECURSIVE
events AS (
    SELECT bus_id, arrival_time, capacity, 1 AS event_kind, 0 AS passenger_delta
    FROM Buses

    UNION ALL

    SELECT NULL, arrival_time, NULL, 0, 1
    FROM Passengers
),
running AS (
    SELECT
        bus_id,
        arrival_time,
        capacity,
        SUM(passenger_delta) OVER (
            ORDER BY arrival_time, event_kind
            ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
        ) AS arrived_passengers
    FROM events
),
ordered_buses AS (
    SELECT
        bus_id,
        capacity,
        arrived_passengers,
        ROW_NUMBER() OVER (ORDER BY arrival_time) AS sequence_number
    FROM running
    WHERE bus_id IS NOT NULL
),
boarded AS (
    SELECT
        sequence_number,
        bus_id,
        CASE
            WHEN capacity < arrived_passengers THEN capacity
            ELSE arrived_passengers
        END AS passengers_cnt,
        CASE
            WHEN capacity < arrived_passengers THEN capacity
            ELSE arrived_passengers
        END AS departed_passengers
    FROM ordered_buses
    WHERE sequence_number = 1

    UNION ALL

    SELECT
        current.sequence_number,
        current.bus_id,
        CASE
            WHEN current.capacity < current.arrived_passengers - previous.departed_passengers
                THEN current.capacity
            ELSE current.arrived_passengers - previous.departed_passengers
        END,
        previous.departed_passengers
            + CASE
                WHEN current.capacity < current.arrived_passengers - previous.departed_passengers
                    THEN current.capacity
                ELSE current.arrived_passengers - previous.departed_passengers
              END
    FROM boarded AS previous
    JOIN ordered_buses AS current
      ON current.sequence_number = previous.sequence_number + 1
)
SELECT bus_id, passengers_cnt
FROM boarded
ORDER BY bus_id;

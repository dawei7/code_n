-- Write your PostgreSQL query statement below
WITH RECURSIVE
    NumberedBuses AS (
        SELECT
            bus_id,
            arrival_time,
            capacity,
            ROW_NUMBER() OVER (ORDER BY arrival_time) AS rn
        FROM Buses
    ),
    Boarding AS (
        SELECT
            nb.rn,
            nb.bus_id,
            nb.capacity,
            LEAST(
                nb.capacity,
                (SELECT COUNT(*) FROM Passengers WHERE arrival_time <= nb.arrival_time)
            ) AS passengers_cnt,
            LEAST(
                nb.capacity,
                (SELECT COUNT(*) FROM Passengers WHERE arrival_time <= nb.arrival_time)
            ) AS accumulated_boarded
        FROM NumberedBuses nb
        WHERE nb.rn = 1

        UNION ALL

        SELECT
            nb.rn,
            nb.bus_id,
            nb.capacity,
            LEAST(
                nb.capacity,
                (SELECT COUNT(*) FROM Passengers WHERE arrival_time <= nb.arrival_time) - b.accumulated_boarded
            ) AS passengers_cnt,
            b.accumulated_boarded + LEAST(
                nb.capacity,
                (SELECT COUNT(*) FROM Passengers WHERE arrival_time <= nb.arrival_time) - b.accumulated_boarded
            ) AS accumulated_boarded
        FROM NumberedBuses nb
        JOIN Boarding b ON nb.rn = b.rn + 1
    )
SELECT
    bus_id,
    passengers_cnt
FROM Boarding
ORDER BY bus_id;


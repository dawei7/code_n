-- Write your PostgreSQL query statement below
WITH
    T AS (
        SELECT
            car_id,
            lot_id,
            SUM(EXTRACT(EPOCH FROM (exit_time - entry_time))) AS duration
        FROM ParkingTransactions
        GROUP BY car_id, lot_id
    ),
    P AS (
        SELECT
            car_id,
            lot_id,
            RANK() OVER (
                PARTITION BY car_id
                ORDER BY duration DESC
            ) AS rk
        FROM T
    )
SELECT
    t1.car_id,
    SUM(t1.fee_paid) AS total_fee_paid,
    ROUND(
        SUM(t1.fee_paid)::numeric / (SUM(EXTRACT(EPOCH FROM (t1.exit_time - t1.entry_time))) / 3600.0),
        2
    ) AS avg_hourly_fee,
    t2.lot_id AS most_time_lot
FROM
    ParkingTransactions AS t1
    LEFT JOIN P AS t2 ON t1.car_id = t2.car_id AND t2.rk = 1
GROUP BY t1.car_id, t2.lot_id
ORDER BY t1.car_id;

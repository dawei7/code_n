WITH LotDurations AS (
    SELECT
        car_id,
        lot_id,
        SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time)) AS duration_seconds
    FROM ParkingTransactions
    GROUP BY car_id, lot_id
),
RankedLots AS (
    SELECT
        car_id,
        lot_id,
        ROW_NUMBER() OVER (
            PARTITION BY car_id
            ORDER BY duration_seconds DESC, lot_id ASC
        ) AS position
    FROM LotDurations
),
CarTotals AS (
    SELECT
        car_id,
        SUM(fee_paid) AS total_fee_paid,
        SUM(TIMESTAMPDIFF(SECOND, entry_time, exit_time)) AS duration_seconds
    FROM ParkingTransactions
    GROUP BY car_id
)
SELECT
    totals.car_id,
    totals.total_fee_paid,
    ROUND(totals.total_fee_paid * 3600 / totals.duration_seconds, 2) AS avg_hourly_fee,
    lots.lot_id AS most_time_lot
FROM CarTotals AS totals
JOIN RankedLots AS lots
    ON lots.car_id = totals.car_id
   AND lots.position = 1
ORDER BY totals.car_id;

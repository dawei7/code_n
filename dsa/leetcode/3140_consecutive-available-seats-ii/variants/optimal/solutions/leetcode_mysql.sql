WITH AvailableSeats AS (
    SELECT
        seat_id,
        seat_id - ROW_NUMBER() OVER (ORDER BY seat_id) AS group_id
    FROM Cinema
    WHERE free = 1
),
Sequences AS (
    SELECT
        MIN(seat_id) AS first_seat_id,
        MAX(seat_id) AS last_seat_id,
        COUNT(*) AS consecutive_seats_len
    FROM AvailableSeats
    GROUP BY group_id
),
RankedSequences AS (
    SELECT
        first_seat_id,
        last_seat_id,
        consecutive_seats_len,
        DENSE_RANK() OVER (ORDER BY consecutive_seats_len DESC) AS length_rank
    FROM Sequences
)
SELECT
    first_seat_id,
    last_seat_id,
    consecutive_seats_len
FROM RankedSequences
WHERE length_rank = 1
ORDER BY first_seat_id ASC;

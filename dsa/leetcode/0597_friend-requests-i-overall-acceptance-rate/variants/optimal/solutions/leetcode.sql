WITH request_pairs AS (
    SELECT DISTINCT sender_id, send_to_id
    FROM FriendRequest
),
accepted_pairs AS (
    SELECT DISTINCT requester_id, accepter_id
    FROM RequestAccepted
)
SELECT ROUND(
    COALESCE(
        1.0 * (SELECT COUNT(*) FROM accepted_pairs)
        / NULLIF((SELECT COUNT(*) FROM request_pairs), 0),
        0
    ),
    2
) AS accept_rate;


WITH ranked_claims AS (
    SELECT
        policy_id,
        state,
        fraud_score,
        RANK() OVER (
            PARTITION BY state
            ORDER BY fraud_score DESC
        ) AS score_rank,
        COUNT(*) OVER (PARTITION BY state) AS state_count
    FROM Fraud
)
SELECT policy_id, state, fraud_score
FROM ranked_claims
WHERE score_rank <= CEIL(state_count * 0.05)
ORDER BY state ASC, fraud_score DESC, policy_id ASC;

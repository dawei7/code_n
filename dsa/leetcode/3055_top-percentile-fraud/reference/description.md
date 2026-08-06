## Description

An insurance fraud model assigns every policy a `fraud_score`, and policies
belong to states. Experienced adjusters should review the highest-scoring five
percent of claims independently within each state; one state's population and
scores must not affect another state's cutoff.

For a state containing $n$ policies, retain the first $\lceil 0.05n\rceil$
ranked positions after sorting scores from greatest to least. Policies tied at
the score occupying the final selected position share its rank and must all be
included. Return the original policy ID, state, and score, ordered by `state`
ascending, `fraud_score` descending, and `policy_id` ascending.

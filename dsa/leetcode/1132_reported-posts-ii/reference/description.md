## Description

For each date containing at least one post reported with the reason `spam`, calculate the percentage of those distinct posts that appear in `Removals`. Duplicate action rows or reports by multiple users must not cause the same post to be counted more than once on one date.

Average those daily percentages with every qualifying date receiving equal weight, then round the final value to two decimal places. Whether a post was removed is determined by its presence in `Removals`; the actual `remove_date` does not affect the calculation.

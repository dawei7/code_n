## Function Contract

**Database Schemas**

**`Candidates`**

| Column | Type | Meaning |
|---|---|---|
| `candidate_id` | int | Unique candidate identifier. |
| `name` | varchar | Display name of the candidate. |
| `years_of_exp` | int | Years of professional experience. |
| `interview_id` | int | Identifier for the candidate's interview. |

**`Rounds`**

| Column | Type | Meaning |
|---|---|---|
| `interview_id` | int | Interview identifier; composite primary key with `round_id`. |
| `round_id` | int | Round number within the interview. |
| `score` | int | Score received in that round. |

**Return value**

Return a table with the single column `candidate_id`. Include candidates for whom `years_of_exp >= 2` and the sum of all matching `score` values across all rounds of their `interview_id` is strictly greater than 15. Row order is unrestricted.

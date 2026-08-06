## Description

The `Candidates` table records one skill for a candidate in each row. A Data
Scientist opening has three mandatory proficiencies: `Python`, `Tableau`, and
`PostgreSQL`. A candidate is suitable only when their recorded skills include
all three exact names; knowing one or two of them is insufficient.

Find every suitable candidate and return only their `candidate_id`. Other
skills neither help nor disqualify a candidate, so a person may have the three
required skills plus any number of additional proficiencies. Order the result
by `candidate_id` in ascending order.

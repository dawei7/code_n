## Vote Table

| Column Name | Type |
|---|---|
| `id` | int |
| `candidateId` | int |

`id` is an auto-incrementing primary key. `candidateId` is a foreign key referencing `Candidate.id`, and row `i` records the candidate who received the $i$th vote in the election.

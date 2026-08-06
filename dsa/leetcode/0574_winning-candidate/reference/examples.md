## Examples

**Example 1**

- **Input:** `Candidate = [[1,"A"],[2,"B"],[3,"C"],[4,"D"],[5,"E"]], Vote = [[1,2],[2,4],[3,3],[4,2],[5,5]]`

Candidate:

| id | name |
|---:|---|
| 1 | A |
| 2 | B |
| 3 | C |
| 4 | D |
| 5 | E |

Vote:

| id | candidateId |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 3 |
| 4 | 2 |
| 5 | 5 |

- **Output:** `[["B"]]`

| name |
|---|
| B |

- **Explanation:** Candidate B receives two votes. Candidates C, D, and E each receive one, while candidate A receives none, so B is the unique winner.

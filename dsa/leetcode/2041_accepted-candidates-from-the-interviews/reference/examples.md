## Examples

**Example 1**

- **Input:** `Candidates = [[11, "Atticus", 1, 101], [9, "Ruben", 6, 104], [6, "Aliza", 10, 109], [8, "Alfredo", 0, 107]], Rounds = [[101, 1, 8], [101, 2, 8], [104, 1, 10], [104, 2, 12], [109, 1, 5], [109, 2, 5], [107, 1, 3], [107, 2, 3]]`

`Candidates` table:

| candidate_id | name | years_of_exp | interview_id |
|---:|---|---:|---:|
| 11 | Atticus | 1 | 101 |
| 9 | Ruben | 6 | 104 |
| 6 | Aliza | 10 | 109 |
| 8 | Alfredo | 0 | 107 |

`Rounds` table:

| interview_id | round_id | score |
|---:|---:|---:|
| 101 | 1 | 8 |
| 101 | 2 | 8 |
| 104 | 1 | 10 |
| 104 | 2 | 12 |
| 109 | 1 | 5 |
| 109 | 2 | 5 |
| 107 | 1 | 3 |
| 107 | 2 | 3 |

- **Output:** `[[9]]`

| candidate_id |
|---:|
| 9 |

- **Explanation:**
  - Candidate 11: `years_of_exp = 1` (< 2), so excluded despite score total of 16.
  - Candidate 9: `years_of_exp = 6` (>= 2), score total $= 10 + 12 = 22$ (> 15). Qualifies.
  - Candidate 6: `years_of_exp = 10` (>= 2), score total $= 5 + 5 = 10$ (not > 15). Excluded.
  - Candidate 8: `years_of_exp = 0` (< 2), score total $= 6$ (not > 15). Excluded.

**Example 2**

- **Input:** `one candidate with years_of_exp = 2 and round scores [8, 8]`
- **Output:** `that candidate's ID`

- **Explanation:** `years_of_exp = 2` satisfies the experience threshold (`years_of_exp >= 2`), and score total 16 > 15 satisfies the score threshold.

**Example 3**

- **Input:** `one experienced candidate with round scores [7, 8]`
- **Output:** `empty result`

- **Explanation:** Score total $7 + 8 = 15$ is not strictly greater than 15, so the candidate is excluded.

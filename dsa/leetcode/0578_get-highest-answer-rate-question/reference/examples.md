## Examples

**Example 1**

- **Input:** `SurveyLog = [[5,"show",285,null,1,123],[5,"answer",285,124124,1,124],[5,"show",369,null,2,125],[5,"skip",369,null,2,126]]`

| id | action | question_id | answer_id | q_num | timestamp |
|---:|---|---:|---:|---:|---:|
| 5 | show | 285 | null | 1 | 123 |
| 5 | answer | 285 | 124124 | 1 | 124 |
| 5 | show | 369 | null | 2 | 125 |
| 5 | skip | 369 | null | 2 | 126 |

- **Output:** `[[285]]`

| survey_log |
|---:|
| 285 |

- **Explanation:** Question `285` is shown once and answered once, giving it an answer rate of `1.0`. Question `369` is shown once and never answered, giving it a rate of `0.0`. Therefore question `285` has the highest answer rate.

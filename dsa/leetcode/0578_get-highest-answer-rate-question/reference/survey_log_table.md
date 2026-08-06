## Survey Log Table

| Column Name | Type |
|---|---|
| `id` | int |
| `action` | ENUM |
| `question_id` | int |
| `answer_id` | int |
| `q_num` | int |
| `timestamp` | int |

The table may contain duplicate rows. `action` is one of `"show"`, `"answer"`, or `"skip"`. Each row records that user `id` performed an action on `question_id` at `timestamp`.

When `action` is `"answer"`, `answer_id` contains that answer's identifier; for the other actions it is `null`. `q_num` is the question's numerical order in the current session.

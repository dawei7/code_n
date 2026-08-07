## Function Contract

**Input**

`SurveyLog(id, action, question_id, answer_id, q_num, timestamp)` contains the recorded survey events. Let $R$ be its row count and $Q$ the number of distinct question identifiers.

Only `"answer"` actions contribute to a rate's numerator and only `"show"` actions contribute to its denominator; `"skip"` actions contribute to neither.

**Return value**

Return a one-row table with a `survey_log` column containing the selected `question_id`.

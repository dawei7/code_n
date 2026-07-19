# Get Highest Answer Rate Question

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 578 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/get-highest-answer-rate-question/) |

## Problem Description
### Goal
Given a `SurveyLog` table of survey interactions, find the question having the highest answer rate. For each `question_id`, define that rate as the number of rows whose action is `answer` divided by the number whose action is `show`; `skip` actions do not increase either count.

Return the selected identifier in a column named `survey_log`. Compare rates rather than raw answer totals, because questions can have different numbers of shows. If multiple questions have the same highest answer rate, choose the one with the smallest `question_id`.

### Function Contract
**Inputs**

- `SurveyLog(id, action, question_id, answer_id, q_num, timestamp)`: survey interaction events whose `action` is `show`, `answer`, or `skip`

**Return value**

- A one-row result grid with column `survey_log` containing the selected `question_id`

### Examples
**Example 1**

- Input: question 1 is answered after two of four shows; question 2 after three of four shows
- Output: `2`

**Example 2**

- Input: questions 3 and 8 both have answer rate `1 / 2`
- Output: `3`

**Example 3**

- Input: one question has shows but no answers
- Output: that question identifier

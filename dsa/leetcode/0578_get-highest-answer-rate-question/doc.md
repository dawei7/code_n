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

### Required Complexity

- **Time:** $O(R \log Q)$
- **Space:** $O(Q)$

<details>
<summary>Approach</summary>

#### General

**Aggregate the two relevant action counts**

Group all log rows by `question_id`. Within each group, conditionally count `answer` actions for the numerator and `show` actions for the denominator. `skip` rows contribute to neither count.

**Compare rates rather than raw answers**

A question shown more often may have more answers but a lower answer rate. Convert one side of the division to a non-integer numeric type so the quotient retains its fractional value.

**Apply the specified tie rule**

Order groups first by descending answer rate and then by ascending `question_id`. The first row is therefore the maximum-rate question, with the smallest identifier chosen when rates match. Alias that identifier as `survey_log`.

**Why the selected group is correct**

Conditional aggregation counts exactly the events named by the rate definition for each question. Dividing those counts yields that question's true answer rate. The lexicographic ordering places every larger rate ahead of every smaller one and resolves only equal rates by identifier, so `LIMIT 1` returns precisely the required question.

#### Complexity detail

For `R` log rows and `Q` distinct questions, aggregation processes all rows and stores $O(Q)$ groups. Ordering the aggregates costs $O(Q \log Q)$, giving $O(R + Q \log Q)$, bounded by $O(R \log Q)$, time and $O(Q)$ space.

#### Alternatives and edge cases

- **Aggregate in a common table expression:** separating rate calculation from ranking can improve readability with the same asymptotic bounds.
- **Window rank:** can rank all computed rates, but only one row is needed and `ORDER BY ... LIMIT 1` is simpler.
- **Correlated count per question:** is correct but can rescan the full log for every question and take $O(QR)$ time.
- **Order by answer count alone:** is incorrect because the denominator may differ between questions.
- **Integer division:** can collapse distinct fractional rates to the same integer; force decimal arithmetic.
- **Skip actions:** affect neither numerator nor denominator.
- **Equal rates:** the smaller `question_id` must win.
- **No answer actions:** produces rate zero when the question has shows.
- **Output alias:** the required column name is `survey_log`, not `question_id`.

</details>

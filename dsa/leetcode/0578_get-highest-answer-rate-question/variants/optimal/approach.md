## General
**Aggregate the two relevant action counts**

Group all log rows by `question_id`. Within each group, conditionally count `answer` actions for the numerator and `show` actions for the denominator. `skip` rows contribute to neither count.

**Compare rates rather than raw answers**

A question shown more often may have more answers but a lower answer rate. Convert one side of the division to a non-integer numeric type so the quotient retains its fractional value.

**Apply the specified tie rule**

Order groups first by descending answer rate and then by ascending `question_id`. The first row is therefore the maximum-rate question, with the smallest identifier chosen when rates match. Alias that identifier as `survey_log`.

**Why the selected group is correct**

Conditional aggregation counts exactly the events named by the rate definition for each question. Dividing those counts yields that question's true answer rate. The lexicographic ordering places every larger rate ahead of every smaller one and resolves only equal rates by identifier, so `LIMIT 1` returns precisely the required question.

## Complexity detail
For `R` log rows and `Q` distinct questions, aggregation processes all rows and stores $O(Q)$ groups. Ordering the aggregates costs $O(Q \log Q)$, giving $O(R + Q \log Q)$, bounded by $O(R \log Q)$, time and $O(Q)$ space.

## Alternatives and edge cases
- **Aggregate in a common table expression:** separating rate calculation from ranking can improve readability with the same asymptotic bounds.
- **Window rank:** can rank all computed rates, but only one row is needed and `ORDER BY ... LIMIT 1` is simpler.
- **Correlated count per question:** is correct but can rescan the full log for every question and take $O(QR)$ time.
- **Order by answer count alone:** is incorrect because the denominator may differ between questions.
- **Integer division:** can collapse distinct fractional rates to the same integer; force decimal arithmetic.
- **Skip actions:** affect neither numerator nor denominator.
- **Equal rates:** the smaller `question_id` must win.
- **No answer actions:** produces rate zero when the question has shows.
- **Output alias:** the required column name is `survey_log`, not `question_id`.

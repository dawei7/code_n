## General

Recovery is anchored to each patient’s earliest positive test, followed by the earliest negative test on a strictly later date. The query computes those two dates in separate grouped CTEs, joins them, and calculates their day difference.

**Earliest positive**

`first_positive` filters rows to `result='Positive'` and groups by patient. `MIN(test_date)` gives one anchor date per patient.

Patients with only negative or inconclusive tests create no row and cannot enter the result.

**Earliest later negative**

The second CTE joins every test `t` to that patient’s positive anchor `p` with:

`t.test_date > p.first_positive_date`.

The strict greater-than condition excludes negatives before the infection evidence and negatives on the same date.

After filtering `t.result='Negative'`, `MIN(t.test_date)` selects the first qualifying recovery evidence. Inconclusive and later positive tests neither qualify nor prevent a later negative.

Grouping produces at most one recovery date per patient. A positive-only patient has no row in this CTE.

**Final joins**

An inner join between the two CTEs keeps only patients having both an earliest positive and a later negative. Joining `patients` attaches name and age.

`DATEDIFF(first_negative_date,first_positive_date)` returns elapsed calendar days. Because the negative date is strictly later, recovery time is positive.

**Why this matches the required anchors**

The statement specifically uses the first positive, not the most recent positive before a negative. Once that date is fixed, the second CTE finds the earliest negative after it.

For a patient with a negative before the first positive, the join date condition rejects that earlier row. For several later negatives, `MIN` selects the first. Every required ordering decision is therefore explicit.

**Ordering**

Results sort by `recovery_time ASC`, placing faster recoveries first, then `patient_name ASC` for equal durations.

No patient ID tie-breaker is requested, so identical names and times may have unspecified relative order.

**Example structure**

A patient with positive January 15, negative January 10, and negative January 25 anchors on January 15. The earlier negative fails the strict join; January 25 becomes the recovery date and `DATEDIFF` returns ten.

## Complexity detail

Let `T` be test rows and `P` patient rows. Filtering and grouping tests can require `O(T\log T)` with sort aggregation, while indexed/hash plans may approach linear expected work. Patient joining and final ordering contribute up to `O(P\log P)`.

A conservative bound is `O(T\log T+P\log P)`. Logical intermediate storage for grouped dates, joins, and output is `O(T+P)` in the broad manifest model.

Indexes on `(result,patient_id,test_date)` or `(patient_id,result,test_date)` can materially affect the physical plan.

## Alternatives and edge cases

- **Correlated subqueries:** Find each patient’s minimum positive and then a correlated minimum negative. It is readable but may repeat scans without good indexes.
- **Window functions:** Ordered conditional dates can solve the problem, but two grouped anchors express the definition directly.
- **Negative before positive:** It is ignored by the strict date join.
- **Negative on the same date:** It is not “later” and is excluded.
- **Multiple positives:** Only the earliest anchors recovery, even if a later positive occurs before the negative.
- **Multiple later negatives:** MIN selects the earliest one.
- **Inconclusive tests:** They are ignored in both CTE filters.
- **Only positive:** Missing second-CTE row excludes the patient.
- **Only negative:** Missing first-CTE row excludes the patient.
- **No tests:** The patient never appears in either aggregate.
- **Equal recovery times:** Name ascending resolves the specified tie.
- **Date arithmetic:** DATEDIFF uses dates rather than subtracting day-of-month numbers, so month and year boundaries work.
- **Inner joins:** They naturally enforce the requirement for catalog identity and both test types.
- **Strict result spelling:** The source compares exact strings `Positive` and `Negative` as provided by the schema.
- **Same-name patients:** They remain separate by unique patient ID even though final tie order is not fully determined.
- **Why the earliest positive is computed first:** Searching for any positive-negative pair and minimizing their gap would answer a different question. The required recovery clock is anchored to the patient’s first positive even when a later positive would yield a shorter interval.
- **Aggregation grain:** Both CTEs group by patient ID, never patient name. Names need not be unique, and grouping by them could merge different people’s medical histories into a false recovery sequence.
- **Positive after recovery:** A later positive does not change the first recovery interval defined by the statement. Once the earliest later negative is selected, subsequent tests are outside this calculation.
- **Database date semantics:** `test_date` is a date rather than a timestamp, so strict comparison and `DATEDIFF` operate in whole calendar days. If time-of-day ordering mattered, the schema and expression would need timestamp precision.
- **Returned age:** Age is read from the patient catalog at query time and does not participate in recovery qualification. Tests establish eligibility and duration; the catalog join supplies descriptive fields only after those medical-date aggregates are fixed.

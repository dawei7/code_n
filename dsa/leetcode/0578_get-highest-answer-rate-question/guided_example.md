# Guided Example: Get Highest Answer Rate Question

`SurveyLog` is an append-only event stream: each row is one interaction, classified by an `action` drawn from a small fixed vocabulary and tagged with the question it concerns. Nothing in the table computes a rate — there is no per-question summary row and no counting column — so the quantity the task asks for exists only as something we construct from the events. This lesson traces the official four-event log, builds the rate as a conditional count over a categorical column, and shows why the ordering needs two keys rather than one.

## 1. The Instance and the Required Outcome

| `id` | `action` | `question_id` | `answer_id` | `q_num` | `timestamp` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | `show` | 285 | absent | 1 | 123 |
| 5 | `answer` | 285 | 124124 | 1 | 124 |
| 5 | `show` | 369 | absent | 2 | 125 |
| 5 | `skip` | 369 | absent | 2 | 126 |

Question 285 was shown once and answered once, so its answer rate is $1/1 = 1.0$. Question 369 was shown once and skipped once, so it was never answered and its rate is $0/1 = 0.0$. The higher rate belongs to 285, and the required output is one row whose column is renamed to `survey_log`:

| `survey_log` |
|:---:|
| 285 |

The rename is part of the contract, not a presentation detail: a result grid carrying the original name `question_id` fails the schema comparison even when the number inside is correct.

## 2. The Rate Function and Its Two Populations

Let $S_q$ be the number of rows with `question_id` $q$ whose `action` is the showing category, and $A_q$ the number of rows for $q$ whose `action` is the answering category. The answer rate is the quotient

$$
\rho_q = \frac{A_q}{S_q},
$$

and the task asks for $\arg\max_q \rho_q$, with the smallest `question_id` breaking a tie. With indicator functions over the event relation,

$$
A_q = \sum_{r \in \text{SurveyLog}} \mathbf{1}\!\left[\,r.\text{question\_id} = q \;\wedge\; r.\text{action} = \text{answer}\,\right],
\qquad
S_q = \sum_{r \in \text{SurveyLog}} \mathbf{1}\!\left[\,r.\text{question\_id} = q \;\wedge\; r.\text{action} = \text{show}\,\right].
$$

Both counts are taken over *disjoint* subpopulations selected by the same categorical column:

| `action` class | Enters the numerator $A_q$? | Enters the denominator $S_q$? | Role in the rate |
|:---:|:---:|:---:|:---|
| showing | no | yes | defines exposure: how often the question was put in front of a user |
| answering | yes | no | defines response: how often the user engaged |
| skipping | no | no | recorded, but excluded from both counts |

The skipping row decides whether a solution measures the right thing. A skip is evidence that the question was seen, yet the denominator counts only the times the question was **shown**, so a skip must not inflate exposure: question 369's skip would give $0/2$ if treated as exposure and $1/2$ if treated as response, both wrong. The payload column is equally irrelevant — only answering rows carry an `answer_id`, so filtering on it happens to select the answering rows here, but the rate is defined by the action category.

> **Ratio invariant.** For every question, $\rho_q$ is determined entirely by the multiset of `action` values attached to it. The responding user, the session ordinal, and the timestamps have no influence on the rate.

## 3. Conditional Counting in One Grouped Pass

The rate needs two counts per question over the same stream, which is the textbook shape for conditional aggregation: partition the events by question and let each partition accumulate one counter per class, advancing by the indicator of the current row's class,

$$
A_q \leftarrow A_q + \mathbf{1}[\text{action} = \text{answer}],
\qquad
S_q \leftarrow S_q + \mathbf{1}[\text{action} = \text{show}],
$$

so each event raises at most one counter and a skipping event raises none. Walking the instance in `timestamp` order:

| Step | `timestamp` | `action` | `question_id` | Numerator change | Denominator change | Accumulated state |
|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 123 | `show` | 285 | unchanged | $S_{285} \to 1$ | $A_{285} = 0,\; S_{285} = 1$ |
| 2 | 124 | `answer` | 285 | $A_{285} \to 1$ | unchanged | $A_{285} = 1,\; S_{285} = 1$ |
| 3 | 125 | `show` | 369 | unchanged | $S_{369} \to 1$ | $A_{369} = 0,\; S_{369} = 1$ |
| 4 | 126 | `skip` | 369 | unchanged | unchanged | $A_{369} = 0,\; S_{369} = 1$ |

Step 4 carries the invariant: the skip leaves both counters untouched, so grouping is complete before any quotient is formed and no question can be ranked on a partially accumulated denominator.

## 4. Ordering by Rate, Then by Identifier

| Rank | `question_id` | $A_q$ | $S_q$ | $\rho_q$ | Primary key | Secondary key | Selected |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 285 | 1 | 1 | 1.0 | highest rate | 285 | **yes** |
| 2 | 369 | 0 | 1 | 0.0 | lower rate | 369 | no |

| Tie scenario | $\rho$ for question 100 | $\rho$ for question 200 | Primary key | Secondary key decides | Reported |
|:---|:---:|:---:|:---:|:---:|:---:|
| Equal rates, distinct identifiers | $1/1 = 1.0$ | $1/1 = 1.0$ | tie | smaller identifier, 100 | 100 |
| Distinct rates | $1/1 = 1.0$ | $2/4 = 0.5$ | 100 wins outright | not consulted | 100 |
| Both zero | $0/1 = 0.0$ | $0/3 = 0.0$ | tie | smaller identifier, 100 | 100 |

Because `question_id` is a key of the grouped relation, the two ordering keys form a total order: two questions can never share an identifier, so equal rates are always separated by the secondary key and the leading row is well defined without reasoning about which tied question is "the" maximum. The third scenario is the degenerate case — with no answers anywhere the rate ordering is constant and the identifier ordering alone still yields one deterministic row.

## 5. Why the Denominator Matters

The official instance cannot distinguish a rate comparison from a raw response count, because both questions have exactly one showing event: $S_{285} = S_{369} = 1$, so ordering by $\rho_q$ coincides with ordering by $A_q$. That coincidence is an accident of the instance's size; the next table separates the two orderings:

| Question | Shows $S_q$ | Answers $A_q$ | Rate $\rho_q$ | Rank by rate | Rank by answer count |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 7 | 1 | 1 | 1.0 | **1** | 2 |
| 8 | 5 | 4 | 0.8 | 2 | **1** |

A method that ranked by responses would report question 8, which collected four answers, while the contract asks for question 7, which has the better rate. The denominator is not decoration: it converts a count into a proportion, and it is the reason the task is about rates at all.

## 6. Correctness of the Rate Maximum and the Tie-Break

The method is correct if it computes every rate exactly and returns the smallest identifier among the maximisers.

*The counts are exact.* Grouping partitions the event relation, so every event belongs to one group and is examined once; the accumulator increments the response counter precisely on answering rows and the exposure counter precisely on showing rows, and rows of the third class increment neither. No count can be distorted by skipped events.

*The comparison is a genuine rate comparison.* Both quotients share the same structure, so comparing them compares response-to-exposure proportions rather than raw counts.

*The reported question maximises the rate.* Ordering by rate descending places a maximiser first, and because identifiers are unique any other maximiser must have a strictly larger identifier to appear later. Every question in the log has a group and hence a rate, so no candidate is overlooked.

One arithmetic subtlety is a correctness hazard rather than a style preference: comparing rationals is not the same as comparing their integer parts. If the quotient is evaluated with integer division, $1/2$ and $0/2$ both become $0$, so genuinely different rates become indistinguishable and the secondary key rather than the rate decides between them. A faithful comparison either keeps the division real or evaluates the cross-product test $A_q S_{q'} > A_{q'} S_q$, which orders the ratios without forming them.

## 7. Boundary Cases and Failure Modes

| Situation | Behaviour | Result |
|:---|:---|:---|
| Two questions share the maximum rate | the secondary key orders them | the smaller `question_id` is reported |
| Every question has rate 0.0 | the primary key is constant | the smallest `question_id` is reported |
| A question is shown but never answered | numerator 0, denominator positive | rate 0.0; it can only win a tie |
| A question has skip events | skips are excluded from both counts | the rate is unaffected by skipped events |
| A question is answered more often than shown | the quotient exceeds 1 | the rate is not clamped; the definition is applied literally |
| A question has only skipping events | the exposure count is 0 | the rate is undefined, so the guarantee that each question was shown at least once must hold |
| Integer division used for the quotient | distinct rates can truncate to the same value | the ordering silently changes, as section 6 describes |
| The projected column is not renamed | the value is right, the schema is not | the result is rejected on the column name |

The undefined-denominator row is the only genuine precondition: a defensive implementation needs a decision about a question seen only through skips, and the contract offers none.

## 8. Alternative Strategies and Their Trade-offs

| Strategy | Relational shape | Cost | Assessment |
|:---|:---|:---|:---|
| One grouped pass with two conditional counters | partition by question, accumulate both counts, order by rate then identifier | $\Theta(N + K \log K)$ | the method traced above; one scan of the log |
| Counting rows per question as exposure | divide responses by every row for that question | $\Theta(N + K \log K)$ | wrong metric: skips enter the denominator and depress genuine rates |
| Rank by response count instead of rate | order the numerators | $\Theta(N + K \log K)$ | wrong metric whenever denominators differ, as section 5 shows |
| Two filtered counts combined by a join | count answering and showing rows separately, then join on the identifier | two scans plus a join over $K$ groups | same asymptotics, more intermediate state |
| Correlated count per question | probe the log twice for each question | $\Theta(K \cdot N)$ without an index, $\Theta(K \log N)$ with one | correct, but scales with the product of questions and events |
| Single-pass running maximum with the compound key | keep the best rate and identifier as groups complete | $\Theta(N + K)$ | removes the ordering term; the comparison must be lexicographic in rate and identifier |

Here $N$ is the number of events and $K$ the number of distinct questions. The last row shows the ordering is a convenience rather than a requirement: as each group completes, its rate is compared against the best so far, and an equal rate is resolved in favour of the smaller identifier.

## 9. Complexity Derivation

Let $N$ be the number of rows in `SurveyLog` and $K$ the number of distinct question identifiers.

- **Time.** The grouped pass reads every event once and performs a constant number of accumulator updates per row, which is $\Theta(N)$. Ordering the $K$ groups by the compound key costs $\Theta(K \log K)$ comparisons, or $\Theta(K)$ with a running maximum. Total: $\Theta(N + K \log K)$, and $\Theta(N + K)$ when the maximum is found by streaming. Since $K \le N$, the bound is never worse than $\Theta(N \log N)$.
- **Auxiliary space.** The accumulator holds two integers per distinct question, so $\Theta(K)$ working memory, and the result is a single row. The event stream is consumed in order and never buffered.

For the official instance $N = 4$ and $K = 2$: four events are read, two accumulator pairs are maintained, two groups are ordered, and one row is projected.
# Guided Example: Reward Top K Students

## 1. How a report becomes a score

Each report is a sentence: lowercase words separated by single spaces. The score
of a student is the sum of the per-word contributions inside their one report,
where a word contributes $+3$ if it appears in `positive_feedback`, $-1$ if it
appears in `negative_feedback`, and $0$ otherwise. Writing a report as a sequence
of words $w_1, w_2, \dots, w_t$, its score is

$$
\text{score}(r) = \sum_{q=1}^{t} c(w_q), \qquad
c(w) = \begin{cases} +3 & w \in P \\ -1 & w \in N \\ 0 & \text{otherwise} \end{cases}
$$

with $P$ and $N$ the two given word sets. The statement guarantees $P \cap N =
\emptyset$, so no word can trigger both branches and the contribution function is
well defined.

Three properties of this definition drive everything that follows:

1. **Occurrences, not distinct words.** A word repeated three times contributes
   three times. Multiplicity is part of the rule.
2. **Membership, not appearance.** A word contributes something only if it is
   *in the supplied list*. A word that merely looks like praise is worth nothing
   when the list does not contain it.
3. **Whole-word matching.** A report is split into its words; the match is against
   a whole token, never against a substring of one. So a negative word embedded in
   a longer word is not a negative word.

Membership must be tested in an average-constant-time structure. With up to
$10^{4}$ list entries, a linear scan per report word would make the total work
quadratic in the input size, so both lists are converted to hash sets once, before
any report is scored.

## 2. Worked trace of the official second instance

The statement's second example is the one where the ranking changes:

$$
P = [\texttt{"smart"}, \texttt{"brilliant"}, \texttt{"studious"}], \quad
N = [\texttt{"not"}], \quad
\texttt{report} = [\texttt{"this student is not studious"}, \texttt{"the student is smart"}],
$$

with `student_id = [1, 2]`. Score the first report word by word.

| Word position | Word | In $P$? | In $N$? | Contribution | Running score |
|:---:|:---|:---:|:---:|:---:|:---:|
| 1 | `this` | no | no | 0 | 0 |
| 2 | `student` | no | no | 0 | 0 |
| 3 | `is` | no | no | 0 | 0 |
| 4 | `not` | no | yes | -1 | -1 |
| 5 | `studious` | yes | no | +3 | 2 |

Student 1 therefore ends with 2 points: one positive word worth 3 and one negative
word worth 1. The second report, `the student is smart`, contains the words `the`,
`student`, `is`, `smart`, of which only `smart` is listed, so student 2 scores
`+3 = 3`. The aggregation table for both students is:

| Student ID | Report | Positive words | Negative words | Score |
|:---:|:---|:---:|:---:|:---:|
| 1 | `this student is not studious` | `studious` (one occurrence) | `not` (one occurrence) | $3 - 1 = 2$ |
| 2 | `the student is smart` | `smart` (one occurrence) | none | $3$ |

Since $3 > 2$, student 2 outranks student 1 and the answer is `[2, 1]`, matching
the official explanation. Note that the raw counts of words are irrelevant:
student 1's report is longer, yet it scores lower because length carries no
reward — only listed words do.

## 3. The ranking rule and its lexicographic key

Ranking is not a single comparison but a two-level order, and the natural way to
express it is as a sort key per student, from a pair (score, id):

$$
\text{key} = (-\text{score},\; \text{id}),
$$

compared lexicographically in ascending order. Negating the score turns
"non-increasing by points" into "increasing by key", and the ID is the plain
ascending tie-breaker the statement requires. The exact same order could be
described as: higher score first; among equal scores, lower ID first.

| Student ID | Score | Key $(-\text{score}, \text{id})$ | Rank |
|:---:|:---:|:---:|:---:|
| 1 | 2 | $(-2, 1)$ | 2 |
| 2 | 3 | $(-3, 2)$ | 1 |

Taking the first $k$ entries of that order gives `[2, 1]` for $k = 2$. Because
$1 \le k \le n$, the result always has exactly $k$ entries: there is no case in
which fewer students qualify, even when many scores are zero or negative.

The statement also says IDs are unique, which matters more than it appears. If two
students could share an ID, the key would not be a strict total order; ties would
be genuinely ambiguous rather than resolved by the second component. Uniqueness
turns the key into a total order, so the sorted sequence — and therefore the
selected top $k$ — is uniquely determined.

## 4. The two official samples, contrasted

The pair of official examples is deliberately chosen to isolate the tie-break
from the score comparison: the only difference between them is the word `not`
inserted into the first report.

| Instance | Student 1 score | Student 2 score | Deciding level | Output |
|:---|:---:|:---:|:---|:---|
| official sample 1 | $3$ | $3$ | equal scores, so the lower ID wins | `[1, 2]` |
| official sample 2 | $3 - 1 = 2$ | $3$ | distinct scores, so the score wins | `[2, 1]` |

In the first sample both reports hold exactly one listed positive word, so both
students score 3 and the ID decides the order. In the second sample the inserted
`not` drops student 1 to 2, and the ID tie-breaker becomes irrelevant. A method
that sorts by score alone passes sample 2 and fails sample 1; a method that sorts
by ID alone passes sample 1 and fails sample 2. Only the two-level key satisfies
both.

## 5. The decisive trap: a word scores only if it is listed

The authored boundary case `trial-boundary-8` narrows `positive_feedback` to the
single word `smart` while keeping the same two reports. The word `studious`
vanishes from the positive list, and the ranking flips.

| Report word | List it is checked against | Member? | Contribution | Effect on the student |
|:---|:---|:---:|:---:|:---|
| `studious` | $P = [\texttt{"smart"}]$ | no | 0 | student 1 ends at 0, not 3 |
| `smart` | $P = [\texttt{"smart"}]$ | yes | +3 | student 2 ends at 3 |
| `not` | $N = [\texttt{"not"}]$ | yes | -1 per occurrence | only relevant when present in a report |

Student 1 now has no listed word at all and scores 0, while student 2 still scores
3, so the answer is `[2, 1]` for a completely different reason than in official
sample 2. The lesson is that "positive-looking" is not a property of a word — it
is a property of the *input lists*, which change from instance to instance. The
companion boundary case `trial-boundary-9` repeats the entry `smart` twice in
`positive_feedback` and expects the identical answer `[2, 1]`, confirming that a
duplicate list entry adds nothing: membership is a yes/no test, and each report
occurrence is still worth exactly 3 points.

The same membership principle creates two related traps that the authored cases
cover. In `trial-repeated-feedback`, the report `great great` scores 6, not 3, so
counting *distinct* listed words instead of *occurrences* gives the wrong order.
And in `trial-score-before-id`, the student with ID 900 (score 3) outranks the
student with ID 3 (score 2), which outranks the student with ID 1 (score -1):
sorting by ID first, or treating the score as a tie-break, produces `[1, 3]`
instead of `[900, 3]`.

## 6. Boundary and edge cases

| Instance | Input condition | Expected | Deciding reason |
|:---|:---|:---:|:---|
| all reports neutral | `ordinary`, `plain`, `average` with no listed words | `[10, 20]` | every score is 0, so the ID tie-break orders the whole field |
| repeated words | `great great` versus `great poor` | `[8, 2]` | occurrences count, not distinct words |
| negative scores | scores $-1$ and $-2$ exist | `[2, 9, 4]` | non-increasing order still applies below zero |
| score beats ID | IDs 1, 3, 900 with scores $-1$, 2, 3 | `[900, 3]` | score is the primary key, ID only the tie-break |
| single student | one report and $k = 1$ | `[999999999]` | the result always has exactly $k$ entries |
| duplicate list entries | `smart` listed twice | `[2, 1]` | list membership is idempotent |
| maximum ID | `999999999` | ranked normally | compare IDs numerically, never as strings |
| $k = n$ | every student selected | full ordering | the truncation is a prefix, not a filter |

Two of these deserve emphasis. First, scores can be negative and the ordering is
still descending, so an implementation that clamps negative scores to zero — a
plausible "points cannot go below zero" misreading — changes the order of the
negative-scoring students. Second, IDs reach $10^{9}$, so they must be compared
as integers; lexicographic comparison of decimal strings would order `"9"` above
`"10"` and scramble every tie.

## 7. Correctness: the scoring invariant and the total order

Two separate claims need support: the score computed for each student is the one
the statement defines, and the sorted prefix really is the top $k$.

> **Scoring invariant.** After processing a report word by word, the running total
> equals the sum of the contributions of the words processed so far.

The invariant holds initially (both are zero) and is preserved by each step,
because the contribution added is exactly the function $c$ applied to the current
word: $+3$ when the word is in $P$, $-1$ when it is in $N$, and $0$ otherwise.
Since $P \cap N = \emptyset$ the three cases are mutually exclusive, so no word is
double-counted or misrouted. Splitting the report on spaces enumerates each word
exactly once per occurrence, which is what makes the sum equal the defined
$\text{score}(r)$ rather than a distinct-word variant. At the end of the report
the running total is therefore the score, and pairing it with the student's ID
records the complete per-student state.

> **Ordering claim.** Sorting by the key $(-\text{score}, \text{id})$ and taking
> the first $k$ entries returns the top $k$ students.

Ascending order on $-\text{score}$ is descending order on the score, so any
student with a strictly higher score precedes any student with a lower one.
Among equal scores the key falls back to the ID in ascending order, exactly as
required. Since IDs are unique the key is a strict total order: the sorted
sequence is unique, every student appears in it once, and the first $k$ entries
are simultaneously the $k$ highest-scoring students and, where scores tie, the
$k$ smallest IDs among them. The back-to-front check also holds: any student left
outside the prefix has either a lower score than every selected student or an
equal score and a larger ID, so it cannot belong in the top $k$.

## 8. Alternatives and their failure modes

| Approach | How it works | Time | Auxiliary space | Failure mode |
|:---|:---|:---|:---|:---|
| Hash sets plus full sort | build both sets, score every report, sort by $(-\text{score}, \text{id})$, take $k$ | $O(W + n \log n)$ | $O(n + \lvert P \rvert + \lvert N \rvert)$ | none; this is the method traced above |
| Linear membership scan | check each report word against both lists as arrays | $O(W \cdot (\lvert P \rvert + \lvert N \rvert))$ | $O(n)$ | correct but quadratic in the list sizes; up to $10^{4}$ comparisons per word |
| Distinct-word counting | add each listed word once even when it repeats | $O(W + n \log n)$ | $O(n)$ | wrong on `great great`, which must score 6, not 3 |
| Substring search | test whether a listed word occurs anywhere in the report string | $O(W')$ with string scanning | $O(n)$ | wrong: a listed word nested inside a longer word would be counted, which whole-word matching forbids |
| Heap of size $k$ | keep the best $k$ keys in a bounded priority queue | $O(W + n \log k)$ | $O(k + \lvert P \rvert + \lvert N \rvert)$ | correct and asymptotically tighter, but $n \le 10^{4}$ makes the plain sort simpler and equally fast in practice |
| Sort by score only, or by ID first | single-level ordering | $O(n \log n)$ | $O(n)$ | fails one of the two official samples, whichever level is dropped |

## 9. Complexity: time and auxiliary space

Let $n$ be the number of reports, $n = \texttt{report.length} =
\texttt{student\_id.length}$, and let $W$ be the total number of words across all
reports, bounded by $50n$ because each report is at most 100 characters with
single-space separators.

**Time.** Building the two hash sets costs $O(\lvert P \rvert + \lvert N \rvert)$
expected. Scoring walks every word of every report exactly once; each word
performs at most two constant-time membership tests, so scoring is $O(W)$
expected, or $O(W \log(\lvert P \rvert + \lvert N \rvert))$ under a strict
worst-case reading of hashing. Sorting $n$ keys of constant size costs $O(n \log
n)$ comparison steps, each comparing two integers on the first level and two on
the second, and the final prefix extraction is $O(k)$. The total is

$$
O\bigl(\lvert P \rvert + \lvert N \rvert + W + n \log n\bigr),
$$

which for $n = 10^{4}$ reports of at most 50 words each means about $5 \cdot
10^{5}$ word evaluations and roughly $1.3 \cdot 10^{5}$ comparisons — trivial for
the stated limits.

**Auxiliary space.** The two sets store $O(\lvert P \rvert + \lvert N \rvert)$
entries, the per-student key list stores $O(n)$ pairs, and the sort itself needs
$O(n)$ for the temporary buffer used by the standard merge strategy. The returned
list holds $k$ IDs. Nothing per-report is retained once its score is folded into
the key, so no copy of the reports is materialized and the space bound is
$O(n + \lvert P \rvert + \lvert N \rvert + k)$.

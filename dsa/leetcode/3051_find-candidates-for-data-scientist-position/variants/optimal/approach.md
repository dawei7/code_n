## General

**Remove irrelevant rows before grouping.** Keep only rows whose `skill` is
one of `Python`, `Tableau`, or `PostgreSQL`. Other skills cannot satisfy a
requirement and do not need to participate in the aggregation.

**Count the required proficiencies per candidate.** Group the filtered rows by
`candidate_id` and retain a group only when `COUNT(DISTINCT skill) = 3`.
Because the filter admits exactly the three required names, a distinct count
of three proves that all three are present. Conversely, every candidate with
all three required skills contributes those three distinct values and passes
the condition. Additional unrelated skills were removed and therefore neither
help nor harm the candidate.

Finally, sort the retained IDs in ascending order to make the required output
deterministic.

## Complexity detail

Let $n$ be the number of skill rows and $c$ the number of qualifying
candidates. Filtering and hash aggregation take expected $O(n)$ time, and
sorting the output costs $O(c\log c)$, for $O(n+c\log c)$ expected time. The
grouped distinct-skill state uses $O(c)$ space because at most three relevant
skills are retained per candidate. Physical database plans and indexes can
change constants.

## Alternatives and edge cases

- **Three self-joins:** Joining separate `Python`, `Tableau`, and `PostgreSQL` rows is correct, but repeats the table access and is more verbose than one grouped scan.
- **Three correlated `EXISTS` clauses:** This expresses the contract directly but may probe the table repeatedly for every candidate without a supporting index.
- **Plain row count without filtering:** A candidate with any three unrelated skills could pass incorrectly; only required skill names may contribute.
- The three skill strings are exact and case-sensitive according to their stored values; `Postgres` is not `PostgreSQL`.
- Extra skills do not disqualify a candidate.
- Required skills recorded for different candidates cannot be combined.
- With no qualifying candidate, the result is empty.
- Numeric IDs require numeric ascending order, so 2 precedes 10.

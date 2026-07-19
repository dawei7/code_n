## General
**Filter candidates by the row-level requirement**

Join `Candidates` to `Rounds` on `interview_id`. Apply
`years_of_exp >= 2` before aggregation so candidates who cannot qualify do not
need to contribute groups. The inclusive comparison is important: exactly two
years meets the requirement.

**Aggregate all rounds for each candidate**

Group the joined rows by `candidate_id` and compute `SUM(score)` for each
candidate. Grouping by the candidate key, rather than returning an interview
identifier, preserves the requested output identity and remains correct even
if multiple candidate rows refer to the same interview.

**Apply the strict aggregate threshold**

Aggregate conditions belong in `HAVING`, so retain only groups satisfying
`SUM(score) > 15`. An inner join also naturally excludes a candidate with no
matching round. Finally, select only `candidate_id`. Adding `ORDER BY
candidate_id` gives deterministic app output while remaining compatible with
the contract's any-order allowance.

Every output row came from an experienced candidate and passed the complete
round-score sum, so it is valid. Conversely, every candidate satisfying both
requirements joins to all of that interview's rounds, forms a group whose sum
passes `HAVING`, and is returned. This proves the result contains exactly the
accepted candidates.

## Complexity detail
With standard hash or indexed join and grouping support, reading both tables
costs $O(C+R)$ expected work. Ordering as many as $C$ result groups costs
$O(C\log C)$ time. Join and grouping structures may occupy $O(C+R)$ space;
exact physical costs depend on the database optimizer and available indexes.

## Alternatives and edge cases
- **Pre-aggregate rounds first:** A derived table grouped by `interview_id`
  can be joined to eligible candidates and has the same semantics.
- **Correlated score subquery:** Summing `Rounds` separately for each candidate
  is concise but can rescan the round table and take $O(CR)$ time without a
  supporting index.
- Exactly two years of experience qualifies; one year does not.
- A score total of exactly `15` is excluded, while `16` qualifies.
- A candidate without matching round rows cannot have a qualifying sum.
- Multiple rounds from one interview must be summed before filtering.
- Multiple candidates may refer to the same interview and must still produce
  separate candidate rows when eligible.

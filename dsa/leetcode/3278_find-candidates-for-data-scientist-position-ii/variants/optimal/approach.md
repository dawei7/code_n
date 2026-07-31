## General

**Build only skill matches**

First count the required skills for each project. Join `Projects` to `Candidates` on equal `skill`, so every joined row represents one requirement that a candidate actually covers. Group these matches by project and candidate.

Within each group, add `10`, `-5`, or `0` according to the comparison between `proficiency` and `importance`, then add the base score of `100` once. Because both source tables make their owner-skill pairs unique, the number of joined rows in a group is exactly the number of distinct project requirements that candidate covers.

Compare that matched count with the project's required-skill count in `HAVING`. Equality proves complete coverage; a smaller count identifies a missing skill and removes the pair. Projects with no complete group disappear naturally.

**Apply the winner rules after eligibility**

Use `ROW_NUMBER()` within each project, ordering first by `score DESC` and then by `candidate_id ASC`. The first row is exactly the highest-scoring suitable candidate with the specified tie-break. Filter to that row and order the remaining projects by ID.

## Complexity detail

Let $J$ be the equal-skill join size. With ordinary indexed or sort-based relational operators, scanning, joining, grouping, and window ordering take $O((C+P+J)\log(C+P+J))$ time and $O(C+P+J)$ working space. Exact constants and access paths remain database-engine dependent.

## Alternatives and edge cases

- **Cross join every skill row:** Pairing all candidate skills with all project skills before testing names is correctable, but creates a quadratic intermediate that the equality join avoids.
- **Require at least one matching skill:** Partial coverage is insufficient; the matched count must equal the project's entire requirement count.
- **Rank before filtering coverage:** A high-scoring but incomplete candidate must never displace a suitable candidate.
- A proficiency equal to importance contributes exactly zero, not a bonus.
- Score adjustments are applied once per required skill, while the base `100` is added once per candidate-project pair.
- Multiple candidates can tie in score; the numerically smaller candidate ID wins.
- A project without any suitable candidate contributes no output row.
- Extra candidate skills that a project does not require neither help nor hurt its score.

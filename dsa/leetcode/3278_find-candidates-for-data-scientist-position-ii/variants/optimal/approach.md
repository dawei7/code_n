## General

The query first builds candidate-project matches through shared skills, rejects pairs missing any required skill, calculates scores, and then selects one winner per project with the required tie-break.

CTE `S` joins `Candidates` and `Projects` with `USING (skill)`. A row exists only when a candidate possesses a skill required by a project. Because both tables have unique keys on their candidate/project plus skill combinations, each matching skill contributes exactly one joined row to that candidate-project group.

`COUNT(*) AS matched_skills` counts how many of the project's requirements this candidate matches. Extra candidate skills that the project does not request never join and do not affect the count or score.

The `CASE` expression awards ten when proficiency exceeds importance, subtracts five when it is lower, and contributes zero when equal. Summing these adjustments and adding one hundred implements the complete score formula once per candidate-project group.

CTE `T` counts `required_skills` separately for every project. Joining `S` to `T` and filtering `matched_skills = required_skills` proves the candidate has every required skill. Since matched rows cannot exceed unique project requirements, equality means complete coverage rather than merely a coincidental count.

CTE `P` ranks only eligible candidates within each project. Its window order is `score DESC, candidate_id`. Higher score comes first, and lower identifier breaks an equal-score tie.

Although the function used is `RANK`, including unique `candidate_id` in the ordering means no two candidates for a project have identical complete ordering keys. Exactly one row receives rank one. In this query, `ROW_NUMBER` would produce the same winner.

The outer query keeps `rk = 1` and projects project, candidate, and score. Projects with no fully skilled candidate never produce a `P` row and are correctly omitted. `ORDER BY 1` arranges project identifiers ascending.

For project 501, candidates are grouped only over Python, Tableau, and PostgreSQL. Candidate 101 matches all three and receives adjustments based on each proficiency comparison. If other eligible candidates tie its score, candidate 101 wins through the lower identifier ordering.

**Why filtering after aggregation matters.** Filtering individual joined rows cannot determine full project coverage. The query must count matches for the complete candidate-project group and compare against the project's independently counted requirements.

**Why the score is not computed for missing skills.** Such a candidate is ineligible regardless of partial score. `S` may temporarily calculate a partial score, but the completeness filter removes it before ranking.

The query is correct because unique skill rows make both counts exact, equality enforces the all-skills condition, the grouped `CASE` sum implements scoring, and the window's total order selects the unique required winner.

## Complexity detail

Let $C$ and $P$ be candidate-skill and project-skill row counts, and $J$ the number of equal-skill join rows. Grouping and window ranking generally require hashing or sorting, with a broad bound of $O((C+P+J)\log(C+P+J))$ time and $O(C+P+J)$ working space.

Actual performance depends on MySQL's indexes and join plan. Indexes beginning with `skill` improve the equality join, while project/candidate grouping may use temporary tables.

The final output contains at most one row per project.

## Alternatives and edge cases

- **Relational division with `NOT EXISTS`:** Reject a candidate when any project skill lacks a candidate match. This expresses “has all skills” directly but scoring still needs matched rows.
- **Compare counts without unique keys:** It could be unsafe if duplicate skill rows existed. The declared keys make the count equality proof valid.
- **`ROW_NUMBER`:** It more directly signals one winner and is equivalent because candidate identifier makes the ordering unique.
- **Rank by score only:** Then all score ties receive rank one and multiple candidates would be returned, violating the lower-ID rule.
- **Candidate has extra skills:** They do not join to that project's requirements and neither help nor hurt.
- **Exact proficiency match:** The `ELSE 0` branch leaves the starting score unchanged for that skill.
- **No eligible candidate:** The project is absent, as required.
- **One required skill:** Coverage equality reduces to possessing that one skill, and scoring still works.
- **Negative adjustment total:** Starting at one hundred does not prevent a score below one hundred when several skills are underqualified.
- **Identifier tie-break:** Candidate IDs are distinct for separate candidates, so the window order is deterministic.
- **Project with no requirements:** Such a project would have no `Projects` rows and cannot appear in this schema-driven query; the intended data represents projects through required skills.
- **Why `COUNT(*)` equals distinct matched skills:** The composite keys prohibit duplicate candidate-skill and project-skill rows. Their equality join can therefore produce at most one row for a particular candidate, project, and skill.
- **Score base added once:** The expression places `+ 100` outside `SUM`. Putting one hundred inside the sum would incorrectly add the starting score once per required skill.
- **Proficiency scale endpoints:** Values one through five need no normalization. The score depends only on greater, equal, or less comparisons, not the magnitude of the difference.
- **Candidate absent from one skill:** Their group has fewer joined rows than `required_skills` and is removed even if their partial score would otherwise be highest.

## General

Let $t$ be the number of rows in \`TeamStats\`.

**Score before ranking**

Use a common table expression to calculate each team's points as \`wins * 3 + draws\`. Losses and \`matches_played\` remain part of the source record but do not enter the score. Naming the derived \`points\` column once keeps ranking, tiering, and final ordering consistent.

**Attach global ranking information**

In a second query layer, apply \`RANK() OVER (ORDER BY points DESC)\`. \`RANK\`, unlike \`ROW_NUMBER\`, gives equal point totals the same competition position and leaves the required gap after a tie. In the same layer, \`COUNT(*) OVER ()\` places the total team count on every row without collapsing the league into a grouped result.

The rounded-up Tier 1 and Tier 2 boundaries are \`CEIL(team_count * 0.33)\` and \`CEIL(team_count * 0.66)\`. Classify a row by comparing its competition position with those boundaries in order. Since every team with equal points receives the same position, every member of a boundary tie takes the same, higher tier automatically.

Finally, order by \`points DESC, team_name ASC\`. Ranking depends only on points; the name is a deterministic presentation tiebreaker and must not split a shared position.

The score expression follows the stated point rules. The ranking window therefore assigns precisely the required position to every score, and the count window supplies the correct population for both boundaries. The ordered \`CASE\` chooses the first boundary containing that position, so it implements all three tiers and the higher-tier tie rule.

## Complexity detail

Scoring and classification are linear passes over $t$ rows. The rank window and final requested order require sorting by points and name, giving $O(t \log t)$ time in the general case. Window and sort state can retain $O(t)$ rows.

## Alternatives and edge cases

- **Correlated rank subquery:** Counting teams with higher points separately for every row reproduces competition rank but can take $O(t^2)$ time.
- **\`DENSE_RANK\`:** Dense ranking removes gaps after ties and therefore produces incorrect positions.
- **\`ROW_NUMBER\`:** Numbering individual tied rows assigns different positions and can split a tie across tiers.
- **\`NTILE(3)\`:** Dividing rows directly can place equal point totals in different tiers, violating the boundary rule.
- All tied teams share one position and tier, even if the tie makes a tier contain more than 33% of the rows.
- A one-team league puts that team at position 1 in Tier 1.
- Zero-point teams are ranked normally and ordered alphabetically within their tie.
- \`team_id\` does not participate in the output ordering.
- The two tier thresholds use the total number of teams, not the number of distinct point totals.

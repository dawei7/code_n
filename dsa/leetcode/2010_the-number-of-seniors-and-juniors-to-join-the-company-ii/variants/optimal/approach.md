## General
**Compute the cost of every salary prefix.** Partition candidates by
`experience`, order each partition by `salary`, and use a windowed cumulative
sum. A candidate's `running_salary` is therefore the exact cost of hiring that
candidate together with every cheaper candidate from the same category.

**Reserve the senior spending before filtering juniors.** Among senior rows
whose cumulative salary does not exceed $70{,}000$, the maximum cumulative
value is the amount committed to seniors; use zero when no senior qualifies.
Return all such senior rows. A junior qualifies when its own cumulative salary
does not exceed `70000 - senior_spending`.

Because salaries are unique, ascending order defines one unambiguous prefix
per category. The company rules hire exactly the longest affordable senior
prefix, then the longest junior prefix under the remainder. The two cumulative
conditions select precisely those prefixes, so every returned ID is hired and
every omitted candidate is either beyond the first unaffordable prefix or
belongs to no affordable prefix.

## Complexity detail
Here $R$ is the number of candidate rows. Partitioned ordering for the window
sum takes $O(R\log R)$ time; the remaining aggregation and filtering are
linear. The ranked intermediate relation contains $R$ rows and uses $O(R)$
space.

## Alternatives and edge cases
- **Correlated prefix sums:** Recomputing the total of every cheaper candidate
  for each row is correct but can require $O(R^2)$ row comparisons.
- **Procedural salary loop:** Repeatedly querying the next cheapest candidate
  mirrors the story but introduces unnecessary iterative database round trips.
- If no senior fits, senior spending is zero and juniors use the entire
  budget.
- If seniors spend exactly $70{,}000$, no junior can be returned.
- The result may be empty when neither category has an affordable first
  candidate.

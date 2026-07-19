## General
**Form the exact reporting groups**

Group rows by both `date_id` and `make_name`. Neither column alone is sufficient: grouping only by date would merge different products, while grouping only by make would combine separate days. Each distinct pair produces exactly one output row.

**Count each identifier domain independently**

Within a group, apply `COUNT(DISTINCT lead_id)` and name it `unique_leads`. Apply a separate `COUNT(DISTINCT partner_id)` and name it `unique_partners`. SQL's distinct aggregate removes repeated identifiers before counting, so duplicated source rows and repeated leads or partners do not inflate the corresponding result.

The two aggregates must not be replaced by a distinct count of `(lead_id, partner_id)`: one lead may be associated with several partners, and each requested column asks for the cardinality of only its own identifier set. Because the contract permits any row order, no `ORDER BY` is needed.

## Complexity detail
A hash aggregation inspects the $R$ input rows once and updates the date-and-make group's two distinct sets, taking expected $O(R)$ time. Across all groups, at most $R$ distinct lead entries and $R$ distinct partner entries are stored, so auxiliary space is $O(R)$. The database engine may choose another equivalent physical plan.

## Alternatives and edge cases
- **Pre-deduplicate full rows:** a `SELECT DISTINCT` subquery remains correct but is unnecessary because each aggregate already removes duplicates in its own column.
- **Count distinct identifier pairs:** this answers a different question and can exceed either requested individual count.
- **Group by date only:** makes sold on the same day would be incorrectly merged.
- **Group by make only:** sales of the same make on different dates would be incorrectly merged.
- **Duplicate rows:** exact duplicates contribute only one value to each distinct identifier set.
- **Repeated lead with new partners:** `unique_leads` stays unchanged while `unique_partners` grows.
- **Output order:** the problem accepts any order, so sorting is not part of the required query.

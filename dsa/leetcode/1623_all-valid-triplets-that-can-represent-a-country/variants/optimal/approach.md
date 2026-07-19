## General
**Generate one member from every school.** Cross join `SchoolA`, `SchoolB`, and `SchoolC`. Each resulting row corresponds to exactly one possible ordered choice $(A,B,C)$, and every possible cross-school triplet appears once.

**Enforce pairwise identity differences.** Apply all three ID inequalities: A versus B, A versus C, and B versus C. Apply the same three comparisons to the student names. Checking only adjacent schools would miss a collision between A and C, so all pairwise relations are necessary.

**Project the requested names.** Select the three student-name fields with the exact aliases `member_A`, `member_B`, and `member_C`. A surviving row satisfies every validity rule. Conversely, any valid triplet appears in the Cartesian product and passes all six comparisons, so the query is complete.

## Complexity detail
The Cartesian product contains $abc$ candidate triplets, and each receives a constant number of comparisons, giving $O(abc)$ time. In the worst case all IDs and names are distinct across schools, so all $abc$ rows must be emitted; the result itself then occupies $O(abc)$ space. Database engines may stream rows or use different join plans, but cannot avoid the worst-case output size.

## Alternatives and edge cases
- **Three inner joins with inequality predicates:** This is logically equivalent, but a cross join followed by the six validity predicates states the all-combinations contract more directly.
- **`NOT IN` subqueries:** Filtering each school separately cannot express whether the three simultaneously chosen rows are pairwise compatible without reconstructing their combinations.
- **Compare only IDs:** Equal names with different IDs still invalidate a triplet.
- **Compare only names:** Equal IDs with different names also invalidate a triplet.
- A collision between schools A and C must be rejected even when both differ from school B.
- If any school has no rows, the Cartesian product and result are empty.
- Different valid triplets may share one member; validity is assessed within each returned triplet.

# All Valid Triplets That Can Represent a Country

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1623 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/all-valid-triplets-that-can-represent-a-country/) |

## Problem Description
### Goal
Tables `SchoolA`, `SchoolB`, and `SchoolC` list students by `student_id` and `student_name`. Form a country-representing triplet by choosing exactly one student from each school.

A triplet is valid only when its three student IDs are pairwise different and its three student names are also pairwise different. Return every valid combination, showing the chosen names from schools A, B, and C as `member_A`, `member_B`, and `member_C` respectively.

### Function Contract
**Inputs**

- `SchoolA(student_id, student_name)`: candidate members from school A.
- `SchoolB(student_id, student_name)`: candidate members from school B.
- `SchoolC(student_id, student_name)`: candidate members from school C.
- Let $a$, $b$, and $c$ be the respective table row counts.

**Return value**

Return one row per valid cross-school triplet with columns `member_A`, `member_B`, and `member_C`. Row order is not semantically significant.

### Examples
**Example 1**

- Input: `SchoolA = [[1,"Alice"],[2,"Bob"]]`, `SchoolB = [[3,"Tom"]]`, `SchoolC = [[3,"Tom"],[2,"Jerry"],[10,"Alice"]]`
- Output: `[ ["Alice","Tom","Jerry"], ["Bob","Tom","Alice"] ]`

**Example 2**

- Input: one student in each school with distinct IDs and names
- Output: the one corresponding triplet

**Example 3**

- Input: every possible choice repeats an ID or a name
- Output: no rows

### Required Complexity
- **Time:** $O(abc)$
- **Space:** $O(abc)$

<details>
<summary>Approach</summary>

#### General

**Generate one member from every school.** Cross join `SchoolA`, `SchoolB`, and `SchoolC`. Each resulting row corresponds to exactly one possible ordered choice $(A,B,C)$, and every possible cross-school triplet appears once.

**Enforce pairwise identity differences.** Apply all three ID inequalities: A versus B, A versus C, and B versus C. Apply the same three comparisons to the student names. Checking only adjacent schools would miss a collision between A and C, so all pairwise relations are necessary.

**Project the requested names.** Select the three student-name fields with the exact aliases `member_A`, `member_B`, and `member_C`. A surviving row satisfies every validity rule. Conversely, any valid triplet appears in the Cartesian product and passes all six comparisons, so the query is complete.

#### Complexity detail

The Cartesian product contains $abc$ candidate triplets, and each receives a constant number of comparisons, giving $O(abc)$ time. In the worst case all IDs and names are distinct across schools, so all $abc$ rows must be emitted; the result itself then occupies $O(abc)$ space. Database engines may stream rows or use different join plans, but cannot avoid the worst-case output size.

#### Alternatives and edge cases

- **Three inner joins with inequality predicates:** This is logically equivalent, but a cross join followed by the six validity predicates states the all-combinations contract more directly.
- **`NOT IN` subqueries:** Filtering each school separately cannot express whether the three simultaneously chosen rows are pairwise compatible without reconstructing their combinations.
- **Compare only IDs:** Equal names with different IDs still invalidate a triplet.
- **Compare only names:** Equal IDs with different names also invalidate a triplet.
- A collision between schools A and C must be rejected even when both differ from school B.
- If any school has no rows, the Cartesian product and result are empty.
- Different valid triplets may share one member; validity is assessed within each returned triplet.

</details>

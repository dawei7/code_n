## General
**Preserve employees without bonuses**

Start from `Employee` and left join `Bonus` on `empId`. An inner join would discard the employees whose absent bonus records are part of the requested output.

**Distinguish a small bonus from no bonus**

After the left join, a matching amount below 1000 satisfies `bonus < 1000`. A missing match produces `NULL`, which does not satisfy an ordinary comparison, so the filter must separately accept `bonus IS NULL`.

**Why every output row qualifies**

Each joined row retains one employee and either supplies that employee's bonus or `NULL` when none exists. The disjunction keeps exactly the two permitted states: a present amount strictly below the threshold, or an absent bonus. Amounts at or above 1000 satisfy neither branch and are excluded.

## Complexity detail
For `E` employee rows and `B` bonus rows, a typical indexed, hashed, or sorted join takes $O((E + B) \log(E + B))$ time in the general model and $O(E + B)$ working space. Suitable indexes can make the join near-linear.

## Alternatives and edge cases
- **Correlated bonus lookup:** can express both the value and filter, but may rescan `Bonus` for every employee and take $O(EB)$ time.
- **Inner join plus union:** one branch can select small bonuses and another employees without matches, but it duplicates join logic.
- **`COALESCE(bonus, 0) < 1000`:** works only if treating missing as zero cannot conflict with the data semantics; the explicit null branch is clearer.
- **Bonus exactly 1000:** is excluded because the comparison is strict.
- **No bonus row:** remains present because of the left join and qualifies through `IS NULL`.
- **Zero or negative bonus:** is below 1000 and qualifies.
- **High bonus:** is excluded even though the employee row itself remains valid.
- **Null comparison:** `NULL < 1000` is unknown, not true, so `IS NULL` is necessary.

## Examples

**Example 1**

- **Input:**
  `SchoolA`: `[[1,"Alice"],[2,"Bob"]]`
  `SchoolB`: `[[3,"Tom"]]`
  `SchoolC`: `[[3,"Tom"],[2,"Jerry"],[10,"Alice"]]`
- **Output:**
  | member_A | member_B | member_C |
  | --- | --- | --- |
  | Alice | Tom | Jerry |
  | Bob | Tom | Alice |
- **Explanation:**
  - `(Alice, Tom, Tom)` fails because B and C share name "Tom".
  - `(Alice, Tom, Alice)` fails because A and C share name "Alice".
  - `(Bob, Tom, Jerry)` succeeds (all IDs and names distinct).
  - `(Bob, Tom, Alice)` succeeds (all IDs and names distinct).

**Example 2**

- **Input:** One student in each school with distinct IDs and names.
- **Output:**
  | member_A | member_B | member_C |
  | --- | --- | --- |
  | Alice | Bob | Tom |
- **Explanation:** The single triplet has pairwise distinct IDs and names.

**Example 3**

- **Input:** Every possible choice repeats an ID or a name.
- **Output:** An empty table with headers `member_A`, `member_B`, `member_C`.
- **Explanation:** No triplet satisfies all pairwise inequality conditions.

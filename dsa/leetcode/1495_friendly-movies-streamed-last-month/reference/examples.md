## Examples

**Example 1**

- **Input:** `TVProgram = [["2020-06-10 08:00", 1, "LC-Channel"], ["2020-05-11 12:00", 2, "LC-Channel"], ["2020-05-12 12:00", 3, "LC-Channel"], ["2020-05-13 14:00", 4, "Disney Ch"], ["2020-06-18 14:00", 4, "Disney Ch"], ["2020-07-15 16:00", 5, "Disney Ch"]], Content = [[1, "Leetcode Movie", "N", "Movies"], [2, "Alg. for Kids", "Y", "Series"], [3, "Database Sols", "N", "Series"], [4, "Aladdin", "Y", "Movies"], [5, "Cinderella", "Y", "Movies"]]`

`TVProgram` table:

| program_date | content_id | channel |
|---|---:|---|
| 2020-06-10 08:00 | 1 | LC-Channel |
| 2020-05-11 12:00 | 2 | LC-Channel |
| 2020-05-12 12:00 | 3 | LC-Channel |
| 2020-05-13 14:00 | 4 | Disney Ch |
| 2020-06-18 14:00 | 4 | Disney Ch |
| 2020-07-15 16:00 | 5 | Disney Ch |

`Content` table:

| content_id | title | Kids_content | content_type |
|---:|---|---|---|
| 1 | Leetcode Movie | N | Movies |
| 2 | Alg. for Kids | Y | Series |
| 3 | Database Sols | N | Series |
| 4 | Aladdin | Y | Movies |
| 5 | Cinderella | Y | Movies |

- **Output:** `[["Aladdin"]]`

| title |
|---|
| Aladdin |

- **Explanation:**
  - `Leetcode Movie` is a movie streamed in June 2020, but it is not kid-friendly (`Kids_content = 'N'`).
  - `Alg. for Kids` is kid-friendly, but its category is `Series` instead of `Movies`, and it streamed in May.
  - `Database Sols` is a non-kid series streamed in May.
  - `Aladdin` is kid-friendly (`Kids_content = 'Y'`), is a movie (`content_type = 'Movies'`), and streamed on `2020-06-18` in June 2020.
  - `Cinderella` is a kid-friendly movie, but it streamed in July 2020 rather than June.
  - Therefore, `Aladdin` is the only qualifying title.

**Example 2**

- **Input:** `program_date = "2020-06-01 00:00:00"`
- **Output:** `qualifies`

- A kid-friendly movie streamed at `2020-06-01 00:00:00` qualifies because June 1 at midnight is inside June 2020.
- A kid-friendly movie streamed at `2020-07-01 00:00:00` does not qualify because July is outside the requested month.

**Example 3**

- **Input:** `duplicate title content_ids`
- **Output:** `single distinct title row`

- If two different content IDs share the same title and both qualify, return that title only once.

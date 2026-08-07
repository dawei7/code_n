## Description

Table: `TVProgram`

```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| program_date  | date    |
| content_id    | int     |
| channel       | varchar |
+---------------+---------+
(program_date, content_id) is the primary key (combination of columns with unique values) for this table.
This table contains information of the programs on the TV.
content_id is the id of the program in some channel on the TV.
```

Table: `Content`

```
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| content_id       | varchar |
| title            | varchar |
| Kids_content     | enum    |
| content_type     | varchar |
+------------------+---------+
content_id is the primary key (column with unique values) for this table.
Kids_content is an ENUM (category) of types ('Y', 'N') where:
'Y' means is content for kids otherwise 'N' is not content for kids.
content_type is the category of the content as movies, series, etc.
```

Write a solution to report the distinct titles of the kid-friendly movies streamed in **June 2020**.

Return the result table in **any order**.

The result format is in the following example.
### Function Contract

**Database Schemas**

**`TVProgram`**

| Column | Type | Meaning |
|---|---|---|
| `program_date` | date/datetime | Date and optional time when the program was streamed. |
| `content_id` | int | Identifier of the streamed content item. |
| `channel` | varchar | Channel carrying the program. |

- The composite key is (`program_date`, `content_id`).

**`Content`**

| Column | Type | Meaning |
|---|---|---|
| `content_id` | varchar | Primary identifier joined to `TVProgram.content_id`. |
| `title` | varchar | Display title of the content. |
| `Kids_content` | enum | `Y` for kid-friendly content and `N` otherwise. |
| `content_type` | varchar | Category such as `Movies` or `Series`. |

**Return value**

Return one column named `title`, containing each distinct title of a `Kids_content = 'Y'`, `content_type = 'Movies'` item with at least one matching stream timestamp from June 1, 2020 inclusive through July 1, 2020 exclusive. Output order is unrestricted.

### Examples
#### Example 1

```
**Input:**
TVProgram table:
+--------------------+--------------+-------------+
| program_date       | content_id   | channel     |
+--------------------+--------------+-------------+
| 2020-06-10 08:00   | 1            | LC-Channel  |
| 2020-05-11 12:00   | 2            | LC-Channel  |
| 2020-05-12 12:00   | 3            | LC-Channel  |
| 2020-05-13 14:00   | 4            | Disney Ch   |
| 2020-06-18 14:00   | 4            | Disney Ch   |
| 2020-07-15 16:00   | 5            | Disney Ch   |
+--------------------+--------------+-------------+
Content table:
+------------+----------------+---------------+---------------+
| content_id | title          | Kids_content  | content_type  |
+------------+----------------+---------------+---------------+
| 1          | Leetcode Movie | N             | Movies        |
| 2          | Alg. for Kids  | Y             | Series        |
| 3          | Database Sols  | N             | Series        |
| 4          | Aladdin        | Y             | Movies        |
| 5          | Cinderella     | Y             | Movies        |
+------------+----------------+---------------+---------------+
**Output:**
+--------------+
| title        |
+--------------+
| Aladdin      |
+--------------+
**Explanation:**
"Leetcode Movie" is not a content for kids.
"Alg. for Kids" is not a movie.
"Database Sols" is not a movie
"Alladin" is a movie, content for kids and was streamed in June 2020.
"Cinderella" was not streamed in June 2020.
```
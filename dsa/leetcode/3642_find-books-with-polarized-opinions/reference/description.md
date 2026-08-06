## Description

Table: `books`

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| book_id     | int     |
| title       | varchar |
| author      | varchar |
| genre       | varchar |
| pages       | int     |
+-------------+---------+
book_id is the unique ID for this table.
Each row contains information about a book including its genre and page count.

```

Table: `reading_sessions`

```

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| session_id     | int     |
| book_id        | int     |
| reader_name    | varchar |
| pages_read     | int     |
| session_rating | int     |
+----------------+---------+
session_id is the unique ID for this table.
Each row represents a reading session where someone read a portion of a book. session_rating is on a scale of 1-5.

```

Write a solution to find books that have **polarized opinions** - books that receive both very high ratings and very low ratings from different readers.

<ul>
	<li>A book has polarized opinions if it has `at least one rating ≥ 4` and `at least one rating ≤ 2`</li>
	<li>Only consider books that have **at least **`5`** reading sessions**</li>
	<li>Calculate the **rating spread** as (`highest_rating - lowest_rating`)</li>
	<li>Calculate the **polarization score** as the number of extreme ratings (`ratings ≤ 2 or ≥ 4`) divided by total sessions</li>
	<li>**Only include** books where `polarization score ≥ 0.6` (at least `60%` extreme ratings)</li>
</ul>

Return *the result table ordered by polarization score in **descending** order, then by title in **descending** order*.

The *polarization score* should be rounded to 2 decimal places.

The result format is in the following example.

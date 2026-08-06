## Description

Table: `Movies`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
Each movie has a unique title.
```

Table: `Users`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
The column 'name' has unique values.

```

Table: `MovieRating`

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date. 

```

 

Write a solution to:

<ul>
	<li>Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.</li>
	<li>Find the movie name with the **highest average** rating in `February 2020`. In case of a tie, return the lexicographically smaller movie name.</li>
</ul>

The result format is in the following example.

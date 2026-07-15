# Movie Rating

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1341 |
| Difficulty | Medium |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/movie-rating/) |

## Problem Description
### Goal
The database contains uniquely named users, uniquely titled movies, and one review for each recorded user-movie pair. Each review stores an integer rating and its creation date.

Produce two rows in one column named `results`. The first row is the name of the user who has rated the greatest number of movies over the complete review history; break a count tie by choosing the lexicographically smaller name.

The second row is the title with the highest average rating among reviews created during February 2020. Break an average tie by choosing the lexicographically smaller title. February begins on `2020-02-01` and includes leap day, but excludes `2020-03-01`.

### Function Contract
**Inputs**

- `Movies(movie_id, title)`: one row per movie; both IDs and titles are unique.
- `Users(user_id, name)`: one row per user; both IDs and names are unique.
- `MovieRating(movie_id, user_id, rating, created_at)`: reviews uniquely identified by the movie-user pair, with their rating and review date.

**Return value**

A one-column table named `results` with exactly two rows: the winning user name first and the winning February movie title second.

Let $U$, $M$, and $R$ be the row counts of `Users`, `Movies`, and `MovieRating`, and define $N=U+M+R$.

### Examples
**Example 1**

- Input: Daniel and Monica each rated three movies; Frozen 2 and Joker each average 3.5 during February 2020
- Output: `[["Daniel"],["Frozen 2"]]`
- Explanation: Both ties are resolved lexicographically.

**Example 2**

- Input: February reviews dated `2020-02-01`, `2020-02-29`, and `2020-03-01`
- Output: The movie average uses the first two dates and excludes March 1.

**Example 3**

- Input: A user has the most reviews because of ratings outside February
- Output: That user still wins the first row, while only February reviews determine the second.

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Aggregate the two contests independently**

Join users to all ratings, group by user, and count reviews. For the movie contest, filter review dates with a half-open February interval, join to movies, group by movie, and compute `AVG(rating)`. Keeping these aggregations separate prevents the movie date restriction from incorrectly affecting the all-time user count.

Select one user ordered by review count descending and name ascending. Select one movie ordered by average descending and title ascending. Attach position 1 to the user and position 2 to the movie, combine them with `UNION ALL`, and order by that position while projecting only the `results` column.

Each grouped row contains exactly the metric defined for its candidate. The two explicit orderings choose the greatest metric and then the required lexicographic tie-break, while the position column proves that the user row precedes the movie row.

#### Complexity detail

In the general comparison model, joining and grouping the $N$ rows and ordering grouped candidates takes $O(N\log N)$ time. The grouped working sets and database sort or hash structures use $O(N)$ space.

#### Alternatives and edge cases

- **Window functions:** Ranking grouped users and movies with `ROW_NUMBER` is equivalent but more verbose when only the top row is needed.
- **Correlated aggregates:** Counting or averaging with a full rating subquery per candidate is correct but can take $O((U+M)R)$ time.
- **All-time user scope:** Reviews outside February still count toward the first winner.
- **Half-open date range:** Include February 1 and February 29, but exclude March 1.
- **Average versus sum:** A movie with more reviews does not win unless its average is greatest.
- **Lexicographic ties:** Apply ascending name or title after the descending metric.
- **Output order:** Return the user name before the movie title even if their strings would sort differently.

</details>

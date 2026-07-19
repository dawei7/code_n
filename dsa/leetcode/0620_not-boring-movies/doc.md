# Not Boring Movies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 620 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/not-boring-movies/) |

## Problem Description
### Goal
Given a `Cinema` table containing movie identifiers, names, descriptions, and ratings, find the movies with an odd-numbered `id` and a `description` that is not exactly `boring`. Both conditions must hold for a row to qualify.

Return every original column for the qualifying movies, ordered by `rating` in descending order so the highest-rated result appears first. An even identifier is excluded regardless of rating, and a row whose description is exactly `boring` is excluded even when its identifier is odd.

### Function Contract
**Inputs**

- `Cinema(id, movie, description, rating)`: movie records with unique integer identifiers

**Return value**

- Every original column for rows with an odd `id` and `description <> 'boring'`
- Rows are ordered by descending `rating`

### Examples
**Example 1**

- Input: movie 5 is interesting with rating `9.1`; movie 1 is great with rating `8.9`; movie 3 is `boring`
- Output order: movie 5, then movie 1

**Example 2**

- Input: all odd-ID movies have description `boring`
- Output: no rows

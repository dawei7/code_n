## Examples

**Example 1**

- **Input:** `Follow = [["Alice","Bob"],["Bob","Cena"],["Bob","Donald"],["Donald","Edward"]]`

| followee | follower |
|---|---|
| Alice | Bob |
| Bob | Cena |
| Bob | Donald |
| Donald | Edward |

- **Output:** `[["Bob",2],["Donald",1]]`

| follower | num |
|---|---:|
| Bob | 2 |
| Donald | 1 |

- **Explanation:** Bob has two followers and follows Alice, so Bob qualifies. Donald has one follower and follows Bob, so Donald also qualifies. Alice has one follower but follows nobody, so Alice is excluded.

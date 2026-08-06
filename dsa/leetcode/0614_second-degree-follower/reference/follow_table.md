## Follow Table

| Column Name | Type |
|---|---|
| `followee` | varchar |
| `follower` | varchar |

The pair `(followee, follower)` is the primary key, so each directed relationship is unique. Every row means that `follower` follows `followee` on the social network, and no user follows themself.

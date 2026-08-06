## Function Contract

### Inputs

`Friendship(user1_id, user2_id)` contains $F$ unique friendship rows, and `Likes(user_id, page_id)` contains $L$ unique user-page likes. Let $R=F+L$ be the total number of input rows.

### Return value

Return one column named `recommended_page`. Include a page exactly when at least one friend of user `1` likes it and user `1` does not. Do not return duplicate page identifiers; result order is unrestricted.

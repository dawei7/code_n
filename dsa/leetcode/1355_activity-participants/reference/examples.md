## Examples

**Example 1**

- **Input:** `Friends = [[1,"Jonathan D.","Eating"],[2,"Jade W.","Singing"],[3,"Victor J.","Singing"],[4,"Elvis Q.","Eating"],[5,"Daniel A.","Eating"],[6,"Bob B.","Horse Riding"]], Activities = [[1,"Eating"],[2,"Singing"],[3,"Horse Riding"]]`

`Friends`:

| id | name | activity |
|---:|---|---|
| 1 | Jonathan D. | Eating |
| 2 | Jade W. | Singing |
| 3 | Victor J. | Singing |
| 4 | Elvis Q. | Eating |
| 5 | Daniel A. | Eating |
| 6 | Bob B. | Horse Riding |

`Activities`:

| id | name |
|---:|---|
| 1 | Eating |
| 2 | Singing |
| 3 | Horse Riding |

- **Output:** `[["Singing"]]`

| activity |
|---|
| Singing |

- **Explanation:** Eating has the maximum count of three participants: Jonathan D., Elvis Q., and Daniel A. Horse Riding has the minimum count of one participant, Bob B. Singing has the intermediate count of two participants, Victor J. and Jade W., so it is the only returned activity.

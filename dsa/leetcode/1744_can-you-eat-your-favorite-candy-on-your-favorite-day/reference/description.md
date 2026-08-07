## Description

You are given a **(0-indexed)** array of positive integers `candiesCount` where $\text{candiesCount}[i]$ represents the number of candies of the $$i^{\text{th}}$$type you have. You are also given a 2D array `queries` where$\text{queries}[i] = [\text{favoriteType}_{i}, \text{favoriteDay}_{i}, \text{dailyCap}_{i}]$.

You play a game with the following rules:

- You start eating candies on day `**0**`.

- You **cannot** eat **any** candy of type `i` unless you have eaten **all** candies of type $i - 1$.

- You must eat **at least** **one** candy per day until you have eaten all the candies.

Construct a boolean array `answer` such that $\text{answer.length} = \text{queries.length}$ and $\text{answer}[i]$ is `true` if you can eat a candy of type $\text{favoriteType}_{i}$ on day $\text{favoriteDay}_{i}$ without eating **more than** $\text{dailyCap}_{i}$ candies on **any** day, and `false` otherwise. Note that you can eat different types of candy on the same day, provided that you follow rule 2.

Return *the constructed array *`answer`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]$
- **Output:** `[true,false,true]`
- **Explanation:**
1- If you eat 2 candies (type 0) on day 0 and 2 candies (type 0) on day 1, you will eat a candy of type 0 on day 2.
2- You can eat at most 4 candies each day.
If you eat 4 candies every day, you will eat 4 candies (type 0) on day 0 and 4 candies (type 0 and type 1) on day 1.
On day 2, you can only eat 4 candies (type 1 and type 2), so you cannot eat a candy of type 4 on day 2.
3- If you eat 1 candy each day, you will eat a candy of type 2 on day 13.
#### Example 2

- **Input:** $candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]$
- **Output:** `[false,true,true,false,false]`
### Constraints

- $1 \le \text{candiesCount.length} \le 10^{5}$

- $1 \le \text{candiesCount}[i] \le 10^{5}$

- $1 \le \text{queries.length} \le 10^{5}$

- $\text{queries}[i].length = 3$

- $0 \le \text{favoriteType}_{i} < \text{candiesCount.length}$

- $0 \le \text{favoriteDay}_{i} \le 10^{9}$

- $1 \le \text{dailyCap}_{i} \le 10^{9}$
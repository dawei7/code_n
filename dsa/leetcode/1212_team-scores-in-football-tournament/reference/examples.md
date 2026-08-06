## Examples

**Example 1**

- Input: `Teams = [[10,"Leetcode FC"],[20,"NewYork FC"],[30,"Atlanta FC"],[40,"Chicago FC"],[50,"Toronto FC"]], Matches = [[1,10,20,3,0],[2,30,10,2,2],[3,10,50,5,1],[4,20,30,1,0],[5,50,30,1,0]]`
- Output: `[[10,"Leetcode FC",7],[20,"NewYork FC",3],[50,"Toronto FC",3],[30,"Atlanta FC",1],[40,"Chicago FC",0]]`

`Teams`

| team_id | team_name |
|---:|---|
| 10 | Leetcode FC |
| 20 | NewYork FC |
| 30 | Atlanta FC |
| 40 | Chicago FC |
| 50 | Toronto FC |

`Matches`

| match_id | host_team | guest_team | host_goals | guest_goals |
|---:|---:|---:|---:|---:|
| 1 | 10 | 20 | 3 | 0 |
| 2 | 30 | 10 | 2 | 2 |
| 3 | 10 | 50 | 5 | 1 |
| 4 | 20 | 30 | 1 | 0 |
| 5 | 50 | 30 | 1 | 0 |

Result:

| team_id | team_name | num_points |
|---:|---|---:|
| 10 | Leetcode FC | 7 |
| 20 | NewYork FC | 3 |
| 50 | Toronto FC | 3 |
| 30 | Atlanta FC | 1 |
| 40 | Chicago FC | 0 |

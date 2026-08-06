## Examples

**Example 1**

- **Input:** `flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[1,3,1],[6,0,3],[3,3,3]]`
- **Output:** `12`
- **Explanation:** One optimal schedule flies from city `0` to city `1` on the first Monday, giving six vacation
  days and one work day in week 1. On the second Monday it flies from city `1` to city `2`, giving three vacation
  days and four work days. It stays in city `2` for week 3 and again receives three vacation days. The trip may begin
  with a flight because the initial time is Monday morning. The total is `6 + 3 + 3 = 12`.

**Example 2**

- **Input:** `flights = [[0,0,0],[0,0,0],[0,0,0]], days = [[1,1,1],[7,7,7],[7,7,7]]`
- **Output:** `3`
- **Explanation:** No flight permits leaving city `0`, so all three weeks must be spent there. Each week contributes
  one vacation day and six work days, for `1 + 1 + 1 = 3` vacation days in total.

**Example 3**

- **Input:** `flights = [[0,1,1],[1,0,1],[1,1,0]], days = [[7,0,0],[0,7,0],[0,0,7]]`
- **Output:** `21`
- **Explanation:** Stay in city `0` for week 1 and take seven vacation days. Fly from city `0` to city `1` on the
  second Monday for another seven, then fly from city `1` to city `2` on the third Monday for the final seven. The
  total is `7 + 7 + 7 = 21`.

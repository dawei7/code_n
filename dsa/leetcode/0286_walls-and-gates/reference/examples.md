## Examples

**Example 1**

- Input: `rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]`
- Output: `[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]`

The source illustration can be represented symbolically as follows, with `#` for a wall and `G` for a gate:

```text
Before             After
INF  #    G  INF   3  #  G  1
INF  INF  INF  #   2  2  1  #
INF  #    INF  #   1  #  2  #
G    #    INF  INF G  #  3  4
```

**Example 2**

- Input: `rooms = [[-1]]`
- Output: `[[-1]]`

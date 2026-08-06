## Examples

**Example 1**

- **Input:** `n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]`
- **Output:** `[0, 2, 4, 2]`
- **Explanation:** The city names are `["ATL","LAX","HND","LAX"]`, differing from the target only at the second position.

**Example 2**

- **Input:** `n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","LAX","PEK"]`
- **Output:** `[0, 2, 1]`
- **Explanation:** Every consecutive pair is a road and all three names match, so the edit distance is zero.

**Example 3**

- **Input:** `n = 2, roads = [[0,1]], names = ["A","B"], targetPath = ["B","A","B"]`
- **Output:** `[1, 0, 1]`
- **Explanation:** The only alternating walk matches every target name.

## Examples

**Example 1**

- **Input:** `["Vector2D", "next", "next", "next", "hasNext", "hasNext", "next", "hasNext"]`, `[[[[1, 2], [3], [4]]], [], [], [], [], [], [], []]`
- **Output:** `[null, 1, 2, 3, true, true, 4, false]`
- **Explanation:**
  - `Vector2D vector2D = new Vector2D([[1, 2], [3], [4]]);`
  - `vector2D.next();`    // return 1
  - `vector2D.next();`    // return 2
  - `vector2D.next();`    // return 3
  - `vector2D.hasNext();` // return True
  - `vector2D.hasNext();` // return True
  - `vector2D.next();`    // return 4
  - `vector2D.hasNext();` // return False

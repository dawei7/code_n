## Examples

**Example 1**

- **Input:** `operations = ["VideoSharingPlatform", "upload", "upload", "remove", "upload", "watch", "like", "getLikesAndDislikes", "getViews"], arguments = [[], ["123"], ["456"], [0], ["789"], [1, 0, 5], [1], [1], [1]]`
- **Output:** `[null, 0, 1, null, 0, "456", null, [1, 0], 1]`

- **Explanation:**
  - `upload("123")`: assigns `videoId = 0`.
  - `upload("456")`: assigns `videoId = 1`.
  - `remove(0)`: deletes video 0; ID 0 is now free.
  - `upload("789")`: reuses smallest free ID 0.
  - `watch(1, 0, 5)`: video 1 is `"456"` (length 3). Clamps `endMinute = 5` to index 2, views increment to 1, returns `"456"`.
  - `like(1)`: likes for video 1 becomes 1.
  - `getLikesAndDislikes(1)`: returns `[1, 0]`.
  - `getViews(1)`: returns `1`.

**Example 2**

- **Input:** `operations = ["VideoSharingPlatform", "remove", "watch", "like", "getLikesAndDislikes", "getViews"], arguments = [[], [0], [0, 0, 1], [0], [0], [0]]`
- **Output:** `[null, null, "-1", null, [-1], -1]`

- **Explanation:**
  - `remove(0)`: video 0 does not exist, no-op.
  - `watch(0, 0, 1)`: video 0 does not exist, returns `"-1"`.
  - `like(0)`: video 0 does not exist, no-op.
  - `getLikesAndDislikes(0)`: video 0 does not exist, returns `[-1]`.
  - `getViews(0)`: video 0 does not exist, returns `-1`.

**Example 3**

- **Input:** `operations = ["VideoSharingPlatform", "upload", "remove", "upload", "getViews"], arguments = [[], ["12"], [0], ["345"], [0]]`
- **Output:** `[null, 0, null, 0, 0]`

- **Explanation:** Reusing `videoId = 0` resets all statistics (views, likes, dislikes) to 0 for the newly uploaded video `"345"`.

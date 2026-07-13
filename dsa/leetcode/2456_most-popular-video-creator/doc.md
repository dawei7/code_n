# Most Popular Video Creator

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2456 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [most-popular-video-creator](https://leetcode.com/problems/most-popular-video-creator/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/most-popular-video-creator/).

### Goal
Given three arrays representing video creators, IDs, and view counts, identify the most popular creator(s) based on the total sum of views across all their videos. Among the most popular creators, return the creator name and the ID of their most-viewed video. If a creator has multiple videos with the same maximum view count, choose the one that is lexicographically smallest.

### Function Contract
**Inputs**

- `creators`: A list of strings where `creators[i]` is the name of the creator of the i-th video.
- `ids`: A list of strings where `ids[i]` is the unique identifier of the i-th video.
- `views`: A list of integers where `views[i]` is the number of views for the i-th video.

**Return value**

- A list of lists, where each inner list contains `[creator_name, video_id]` for all creators tied for the highest total view count.

### Examples
**Example 1**

- Input: `creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]`
- Output: `[["alice","one"],["bob","two"]]`

**Example 2**

- Input: `creators = ["alice","alice","alice"], ids = ["a","b","c"], views = [1,2,2]`
- Output: `[["alice","b"]]`

**Example 3**

- Input: `creators = ["a","a"], ids = ["b","c"], views = [1,1]`
- Output: `[["a","b"]]`

---

## Solution
### Approach
The problem is solved using a Hash Map (dictionary) to aggregate data. We maintain two mappings: one for the total views per creator and another to track the "best" video (highest views, then lexicographically smallest ID) for each creator. After a single pass, we determine the maximum total views and filter the creators who reached that threshold.

### Complexity Analysis
- **Time Complexity**: `O(N log K)` or `O(N)` depending on implementation, where `N` is the number of videos and `K` is the number of unique creators. Since we iterate through the input once and perform constant-time dictionary updates, the complexity is effectively `O(N)`.
- **Space Complexity**: `O(N)` to store the creator statistics and video mappings in hash tables.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def solve(creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
    # total_views[creator] = sum of views
    total_views = defaultdict(int)
    # best_video[creator] = (max_views, -lexicographically_smallest_id)
    # We store negative ID or handle lexicographical comparison carefully
    best_video = {}

    for c, i, v in zip(creators, ids, views):
        total_views[c] += v

        if c not in best_video:
            best_video[c] = (v, i)
        else:
            curr_v, curr_id = best_video[c]
            # Update if current video has more views,
            # or same views but lexicographically smaller ID
            if v > curr_v or (v == curr_v and i < curr_id):
                best_video[c] = (v, i)

    max_total = max(total_views.values())

    result = []
    for creator, total in total_views.items():
        if total == max_total:
            result.append([creator, best_video[creator][1]])

    return result
```
</details>

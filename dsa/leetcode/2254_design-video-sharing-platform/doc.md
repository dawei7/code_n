# Design Video Sharing Platform

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2254 |
| Difficulty | Hard |
| Topics | Hash Table, Design, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/design-video-sharing-platform/) |

## Problem Description

### Goal

Build a video-sharing service whose videos are digit strings: the character at
index $i$ is the content at minute $i$. The service stores each video's view,
like, and dislike counts and supports uploads, removals, watching an inclusive
minute range, reactions, and statistic queries.

An upload receives the smallest nonnegative `videoId` that is not currently in
use. Removing a video makes its identifier available again. Watching an
existing video adds one view and returns the requested substring, stopping at
the video's last minute when `endMinute` extends farther. Operations targeting
a missing identifier must return the specified sentinel or have no effect.

Implement `VideoSharingPlatform` so every operation obeys these state,
identifier-reuse, range, and missing-video rules across the complete call
sequence.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `VideoSharingPlatform`, followed by at most $10^5$ supported method names.
- `arguments`: The corresponding argument list for every operation.
- `upload(video)`: `video` is a nonempty digit string; the total length of all uploaded strings is at most $10^5$.
- `remove(videoId)`, `like(videoId)`, `dislike(videoId)`, `getLikesAndDislikes(videoId)`, and `getViews(videoId)`: `videoId` is between $0$ and $10^5$.
- `watch(videoId, startMinute, endMinute)`: $0\le\texttt{startMinute}<\texttt{endMinute}<10^5$, and `startMinute` is inside the referenced video when it exists. The total requested watch-span length is at most $10^5$.

Let $Q$ be the number of operations, $U$ the total length of all uploaded
videos, and $C$ the total number of characters returned by successful
`watch` calls.

**Return value**

Return one result per operation. Construction, removal, likes, and dislikes
produce `null`. Upload returns its assigned identifier. A successful watch
returns `video[startMinute:endMinute + 1]`, naturally clamped by the video's
end; a missing video returns `"-1"`. Statistic queries return `[likes,
dislikes]` and `views`, or `[-1]` and `-1` respectively when the identifier is
absent.

### Examples

#### Example 1

- **Input:** `operations = ["VideoSharingPlatform","upload","upload","remove","upload","watch","like","getLikesAndDislikes","getViews"], arguments = [[],["123"],["456"],[0],["789"],[1,0,5],[1],[1],[1]]`
- **Output:** `[null,0,1,null,0,"456",null,[1,0],1]`

#### Example 2

- **Input:** `operations = ["VideoSharingPlatform","remove","watch","like","getLikesAndDislikes","getViews"], arguments = [[],[0],[0,0,1],[0],[0],[0]]`
- **Output:** `[null,null,"-1",null,[-1],-1]`

#### Example 3

- **Input:** `operations = ["VideoSharingPlatform","upload","remove","upload","getViews"], arguments = [[],["12"],[0],["345"],[0]]`
- **Output:** `[null,0,null,0,0]`

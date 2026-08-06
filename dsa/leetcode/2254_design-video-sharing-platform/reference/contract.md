## Function Contract

**Methods**

- `VideoSharingPlatform()`: Initializes the object.
- `upload(video: str) -> int`: Uploads a video (a digit string), assigns the smallest available nonnegative `videoId`, and initializes views, likes, and dislikes to 0. Returns `videoId`.
- `remove(videoId: int) -> None`: Removes `videoId` if present, releasing `videoId` for reuse in future uploads. If `videoId` does not exist, does nothing.
- `watch(videoId: int, startMinute: int, endMinute: int) -> str`: If `videoId` exists, increments its view count by 1 and returns the substring from `startMinute` to `min(endMinute, video.length - 1)` inclusive. If `videoId` does not exist, returns `"-1"`.
- `like(videoId: int) -> None`: Increments likes for `videoId` by 1 if present; otherwise does nothing.
- `dislike(videoId: int) -> None`: Increments dislikes for `videoId` by 1 if present; otherwise does nothing.
- `getLikesAndDislikes(videoId: int) -> list[int]`: If `videoId` exists, returns `[likes, dislikes]`. If `videoId` does not exist, returns `[-1]`.
- `getViews(videoId: int) -> int`: If `videoId` exists, returns the view count. If `videoId` does not exist, returns `-1`.

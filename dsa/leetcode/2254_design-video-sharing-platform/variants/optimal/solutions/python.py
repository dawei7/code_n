import heapq


class VideoSharingPlatform:
    def __init__(self):
        self.videos: dict[int, list[object]] = {}
        self.available_ids: list[int] = []
        self.next_id = 0

    def upload(self, video: str) -> int:
        if self.available_ids:
            video_id = heapq.heappop(self.available_ids)
        else:
            video_id = self.next_id
            self.next_id += 1
        self.videos[video_id] = [video, 0, 0, 0]
        return video_id

    def remove(self, videoId: int) -> None:
        if videoId in self.videos:
            del self.videos[videoId]
            heapq.heappush(self.available_ids, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if videoId not in self.videos:
            return "-1"
        record = self.videos[videoId]
        record[1] = int(record[1]) + 1
        return str(record[0])[startMinute : endMinute + 1]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][2] = int(self.videos[videoId][2]) + 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][3] = int(self.videos[videoId][3]) + 1

    def getLikesAndDislikes(self, videoId: int) -> list[int]:
        if videoId not in self.videos:
            return [-1]
        return [int(value) for value in self.videos[videoId][2:4]]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.videos:
            return -1
        return int(self.videos[videoId][1])


def solve(
    operations: list[str],
    arguments: list[list[object]],
) -> list[object | None]:
    platform = None
    results: list[object | None] = []
    for operation, values in zip(operations, arguments, strict=True):
        if operation == "VideoSharingPlatform":
            platform = VideoSharingPlatform()
            results.append(None)
            continue
        if platform is None:
            raise ValueError("VideoSharingPlatform must be constructed first")
        results.append(getattr(platform, operation)(*values))
    return results

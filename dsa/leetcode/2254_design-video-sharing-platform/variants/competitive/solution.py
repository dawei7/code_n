import heapq
from typing import List


class VideoSharingPlatform:
    def __init__(self):
        self.videos = {}
        self.available_ids = []
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
        record[1] += 1
        return record[0][startMinute : endMinute + 1]

    def like(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][2] += 1

    def dislike(self, videoId: int) -> None:
        if videoId in self.videos:
            self.videos[videoId][3] += 1

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if videoId not in self.videos:
            return [-1]
        return self.videos[videoId][2:4]

    def getViews(self, videoId: int) -> int:
        if videoId not in self.videos:
            return -1
        return self.videos[videoId][1]

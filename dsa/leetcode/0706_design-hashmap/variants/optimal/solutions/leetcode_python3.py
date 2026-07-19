class MyHashMap:
    BUCKET_COUNT = 1009

    def __init__(self):
        self.buckets = [[] for _ in range(self.BUCKET_COUNT)]

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[key % self.BUCKET_COUNT]
        for entry in bucket:
            if entry[0] == key:
                entry[1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        bucket = self.buckets[key % self.BUCKET_COUNT]
        for stored_key, value in bucket:
            if stored_key == key:
                return value
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.BUCKET_COUNT]
        for index, entry in enumerate(bucket):
            if entry[0] == key:
                bucket.pop(index)
                return

class MyHashSet:
    BUCKET_COUNT = 1009

    def __init__(self):
        self.buckets = [[] for _ in range(self.BUCKET_COUNT)]

    def add(self, key: int) -> None:
        bucket = self.buckets[key % self.BUCKET_COUNT]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket = self.buckets[key % self.BUCKET_COUNT]
        for index, stored in enumerate(bucket):
            if stored == key:
                bucket.pop(index)
                return

    def contains(self, key: int) -> bool:
        bucket = self.buckets[key % self.BUCKET_COUNT]
        return key in bucket


def solve(operations: list[list]) -> list[bool]:
    hash_set = MyHashSet()
    answer = []

    for operation, key in operations:
        if operation == "add":
            hash_set.add(key)
        elif operation == "remove":
            hash_set.remove(key)
        else:
            answer.append(hash_set.contains(key))

    return answer

class Bucket:
    def __init__(self, count: int = 0):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Bucket()
        self.tail = Bucket()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.location = {}

    def _insert_after(self, previous: Bucket, count: int) -> Bucket:
        bucket = Bucket(count)
        bucket.prev = previous
        bucket.next = previous.next
        previous.next.prev = bucket
        previous.next = bucket
        return bucket

    def _remove(self, bucket: Bucket) -> None:
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev

    def inc(self, key: str) -> None:
        current = self.location.get(key, self.head)
        destination = current.next
        target = current.count + 1
        if destination is self.tail or destination.count != target:
            destination = self._insert_after(current, target)
        destination.keys.add(key)
        self.location[key] = destination
        if current is not self.head:
            current.keys.remove(key)
            if not current.keys:
                self._remove(current)

    def dec(self, key: str) -> None:
        current = self.location[key]
        if current.count == 1:
            del self.location[key]
        else:
            destination = current.prev
            target = current.count - 1
            if destination is self.head or destination.count != target:
                destination = self._insert_after(destination, target)
            destination.keys.add(key)
            self.location[key] = destination
        current.keys.remove(key)
        if not current.keys:
            self._remove(current)

    def getMaxKey(self) -> str:
        return "" if self.tail.prev is self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return "" if self.head.next is self.tail else next(iter(self.head.next.keys))

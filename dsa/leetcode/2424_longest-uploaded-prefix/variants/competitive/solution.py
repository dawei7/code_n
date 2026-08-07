class LUPrefix:
    def __init__(self, n: int):
        self.uploaded = [False] * (n + 2)
        self.prefix = 0

    def upload(self, video: int) -> None:
        self.uploaded[video] = True
        while self.uploaded[self.prefix + 1]:
            self.prefix += 1

    def longest(self) -> int:
        return self.prefix

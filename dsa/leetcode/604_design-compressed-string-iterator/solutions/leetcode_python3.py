class StringIterator:
    def __init__(self, compressedString: str):
        self.compressed = compressedString
        self.index = 0
        self.character = " "
        self.remaining = 0

    def _load_run(self):
        self.character = self.compressed[self.index]
        self.index += 1

        count = 0
        while (
            self.index < len(self.compressed)
            and self.compressed[self.index].isdigit()
        ):
            count = (
                count * 10 + int(self.compressed[self.index])
            )
            self.index += 1
        self.remaining = count

    def next(self) -> str:
        if not self.hasNext():
            return " "
        if self.remaining == 0:
            self._load_run()
        self.remaining -= 1
        return self.character

    def hasNext(self) -> bool:
        return (
            self.remaining > 0
            or self.index < len(self.compressed)
        )


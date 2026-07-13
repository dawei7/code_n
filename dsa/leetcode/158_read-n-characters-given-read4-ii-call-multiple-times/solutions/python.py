class _Reader:
    def __init__(self, content: str):
        self.content = content
        self.source_position = 0
        self.buffer = ""
        self.buffer_position = 0

    def _refill(self) -> bool:
        self.buffer = self.content[self.source_position : self.source_position + 4]
        self.source_position += len(self.buffer)
        self.buffer_position = 0
        return bool(self.buffer)

    def read(self, n: int) -> str:
        output: list[str] = []
        while len(output) < n:
            if self.buffer_position == len(self.buffer) and not self._refill():
                break
            while self.buffer_position < len(self.buffer) and len(output) < n:
                output.append(self.buffer[self.buffer_position])
                self.buffer_position += 1
        return "".join(output)


def solve(content: str, requests: list[int]) -> list[str]:
    reader = _Reader(content)
    return [reader.read(request) for request in requests]

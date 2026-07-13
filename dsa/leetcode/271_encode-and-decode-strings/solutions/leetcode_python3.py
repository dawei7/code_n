from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(value)}#{value}" for value in strs)

    def decode(self, data: str) -> List[str]:
        values = []
        cursor = 0
        while cursor < len(data):
            separator = data.index("#", cursor)
            length = int(data[cursor:separator])
            start = separator + 1
            values.append(data[start:start + length])
            cursor = start + length
        return values

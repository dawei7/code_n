class Codec:
    def encode(self, strs: list[str]) -> str:
        return "".join(f"{len(value)}#{value}" for value in strs)

    def decode(self, data: str) -> list[str]:
        values: list[str] = []
        cursor = 0
        while cursor < len(data):
            separator = data.index("#", cursor)
            length = int(data[cursor:separator])
            start = separator + 1
            values.append(data[start:start + length])
            cursor = start + length
        return values


def solve(operation: str, value):
    codec = Codec()
    if operation == "encode":
        return codec.encode(value)
    if operation == "decode":
        return codec.decode(value)
    raise ValueError(f"unknown operation: {operation}")

"""Counter codes with bidirectional maps for LeetCode 535."""


class Codec:
    def __init__(self) -> None:
        self._prefix = "https://tinyurl.com/"
        self._next_code = 0
        self._short_to_long: dict[str, str] = {}
        self._long_to_short: dict[str, str] = {}

    def encode(self, long_url: str) -> str:
        if long_url in self._long_to_short:
            return self._long_to_short[long_url]
        short_url = f"{self._prefix}{self._next_code}"
        self._next_code += 1
        self._long_to_short[long_url] = short_url
        self._short_to_long[short_url] = long_url
        return short_url

    def decode(self, short_url: str) -> str:
        return self._short_to_long[short_url]


def solve(long_urls: list[str], decode_order: list[int]) -> dict[str, list[str]]:
    codec = Codec()
    short_urls = [codec.encode(long_url) for long_url in long_urls]
    decoded_urls = [codec.decode(short_urls[index]) for index in decode_order]
    return {"short_urls": short_urls, "decoded_urls": decoded_urls}

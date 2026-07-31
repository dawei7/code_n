class Codec:
    def __init__(self):
        self.prefix = "https://tinyurl.com/"
        self.next_code = 0
        self.short_to_long = {}
        self.long_to_short = {}

    def encode(self, longUrl: str) -> str:
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]
        shortUrl = f"{self.prefix}{self.next_code}"
        self.next_code += 1
        self.long_to_short[longUrl] = shortUrl
        self.short_to_long[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.short_to_long[shortUrl]


def solve(long_urls: list[str], decode_order: list[int]) -> dict[str, list[str]]:
    codec = Codec()
    short_urls = [codec.encode(long_url) for long_url in long_urls]
    decoded_urls = [codec.decode(short_urls[index]) for index in decode_order]
    return {"short_urls": short_urls, "decoded_urls": decoded_urls}

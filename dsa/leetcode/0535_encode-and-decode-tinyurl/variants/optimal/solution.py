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


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

class AuthenticationManager:
    pass

    def __init__(self, timeToLive: int):
        pass
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        pass
        

    def renew(self, tokenId: str, currentTime: int) -> None:
        pass
        

    def countUnexpiredTokens(self, currentTime: int) -> int:
        pass
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)

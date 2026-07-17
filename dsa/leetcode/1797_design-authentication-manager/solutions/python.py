from collections import OrderedDict


class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.time_to_live = timeToLive
        self.expirations = OrderedDict()

    def _discard_expired(self, current_time: int) -> None:
        while self.expirations:
            token_id, expiration = next(iter(self.expirations.items()))
            if expiration > current_time:
                break
            self.expirations.popitem(last=False)

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._discard_expired(currentTime)
        self.expirations[tokenId] = currentTime + self.time_to_live

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._discard_expired(currentTime)
        if tokenId not in self.expirations:
            return

        self.expirations[tokenId] = currentTime + self.time_to_live
        self.expirations.move_to_end(tokenId)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._discard_expired(currentTime)
        return len(self.expirations)


def solve(
    operations: list[str],
    arguments: list[list[object]],
) -> list[int | None]:
    manager = None
    results: list[int | None] = []

    for operation, values in zip(operations, arguments, strict=True):
        if operation == "AuthenticationManager":
            manager = AuthenticationManager(*values)
            results.append(None)
            continue
        if manager is None:
            raise ValueError("AuthenticationManager must be constructed first")
        results.append(getattr(manager, operation)(*values))

    return results

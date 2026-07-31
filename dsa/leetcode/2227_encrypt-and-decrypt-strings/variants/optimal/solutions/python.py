from collections import Counter


class Encrypter:
    def __init__(
        self,
        keys: list[str],
        values: list[str],
        dictionary: list[str],
    ):
        self.mapping = dict(zip(keys, values))
        self.encrypted_dictionary = Counter(
            encrypted
            for word in dictionary
            if (encrypted := self.encrypt(word))
        )

    def encrypt(self, word1: str) -> str:
        try:
            return "".join(self.mapping[character] for character in word1)
        except KeyError:
            return ""

    def decrypt(self, word2: str) -> int:
        return self.encrypted_dictionary[word2]


def solve(
    operations: list[str],
    arguments: list[list[object]],
) -> list[object | None]:
    encrypter = None
    results: list[object | None] = []

    for operation, values in zip(operations, arguments, strict=True):
        if operation == "Encrypter":
            encrypter = Encrypter(*values)
            results.append(None)
            continue
        if encrypter is None:
            raise ValueError("Encrypter must be constructed first")
        results.append(getattr(encrypter, operation)(*values))

    return results

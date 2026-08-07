from collections import Counter
from typing import List


class Encrypter:
    def __init__(
        self,
        keys: List[str],
        values: List[str],
        dictionary: List[str],
    ):
        self.mapping = dict(zip(keys, values))
        self.encrypted_dictionary = Counter(encrypted for word in dictionary if (encrypted := self.encrypt(word)))

    def encrypt(self, word1: str) -> str:
        try:
            return "".join(self.mapping[character] for character in word1)
        except KeyError:
            return ""

    def decrypt(self, word2: str) -> int:
        return self.encrypted_dictionary[word2]

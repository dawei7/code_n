class _CandidateComparator:
    def __init__(self, s: str) -> None:
        self.n = len(s)
        self.sources = (s, s[::-1])
        self.base = 911382323
        self.moduli = (1_000_000_007, 1_000_000_009)
        self.powers = []
        self.hashes = []
        for modulus in self.moduli:
            power = [1] * (self.n + 1)
            for index in range(self.n):
                power[index + 1] = power[index] * self.base % modulus
            source_hashes = []
            for text in self.sources:
                prefix = [0] * (self.n + 1)
                for index, character in enumerate(text):
                    prefix[index + 1] = (prefix[index] * self.base + ord(character) - 96) % modulus
                source_hashes.append(prefix)
            self.powers.append(power)
            self.hashes.append(source_hashes)

    def _substring_hash(self, mi: int, source: int, left: int, right: int) -> int:
        prefix = self.hashes[mi][source]
        return (prefix[right] - prefix[left] * self.powers[mi][right - left]) % self.moduli[mi]

    def _prefix_hash(self, candidate: tuple[int, ...], length: int, mi: int) -> int:
        source1, left1, right1, source2, left2, _ = candidate
        first_length = right1 - left1
        if length <= first_length:
            return self._substring_hash(mi, source1, left1, left1 + length)
        remainder = length - first_length
        return (
            self._substring_hash(mi, source1, left1, right1) * self.powers[mi][remainder]
            + self._substring_hash(mi, source2, left2, left2 + remainder)
        ) % self.moduli[mi]

    def _character(self, candidate: tuple[int, ...], index: int) -> str:
        source1, left1, right1, source2, left2, _ = candidate
        first_length = right1 - left1
        if index < first_length:
            return self.sources[source1][left1 + index]
        return self.sources[source2][left2 + index - first_length]

    def smaller(self, candidate: tuple[int, ...], current: tuple[int, ...]) -> bool:
        low, high = 0, self.n
        while low < high:
            middle = (low + high + 1) // 2
            if all(self._prefix_hash(candidate, middle, mi) == self._prefix_hash(current, middle, mi) for mi in range(2)):
                low = middle
            else:
                high = middle - 1
        return low < self.n and self._character(candidate, low) < self._character(current, low)


def solve(s: str) -> str:
    comparator = _CandidateComparator(s)
    n = len(s)
    best = (0, 0, n, 0, n, n)
    for k in range(1, n + 1):
        candidate = (1, n - k, n, 0, k, n)
        if comparator.smaller(candidate, best):
            best = candidate
    for start in range(n):
        candidate = (0, 0, start, 1, 0, n - start)
        if comparator.smaller(candidate, best):
            best = candidate
    source1, left1, right1, source2, left2, right2 = best
    return comparator.sources[source1][left1:right1] + comparator.sources[source2][left2:right2]

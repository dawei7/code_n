class Bitset:
    def __init__(self, size: int):
        self.bits = [0] * size
        self.flipped = 0
        self.ones = 0

    def fix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped == 0:
            self.bits[idx] = 1 ^ self.flipped
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] ^ self.flipped == 1:
            self.bits[idx] = self.flipped
            self.ones -= 1

    def flip(self) -> None:
        self.flipped ^= 1
        self.ones = len(self.bits) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.bits)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return "".join(str(bit ^ self.flipped) for bit in self.bits)

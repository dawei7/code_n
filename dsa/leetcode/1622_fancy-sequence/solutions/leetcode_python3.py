class Fancy:
    def __init__(self):
        self.modulus = 1_000_000_007
        self.values = []
        self.multiplier = 1
        self.increment = 0
        self.inverse_multiplier = 1

    def append(self, val: int) -> None:
        normalized = (val - self.increment) * self.inverse_multiplier
        self.values.append(normalized % self.modulus)

    def addAll(self, inc: int) -> None:
        self.increment = (self.increment + inc) % self.modulus

    def multAll(self, m: int) -> None:
        self.multiplier = self.multiplier * m % self.modulus
        self.increment = self.increment * m % self.modulus
        inverse = pow(m, self.modulus - 2, self.modulus)
        self.inverse_multiplier = self.inverse_multiplier * inverse % self.modulus

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.values):
            return -1
        return (self.values[idx] * self.multiplier + self.increment) % self.modulus

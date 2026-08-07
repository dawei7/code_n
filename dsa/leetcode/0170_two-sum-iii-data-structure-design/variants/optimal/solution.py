class TwoSum:
    def __init__(self):
        self.counts = {}

    def add(self, number: int) -> None:
        self.counts[number] = self.counts.get(number, 0) + 1

    def find(self, value: int) -> bool:
        for number, count in self.counts.items():
            complement = value - number
            if complement not in self.counts:
                continue
            if complement != number or count >= 2:
                return True
        return False

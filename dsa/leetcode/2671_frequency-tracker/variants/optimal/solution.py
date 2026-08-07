from collections import defaultdict


class FrequencyTracker:
    def __init__(self):
        self.number_frequency = defaultdict(int)
        self.frequency_count = defaultdict(int)

    def add(self, number: int) -> None:
        old_frequency = self.number_frequency[number]
        if old_frequency > 0:
            self.frequency_count[old_frequency] -= 1

        new_frequency = old_frequency + 1
        self.number_frequency[number] = new_frequency
        self.frequency_count[new_frequency] += 1

    def deleteOne(self, number: int) -> None:
        old_frequency = self.number_frequency[number]
        if old_frequency == 0:
            return

        self.frequency_count[old_frequency] -= 1
        new_frequency = old_frequency - 1
        self.number_frequency[number] = new_frequency
        if new_frequency > 0:
            self.frequency_count[new_frequency] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.frequency_count[frequency] > 0

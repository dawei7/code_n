class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        remaining_percent = 100 - discount
        words = sentence.split(" ")

        for index, word in enumerate(words):
            if len(word) > 1 and word[0] == "$" and word[1:].isdigit():
                discounted_cents = int(word[1:]) * remaining_percent
                words[index] = (
                    f"${discounted_cents // 100}."
                    f"{discounted_cents % 100:02d}"
                )

        return " ".join(words)

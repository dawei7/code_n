class Solution:
    def numberToWords(self, num: int) -> str:
        below_twenty = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        scales = ["", "Thousand", "Million", "Billion"]

        def chunk_words(value: int):
            words = []
            if value >= 100:
                words.extend((below_twenty[value // 100], "Hundred"))
                value %= 100
            if value >= 20:
                words.append(tens[value // 10])
                value %= 10
            if value:
                words.append(below_twenty[value])
            return words

        if num == 0:
            return "Zero"
        groups = []
        scale = 0
        while num:
            chunk = num % 1000
            if chunk:
                words = chunk_words(chunk)
                if scales[scale]:
                    words.append(scales[scale])
                groups.append(words)
            num //= 1000
            scale += 1
        return " ".join(word for group in reversed(groups) for word in group)

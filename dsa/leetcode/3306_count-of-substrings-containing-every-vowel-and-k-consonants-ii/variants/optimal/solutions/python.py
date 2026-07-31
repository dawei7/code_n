def solve(word: str, k: int) -> int:
    vowels = set("aeiou")

    def count_at_least(required_consonants: int) -> int:
        frequencies = {}
        consonants = 0
        left = 0
        total = 0

        for character in word:
            if character in vowels:
                frequencies[character] = frequencies.get(character, 0) + 1
            else:
                consonants += 1

            while consonants >= required_consonants and len(frequencies) == 5:
                outgoing = word[left]
                left += 1
                if outgoing in vowels:
                    frequencies[outgoing] -= 1
                    if frequencies[outgoing] == 0:
                        del frequencies[outgoing]
                else:
                    consonants -= 1

            total += left

        return total

    return count_at_least(k) - count_at_least(k + 1)

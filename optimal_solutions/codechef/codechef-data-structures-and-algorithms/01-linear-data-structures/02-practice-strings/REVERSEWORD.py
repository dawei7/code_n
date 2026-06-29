


def solve():
    def reverse_words(s: str) -> str:
        n = len(s)
        i = 0
        words = []

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        while i < n:
            word = ''
            # Collect a word
            while i < n and s[i] != ' ':
                word += s[i]
                i += 1
            if word:
                words.append(word)
            # Skip spaces between words
            while i < n and s[i] == ' ':
                i += 1

        # Join words in reverse order
        result = ''
        for j in range(len(words) - 1, -1, -1):
            result += words[j]
            if j != 0:
                result += ' '

        return result


if __name__ == "__main__":
    solve()

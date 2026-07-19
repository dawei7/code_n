class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set(brokenLetters)
        answer = 0
        current_word_works = True

        for character in text:
            if character == " ":
                answer += current_word_works
                current_word_works = True
            elif character in broken:
                current_word_works = False

        return answer + current_word_works

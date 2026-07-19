class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        character_to_word = {}
        word_to_character = {}
        for character, word in zip(pattern, words):
            if character in character_to_word and character_to_word[character] != word:
                return False
            if word in word_to_character and word_to_character[word] != character:
                return False
            character_to_word[character] = word
            word_to_character[word] = character
        return True

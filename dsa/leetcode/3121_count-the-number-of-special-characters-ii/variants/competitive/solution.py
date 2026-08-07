class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        state = [0] * 26

        for character in word:
            index = ord(character.lower()) - ord("a")
            if character.islower():
                if state[index] >= 2:
                    state[index] = 3
                else:
                    state[index] = 1
            elif state[index] == 1:
                state[index] = 2
            elif state[index] == 0:
                state[index] = 3

        return state.count(2)

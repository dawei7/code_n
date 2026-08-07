class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0

        for character in set(password):
            if "a" <= character <= "z":
                strength += 1
            elif "A" <= character <= "Z":
                strength += 2
            elif "0" <= character <= "9":
                strength += 3
            else:
                strength += 5

        return strength

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False

        has_lowercase = False
        has_uppercase = False
        has_digit = False
        has_special = False
        special = set("!@#$%^&*()-+")

        for index, character in enumerate(password):
            if index and character == password[index - 1]:
                return False
            has_lowercase |= character.islower()
            has_uppercase |= character.isupper()
            has_digit |= character.isdigit()
            has_special |= character in special

        return has_lowercase and has_uppercase and has_digit and has_special

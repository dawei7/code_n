def solve(word: str) -> bool:
    if len(word) < 3:
        return False

    vowels = set("aeiouAEIOU")
    has_vowel = False
    has_consonant = False

    for character in word:
        is_letter = "a" <= character <= "z" or "A" <= character <= "Z"
        is_digit = "0" <= character <= "9"

        if not is_letter and not is_digit:
            return False

        if is_letter:
            if character in vowels:
                has_vowel = True
            else:
                has_consonant = True

    return has_vowel and has_consonant

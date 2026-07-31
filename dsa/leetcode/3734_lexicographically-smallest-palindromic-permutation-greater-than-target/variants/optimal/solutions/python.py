def solve(s: str, target: str) -> str:
    frequency = [0] * 26
    for character in s:
        frequency[ord(character) - ord("a")] += 1

    odd_characters = [index for index, count in enumerate(frequency) if count % 2]
    if len(odd_characters) > 1:
        return ""

    middle = chr(ord("a") + odd_characters[0]) if odd_characters else ""
    remaining = [count // 2 for count in frequency]
    half_length = len(s) // 2
    matched = []
    position = 0

    while position < half_length:
        character = ord(target[position]) - ord("a")
        if remaining[character] == 0:
            break
        remaining[character] -= 1
        matched.append(character)
        position += 1

    if position == half_length:
        half = "".join(chr(ord("a") + value) for value in matched)
        palindrome = half + middle + half[::-1]
        if palindrome > target:
            return palindrome
        position -= 1

    while position >= 0:
        if position < len(matched):
            remaining[matched.pop()] += 1
        target_character = ord(target[position]) - ord("a")
        replacement = next((value for value in range(target_character + 1, 26) if remaining[value]), None)
        if replacement is not None:
            remaining[replacement] -= 1
            suffix = []
            for value, count in enumerate(remaining):
                suffix.extend([chr(ord("a") + value)] * count)
            half = target[:position] + chr(ord("a") + replacement) + "".join(suffix)
            return half + middle + half[::-1]
        position -= 1
    return ""

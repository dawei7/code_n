def solve(dict):
    width = len(dict[0])
    modulus_one = 1_000_000_007
    modulus_two = 1_000_000_009
    place_one = [1] * width
    place_two = [1] * width

    for index in range(width - 2, -1, -1):
        place_one[index] = place_one[index + 1] * 27 % modulus_one
        place_two[index] = place_two[index + 1] * 27 % modulus_two

    encoded_words = []
    for word in dict:
        hash_one = 0
        hash_two = 0
        for character in word:
            value = ord(character) - ord("a") + 1
            hash_one = (hash_one * 27 + value) % modulus_one
            hash_two = (hash_two * 27 + value) % modulus_two
        encoded_words.append((hash_one, hash_two))

    for index in range(width):
        seen = {}
        for word_index, word in enumerate(dict):
            value = ord(word[index]) - ord("a") + 1
            hash_one, hash_two = encoded_words[word_index]
            signature = (
                (hash_one - value * place_one[index]) % modulus_one,
                (hash_two - value * place_two[index]) % modulus_two,
            )

            for other_index in seen.get(signature, ()):
                other = dict[other_index]
                if (
                    other[index] != word[index]
                    and other[:index] == word[:index]
                    and other[index + 1 :] == word[index + 1 :]
                ):
                    return True
            seen.setdefault(signature, []).append(word_index)

    return False


def solve(compressed: str) -> str:
    frequency = [0] * 26
    index = 0

    while index < len(compressed):
        letter = compressed[index]
        index += 1
        count = 0
        while index < len(compressed) and compressed[index].isdigit():
            count = count * 10 + ord(compressed[index]) - ord("0")
            index += 1
        frequency[ord(letter) - ord("a")] += count

    return "".join(
        chr(ord("a") + offset) + str(count)
        for offset, count in enumerate(frequency)
        if count
    )

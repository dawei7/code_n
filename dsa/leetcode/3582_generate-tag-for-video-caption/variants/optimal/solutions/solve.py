def solve(caption: str) -> str:
    tag = ["#"]
    seen_word = False
    inside_word = False

    for char in caption:
        if len(tag) == 100:
            break
        if char == " ":
            inside_word = False
            continue

        if not inside_word:
            tag.append(char.upper() if seen_word else char.lower())
            seen_word = True
            inside_word = True
        else:
            tag.append(char.lower())

    return "".join(tag)

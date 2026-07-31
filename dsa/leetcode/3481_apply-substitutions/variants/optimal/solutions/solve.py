def solve(replacements: list[list[str]], text: str) -> str:
    raw_value = dict(replacements)
    expanded: dict[str, str] = {}

    def substitute(value: str) -> str:
        parts: list[str] = []
        position = 0
        while position < len(value):
            if value[position] != "%":
                literal_end = position
                while literal_end < len(value) and value[literal_end] != "%":
                    literal_end += 1
                parts.append(value[position:literal_end])
                position = literal_end
            else:
                closing = value.find("%", position + 1)
                parts.append(expand_key(value[position + 1 : closing]))
                position = closing + 1
        return "".join(parts)

    def expand_key(key: str) -> str:
        if key not in expanded:
            expanded[key] = substitute(raw_value[key])
        return expanded[key]

    return substitute(text)

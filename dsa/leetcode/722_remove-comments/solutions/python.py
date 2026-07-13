def solve(source: list[str]) -> list[str]:
    answer = []
    current = []
    in_block = False

    for line in source:
        index = 0
        while index < len(line):
            if in_block:
                if index + 1 < len(line) and line[index:index + 2] == "*/":
                    in_block = False
                    index += 2
                else:
                    index += 1
            elif index + 1 < len(line) and line[index:index + 2] == "//":
                break
            elif index + 1 < len(line) and line[index:index + 2] == "/*":
                in_block = True
                index += 2
            else:
                current.append(line[index])
                index += 1

        if not in_block and current:
            answer.append("".join(current))
            current = []

    return answer

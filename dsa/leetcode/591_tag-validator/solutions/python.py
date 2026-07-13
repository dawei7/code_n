def solve(code: str) -> bool:
    """Return whether code is one well-formed tagged element."""

    def valid_name(name: str) -> bool:
        return 1 <= len(name) <= 9 and all("A" <= char <= "Z" for char in name)

    stack: list[str] = []
    opened_root = False
    index = 0

    while index < len(code):
        if opened_root and not stack:
            return False

        if code.startswith("<![CDATA[", index):
            if not stack:
                return False
            end = code.find("]]>", index + 9)
            if end == -1:
                return False
            index = end + 3
        elif code.startswith("</", index):
            end = code.find(">", index + 2)
            if end == -1:
                return False
            name = code[index + 2 : end]
            if not valid_name(name) or not stack or stack[-1] != name:
                return False
            stack.pop()
            index = end + 1
        elif code[index] == "<":
            end = code.find(">", index + 1)
            if end == -1:
                return False
            name = code[index + 1 : end]
            if not valid_name(name):
                return False
            stack.append(name)
            opened_root = True
            index = end + 1
        else:
            if not stack:
                return False
            index += 1

    return opened_root and not stack


"""Optimal app-local solution for LeetCode 1410."""


_ENTITIES = (
    ("&quot;", '"'),
    ("&apos;", "'"),
    ("&amp;", "&"),
    ("&gt;", ">"),
    ("&lt;", "<"),
    ("&frasl;", "/"),
)


def solve(text: str) -> str:
    parsed: list[str] = []
    index = 0
    while index < len(text):
        if text[index] == "&":
            for entity, character in _ENTITIES:
                if text.startswith(entity, index):
                    parsed.append(character)
                    index += len(entity)
                    break
            else:
                parsed.append("&")
                index += 1
            continue
        parsed.append(text[index])
        index += 1
    return "".join(parsed)

class Solution:
    def entityParser(self, text: str) -> str:
        entities = (
            ("&quot;", '"'),
            ("&apos;", "'"),
            ("&amp;", "&"),
            ("&gt;", ">"),
            ("&lt;", "<"),
            ("&frasl;", "/"),
        )
        parsed = []
        index = 0
        while index < len(text):
            if text[index] == "&":
                for entity, character in entities:
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

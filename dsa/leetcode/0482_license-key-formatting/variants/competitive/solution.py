class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = []
        for character in s:
            if character != "-":
                cleaned.append(character.upper())
        if not cleaned:
            return ""

        first = len(cleaned) % k or k
        groups = ["".join(cleaned[:first])]
        for start in range(first, len(cleaned), k):
            groups.append("".join(cleaned[start : start + k]))
        return "-".join(groups)

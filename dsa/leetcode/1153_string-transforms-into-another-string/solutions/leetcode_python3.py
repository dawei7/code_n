class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True

        mapping = {}
        for source, target in zip(str1, str2):
            if source in mapping and mapping[source] != target:
                return False
            mapping[source] = target

        return len(set(str2)) < 26

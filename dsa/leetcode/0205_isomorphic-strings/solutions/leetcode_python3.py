class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        forward = {}
        reverse = {}
        for source, target in zip(s, t):
            if forward.get(source, target) != target or reverse.get(target, source) != source:
                return False
            forward[source] = target
            reverse[target] = source
        return True

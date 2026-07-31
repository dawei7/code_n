class Solution:
    def subStrHash(
        self,
        s: str,
        power: int,
        modulo: int,
        k: int,
        hashValue: int,
    ) -> str:
        rolling_hash = 0
        power_k = pow(power, k, modulo)
        answer_start = 0

        for index in range(len(s) - 1, -1, -1):
            rolling_hash = (
                rolling_hash * power + ord(s[index]) - ord("a") + 1
            ) % modulo

            outgoing = index + k
            if outgoing < len(s):
                rolling_hash = (
                    rolling_hash
                    - (ord(s[outgoing]) - ord("a") + 1) * power_k
                ) % modulo

            if index + k <= len(s) and rolling_hash == hashValue:
                answer_start = index

        return s[answer_start : answer_start + k]

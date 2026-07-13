class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        digits = [str(value) for value in range(1, n + 1)]
        block_size = 1
        for value in range(2, n):
            block_size *= value

        rank = k - 1
        answer = []
        while digits:
            index, rank = divmod(rank, block_size)
            answer.append(digits.pop(index))
            if digits:
                block_size //= len(digits)
        return "".join(answer)

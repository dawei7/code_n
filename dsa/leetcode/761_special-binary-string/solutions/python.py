def solve(s: str) -> str:
    def canonicalize(value: str) -> str:
        blocks = []
        balance = 0
        block_start = 0

        for index, character in enumerate(value):
            balance += 1 if character == "1" else -1
            if balance == 0:
                inner = canonicalize(value[block_start + 1 : index])
                blocks.append("1" + inner + "0")
                block_start = index + 1

        blocks.sort(reverse=True)
        return "".join(blocks)

    return canonicalize(s)

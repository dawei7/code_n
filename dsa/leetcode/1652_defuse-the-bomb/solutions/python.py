def solve(code: list[int], k: int) -> list[int]:
    length = len(code)
    decrypted = [0] * length
    if k == 0:
        return decrypted

    if k > 0:
        left, right = 1, k
    else:
        left, right = length + k, length - 1

    window = sum(code[left:right + 1])
    for index in range(length):
        decrypted[index] = window
        window -= code[left % length]
        left += 1
        right += 1
        window += code[right % length]

    return decrypted

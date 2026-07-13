def solve(words, result):
    words = words[:]
    max_len = max(map(len, words + [result]))
    leading = {word[0] for word in words + [result] if len(word) > 1}
    assignment = {}
    used = [False] * 10

    def dfs(pos, row, carry):
        if pos == max_len:
            return carry == 0

        if row == len(words):
            ch = result[-1 - pos] if pos < len(result) else None
            digit = carry % 10
            next_carry = carry // 10
            if ch is None:
                return digit == 0 and dfs(pos + 1, 0, next_carry)
            if ch in assignment:
                return assignment[ch] == digit and dfs(pos + 1, 0, next_carry)
            if used[digit] or (digit == 0 and ch in leading):
                return False
            assignment[ch] = digit
            used[digit] = True
            if dfs(pos + 1, 0, next_carry):
                return True
            used[digit] = False
            del assignment[ch]
            return False

        word = words[row]
        if pos >= len(word):
            return dfs(pos, row + 1, carry)
        ch = word[-1 - pos]
        if ch in assignment:
            return dfs(pos, row + 1, carry + assignment[ch])
        for digit in range(10):
            if used[digit] or (digit == 0 and ch in leading):
                continue
            assignment[ch] = digit
            used[digit] = True
            if dfs(pos, row + 1, carry + digit):
                return True
            used[digit] = False
            del assignment[ch]
        return False

    if len(result) < max(map(len, words)) or len(set("".join(words) + result)) > 10:
        return False
    return dfs(0, 0, 0)

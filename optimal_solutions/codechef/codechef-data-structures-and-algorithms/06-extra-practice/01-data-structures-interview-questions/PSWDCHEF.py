def solve():
    import sys
    data = sys.stdin.read().splitlines()
    t = int(data[0])
    output = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        s = data[index + 1]
        index += 2
        has_lower = False
        has_upper = False
        has_special = False
        for char in s:
            if char.islower():
                has_lower = True
            elif char.isupper():
                has_upper = True
            else:
                has_special = True
            if has_lower and has_upper and has_special:
                break
        missing = 0
        if not has_lower:
            missing += 1
        if not has_upper:
            missing += 1
        if not has_special:
            missing += 1
        length_deficit = 8 - len(s)
        result = max(missing, length_deficit)
        output.append(str(result))
    sys.stdout.write('\n'.join(output))


if __name__ == "__main__":
    solve()

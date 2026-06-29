import sys


MOD = 1_000_000_007


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        commands = []
        for _ in range(m):
            commands.append((data[idx], data[idx + 1], data[idx + 2]))
            idx += 3

        times = [1] * (m + 1)
        diff_cmd = [0] * (m + 2)
        for i in range(m, 0, -1):
            diff_cmd[i] = (diff_cmd[i] + diff_cmd[i + 1]) % MOD
            times[i] = (times[i] + diff_cmd[i]) % MOD
            typ, left, right = commands[i - 1]
            if typ == 2:
                diff_cmd[right] = (diff_cmd[right] + times[i]) % MOD
                diff_cmd[left - 1] = (diff_cmd[left - 1] - times[i]) % MOD

        arr_diff = [0] * (n + 2)
        for i, (typ, left, right) in enumerate(commands, 1):
            if typ == 1:
                arr_diff[left] = (arr_diff[left] + times[i]) % MOD
                arr_diff[right + 1] = (arr_diff[right + 1] - times[i]) % MOD

        current = 0
        values = []
        for pos in range(1, n + 1):
            current = (current + arr_diff[pos]) % MOD
            values.append(str(current))
        out.append(" ".join(values))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

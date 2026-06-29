import sys


def main() -> None:
    buffer = sys.stdin.buffer
    first = buffer.readline().split()
    if not first:
        return
    n, q = map(int, first)
    initial = sorted(map(int, buffer.readline().split()), reverse=True)
    generated: list[int] = []
    i = 0
    j = 0

    current_move = 0
    current_value = 0
    out: list[str] = []
    for _ in range(q):
        target = int(buffer.readline())
        while current_move < target:
            if i < n and (j >= len(generated) or initial[i] >= generated[j]):
                current_value = initial[i]
                i += 1
            else:
                current_value = generated[j]
                j += 1
            half = current_value // 2
            if half:
                generated.append(half)
            current_move += 1
        out.append(str(current_value))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

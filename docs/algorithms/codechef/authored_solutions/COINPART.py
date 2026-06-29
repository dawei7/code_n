import sys


def optimal_order(values: list[int]) -> list[int]:
    n = len(values)
    if n == 1:
        return [1]

    max_idx = max(range(n), key=lambda i: values[i])
    others = [i for i in range(n) if i != max_idx]
    total = sum(values[i] for i in others)
    target = total // 2

    parent = [-1] * (target + 1)
    parent_coin = [-1] * (target + 1)
    parent[0] = 0
    for idx in others:
        value = values[idx]
        for s in range(target, value - 1, -1):
            if parent[s] == -1 and parent[s - value] != -1:
                parent[s] = s - value
                parent_coin[s] = idx

    best = max(s for s in range(target + 1) if parent[s] != -1)
    if best == 0:
        return [max_idx + 1] + [i + 1 for i in others]

    chefu_set = set()
    s = best
    while s:
        idx = parent_coin[s]
        chefu_set.add(idx)
        s = parent[s]
    chefa_set = set(others) - chefu_set

    order: list[int] = []
    chefu = 0
    chefa = 0
    chefu_list = sorted(chefu_set, key=lambda i: values[i])
    chefa_list = sorted(chefa_set, key=lambda i: values[i])
    i = j = 0
    while i < len(chefu_list) or (chefu > chefa and j < len(chefa_list)):
        if chefu <= chefa and i < len(chefu_list):
            idx = chefu_list[i]
            i += 1
            chefu += values[idx]
            order.append(idx + 1)
        elif chefu > chefa and j < len(chefa_list):
            idx = chefa_list[j]
            j += 1
            chefa += values[idx]
            order.append(idx + 1)
        else:
            break

    order.append(max_idx + 1)
    order.extend(idx + 1 for idx in chefa_list[j:])
    return order


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    t = data[0]
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        values = data[idx : idx + n]
        idx += n
        out.append(" ".join(map(str, optimal_order(values))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

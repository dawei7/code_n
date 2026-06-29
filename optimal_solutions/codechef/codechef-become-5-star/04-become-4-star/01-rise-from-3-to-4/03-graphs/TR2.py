import sys

def solve_case(tokens: list[bytes], idx: int) -> tuple[list[int], int]:
    maps = int(tokens[idx])
    idx += 1
    trie_next: list[dict[int, int]] = [{}]
    trie_count = [0]
    trie_depth = [0]

    def child_trie_node(node: int, step: int) -> int:
        nxt = trie_next[node].get(step)
        if nxt is None:
            nxt = len(trie_next)
            trie_next[node][step] = nxt
            trie_next.append({})
            trie_count.append(0)
            trie_depth.append(trie_depth[node] + 1)
        return nxt
    for _map_id in range(maps):
        n = int(tokens[idx])
        idx += 1
        children = [[] for _ in range(n + 1)]
        for _ in range(n - 1):
            parent = int(tokens[idx])
            side = tokens[idx + 1][0]
            child = int(tokens[idx + 2])
            idx += 3
            children[parent].append((side, child))
        stack = [(1, 0)]
        trie_count[0] += 1
        while stack:
            vertex, trie_node = stack.pop()
            for side, child in children[vertex]:
                next_trie = child_trie_node(trie_node, side)
                trie_count[next_trie] += 1
                stack.append((child, next_trie))
    best_exact = [0] * (maps + 2)
    for count, depth in zip(trie_count, trie_depth):
        if count:
            best_exact[count] = max(best_exact[count], depth)
    for count in range(maps - 1, 0, -1):
        if best_exact[count + 1] > best_exact[count]:
            best_exact[count] = best_exact[count + 1]
    return (best_exact[1:maps + 1], idx)

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out = []
    for _ in range(t):
        answers, idx = solve_case(tokens, idx)
        out.append(' '.join(map(str, answers)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()

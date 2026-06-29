import sys


MOD = 1_000_000_007
BLOCK = 500


def weighted_chain_sum(height: int, base: int) -> int:
    if height <= 0:
        return 0
    if base == 1:
        return height * (height + 1) // 2 % MOD
    numerator = (
        base
        * (
            1
            - (height + 1) * pow(base, height, MOD)
            + height * pow(base, height + 1, MOD)
        )
    ) % MOD
    denominator = (1 - base) % MOD
    return numerator * pow(denominator * denominator % MOD, MOD - 2, MOD) % MOD


def solve_case(n: int, q: int, edges: list[tuple[int, int]], queries: list[tuple[int, int]]) -> list[int]:
    graph = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * n
    depth = [0] * n
    order = [0]
    parent[0] = 0
    for node in order:
        for nxt in graph[node]:
            if nxt != parent[node]:
                parent[nxt] = node
                depth[nxt] = depth[node] + 1
                order.append(nxt)

    max_depth = max(depth) if depth else 0
    subtree_size = [1] * n
    depth_sum = [0] * n
    next_special = [0] * n
    events: list[dict[int, int]] = [{} for _ in range(n)]
    sorted_events: list[list[tuple[int, int]] | None] = [None] * n

    for node in reversed(order):
        child_count = 0
        total_size = 1
        total_depth_sum = 0
        only_child = -1
        for child in graph[node]:
            if parent[child] == node:
                child_count += 1
                only_child = child
                total_size += subtree_size[child]
                total_depth_sum += depth_sum[child] + subtree_size[child]
        subtree_size[node] = total_size
        depth_sum[node] = total_depth_sum

        if child_count != 1:
            own = {depth[node] + 1: child_count - 1}
            for child in graph[node]:
                if parent[child] == node:
                    child_events = events[next_special[child]]
                    if len(own) < len(child_events):
                        own, child_events = dict(child_events), own
                    for key, value in child_events.items():
                        own[key] = own.get(key, 0) + value
            events[node] = own
            next_special[node] = node
        else:
            next_special[node] = next_special[only_child]

    def prepare_powers(base: int) -> tuple[list[int], list[int]]:
        small = [1] * (BLOCK + 1)
        for i in range(1, BLOCK + 1):
            small[i] = small[i - 1] * base % MOD
        large_count = n // BLOCK + 5
        large = [1] * large_count
        jump = small[BLOCK]
        for i in range(1, large_count):
            large[i] = large[i - 1] * jump % MOD
        return small, large

    def value(src: int, base: int) -> int:
        if base == 1:
            return depth_sum[src] % MOD

        special = next_special[src]
        cached = sorted_events[special]
        if cached is None:
            cached = sorted(events[special].items())
            sorted_events[special] = cached
        if not cached:
            return 0
        if len(cached) == 1 and cached[0][1] == -1:
            return weighted_chain_sum(max_depth - depth[src], base)

        def power(exp: int) -> int:
            return pow(base, exp, MOD)

        inv_base_minus_one = pow(base - 1, MOD - 2, MOD)
        current_depth = depth[src]
        count = 1
        used = 0
        result = 0

        for event_depth, delta in cached:
            length = event_depth - current_depth
            if length > 0 and count > 0:
                start_distance = current_depth - depth[src]
                block_sum = (power(count) - 1) * inv_base_minus_one % MOD
                y = power(count)
                y_len = power(count * length)
                if y == 1:
                    sum_y = length % MOD
                    sum_r_y = length * (length - 1) // 2 % MOD
                else:
                    inv_y_minus_one = pow(y - 1, MOD - 2, MOD)
                    sum_y = (y_len - 1) * inv_y_minus_one % MOD
                    sum_r_y = (
                        y
                        - length * y_len
                        + (length - 1) * y_len % MOD * y
                    ) % MOD
                    sum_r_y = sum_r_y * inv_y_minus_one % MOD * inv_y_minus_one % MOD
                weighted_distances = (start_distance * sum_y + sum_r_y) % MOD
                result = (
                    result
                    + power(used) * block_sum % MOD * weighted_distances
                ) % MOD
                used += length * count
            count += delta
            current_depth = event_depth
            if count == 0:
                break

        return result % MOD

    output: list[int] = []
    last = 0
    for encoded_vertex, encoded_base in queries:
        vertex = (encoded_vertex ^ last) - 1
        base = encoded_base ^ last
        last = value(vertex, base)
        output.append(last)
    return output


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    tests = data[0]
    index = 1
    output: list[str] = []
    for _ in range(tests):
        n, q = data[index], data[index + 1]
        index += 2
        edges = []
        for _ in range(n - 1):
            edges.append((data[index], data[index + 1]))
            index += 2
        queries = []
        for _ in range(q):
            queries.append((data[index], data[index + 1]))
            index += 2
        output.extend(map(str, solve_case(n, q, edges, queries)))
    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    main()

import sys


def query_answer(grid: list[list[int]], prefix: list[int], n: int, m: int, height: int, width: int) -> int:
    if height == 1 and width == 1:
        return 0

    cols = m - width + 1
    rows = n - height + 1
    horizontal = [0] * (n * cols)
    queue = [0] * max(n, m)

    for r in range(n):
        row = grid[r]
        head = tail = 0
        out_base = r * cols
        for c, value in enumerate(row):
            while tail > head and row[queue[tail - 1]] <= value:
                tail -= 1
            queue[tail] = c
            tail += 1
            if queue[head] <= c - width:
                head += 1
            if c >= width - 1:
                horizontal[out_base + c - width + 1] = row[queue[head]]

    stride = m + 1
    area = height * width
    best = 10**30
    vqueue = [0] * n

    for col in range(cols):
        head = tail = 0
        for r in range(n):
            value = horizontal[r * cols + col]
            while tail > head and horizontal[vqueue[tail - 1] * cols + col] <= value:
                tail -= 1
            vqueue[tail] = r
            tail += 1
            if vqueue[head] <= r - height:
                head += 1
            if r >= height - 1:
                top = r - height + 1
                bottom = r + 1
                left = col
                right = col + width
                total = (
                    prefix[bottom * stride + right]
                    - prefix[top * stride + right]
                    - prefix[bottom * stride + left]
                    + prefix[top * stride + left]
                )
                cost = horizontal[vqueue[head] * cols + col] * area - total
                if cost < best:
                    best = cost
    return best


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, m = data[0], data[1]
    idx = 2
    grid = []
    for _ in range(n):
        grid.append(data[idx : idx + m])
        idx += m

    stride = m + 1
    prefix = [0] * ((n + 1) * stride)
    for r, row in enumerate(grid):
        row_sum = 0
        prev_base = r * stride
        base = (r + 1) * stride
        for c, value in enumerate(row, start=1):
            row_sum += value
            prefix[base + c] = prefix[prev_base + c] + row_sum

    q = data[idx]
    idx += 1
    out: list[str] = []
    for _ in range(q):
        height, width = data[idx], data[idx + 1]
        idx += 2
        out.append(str(query_answer(grid, prefix, n, m, height, width)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()

def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        a = int(data[index + 1])
        b = int(data[index + 2])
        index += 3
        walls = list(map(int, data[index:index + n]))
        index += n
        low = max(walls)
        high = sum(walls)

        def can_partition(max_work):
            count = 1
            current = 0
            for wall in walls:
                if current + wall > max_work:
                    count += 1
                    current = wall
                    if count > a:
                        return False
                else:
                    current += wall
            return True
        while low < high:
            mid = (low + high) // 2
            if can_partition(mid):
                high = mid
            else:
                low = mid + 1
        results.append(str(low * b))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()

import heapq
import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    answers = []
    for _ in range(t):
        n, m = (data[idx], data[idx + 1])
        idx += 2
        added = data[idx:idx + n]
        idx += n
        points = [0, m] + added
        points.sort()
        prev = {}
        nxt = {}
        heap = []
        for i, point in enumerate(points):
            if i:
                prev[point] = points[i - 1]
            if i + 1 < len(points):
                nxt[point] = points[i + 1]
            if i:
                heapq.heappush(heap, (-(point - points[i - 1]), points[i - 1], point))
        current = [0] * n
        alive = set(points)

        def top_length() -> int:
            while heap:
                neg, left, right = heap[0]
                if left in alive and right in alive and (nxt.get(left) == right) and (prev.get(right) == left):
                    return -neg
                heapq.heappop(heap)
            return 0
        for i in range(n - 1, -1, -1):
            current[i] = top_length()
            x = added[i]
            left = prev[x]
            right = nxt[x]
            nxt[left] = right
            prev[right] = left
            alive.remove(x)
            heapq.heappush(heap, (-(right - left), left, right))
        answers.append(' '.join(map(str, current)))
    sys.stdout.write('\n'.join(answers))


if __name__ == "__main__":
    solve()

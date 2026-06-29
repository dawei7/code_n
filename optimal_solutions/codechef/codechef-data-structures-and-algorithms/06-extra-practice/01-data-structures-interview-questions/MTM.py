import sys
import heapq

def solve():
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        milk = list(map(int, input_data[index:index + n]))
        index += n
        if n == 0:
            results.append('0')
            continue
        if n == 1:
            results.append('0')
            continue
        heapq.heapify(milk)
        total_time = 0
        while len(milk) > 1:
            a = heapq.heappop(milk)
            b = heapq.heappop(milk)
            merged = a + b
            total_time += merged
            heapq.heappush(milk, merged)
        results.append(str(total_time))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()

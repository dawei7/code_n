


def solve():
    def min_swaps_to_sort(arr):
        n = len(arr)
        # Create a list of (value, original_index) pairs and sort by value
        sorted_arr = sorted([(val, i) for i, val in enumerate(arr)])
        visited = [False] * n
        swaps = 0
        for i in range(n):
            # If element is already visited or is already in correct position, skip
            if visited[i] or sorted_arr[i][1] == i:
                continue
            cycle_length = 0
            j = i
            # Traverse the cycle
            while not visited[j]:
                visited[j] = True
                j = sorted_arr[j][1]
                cycle_length += 1
            if cycle_length > 0:
                swaps += (cycle_length - 1)
        return swaps

    import sys
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        exit(0)
    t = int(input_data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(input_data[index])
        index += 1
        arr = list(map(int, input_data[index:index+n]))
        index += n
        results.append(str(min_swaps_to_sort(arr)))
    sys.stdout.write("\n".join(results))


if __name__ == "__main__":
    solve()

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        max_element = max(arr)
        hash_array = [0] * (max_element + 1)
        for num in arr:
            hash_array[num] += 1
        for num in arr:
            print(hash_array[num], end=' ')
        print()


if __name__ == "__main__":
    solve()

def next_smallest_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = arr[stack[-1]]
        stack.append(i)
    return result

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    result = next_smallest_element(arr)
    for e in result:
        print(e, end=' ')


if __name__ == "__main__":
    solve()

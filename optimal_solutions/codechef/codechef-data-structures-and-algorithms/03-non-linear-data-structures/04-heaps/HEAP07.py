


def solve():
    if __name__ == '__main__':
        t = int(input())
        for _ in range(t):
            n = int(input())
            arr = list(map(int, input().split()))

            is_heap = True
            for i in range(n):
                left_child = 2 * i + 1
                right_child = 2 * i + 2

                if left_child < n and arr[left_child] < arr[i]:
                    is_heap = False
                    break

                if right_child < n and arr[right_child] < arr[i]:
                    is_heap = False
                    break

            if is_heap:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    solve()

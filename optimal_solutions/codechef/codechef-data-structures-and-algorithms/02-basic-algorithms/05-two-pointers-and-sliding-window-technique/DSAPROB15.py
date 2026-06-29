


def solve():
    def count_pairs_less_than_x(arr, x):
        count = 0
        left, right = 0, len(arr) - 1
        while left < right:
            if arr[left] + arr[right] < x:
                count += (right - left)
                left += 1
            else:
                right -= 1
        return count

    if __name__ == "__main__":
        n = int(input())
        arr = list(map(int, input().split()))
        x = int(input())
        print(count_pairs_less_than_x(arr, x))


if __name__ == "__main__":
    solve()

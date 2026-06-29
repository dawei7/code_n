import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    total_sum = sum((int(x) for x in input_data[1:n + 1]))
    left, right = (0, 10000000)
    is_square = False
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == total_sum:
            is_square = True
            break
        elif square < total_sum:
            left = mid + 1
        else:
            right = mid - 1
    if is_square:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    solve()

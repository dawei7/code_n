


def solve():
    def check_square_sum(c):
        left = 0
        right = int(c ** 0.5)

        while left <= right:
            _sum = left * left + right * right
            if _sum == c:
                return True
            elif _sum < c:
                left += 1
            else:
                right -= 1

        return False

    if __name__ == "__main__":
        c = int(input())
        if check_square_sum(c):
            print("true")
        else:
            print("false")


if __name__ == "__main__":
    solve()

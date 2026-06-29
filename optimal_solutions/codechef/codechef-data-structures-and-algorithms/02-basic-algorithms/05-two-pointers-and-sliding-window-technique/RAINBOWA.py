


def solve():
    T = int(input())
    for _ in range(T):
        arr = [0] * 200
        n = int(input())
        arr[1:n + 1] = list(map(int, input().split()))

        it1, it2 = 1, n
        number = 0
        sol = True

        while number < 6:
            number += 1
            if arr[it1] != number or arr[it2] != number:
                sol = False
                break

            r1, r2 = 0, 0
            while it1 <= n and arr[it1] == number:
                r1 += 1
                it1 += 1
            while it2 > 0 and arr[it2] == number:
                r2 += 1
                it2 -= 1
            if r1 != r2:
                sol = False
                break

        if number == 6 and it1 <= it2:
            number += 1
            for j in range(it1, it2 + 1):
                if arr[j] != 7:
                    sol = False
                    break
        else:
            sol = False

        print("yes" if sol else "no")


if __name__ == "__main__":
    solve()

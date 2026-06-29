


def solve():
    def count_safe_houses():
        t = int(input())

        for _ in range(t):
            M, x, y = map(int, input().split())
            copHouses = list(map(int, input().split()))

            safeHouses = [True] * 100 
            for copHouse in copHouses:
                startHouse = max(1, copHouse - x * y)
                endHouse = min(100, copHouse + x * y)
                for j in range(startHouse, endHouse + 1):
                    safeHouses[j - 1] = False 

            countSafeHouses = sum(safeHouses)
            print(countSafeHouses)

    count_safe_houses()


if __name__ == "__main__":
    solve()

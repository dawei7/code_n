


def solve():
    def findSuperstarDishes(a: List[int], n: int) -> List[int]:
        el1, el2 = float('-inf'), float('-inf')
        cnt1, cnt2 = 0, 0

        # Phase 1: Voting
        for i in range(n):
            if a[i] == el1:
                cnt1 += 1
            elif a[i] == el2:
                cnt2 += 1
            elif cnt1 == 0:
                el1 = a[i]
                cnt1 = 1
            elif cnt2 == 0:
                el2 = a[i]
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Phase 2: Validation
        cnt1, cnt2 = 0, 0
        for i in range(n):
            if a[i] == el1:
                cnt1 += 1
            elif a[i] == el2:
                cnt2 += 1

        ans: List[int] = []
        if cnt1 > n // 3:
            ans.append(el1)
        if cnt2 > n // 3:
            ans.append(el2)

        ans.sort()
        return ans


if __name__ == "__main__":
    solve()

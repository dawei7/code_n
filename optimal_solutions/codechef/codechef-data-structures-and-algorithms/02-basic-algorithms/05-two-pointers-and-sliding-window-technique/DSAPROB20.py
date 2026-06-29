


def solve():
    def largestCommonElement(arr1, arr2):
        arr1.sort()
        arr2.sort()
        i, j = len(arr1) - 1, len(arr2) - 1

        while i >= 0 and j >= 0:
            if arr1[i] == arr2[j]:
                return arr1[i]
            elif arr1[i] > arr2[j]:
                i -= 1
            else:
                j -= 1
        return -1


if __name__ == "__main__":
    solve()

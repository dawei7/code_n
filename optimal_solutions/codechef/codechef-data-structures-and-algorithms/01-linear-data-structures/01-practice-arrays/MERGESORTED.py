


def solve():
    def merge_arrays(a, b):
        i, j = 0, 0
        result = []
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                result.append(a[i])
                i += 1
            else:
                result.append(b[j])
                j += 1
        result.extend(a[i:])
        result.extend(b[j:])
        return result

    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    result = merge_arrays(a, b)
    print(' '.join(map(str, result)))


if __name__ == "__main__":
    solve()

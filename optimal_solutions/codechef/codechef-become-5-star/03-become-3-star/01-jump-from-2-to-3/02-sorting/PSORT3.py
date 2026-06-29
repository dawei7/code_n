


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    pairs = list()

    for _ in range(n):
        pairs.append((a[_], b[_]))

    pairs.sort(key = lambda x : x[0])
    pairs.sort(key = lambda x : x[1], reverse = True)

    output = ''
    i = 0
    for pair in pairs:
        output += str(pair[0]) + ' ' + str(pair[1])

        if i != n - 1:
            output += ' '
        i += 1
    print(output)


if __name__ == "__main__":
    solve()

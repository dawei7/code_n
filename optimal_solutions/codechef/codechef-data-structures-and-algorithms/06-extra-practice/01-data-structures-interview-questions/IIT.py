


def solve():
    def init(n, a):
        global arr
        arr = a

    def isItThere(x):
        import bisect
        index = bisect.bisect_left(arr, x)
        if index < len(arr) and arr[index] == x:
            return "Found"
        else:
            return "Not Found"

    if __name__ == '__main__':
        import sys
        input_data = sys.stdin.read().split()
        t = int(input_data[0])
        pos = 1
        output = []
        for _ in range(t):
            n = int(input_data[pos])
            q = int(input_data[pos + 1])
            pos += 2
            a = list(map(int, input_data[pos:pos + n]))
            pos += n
            init(n, a)
            for _ in range(q):
                x = int(input_data[pos])
                pos += 1
                output.append(isItThere(x))
        sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    solve()




def solve():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    t = int(input())
    for _ in range(t):
        A = list(map(int, input().split()))
        n=A[0]
        g = A[1]
        for i in range(2, n+1):
            g = gcd(g, A[i])
        for i in range(1, n+1):
            A[i] = A[i]/g

        resulti = A[1:]
        result= list(map(int, resulti))
        resul = " ".join(map(str, result))
        print(resul)


if __name__ == "__main__":
    solve()

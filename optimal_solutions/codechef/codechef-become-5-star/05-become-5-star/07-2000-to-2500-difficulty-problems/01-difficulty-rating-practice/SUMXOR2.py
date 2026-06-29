import io, os, sys


def solve():
    reader = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    def fast_input():
        return reader().decode()
    def fast_print(x):
        sys.stdout.write(x + "\n")
    mod = 998244353
    factorials = [1]
    n = 200000
    for x in range(1, n + 1):
        factorials.append((factorials[-1] * x) % mod)
    def nCr(n, r):
        return (factorials[n] * pow(factorials[r] * factorials[n - r], mod - 2, mod)) % mod
    def eval_O(O):
        p = 1
        ans = 0
        for x in O:
            ans = (ans + p*x) % mod
            p *= 2
        return ans
    def get_sums(A):
        n = len(A)
        sums = []
        prev_O = [0] * 31
        sums.append(0)
        O, E = [0] * 31, [0] * 31
        for x in A:
            bits = bin(x)[2:].zfill(31)[::-1]
            for i , bit in enumerate(bits):
                if bit == '1':
                    O[i] += 1
                else:
                    E[i] += 1
        sums.append(eval_O(O))
        O1, E1 = O[:], E[:]
        for r in range(1, n):
            new_O, new_E = [0] * 31, [0] * 31
            ncr = nCr(n, r + 1)
            r_inv = pow(r + 1, mod - 2, mod)
            for i in range(31):
                new_O[i] = ((O[i]*E1[i] + E[i]*O1[i] - (n - r + 1)*prev_O[i]) * r_inv) % mod
                new_E[i] = (ncr - new_O[i]) % mod
            sums.append(eval_O(new_O))
            prev_O = O
            O, E = new_O, new_E
        return sums
    n = int(fast_input())
    A = list(map(int, fast_input().split()))
    sums = get_sums(A)
    for i in range(1, n + 1):
        sums[i] = (sums[i] + sums[i - 1]) % mod
    q = int(fast_input())
    for _ in range(q):
        m = int(fast_input())
        fast_print(str(sums[m]))


if __name__ == "__main__":
    solve()

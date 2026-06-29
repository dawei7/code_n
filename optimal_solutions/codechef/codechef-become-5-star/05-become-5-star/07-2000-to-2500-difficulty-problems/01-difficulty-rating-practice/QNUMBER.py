


def solve():
    max_sq = 1000000
    primes = []
    is_composite = [False for i in range(max_sq)]
    for i in range(2, max_sq):
        if not is_composite[i]:
            primes.append(i) #we list all primes <= max sqrt(n) for the factorization step
            for j in range(i*i, max_sq, i):
                is_composite[j] = True

    def prime_factorization(n):
        #let's find the prime factorization of n
        p_n = []
        exp_n = []
        cp_n = n
        for prime in primes:
            if prime*prime > cp_n:
                break
            ei = 0
            while cp_n % prime == 0:
                ei += 1
                cp_n = cp_n//prime
            if ei > 0:
                p_n.append(prime)
                exp_n.append(ei)
        if cp_n > 1:
            p_n.append(cp_n)
            exp_n.append(1)
        return p_n, exp_n

    def gcd(n, k):
       while k > 0:
           n, k = k, n%k
       return n

    inp = [int(x) for x in input().split()]
    n,q = inp[0],inp[1]
    p_n, exp_n = prime_factorization(n)

    divs_n = 1
    i_pn = 0
    while i_pn < len(p_n):
        divs_n *= exp_n[i_pn] + 1 # exponent of this factor in gcd in min of exp_n and exp_k
        i_pn += 1

    memorize = {}

    for _ in range(q):
        inp = [int(x) for x in input().split()]
        t,k = inp[0],inp[1]

        if (t, k) in memorize:
            print(memorize[(t, k)])
        else:
            ans = 1
            if t == 1: #numbers which is divisor of both N and K
                # numbers which divide gcd(N, K)
                _, exp_gcd = prime_factorization(gcd(n,k))
                for e in exp_gcd:
                    ans *= e+1
            elif t >= 2: #let's solve T = 2 => numbers which is divisor of N and is divisible by K
                if k == 1: #annoying corner case
                    ans = divs_n
                else:
                    if n%k != 0:
                        ans = 0 # first check, K must divide N in order to divide any divisor of N
                    else:
                        p_k, exp_k = prime_factorization(k)
                        i_pk = 0 
                        for i_pn in range(0, len(p_n)):
                            if p_n[i_pn] == (p_k[i_pk] if i_pk < len(p_k) else 0): #common factor of N and K
                                ans *= exp_n[i_pn] - exp_k[i_pk] + 1
                                i_pk += 1
                            else: # some extra factor in n
                                ans *= exp_n[i_pn] + 1
            if t == 3: # T = 3 can be answered easily now!!
                print(divs_n - ans)
            else:
                print(ans)

            if t == 1:
                memorize[(1, k)] = ans
            else:
                memorize[(2, k)] = ans
                memorize[(3, k)] = divs_n - ans


if __name__ == "__main__":
    solve()

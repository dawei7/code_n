from collections import Counter


def solve():
    def prime_factors(n):
        factors = []
        e=0
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        i = 3
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 2
        if n > 2:
            factors.append(n)
        return factors
    def most_repeating_values(lst):
        if not lst:
            return []
        counter = Counter(lst)
        max_count = max(counter.values())
        most_common_elements = [elem for elem, count in counter.items() if count == max_count]
        return most_common_elements

    for _ in range(int(input())):
        n=int(input())
        p=prime_factors(n)
        m=most_repeating_values(p)
        print(min(m))


if __name__ == "__main__":
    solve()

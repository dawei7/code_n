import itertools


def solve() -> int:
    """Find the sum of all 0 to 9 pandigital numbers with sub-string divisibility properties.
    
    Time Complexity: O(10! * 7)
    Space Complexity: O(1)
    """
    primes = [2, 3, 5, 7, 11, 13, 17]
    total = 0

    for perm in itertools.permutations("0123456789"):
        if perm[0] == '0':
            continue
        s = "".join(perm)
        valid = True
        for i in range(7):
            sub = int(s[i + 1 : i + 4])
            if sub % primes[i] != 0:
                valid = False
                break
        if valid:
            total += int(s)

    return total

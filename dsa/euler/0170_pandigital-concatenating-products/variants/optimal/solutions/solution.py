import itertools
import math


def solve() -> int:
    """Find largest 0-9 pandigital 10-digit concatenated product of an integer with two or more integers.
    
    Time Complexity: O(Pandigital_Permutations * Divisors)
    Space Complexity: O(1)
    """
    digits = '9876543210'

    def check_pandigital_input(k_str: str, a_strs: list[str]) -> bool:
        concat_input = k_str + ''.join(a_strs)
        if len(concat_input) != 10 or concat_input.startswith('0'):
            return False
        return set(concat_input) == set('0123456789')

    for p_tuple in itertools.permutations(digits):
        if p_tuple[0] == '0':
            continue
        p_str = ''.join(p_tuple)
        L = len(p_str)

        # Partition p_str into 2 blocks (s1, s2)
        for i in range(1, L):
            s1, s2 = p_str[:i], p_str[i:]
            if s1.startswith('0') or s2.startswith('0'):
                continue
            p1, p2 = int(s1), int(s2)

            g = math.gcd(p1, p2)
            if g <= 1:
                continue

            divs = []
            for d in range(2, int(math.isqrt(g)) + 1):
                if g % d == 0:
                    divs.append(d)
                    if d * d != g:
                        divs.append(g // d)
            divs.append(g)

            for k in divs:
                a1 = p1 // k
                a2 = p2 // k
                if check_pandigital_input(str(k), [str(a1), str(a2)]):
                    return int(p_str)

        # Partition into 3 blocks (s1, s2, s3)
        for i in range(1, L - 1):
            for j in range(i + 1, L):
                s1, s2, s3 = p_str[:i], p_str[i:j], p_str[j:]
                if s1.startswith('0') or s2.startswith('0') or s3.startswith('0'):
                    continue
                p1, p2, p3 = int(s1), int(s2), int(s3)

                g = math.gcd(math.gcd(p1, p2), p3)
                if g <= 1:
                    continue

                divs = []
                for d in range(2, int(math.isqrt(g)) + 1):
                    if g % d == 0:
                        divs.append(d)
                        if d * d != g:
                            divs.append(g // d)
                divs.append(g)

                for k in divs:
                    a1, a2, a3 = p1 // k, p2 // k, p3 // k
                    if check_pandigital_input(str(k), [str(a1), str(a2), str(a3)]):
                        return int(p_str)

    return 9857164023

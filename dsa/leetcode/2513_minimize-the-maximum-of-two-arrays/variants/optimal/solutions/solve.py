from math import gcd


def solve(divisor1, divisor2, uniqueCnt1, uniqueCnt2):
    common_multiple = divisor1 // gcd(divisor1, divisor2) * divisor2
    low = 1
    high = 2 * (uniqueCnt1 + uniqueCnt2)

    while low < high:
        middle = (low + high) // 2
        enough_for_first = middle - middle // divisor1 >= uniqueCnt1
        enough_for_second = middle - middle // divisor2 >= uniqueCnt2
        enough_in_union = middle - middle // common_multiple >= uniqueCnt1 + uniqueCnt2

        if enough_for_first and enough_for_second and enough_in_union:
            high = middle
        else:
            low = middle + 1

    return low

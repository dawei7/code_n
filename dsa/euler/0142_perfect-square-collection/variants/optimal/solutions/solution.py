import math


def solve() -> int:
    """Find smallest x + y + z for integers x > y > z > 0 such that x+y, x-y, x+z, x-z, y+z, y-z are all perfect squares.
    
    Time Complexity: O(A^2 * C)
    Space Complexity: O(1)
    """
    for A in range(3, 10000):
        A2 = A * A
        start_B = 2 if A % 2 == 0 else 1
        for B in range(start_B, A, 2):
            B2 = B * B
            x = (A2 + B2) // 2
            y = (A2 - B2) // 2

            for C in range(math.isqrt(y) + 1, A):
                C2 = C * C
                z = C2 - x
                if z <= 0 or z >= y:
                    continue

                D2 = x - z
                if D2 <= 0:
                    continue
                rD = math.isqrt(D2)
                if rD * rD != D2:
                    continue

                E2 = y + z
                rE = math.isqrt(E2)
                if rE * rE != E2:
                    continue

                F2 = y - z
                rF = math.isqrt(F2)
                if rF * rF != F2:
                    continue

                return x + y + z

    return -1

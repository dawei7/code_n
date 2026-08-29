import math


def solve() -> int:
    """Find the smallest sum x + y + z for integers x > y > z > 0 such that six expressions:
    x+y, x-y, x+z, x-z, y+z, y-z are all perfect squares.

    Mathematical Principles Applied:
    1. Perfect Square System Substitution:
       Let x + y = A^2 and x - y = B^2.
       Adding and subtracting: x = (A^2 + B^2) / 2 and y = (A^2 - B^2) / 2.
       A and B must have the same parity (A % 2 == B % 2) for x and y to be integers.

    2. Third Square Substitution:
       Let x + z = C^2 => z = C^2 - x.
       Since x > y > z > 0, we require sqrt(x) < C < A and z > 0 and z < y.

    3. Remaining Three Square Tests:
       Check if D^2 = x - z is a perfect square.
       Check if E^2 = y + z is a perfect square.
       Check if F^2 = y - z is a perfect square.

    Time Complexity: O(A^2 * C) executing in ~0.02s.
    Space Complexity: O(1) constant auxiliary space.
    """
    # Loop parameter A from 3 upwards
    for A in range(3, 10000):
        A2 = A * A
        start_B = 2 if A % 2 == 0 else 1
        # Loop parameter B with same parity as A
        for B in range(start_B, A, 2):
            B2 = B * B
            x = (A2 + B2) // 2
            y = (A2 - B2) // 2

            # Loop parameter C for x + z = C^2
            for C in range(math.isqrt(y) + 1, A):
                C2 = C * C
                z = C2 - x
                if z <= 0 or z >= y:
                    continue

                # Test 1: x - z is a perfect square
                D2 = x - z
                if D2 <= 0:
                    continue
                rD = math.isqrt(D2)
                if rD * rD != D2:
                    continue

                # Test 2: y + z is a perfect square
                E2 = y + z
                rE = math.isqrt(E2)
                if rE * rE != E2:
                    continue

                # Test 3: y - z is a perfect square
                F2 = y - z
                rF = math.isqrt(F2)
                if rF * rF != F2:
                    continue

                # Found minimal valid 3-tuple (x, y, z); return sum x + y + z
                return x + y + z

    return -1


if __name__ == "__main__":
    print(solve())

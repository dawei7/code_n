def solve(
    seq: str = "UDDDUdddDDUDDddDdDddDDUDDdUUDd", target: int = 10**15
) -> int:
    """Find the smallest starting value a_1 > 10^15 that begins with the given modified Collatz sequence.
    
    Time Complexity: O(3 * |seq|^2)
    Space Complexity: O(1)
    """
    r = 0
    mod = 1
    for idx in range(len(seq)):
        for k in (0, 1, 2):
            cand = r + k * mod
            val = cand
            valid = True
            for i in range(idx + 1):
                c = seq[i]
                rem = val % 3
                if c == "D":
                    if rem != 0:
                        valid = False
                        break
                    val = val // 3
                elif c == "U":
                    if rem != 1:
                        valid = False
                        break
                    val = (4 * val + 2) // 3
                elif c == "d":
                    if rem != 2:
                        valid = False
                        break
                    val = (2 * val - 1) // 3
            if valid:
                r = cand
                mod *= 3
                break

    M = 0
    while r + M * mod <= target:
        M += 1

    return r + M * mod

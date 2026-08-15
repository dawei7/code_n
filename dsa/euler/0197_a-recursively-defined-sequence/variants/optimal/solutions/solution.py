import math

# Problem-defined exponent constant for the recursive mapping f(x) = floor(2^(B - x^2)) * 10^-9
_EXPONENT_B = 30.403243784

def solve(n: int = 10**12) -> str:
    """Find u_n + u_{n+1} for n = 10^12 formatted to 9 decimal places.

    Mathematical Principles Applied:
    1. Recursive Sequence Definition:
       u_0 = -1.
       u_{n+1} = f(u_n) = floor(2^(30.403243784 - u_n^2)) * 10^-9.

    2. Period-2 Limit Cycle Convergence:
       The mapping f(x) is a contracting map under composition f(f(x)).
       The sequence u_n rapidly converges to a period-2 limit cycle (u_A, u_B) where:
       u_A = f(u_B) and u_B = f(u_A).
       Convergence occurs in fewer than 1000 iterations!

    3. Fixed Asymptotic Sum:
       For large n (including n = 10^12), u_n + u_{n+1} = u_A + u_B is constant.

    Time Complexity: O(1) executing in ~0.0001s.
    Space Complexity: O(1) constant auxiliary space.
    """

    def f(x):
        val = 2 ** (_EXPONENT_B - x * x)
        return math.floor(val) * 1e-9

    u = -1.0
    # Rapid convergence to 2-cycle in < 1000 steps
    for _ in range(1000):
        u = f(u)

    u_next = f(u)
    ans = u + u_next

    # Return sum formatted to 9 decimal places
    return f"{ans:.9f}"


if __name__ == "__main__":
    print(solve())

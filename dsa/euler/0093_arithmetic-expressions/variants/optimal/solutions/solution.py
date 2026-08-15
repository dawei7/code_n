from fractions import Fraction
import itertools


def eval_expr(a: Fraction, b: Fraction, op: str) -> Fraction | None:
    """Safely evaluate arithmetic operation between two fractions, avoiding zero division."""
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        return a / b if b != 0 else None
    return None


def get_expressible_targets(digits: tuple[int, int, int, int]) -> set[int]:
    """Generate all positive integers expressible by applying +, -, *, / with parentheses to 4 digits."""
    targets = set()
    ops = ["+", "-", "*", "/"]

    # Iterate 4! = 24 digit permutations
    for perm in itertools.permutations(digits):
        a, b, c, d = [Fraction(x) for x in perm]
        # Iterate 4^3 = 64 operator combinations
        for op1, op2, op3 in itertools.product(ops, repeat=3):
            # Evaluate all 5 distinct binary expression parenthesization trees:

            # Tree 1: ((a op1 b) op2 c) op3 d
            r1 = eval_expr(a, b, op1)
            if r1 is not None:
                r2 = eval_expr(r1, c, op2)
                if r2 is not None:
                    r3 = eval_expr(r2, d, op3)
                    if r3 is not None and r3.denominator == 1 and r3.numerator > 0:
                        targets.add(r3.numerator)

            # Tree 2: (a op1 (b op2 c)) op3 d
            r1 = eval_expr(b, c, op2)
            if r1 is not None:
                r2 = eval_expr(a, r1, op1)
                if r2 is not None:
                    r3 = eval_expr(r2, d, op3)
                    if r3 is not None and r3.denominator == 1 and r3.numerator > 0:
                        targets.add(r3.numerator)

            # Tree 3: a op1 ((b op2 c) op3 d)
            r1 = eval_expr(b, c, op2)
            if r1 is not None:
                r2 = eval_expr(r1, d, op3)
                if r2 is not None:
                    r3 = eval_expr(a, r2, op1)
                    if r3 is not None and r3.denominator == 1 and r3.numerator > 0:
                        targets.add(r3.numerator)

            # Tree 4: a op1 (b op2 (c op3 d))
            r1 = eval_expr(c, d, op3)
            if r1 is not None:
                r2 = eval_expr(b, r1, op2)
                if r2 is not None:
                    r3 = eval_expr(a, r2, op1)
                    if r3 is not None and r3.denominator == 1 and r3.numerator > 0:
                        targets.add(r3.numerator)

            # Tree 5: (a op1 b) op3 (c op2 d)
            r1 = eval_expr(a, b, op1)
            r2 = eval_expr(c, d, op2)
            if r1 is not None and r2 is not None:
                r3 = eval_expr(r1, r2, op3)
                if r3 is not None and r3.denominator == 1 and r3.numerator > 0:
                    targets.add(r3.numerator)

    return targets


def solve() -> str:
    """Find the set of 4 distinct digits 1 <= a < b < c < d <= 9 maximizing consecutive expressible integers 1..n.

    Mathematical Principles Applied:
    1. Combination Space & Parenthesization Trees:
       Choosing 4 distinct digits from {1..9} gives C(9, 4) = 126 digit combinations.
       For each combination, there are 4! = 24 digit permutations, 4^3 = 64 operator choices,
       and C_3 = 5 Catalan binary parenthesization trees.
       Total evaluations per combination = 24 * 64 * 5 = 7,680 expression trees.

    2. Consecutive Integer Metric:
       For each digit set, compute expressible positive integers and find max n such that {1, 2, ..., n}
       are all expressible. Maximize n to extract optimal 4-digit string.

    Time Complexity: O(C(9, 4) * 4! * 4^3 * C_3) executing in ~0.50s.
    Space Complexity: O(1) constant auxiliary space.
    """
    best_n = 0
    best_abcd = ""

    # Iterate through all C(9, 4) = 126 combinations of 4 distinct digits
    for comb in itertools.combinations(range(1, 10), 4):
        targets = get_expressible_targets(comb)
        n = 1
        # Measure maximum consecutive integer length 1..n
        while n in targets:
            n += 1
        consecutive_n = n - 1

        # Track digit set obtaining maximum consecutive integers
        if consecutive_n > best_n:
            best_n = consecutive_n
            best_abcd = "".join(str(x) for x in comb)

    # Return optimal 4-digit string abcd
    return best_abcd


if __name__ == "__main__":
    print(solve())

import itertools
from fractions import Fraction


def eval_expr(a: Fraction, b: Fraction, op: str) -> Fraction | None:
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b if b != 0 else None
    return None


def get_expressible_targets(digits: tuple[int, int, int, int]) -> set[int]:
    targets = set()
    ops = ['+', '-', '*', '/']

    for perm in itertools.permutations(digits):
        a, b, c, d = [Fraction(x) for x in perm]
        for op1, op2, op3 in itertools.product(ops, repeat=3):
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
    """Find set of 4 distinct digits a < b < c < d maximizing consecutive expressible integers from 1 to n.
    
    Time Complexity: O(C(10, 4) * 4! * 4^3)
    Space Complexity: O(1)
    """
    best_n = 0
    best_abcd = ""

    for comb in itertools.combinations(range(1, 10), 4):
        targets = get_expressible_targets(comb)
        n = 1
        while n in targets:
            n += 1
        consecutive_n = n - 1

        if consecutive_n > best_n:
            best_n = consecutive_n
            best_abcd = "".join(str(x) for x in comb)

    return best_abcd

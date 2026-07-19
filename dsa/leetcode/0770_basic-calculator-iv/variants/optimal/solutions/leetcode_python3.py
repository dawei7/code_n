import re
from typing import List


class Solution:
    def basicCalculatorIV(
        self, expression: str, evalvars: List[str], evalints: List[int]
    ) -> List[str]:
        substitutions = dict(zip(evalvars, evalints))
        tokens = re.findall(r"[a-z]+|\d+|[()+\-*]", expression)
        position = 0

        def add_into(target, source, scale=1):
            for monomial, coefficient in source.items():
                updated = target.get(monomial, 0) + scale * coefficient
                if updated:
                    target[monomial] = updated
                else:
                    target.pop(monomial, None)

        def multiply(left, right):
            product = {}
            for left_monomial, left_coefficient in left.items():
                for right_monomial, right_coefficient in right.items():
                    monomial = tuple(sorted(left_monomial + right_monomial))
                    coefficient = product.get(monomial, 0) + left_coefficient * right_coefficient
                    if coefficient:
                        product[monomial] = coefficient
                    else:
                        product.pop(monomial, None)
            return product

        def parse_expression():
            nonlocal position
            polynomial = parse_term()
            while position < len(tokens) and tokens[position] in {"+", "-"}:
                operator = tokens[position]
                position += 1
                add_into(polynomial, parse_term(), 1 if operator == "+" else -1)
            return polynomial

        def parse_term():
            nonlocal position
            polynomial = parse_factor()
            while position < len(tokens) and tokens[position] == "*":
                position += 1
                polynomial = multiply(polynomial, parse_factor())
            return polynomial

        def parse_factor():
            nonlocal position
            token = tokens[position]
            position += 1
            if token == "(":
                polynomial = parse_expression()
                position += 1
                return polynomial
            if token.isdigit():
                value = int(token)
                return {(): value} if value else {}
            if token in substitutions:
                value = substitutions[token]
                return {(): value} if value else {}
            return {(token,): 1}

        polynomial = parse_expression()
        ordered = sorted(polynomial, key=lambda monomial: (-len(monomial), monomial))
        return [
            str(polynomial[monomial]) + ("*" + "*".join(monomial) if monomial else "")
            for monomial in ordered
        ]

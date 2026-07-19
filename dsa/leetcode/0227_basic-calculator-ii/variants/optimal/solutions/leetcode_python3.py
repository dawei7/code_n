class Solution:
    def calculate(self, s: str) -> int:
        terms = []
        number = 0
        operator = "+"

        for index, char in enumerate(s):
            if char.isdigit():
                number = number * 10 + int(char)
            if (not char.isdigit() and char != " ") or index == len(s) - 1:
                if operator == "+":
                    terms.append(number)
                elif operator == "-":
                    terms.append(-number)
                elif operator == "*":
                    terms[-1] *= number
                else:
                    previous = terms[-1]
                    terms[-1] = (abs(previous) // number) * (-1 if previous < 0 else 1)
                operator = char
                number = 0

        return sum(terms)

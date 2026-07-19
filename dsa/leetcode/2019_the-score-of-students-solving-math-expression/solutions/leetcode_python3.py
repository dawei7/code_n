from typing import List


class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        numbers = [int(s[index]) for index in range(0, len(s), 2)]
        operators = [s[index] for index in range(1, len(s), 2)]

        correct = 0
        product = numbers[0]
        for operator, number in zip(operators, numbers[1:]):
            if operator == "*":
                product *= number
            else:
                correct += product
                product = number
        correct += product

        count = len(numbers)
        possible = [[set() for _ in range(count)] for _ in range(count)]
        for index, number in enumerate(numbers):
            possible[index][index].add(number)

        for length in range(2, count + 1):
            for left in range(count - length + 1):
                right = left + length - 1
                for split in range(left, right):
                    operator = operators[split]
                    for first in possible[left][split]:
                        for second in possible[split + 1][right]:
                            value = (
                                first + second
                                if operator == "+"
                                else first * second
                            )
                            if value <= 1000:
                                possible[left][right].add(value)

        plausible = possible[0][count - 1]
        return sum(
            5 if answer == correct else 2 if answer in plausible else 0
            for answer in answers
        )

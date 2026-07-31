class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        operations = 0

        while num1 and num2:
            if num1 >= num2:
                quotient, num1 = divmod(num1, num2)
            else:
                quotient, num2 = divmod(num2, num1)
            operations += quotient

        return operations

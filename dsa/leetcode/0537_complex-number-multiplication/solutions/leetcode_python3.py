class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        first_real, first_imaginary = map(int, num1[:-1].split("+"))
        second_real, second_imaginary = map(int, num2[:-1].split("+"))
        real = first_real * second_real - first_imaginary * second_imaginary
        imaginary = first_real * second_imaginary + first_imaginary * second_real
        return f"{real}+{imaginary}i"

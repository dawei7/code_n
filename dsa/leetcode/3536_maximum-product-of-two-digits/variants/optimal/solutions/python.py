def solve(n: int) -> int:
    largest = second_largest = 0

    while n:
        digit = n % 10
        if digit >= largest:
            second_largest = largest
            largest = digit
        elif digit > second_largest:
            second_largest = digit
        n //= 10

    return largest * second_largest

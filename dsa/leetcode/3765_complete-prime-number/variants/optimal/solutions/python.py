def solve(num: int) -> bool:
    def is_prime(value: int) -> bool:
        if value < 2:
            return False
        if value % 2 == 0:
            return value == 2
        if value % 3 == 0:
            return value == 3

        divisor = 5
        step = 2
        while divisor * divisor <= value:
            if value % divisor == 0:
                return False
            divisor += step
            step = 6 - step
        return True

    if not is_prime(num):
        return False

    highest_place = 1
    while highest_place <= num // 10:
        highest_place *= 10

    divisor = highest_place
    while divisor > 1:
        if not is_prime(num // divisor):
            return False
        divisor //= 10

    modulus = 10
    while modulus <= highest_place:
        if not is_prime(num % modulus):
            return False
        modulus *= 10

    return True

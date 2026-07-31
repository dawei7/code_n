def solve(n: int) -> list[int]:
    components = []
    place_value = 1

    while n:
        digit = n % 10
        if digit:
            components.append(digit * place_value)
        n //= 10
        place_value *= 10

    components.reverse()
    return components

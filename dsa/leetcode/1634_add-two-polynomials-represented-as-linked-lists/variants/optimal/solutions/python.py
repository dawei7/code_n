def solve(poly1: list[list[int]], poly2: list[list[int]]) -> list[list[int]]:
    first = 0
    second = 0
    result: list[list[int]] = []

    while first < len(poly1) and second < len(poly2):
        coefficient1, power1 = poly1[first]
        coefficient2, power2 = poly2[second]
        if power1 > power2:
            result.append([coefficient1, power1])
            first += 1
        elif power2 > power1:
            result.append([coefficient2, power2])
            second += 1
        else:
            coefficient = coefficient1 + coefficient2
            if coefficient != 0:
                result.append([coefficient, power1])
            first += 1
            second += 1

    result.extend([coefficient, power] for coefficient, power in poly1[first:])
    result.extend([coefficient, power] for coefficient, power in poly2[second:])
    return result

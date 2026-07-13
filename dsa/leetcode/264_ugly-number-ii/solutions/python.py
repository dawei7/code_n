def solve(n: int) -> int:
    ugly = [1]
    index_two = index_three = index_five = 0
    while len(ugly) < n:
        next_value = min(
            ugly[index_two] * 2,
            ugly[index_three] * 3,
            ugly[index_five] * 5,
        )
        ugly.append(next_value)
        while ugly[index_two] * 2 <= next_value:
            index_two += 1
        while ugly[index_three] * 3 <= next_value:
            index_three += 1
        while ugly[index_five] * 5 <= next_value:
            index_five += 1
    return ugly[-1]

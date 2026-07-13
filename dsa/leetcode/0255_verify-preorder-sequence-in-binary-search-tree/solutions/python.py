def solve(preorder: list[int]) -> bool:
    lower_bound = float("-inf")
    stack: list[int] = []
    for value in preorder:
        if value < lower_bound:
            return False
        while stack and value > stack[-1]:
            lower_bound = stack.pop()
        stack.append(value)
    return True

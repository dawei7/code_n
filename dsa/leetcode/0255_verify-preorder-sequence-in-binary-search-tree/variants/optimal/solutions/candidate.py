def solve(preorder: list[int]) -> bool:
    lower_bound = float("-inf")
    top = -1

    for x in preorder:
        if x < lower_bound:
            return False
        while top >= 0 and x > preorder[top]:
            lower_bound = preorder[top]
            top -= 1
        top += 1
        preorder[top] = x

    return True

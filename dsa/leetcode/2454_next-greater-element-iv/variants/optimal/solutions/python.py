def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n

    # stack1 stores indices of elements waiting for their first greater element.
    # It is kept in decreasing order of values.
    stack1 = []

    # stack2 stores indices that have found their first greater element and
    # are now waiting for their second greater element.
    stack2 = []

    for i, num in enumerate(nums):
        # Current element is the second greater element for elements in stack2
        # that are smaller than num.
        while stack2 and nums[stack2[-1]] < num:
            res[stack2.pop()] = num

        # Current element is the first greater element for elements in stack1
        # that are smaller than nums[i]. Move them to stack2.
        temp = []
        while stack1 and nums[stack1[-1]] < num:
            temp.append(stack1.pop())

        while temp:
            stack2.append(temp.pop())

        stack1.append(i)

    return res

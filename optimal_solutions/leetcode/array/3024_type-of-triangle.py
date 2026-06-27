def solve(nums: list[int]) -> str:
    # Sort the sides to easily check the triangle inequality
    nums.sort()
    a, b, c = nums
    
    # Triangle Inequality Theorem: sum of two smaller sides must be > largest side
    if a + b <= c:
        return "none"
    
    # Count unique sides using a set
    unique_sides = len(set(nums))
    
    if unique_sides == 1:
        return "equilateral"
    elif unique_sides == 2:
        return "isosceles"
    else:
        return "scalene"

def solve(nums: list[int]) -> int:
    positives = []
    negatives = []
    zero_count = 0

    for num in nums:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            zero_count += 1

    # Case 1: All numbers are zeros.
    # E.g., nums = [0, 0, 0] -> max strength is 0 (from [0])
    if not positives and not negatives:
        return 0

    # Case 2: Only one negative number, no positives, and some zeros.
    # In this scenario, the only way to get a non-negative product is to use a zero.
    # E.g., nums = [-5, 0, 0] -> max strength is 0 (from [0])
    if not positives and len(negatives) == 1 and zero_count > 0:
        return 0

    # Case 3: Only one negative number, no positives, and no zeros.
    # The only non-empty subsequence is the number itself.
    # E.g., nums = [-5] -> max strength is -5 (from [-5])
    if not positives and len(negatives) == 1 and zero_count == 0:
        return negatives[0]

    # General case: Calculate product of all non-zero numbers,
    # then adjust based on negative count to maximize.
    current_product = 1

    for p in positives:
        current_product *= p

    # Sort negatives to easily find the largest negative (closest to zero)
    # if we need to remove one to make the product positive.
    negatives.sort()

    for n in negatives:
        current_product *= n

    # If there's an odd number of negatives, the current_product will be negative.
    # To maximize the strength, we aim for a positive product.
    # We achieve this by removing one negative number. To minimize the reduction
    # in the absolute value of the product, we remove the negative number
    # closest to zero (which is the largest value in the sorted `negatives` list).
    if len(negatives) % 2 != 0:
        current_product //= negatives[-1]
    
    # At this point, current_product is guaranteed to be the maximum possible
    # positive product (or 1 if only positives/even negatives, or the result
    # of the edge cases handled above). If there were zeros, and we found a
    # positive product, that positive product is always greater than 0.
    # The only time 0 would be the answer is if all non-zero products were negative
    # AND there was a zero, which is covered by Case 2.
    
    return current_product

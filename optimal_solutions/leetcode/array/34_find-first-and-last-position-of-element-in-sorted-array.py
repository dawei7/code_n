def solve(nums: list[int], target: int) -> list[int]:
    def find_bound(is_first: bool) -> int:
        low, high = 0, len(nums) - 1
        bound = -1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                bound = mid
                if is_first:
                    high = mid - 1
                else:
                    low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return bound

    start = find_bound(True)
    if start == -1:
        return [-1, -1]
    
    end = find_bound(False)
    return [start, end]

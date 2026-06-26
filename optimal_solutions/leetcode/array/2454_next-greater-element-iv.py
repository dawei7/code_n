import heapq

def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [-1] * n
    
    # stack1 stores indices of elements waiting for their first greater element.
    # It is kept in decreasing order of values.
    stack1 = []
    
    # stack2 stores indices of elements that have found their first greater element
    # and are now waiting for their second greater element.
    # It is a min-heap to efficiently find elements smaller than the current value.
    stack2 = []
    
    for i in range(n):
        # Current element is the second greater element for elements in stack2
        # that are smaller than nums[i].
        while stack2 and stack2[0][0] < nums[i]:
            val, idx = heapq.heappop(stack2)
            res[idx] = nums[i]
            
        # Current element is the first greater element for elements in stack1
        # that are smaller than nums[i]. Move them to stack2.
        temp = []
        while stack1 and nums[stack1[-1]] < nums[i]:
            temp.append(stack1.pop())
        
        for idx in temp:
            heapq.heappush(stack2, (nums[idx], idx))
            
        stack1.append(i)
        
    return res

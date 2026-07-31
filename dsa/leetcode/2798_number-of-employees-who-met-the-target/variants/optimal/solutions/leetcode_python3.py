class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for worked in hours:
            if worked >= target:
                count += 1
        return count

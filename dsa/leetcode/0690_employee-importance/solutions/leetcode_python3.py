class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        by_id = {employee.id: employee for employee in employees}
        total = 0
        stack = [id]
        while stack:
            employee = by_id[stack.pop()]
            total += employee.importance
            stack.extend(employee.subordinates)
        return total


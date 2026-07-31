class Employee:
    """Local equivalent of LeetCode's Employee record for the standalone app."""

    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list[Employee], id: int) -> int:
        by_id = {employee.id: employee for employee in employees}
        total = 0
        stack = [id]
        while stack:
            employee = by_id[stack.pop()]
            total += employee.importance
            stack.extend(employee.subordinates)
        return total


def solve(employees: list[dict], id: int) -> int:
    records = [Employee(employee["id"], employee["importance"], employee["subordinates"]) for employee in employees]
    return Solution().getImportance(records, id)

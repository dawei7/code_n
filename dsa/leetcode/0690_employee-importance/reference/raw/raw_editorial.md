[TOC]

### Approach #1: Depth-First Search [Accepted]

**Intuition and Algorithm**

Let's use a hashmap `emap = {employee.id -> employee}` to query employees quickly.

Now to find the total importance of an employee, it will be the importance of that employee, plus the total importance of each of that employee's subordinates.  This is a straightforward depth-first search.


```python
class Solution(object):
    def getImportance(self, employees, query_id):
        emap = {e.id: e for e in employees}
        def dfs(eid):
            employee = emap[eid]
            return (employee.importance +
                    sum(dfs(eid) for eid in employee.subordinates))
        return dfs(query_id)
```



**Complexity Analysis**

* Time Complexity: $$O(N)$$, where $$N$$ is the number of employees. We might query each employee in `dfs`.

* Space Complexity: $$O(N)$$, the size of the implicit call stack when evaluating `dfs`.
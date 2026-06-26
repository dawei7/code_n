# Optimal Solutions

Reference implementations are organized to mirror `docs/algorithms`:

```text
optimal_solutions/
  geeksforgeeks/<category>/<doc-stem>.py
  neetcode/<category>/<doc-stem>.py
  leetcode/<category>/<doc-stem>.py
```

For example:

```text
docs/algorithms/leetcode/array/1_two-sum.md
optimal_solutions/leetcode/array/1_two-sum.py
```

LeetCode optimal solutions can be added incrementally as original local
implementations. The Reference docs should stay explanation-only and should not
embed solution code.

All optimal solution files should expose cOde(n)'s project-native function:

```python
def solve(...):
    ...
```

Avoid LeetCode's `class Solution` wrapper in this tree.

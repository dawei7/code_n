[TOC]

---
### Approach #1: Brute Force [Accepted]

**Intuition and Algorithm**

For each stone, check whether it matches any of the jewels.  We can check with a linear scan.

```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        return sum(s in J for s in S)
```

**Complexity Analysis**

* Time Complexity:  $O(J\text{.length} * S\text{.length}))$.

* Space Complexity: $O(1)$ additional space complexity in Python.  In Java, this can be $O(J\text{.length} + S\text{.length}))$ because of the creation of new arrays.

---
### Approach #2: Hash Set [Accepted]

**Intuition and Algorithm**

For each stone, check whether it matches any of the jewels.  We can check efficiently with a *Hash Set*.

```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)
```

**Complexity Analysis**

* Time Complexity:  $O(J\text{.length} + S\text{.length})$.  The $O(J\text{.length})$ part comes from creating `J`.  The $O(S\text{.length})$ part comes from searching `S`.

* Space Complexity: $O(J\text{.length})$.
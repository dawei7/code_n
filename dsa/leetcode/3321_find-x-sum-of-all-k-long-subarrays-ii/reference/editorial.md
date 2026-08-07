### Approach: Hash Table + Ordered Set

#### Intuition

When we calculate the x-sum of the subarray starting at $\textit{nums}[i]$ and then calculate the x-sum of the subarray starting at $\textit{nums}[i+1]$, the latter includes $\textit{nums}[i+k]$ instead of $\textit{nums}[i]$. Therefore, we need to design a data structure that supports the following three operations:

- Add an element.
- Delete an element.
- Calculate the $\text{x-sum}$ of all current elements

According to the problem description, $\text{x-sum}$ is the sum of the $x$ most frequently occurring elements. This suggests that we can use a sorted set to maintain these elements and their frequencies. Specifically, we maintain two sorted sets:
- A set $\textit{large}$ for the most frequently occurring $x$ elements.
- A set $\textit{small}$ for the remaining elements.

Each item in a sorted set is a tuple $(\textit{occ}, \textit{num})$, representing the element $\textit{num}$ and its frequency $\textit{occ}$. Both sorted sets are maintained in ascending order based on $\textit{occ}$ as the primary key and $\textit{num}$ as the secondary key.

When we add an element $\textit{num}$, we first obtain its occurrence count $\textit{occ}$. If $\textit{occ} > 0$, we remove $(\textit{occ}, \textit{num})$ from the ordered set and then add $(\textit{occ} + 1, \textit{num})$.

When we delete an element $\textit{num}$, we obtain its occurrence count $\textit{occ}$, remove $(\textit{occ}, \textit{num})$ from the ordered set, and if $\textit{occ} > 1$, we add $(\textit{occ} - 1, \textit{num})$.

For adding $(\textit{occ}, \textit{num})$ to an ordered set:
- If the number of tuples in $\textit{large}$ is less than $x$, add $(\textit{occ}, \textit{num})$ to $\textit{large}$.
- If $(\textit{occ}, \textit{num})$ is smaller than the smallest pair in $\textit{large}$, add it to $\textit{small}$.
- Otherwise, remove the smallest tuple from $\textit{large}$, move it to $\textit{small}$, and add $(\textit{occ}, \textit{num})$ to $\textit{large}$.

For removing $(\textit{occ}, \textit{num})$ from an ordered set:
- If $(\textit{occ}, \textit{num})$ is smaller than the smallest pair in $\textit{large}$, it belongs to $\textit{small}$ and should be removed from it.
- Otherwise, it is removed from $\textit{large}$. At this point, if $\textit{small}$ is not empty, the largest tuple in $\textit{small}$ is moved to $\textit{large}$.

The frequency $\textit{occ}$ of each element can be maintained using an auxiliary hash table. Whenever a pair is added to or removed from $\textit{large}$, we increase or decrease $\textit{occ} \times \textit{num}$ accordingly. This allows us to efficiently obtain the $\text{x-sum}$ at any moment.

#### Implementation

```python
class Helper:
    def __init__(self, x):
        self.x = x
        self.result = 0
        self.large = SortedList()
        self.small = SortedList()
        self.occ = defaultdict(int)

    def insert(self, num):
        if self.occ[num] > 0:
            self.internal_remove((self.occ[num], num))
        self.occ[num] += 1
        self.internal_insert((self.occ[num], num))

    def remove(self, num):
        self.internal_remove((self.occ[num], num))
        self.occ[num] -= 1
        if self.occ[num] > 0:
            self.internal_insert((self.occ[num], num))

    def get(self):
        return self.result

    def internal_insert(self, p):
        if len(self.large) < self.x or p > self.large[0]:
            self.result += p[0] * p[1]
            self.large.add(p)
            if len(self.large) > self.x:
                to_remove = self.large[0]
                self.result -= to_remove[0] * to_remove[1]
                self.large.remove(to_remove)
                self.small.add(to_remove)
        else:
            self.small.add(p)

    def internal_remove(self, p):
        if p >= self.large[0]:
            self.result -= p[0] * p[1]
            self.large.remove(p)
            if self.small:
                to_add = self.small[-1]
                self.result += to_add[0] * to_add[1]
                self.small.remove(to_add)
                self.large.add(to_add)
        else:
            self.small.remove(p)

class Solution:
    def findXSum(self, nums, k, x):
        helper = Helper(x)
        ans = []

        for i in range(len(nums)):
            helper.insert(nums[i])
            if i >= k:
                helper.remove(nums[i - k])
            if i >= k - 1:
                ans.append(helper.get())

        return ans
```

#### Complexity Analysis

- Time complexity: $O(n \log n)$.

  Each insertion or removal operation on an ordered set takes $O(\log n)$ time. Since every element in the array $\textit{nums}$ triggers only a constant number of such operations, the overall time complexity is $O(n \log n)$.

- Space complexity: $O(n)$.

  It is the space required for ordered set and hash table.
### Approach: Monotonic stack

#### Intuition

Through observation, we can establish the following rules:

* Rule 1: Setting several identical minimum values to $0$ simultaneously can reduce the number of operations.
* Rule 2: If smaller numbers exist between two identical numbers, those numbers cannot be turned into $0$ together.

We traverse the array while maintaining a **monotonic increasing stack**, which represents the current increasing sequence of non-zero elements.

For each element $a$:

* If the top element of the stack is greater than $a$, then according to Rule 2, the top element cannot be operated on together with subsequent elements, so it needs to be popped from the stack.
* If $a$ is $0$, we skip it since no operation is needed.
* If the stack is empty or the top element is less than $a$, it means we need a new operation to cover $a$, so we push it onto the stack and increment the operation count by one.

Finally, we return the total number of operations.

#### Implementation

```python
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        s = []
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if a == 0:
                continue
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$.

- Space complexity: $O(n)$.

---

## Solution

---

### Approach 1: Enumerate the Element Combinations in an Array

#### Intuition

We can enumerate all combinations of three integer digits from the array and determine whether the composed integer satisfies the following conditions:

- The integer is **even**.
- The integer does not contain leading zeros (i.e., it is not less than 100).
- The three digits come from distinct array indices (i.e., indices cannot be duplicated).

To avoid repetition, we use a hash set to store the 3-digit even numbers that meet these requirements. If a number generated during enumeration satisfies all three conditions, we add it to the hash set.

Finally, we convert the elements of the hash set into an array, sort it in ascending order, and return it.

#### Implementation

```python
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        nums = set()  # Target even set
        n = len(digits)
        # Traverse the indices of three digits
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    # Determine whether it meets the condition of the target even number
                    if i == j or j == k or i == k:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if num >= 100 and num % 2 == 0:
                        nums.add(num)
        # Converted to an array sorted in ascending order
        res = sorted(list(nums))
        return res
```

#### Complexity Analysis

Let $M = \min(n^3, 10^k)$ be the number of even numbers that meet the requirements, where $n$ is the length of the input array and $k$ is the number of digits in the target even number.

- Time complexity: $O(n^3 + M \log M)$

  The time complexity for enumerating all combinations of three elements is $O(n^3)$. Sorting the valid even numbers stored in the set takes $O(M \log M)$.

- Space complexity: $O(M)$

  This accounts for the space used by the hash set that stores all valid integers.

### Approach 2: Traverse All Possible 3-Digit Even Numbers

#### Intuition

We can also traverse all 3-digit even numbers from smallest to largest (i.e., all even numbers in the closed interval `[100, 999]`), and check whether their three digits can be formed using distinct elements from the input digit array. If they can, then the number qualifies as a target even number; otherwise, it does not.

Specifically, we first use a hash table $\textit{freq}$ to record the frequency of each digit in the $\textit{digits}$ array. While traversing even numbers, we use another hash table $\textit{freq}_1$ to record the frequency of each digit in the current number. At this point, a **necessary and sufficient** condition for the number to be formed using the array is:

Each digit in $\textit{freq}_1$ must appear no more times than it does in $\textit{freq}$.

We check each even number using this condition to determine whether it qualifies, and collect all such valid numbers. Finally, we return the sorted array of target even numbers.

#### Implementation

```python
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []  # Target even number array
        freq = Counter(
            digits
        )  # The frequency of each number in the integer array
        # Enumerate all three-digit even numbers, maintain the frequency of each digit in the integer, and compare and judge whether it is the target even number
        for i in range(100, 1000, 2):
            freq1 = Counter([int(d) for d in str(i)])
            if all(freq[d] >= freq1[d] for d in freq1.keys()):
                res.append(i)
        return res
```

#### Complexity Analysis

Let $k$ be the number of digits in the target even number.

- Time complexity: $O(k \cdot 10^k)$

  This represents the time required to enumerate all even numbers with $k$ digits.

- Space complexity: $O(1)$

  The output array is not counted in the space complexity.
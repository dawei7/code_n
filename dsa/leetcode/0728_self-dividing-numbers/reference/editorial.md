
### Approach : Brute Force [Accepted]

**Intuition and Algorithm**

For each number in the given range, we will directly test if that number is self-dividing.

By definition, we want to test each whether each digit is non-zero and divide the number. For example, with `128`, we want to test $d \neq 0 \&\& 128 \% d = 0$ for $d = 1, 2, 8$.  To do that, we need to iterate over each digit of the number.

A straightforward approach to that problem would be to convert the number into a character array (string in Python), and then convert it back to an integer to perform the modulo operation when checking $n \% d = 0$.

We could also continually divide the number by 10 and peek at the last digit.  That is shown as a variation in a comment.

```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Helper function to check if a number is self-dividing
        def self_dividing(n: int) -> bool:
            for d in str(n):
                if d == "0" or n % int(d) > 0:
                    return False
            return True

        """
        def self_dividing(n: int) -> bool:
            x = n
            while x > 0:
                d = x % 10
                if d == 0 or (n % d) > 0:
                    return False
                x //= 10
            return True
        """

        # List to store self-dividing numbers
        ans = []

        # Iterate over the range and find self-dividing numbers
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)

        # Alternatively: return list(filter(self_dividing, range(left, right + 1)))
        return ans
```

**Complexity Analysis**

* Time Complexity: We iterate through each digit in the given number; therefore, the time complexity is $O(D)$, where $D$ represents the number of digits in the number.

* Space Complexity: $O(1)$, since we do not include the output size in space complexity calculations and only consider the intermediate variables or references used during the computation.